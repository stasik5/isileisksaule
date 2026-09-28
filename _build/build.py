#!/usr/bin/env python3
"""Generates the static site for isileisksaule.lt.

Edit texts in _build/content.py, then run:
    python3 _build/build.py
It writes the HTML pages into the repository root. Commit and push; Hostinger deploys the repo.
"""
import json, os, re, html, datetime, hashlib
from urllib.parse import quote
from content import SITE, SERVICES, REVIEWS, FAQ_HOME, ARTICLES, GALLERY, HOME, KALKES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = SITE["url"]  # canonical base, no trailing slash
# cache-busting version = hash of the CSS+JS, so browsers fetch new styles after every change
VER = hashlib.md5(b"".join(open(os.path.join(ROOT, "assets", f), "rb").read() for f in ("site.css", "site.js"))).hexdigest()[:8]
E = html.escape
KALKES_URL = f'/{KALKES["slug"]}/'

ICON = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>',
}

# ---------- small building blocks ----------
def mail_href():
    return f'mailto:{SITE["email"]}?subject={quote(SITE["mail_subject"])}&body={quote(SITE["mail_body"])}'

def pair(loc):
    """The two main buttons, exactly like the original site: 'Siųsti nuotraukas' (pink) + 'Skambinti' (teal).
    Phones show photos first, desktop shows call first (CSS order)."""
    return (f'<div class="pair">'
            f'<a class="btn btn-call" href="tel:{SITE["phone_e164"]}" data-loc="{loc}">Skambinti</a>'
            f'<a class="btn btn-photo" href="{mail_href()}" data-loc="{loc}">Siųsti nuotraukas</a>'
            f'</div>')

DIV = '<hr class="divider">'

def img(name, alt, lazy=True, cls=""):
    from PIL import Image
    with Image.open(os.path.join(ROOT, "img", name)) as im: w, h = im.size
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    if cls: extra += f' class="{cls}"'
    return f'<img src="/img/{name}" alt="{E(alt)}" width="{w}" height="{h}"{extra}>'

def faq_html(faq):
    return '<div class="faq">' + "".join(f"<details><summary>{E(q)}</summary><p>{a}</p></details>" for q,a in faq) + "</div>"

def reviews_html():
    return '<div class="reviews">' + "".join(f'<blockquote><p>{E(t)}</p><cite>{E(who)}</cite></blockquote>' for t,who in REVIEWS) + "</div>"

def gallery_html():
    return '<div class="gallery">' + "".join(img(f, alt) for f,alt in GALLERY) + "</div>"

def prices_html():
    rows = [r for r in SITE["prices"] if not r[2]]
    lines = "".join(
        f'<li class="{"main" if i == 0 else ("sub" if r[0].startswith("&nbsp;") else "")}"><span>{r[0].replace("&nbsp;&nbsp;· ", "")}</span><b>{r[1]}</b></li>'
        for i, r in enumerate(rows))
    return f'<ul class="prices">{lines}</ul><div class="notice">{SITE["notice"]}</div>'

def svc_card(s):
    """Service card: price and key facts at a glance; the page behind it has the details."""
    facts = "".join(f"<li>{E(f)}</li>" for f in s["facts"])
    return (f'<a class="svc" href="/{s["slug"]}/"><h3>{E(s["short"])}</h3>'
            f'<p class="svc-price">{E(s["card_price"])}</p><ul class="facts">{facts}</ul>'
            f'<span class="more">Plačiau →</span></a>')

# ---------- JSON-LD ----------
def business_ld():
    return {
      "@context": "https://schema.org", "@type": "LocalBusiness", "@id": BASE + "/#business",
      "name": SITE["name"], "legalName": SITE["legal_name"], "url": BASE + "/",
      "logo": BASE + "/img/logo.png", "image": BASE + "/img/og.jpg",
      "telephone": SITE["phone_e164"], "email": SITE["email"], "priceRange": "€€", "foundingDate": SITE["since"],
      "address": {"@type": "PostalAddress", "streetAddress": SITE["street"], "addressLocality": "Vilnius", "addressCountry": "LT"},
      "areaServed": [{"@type": "City", "name": "Vilnius"}, {"@type": "AdministrativeArea", "name": "Vilniaus rajonas"}],
      "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
          "opens": SITE["opens"], "closes": SITE["closes"]}],
      "sameAs": SITE["same_as"],
    }

def crumbs_ld(items):
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":i+1,"name":n,"item":BASE+u} for i,(n,u) in enumerate(items)]}

def faq_ld(faq):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":re.sub("<[^>]+>","",html.unescape(a))}} for q,a in faq]}

# ---------- link every "kalkės" word to the explainer page ----------
KALK_RE = re.compile(r"(?<!\w)([Kk]alk(?:ės|ių|es|ėmis|ėms|ėse))(?!\w)")
SKIP_TAGS = {"a", "h1", "h2", "h3", "summary", "script", "style", "title", "button", "b"}

def link_kalkes(body):
    out, stack = [], []
    for part in re.split(r"(<[^>]+>)", body):
        if part.startswith("<"):
            m = re.match(r"<\s*(/)?\s*([a-zA-Z0-9]+)", part)
            if m:
                tag = m.group(2).lower()
                if m.group(1):
                    if tag in stack:
                        while stack and stack.pop() != tag: pass
                elif not part.endswith("/>") and tag not in ("br","img","hr","meta","link","input"):
                    stack.append(tag)
            out.append(part)
        elif part and not (SKIP_TAGS & set(stack)):
            out.append(KALK_RE.sub(lambda m: f'<a class="kalk" href="{KALKES_URL}">{m.group(1)}</a>', part))
        else:
            out.append(part)
    return "".join(out)

# ---------- page shell ----------
def page(path, title, desc, body, ld=(), og_img="og.jpg"):
    if path != KALKES_URL:
        body = link_kalkes(body)
    url = BASE + path
    nav = "".join(f'<a href="{u}">{E(n)}</a>' for n,u in SITE["nav"])
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    ga = SITE["ga4"]
    services_links = "".join(f'<a href="/{s["slug"]}/">{E(s["short"])}</a>' for s in SERVICES)
    doc = f'''<!doctype html>
<html lang="lt">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="lt_LT">
<meta property="og:site_name" content="{E(SITE["name"])}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/img/{og_img}">
<meta name="theme-color" content="#ed3a7b">
<link rel="icon" href="/img/favicon.png" type="image/png">
<link rel="preload" href="/assets/fonts/rubik-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={VER}">
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{analytics_storage:'denied',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500}});
gtag('js',new Date());gtag('config','{ga}');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id={ga}"></script>
{lds}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/" aria-label="{E(SITE["name"])} – pradžia"><img src="/img/logo.webp" alt="{E(SITE["name"])}" width="520" height="187"></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav" aria-label="Meniu"><span></span><span></span><span></span></button>
<nav class="nav" id="nav">{nav}<a class="tel" href="tel:{SITE["phone_e164"]}" data-loc="header">{SITE["phone_display"]}</a></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="fcols">
<div><h3>Mūsų rekvizitai:</h3><p>{E(SITE["legal_name"])}<br>Įm. k. {SITE["company_code"]}<br>{E(SITE["street"])}, Vilnius</p></div>
<div><h3>Susisiekite</h3><p><a href="mailto:{SITE["email"]}" data-loc="footer">{SITE["email"]}</a><br><a href="tel:{SITE["phone_e164"]}" data-loc="footer">{SITE["phone_display"]}</a></p></div>
<div><h3>Darbo laikas</h3><p>Pirmadienį–šeštadienį<br>{SITE["opens"]}–{SITE["closes"]}<br>Sekmadienį nedirbame</p></div>
</div>
<nav class="flinks" aria-label="Paslaugos">{services_links}<a href="{KALKES_URL}">Kas yra kalkės?</a><a href="/papildoma-informacija/">Patarimai</a><a href="/privatumo-politika/">Privatumo politika</a><a href="#" data-open-consent>Slapukų nustatymai</a></nav>
<p class="copy">© {datetime.date.today().year} {E(SITE["legal_name"])}</p>
</div></footer>
<a class="fab" href="{SITE["whatsapp"]}" target="_blank" rel="noopener" data-loc="floating" aria-label="Parašyti WhatsApp">{ICON["wa"]}</a>
<div class="consent" id="consent" role="dialog" aria-label="Slapukai">
<strong>Slapukai</strong>
<p>Naudojame analitinius ir reklamos slapukus, kad matytume, kaip lankytojai randa mūsų svetainę, ir tobulintume reklamą. Jūs renkatės. <a href="/privatumo-politika/">Daugiau</a></p>
<div class="cbtns"><button class="btn btn-photo" data-consent="all">Sutinku</button><button class="btn btn-ghost" data-consent="necessary">Tik būtini</button></div>
</div>
<script src="/assets/site.js?v={VER}" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f: f.write(doc)
    return path

# ---------- pages ----------
def build():
    pages = []

    # HOME — same structure as the original site. Desktop order = DOM order; phones reorder with CSS (see .flow).
    steps = "".join(
        f'<li><img src="/img/icons/{ic}.webp" alt="" width="64" height="64" loading="lazy"><span>{i}. {E(a)} {E(b)}</span></li>'
        for i, ((a, b), ic) in enumerate(zip(SITE["steps"], HOME["process_icons"]), start=1))
    svc = "".join(svc_card(s) for s in SERVICES)
    home = f'''
<div class="flow">
<section class="hero s-hero" style="background-image:url(/img/hero-langas.webp)"><div class="wrap">
<div class="hero-box">
<h1>{E(HOME["hero_h1"])}</h1>
<p class="hero-sub">{E(HOME["hero_h2"])}<br><a href="tel:{SITE["phone_e164"]}" data-loc="hero_number">{SITE["phone_display"]}</a></p>
</div>
{pair("hero")}
</div></section>

<section class="s-works" id="darbai"><div class="wrap">
<h2>Darbų pavyzdžiai:</h2>
{gallery_html()}
</div></section>

<section class="s-reviews" id="atsiliepimai"><div class="wrap">
{DIV}
<h2>Atsiliepimai:</h2>
<p class="stars-line"><span class="stars">★★★★★</span> 5,0 iš {SITE["google_reviews"]} atsiliepimų <a href="{SITE["gbp"]}" target="_blank" rel="noopener">Google</a></p>
{reviews_html()}
<p class="note">{E(HOME["reviews_note"])}</p>
</div></section>

<section class="s-services" id="paslaugos"><div class="wrap">
{DIV}
<h2>Atliekame:</h2>
<div class="svcs">{svc}</div>
</div></section>

<section class="s-prices" id="kainos"><div class="wrap narrow">
{DIV}
<h2>Kainos:</h2>
{prices_html()}
</div></section>

<section class="s-order" id="uzsakymas"><div class="wrap narrow">
{DIV}
<h2>Kaip užsakyti?</h2>
<p class="t-pink">{E(HOME["order_call"])}</p>
<p class="t-teal">{E(HOME["order_photos"])}</p>
{pair("order")}
</div></section>

<section class="s-process"><div class="wrap narrow">
{DIV}
<p class="t-teal big">{E(HOME["process_intro"])}</p>
<ol class="steps">{steps}</ol>
{pair("process")}
</div></section>

<section class="s-about" id="apie"><div class="wrap narrow">
{DIV}
<h2>Apie mus:</h2>
<p class="t-teal">{E(HOME["about_lead"])}</p>
{"".join(f"<p>{E(p)}</p>" for p in HOME["about"])}
{pair("about")}
</div></section>

<section class="s-faq"><div class="wrap narrow">
{DIV}
<h2>Dažni klausimai:</h2>
{faq_html(FAQ_HOME)}
</div></section>
</div>
'''
    pages.append(page("/", SITE["home_title"], SITE["home_desc"], home, ld=[business_ld(), faq_ld(FAQ_HOME)]))

    # SERVICE PAGES — same look: pink centred title, teal lead, the two buttons, then details.
    for s in SERVICES:
        others = "".join(svc_card(o) for o in SERVICES if o is not s)
        facts = "".join(f"<li>{E(f)}</li>" for f in s["facts"])
        body = f'''
<section class="svc-page"><div class="wrap">
<p class="crumbs"><a href="/">Pradžia</a> › {E(s["short"])}</p>
<h1>{E(s["h1"])}</h1>
<div class="svc-grid">
<aside class="svc-box">
<p class="svc-price">{E(s["card_price"])}</p>
<ul class="facts">{facts}</ul>
<p class="svc-detail">{s["price_detail"]}</p>
<div class="notice">{SITE["notice"]}</div>
<div class="stack"><a class="btn btn-call" href="tel:{SITE["phone_e164"]}" data-loc="service_box">Skambinti {SITE["phone_display"]}</a><a class="btn btn-photo" href="{mail_href()}" data-loc="service_box">Siųsti nuotraukas</a></div>
</aside>
<div class="article">
{s["body"]}
<figure class="svc-img">{img(s["image"], s["image_alt"])}</figure>
<h2>Klausimai</h2>
{faq_html(s["faq"])}
</div>
</div>
</div></section>
<section><div class="wrap">
{DIV}
<h2>Kitos paslaugos:</h2>
<div class="svcs">{others}</div>
</div></section>
'''
        pages.append(page(f'/{s["slug"]}/', s["title"], s["desc"], body,
            ld=[business_ld(),
                {"@context":"https://schema.org","@type":"Service","name":s["h1"],"serviceType":s["short"],
                 "provider":{"@id":BASE+"/#business"},"areaServed":"Vilnius","url":BASE+f'/{s["slug"]}/'},
                crumbs_ld([("Pradžia","/"),(s["short"],f'/{s["slug"]}/')]),
                faq_ld(s["faq"])]))

    # KALKĖS explainer
    body = f'''
<section class="page-head"><div class="wrap narrow">
<p class="crumbs"><a href="/">Pradžia</a> › Kas yra kalkės?</p>
<h1>{E(KALKES["h1"])}</h1>
<p class="t-teal lead">{E(KALKES["lead"])}</p>
</div></section>
<section><div class="wrap narrow">
{DIV}
<figure class="svc-img">{img("privataus-namo-stiklo-fasadas.webp", "Dideli stiklai, ant kurių dažnai kaupiasi kalkės")}</figure>
<div class="article">{KALKES["body"]}</div>
<div class="notice">{SITE["notice"]}</div>
{pair("kalkes")}
</div></section>
'''
    pages.append(page(KALKES_URL, KALKES["title"], KALKES["desc"], body,
        ld=[{"@context":"https://schema.org","@type":"Article","headline":KALKES["h1"],"publisher":{"@id":BASE+"/#business"},"mainEntityOfPage":BASE+KALKES_URL},
            crumbs_ld([("Pradžia","/"),("Kas yra kalkės?",KALKES_URL)])]))

    # ARTICLES + tips list (keeps the old /papildoma-informacija address)
    cards = f'<a class="svc" href="{KALKES_URL}"><h3>Kas yra kalkės ant langų?</h3><p>{E(KALKES["desc"])}</p><span class="more">Skaityti →</span></a>'
    for a in ARTICLES:
        body = f'''<section class="page-head"><div class="wrap narrow">
<p class="crumbs"><a href="/">Pradžia</a> › <a href="/papildoma-informacija/">Patarimai</a></p>
<h1>{E(a["title"])}</h1>
<p class="small center">{E(a["author"])} · {a["date"]}</p>
</div></section>
<section><div class="wrap narrow">{DIV}<div class="article">{a["body"]}</div>
<p class="t-teal center">Norite, kad langai žvilgėtų? Paskambinkite arba atsiųskite nuotraukas – pasakysime kainą.</p>
{pair("article")}
</div></section>'''
        pages.append(page(f'/{a["slug"]}/', a["title"] + " | " + SITE["name"], a["desc"], body,
            ld=[{"@context":"https://schema.org","@type":"Article","headline":a["title"],"datePublished":a["date"],
                 "author":{"@type":"Person","name":a["author"]},"publisher":{"@id":BASE+"/#business"},"mainEntityOfPage":BASE+f'/{a["slug"]}/'},
                crumbs_ld([("Pradžia","/"),("Patarimai","/papildoma-informacija/"),(a["title"],f'/{a["slug"]}/')])]))
        cards += f'<a class="svc" href="/{a["slug"]}/"><h3>{E(a["title"])}</h3><p>{E(a["desc"])}</p><span class="more">Skaityti →</span></a>'
    pages.append(page("/papildoma-informacija/", "Patarimai apie langų priežiūrą | " + SITE["name"],
        "Patarimai apie langų valymą ir priežiūrą Vilniuje: kodėl verta valyti langus reguliariai, kas yra kalkės ir kaip jų išvengti.",
        f'<section class="page-head"><div class="wrap narrow"><p class="crumbs"><a href="/">Pradžia</a> › Patarimai</p><h1>Patarimai</h1></div></section><section><div class="wrap">{DIV}<div class="svcs">{cards}</div></div></section>'))

    # PRIVACY
    pages.append(page("/privatumo-politika/", "Privatumo politika | " + SITE["name"],
        "Kaip " + SITE["name"] + " tvarko asmens duomenis ir naudoja slapukus.", SITE["privacy_html"]))

    # 404
    body404 = f'<section class="page-head"><div class="wrap narrow"><h1>Puslapis nerastas</h1><p class="t-teal lead">Tokio puslapio nėra. Grįžkite į <a href="/">pradžią</a> arba susisiekite:</p>{pair("404")}</div></section>'
    page("/404-page/", "Puslapis nerastas | " + SITE["name"], "Puslapis nerastas.", body404)
    os.replace(os.path.join(ROOT, "404-page", "index.html"), os.path.join(ROOT, "404.html")); os.rmdir(os.path.join(ROOT, "404-page"))

    # sitemap / robots
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod></url>\n" for p in pages) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("built", len(pages), "pages")

if __name__ == "__main__":
    build()
