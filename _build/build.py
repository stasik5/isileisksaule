#!/usr/bin/env python3
"""Generates the static site for isileisksaule.lt.

Edit the content in this file (and _build/content.py), then run:
    python3 _build/build.py
It writes the HTML pages into the repository root. Commit and push; Hostinger deploys the repo.
"""
import json, os, html, datetime
from content import SITE, SERVICES, REVIEWS, FAQ_HOME, ARTICLES, GALLERY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = SITE["url"]  # canonical base, no trailing slash
VER = datetime.date.today().strftime("%Y%m%d")
E = html.escape

ICON = {
 "phone": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6c0-1.1.9-2 2-2zm8 7.2L4.3 6.5H19.7L12 11.2zM4 8.4V18h16V8.4l-8 4.9-8-4.9z"/></svg>',
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.5l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.5.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg>',
}

def tel_link(loc, cls="btn btn-call", label=None):
    return f'<a class="{cls}" href="tel:{SITE["phone_e164"]}" data-loc="{loc}">{ICON["phone"]}{E(label or "Skambinti " + SITE["phone_display"])}</a>'

def mail_link(loc, cls="btn btn-mail", label="Siųsti nuotraukas el. paštu"):
    from urllib.parse import quote
    href = f'mailto:{SITE["email"]}?subject={quote(SITE["mail_subject"])}&body={quote(SITE["mail_body"])}'
    return f'<a class="{cls}" href="{href}" data-loc="{loc}">{ICON["mail"]}{E(label)}</a>'

def wa_link(loc, cls="btn btn-wa", label="Parašyti WhatsApp"):
    return f'<a class="{cls}" href="{SITE["whatsapp"]}" target="_blank" rel="noopener" data-loc="{loc}">{ICON["wa"]}{E(label)}</a>'

def ctas(loc):
    return f'<div class="btns">{tel_link(loc)}{mail_link(loc)}{wa_link(loc)}</div>'

def img(name, alt, w=None, h=None, lazy=True, cls=""):
    from PIL import Image
    p = os.path.join(ROOT, "img", name)
    if w is None:
        with Image.open(p) as im: w, h = im.size
    extra = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    if cls: extra += f' class="{cls}"'
    return f'<img src="/img/{name}" alt="{E(alt)}" width="{w}" height="{h}"{extra}>'

def business_ld():
    return {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "@id": BASE + "/#business",
      "name": SITE["name"],
      "legalName": SITE["legal_name"],
      "url": BASE + "/",
      "logo": BASE + "/img/logo.png",
      "image": BASE + "/img/og.jpg",
      "telephone": SITE["phone_e164"],
      "email": SITE["email"],
      "priceRange": "€€",
      "foundingDate": SITE["since"],
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
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}

def page(path, title, desc, body, ld=(), og_img="og.jpg"):
    url = BASE + path
    nav = "".join(f'<a href="{u}">{E(n)}</a>' for n,u in SITE["nav"])
    lds = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    ga = SITE["ga4"]
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
<meta name="theme-color" content="#39bec3">
<link rel="icon" href="/img/favicon.png" type="image/png">
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
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Meniu</button>
<nav class="nav" id="nav">{nav}<a class="tel" href="tel:{SITE["phone_e164"]}" data-loc="header">{SITE["phone_display"]}</a></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
<div class="grid">
<div><h3>{E(SITE["name"])}</h3><p>Langų valymas Vilniuje ir Vilniaus rajone nuo {SITE["since"]} m.</p><p>{E(SITE["legal_name"])}<br>Įm. k. {SITE["company_code"]}<br>{E(SITE["street"])}, Vilnius</p></div>
<div><h3>Kontaktai</h3><p><a href="tel:{SITE["phone_e164"]}" data-loc="footer">{SITE["phone_display"]}</a><br><a href="mailto:{SITE["email"]}" data-loc="footer">{SITE["email"]}</a><br><a href="{SITE["whatsapp"]}" target="_blank" rel="noopener" data-loc="footer">WhatsApp</a> · <a href="{SITE["viber"]}" data-loc="footer">Viber</a></p><p>Darbo laikas: {SITE["days_label"]} {SITE["opens"]}–{SITE["closes"]}<br>Sekmadienį nedirbame</p></div>
<div><h3>Paslaugos</h3><p>{"<br>".join(f'<a href="/{s["slug"]}/">{E(s["short"])}</a>' for s in SERVICES)}</p></div>
<div><h3>Daugiau</h3><p><a href="/papildoma-informacija/">Patarimai</a><br><a href="{SITE["gbp"]}" target="_blank" rel="noopener">Atsiliepimai Google</a><br><a href="/privatumo-politika/">Privatumo politika</a><br><a href="#" data-open-consent>Slapukų nustatymai</a></p></div>
</div>
<p class="small" style="margin-top:24px;color:#8b9ba0">© {datetime.date.today().year} {E(SITE["legal_name"])}</p>
</div></footer>
<div class="bar">{tel_link("mobile_bar", label="Skambinti")}{wa_link("mobile_bar", label="WhatsApp")}</div>
<div class="consent" id="consent" role="dialog" aria-label="Slapukai">
<strong>Slapukai</strong>
<p style="margin:.4em 0 0">Naudojame analitinius ir reklamos slapukus, kad matytume, kaip lankytojai randa mūsų svetainę, ir tobulintume reklamą. Jūs renkatės. <a href="/privatumo-politika/">Daugiau</a></p>
<div class="btns"><button class="btn btn-call" data-consent="all">Sutinku</button><button class="btn btn-ghost" data-consent="necessary">Tik būtini</button></div>
</div>
<script src="/assets/site.js?v={VER}" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f: f.write(doc)
    return path

def faq_html(faq):
    return "".join(f"<details><summary>{E(q)}</summary><p>{a}</p></details>" for q,a in faq)

def reviews_html(n=None):
    rs = REVIEWS[:n] if n else REVIEWS
    return "".join(f'<blockquote class="review"><p>{E(t)}</p><cite>{E(who)}</cite></blockquote>' for t,who in rs)

def gallery_html(items):
    return '<div class="gallery">' + "".join(f"<figure>{img(f, alt)}<figcaption>{E(alt)}</figcaption></figure>" for f,alt in items) + "</div>"

def price_rows():
    hl = ' class="hl"'
    return "".join(f'<tr{hl if r[2] else ""}><td>{r[0]}</td><td>{r[1]}</td></tr>' for r in SITE["prices"])

def build():
    pages = []
    # ---------- HOME ----------
    svc_cards = "".join(f'''<a class="card" href="/{s["slug"]}/"><span class="price-tag">{E(s["price_short"])}</span><h3>{E(s["h1"])}</h3><p>{E(s["card"])}</p><span class="more">Plačiau →</span></a>''' for s in SERVICES)
    steps = "".join(f"<li><strong>{E(a)}</strong> {E(b)}</li>" for a,b in SITE["steps"])
    home = f'''
<section class="hero"><div class="wrap">
<div>
<h1>Langų valymas Vilniuje</h1>
<p class="lead">Butų, namų ir verslo langai, balkonai, vitrinos. Aiški kaina už stiklą, savo įranga ir priemonės, po darbų – tvarka. Dirbame nuo {SITE["since"]} m.</p>
{ctas("hero")}
<ul class="trust"><li><span class="stars">★★★★★</span> 5,0 Google ({SITE["google_reviews"]} atsiliepimai)</li><li>~8 € už stiklą</li><li>Min. užsakymas 60 €</li><li>Vilnius ir Vilniaus r.</li></ul>
</div>
{img("biuro-pastato-langai-ir-terasa.webp", "Išvalyti biuro pastato langai Vilniuje", lazy=False)}
</div></section>

<section id="paslaugos"><div class="wrap">
<h2>Ką valome</h2>
<p class="lead">Dažniausiai užsakomas periodinis butų ir namų langų valymas. Sudėtingesniems darbams – atskiros paslaugos.</p>
<div class="grid g3">{svc_cards}</div>
</div></section>

<section class="alt" id="kainos"><div class="wrap">
<h2>Kainos</h2>
<p class="lead">Kaina skaičiuojama už stiklą, valant iš abiejų pusių. Vidutiniškai ~8 € už stiklą – tikslią kainą pasakysime pamatę nuotraukas.</p>
<table class="prices"><thead><tr><th>Paslauga</th><th>Kaina</th></tr></thead><tbody>{price_rows()}</tbody></table>
<div class="notice">{SITE["notice"]}</div>
{ctas("prices")}
</div></section>

<section><div class="wrap two">
<div>
<h2>Kaip dirbame</h2>
<ol class="steps">{steps}</ol>
</div>
{img("privataus-namo-langu-valymas.webp", "Privataus namo langai po valymo")}
</div></section>

<section class="alt" id="darbai"><div class="wrap">
<h2>Mūsų darbai</h2>
{gallery_html(GALLERY)}
</div></section>

<section id="atsiliepimai"><div class="wrap">
<h2>Atsiliepimai</h2>
<p class="lead"><span class="stars">★★★★★</span> 5,0 iš {SITE["google_reviews"]} atsiliepimų <a href="{SITE["gbp"]}" target="_blank" rel="noopener">Google</a>. Keletas klientų žodžių:</p>
<div class="grid g3">{reviews_html()}</div>
</div></section>

<section class="alt" id="apie"><div class="wrap two">
<div>
<h2>Apie mus</h2>
<p>Esame nedidelė mandagių specialistų komanda, nuo {SITE["since"]} metų valanti langus Vilniuje ir Vilniaus rajone. Langai ir vitrinos – namų ir verslo „veidas“, todėl dirbame atsakingai ir kruopščiai.</p>
<p>Langų valymas – ne tik grožis. Gatvės purvas, kieto vandens mineralai (kalkės) ir kiti nešvarumai ilgainiui įsigeria į stiklo paviršių. Tada net išvalius langus matosi pilkos dėmės ar „upeliai“, o juos pašalinti kainuoja gerokai brangiau. Reguliarus valymas to išvengia.</p>
<p>Po kiekvieno valymo pasiūlome priminti apie kitą – po 3 ar 6 mėnesių. Nereikės atsiminti ar vėl ieškoti mūsų kontaktų.</p>
</div>
{img("kavines-vitrinu-valymas.webp", "Kavinės vitrinos po valymo")}
</div></section>

<section><div class="wrap">
<h2>Dažni klausimai</h2>
{faq_html(FAQ_HOME)}
</div></section>

<section class="cta"><div class="wrap">
<h2>Sužinokite kainą per kelias minutes</h2>
<p>Paskambinkite – pasakysime preliminarią kainą ir laisvus laikus. Arba atsiųskite langų nuotraukas el. paštu ir gausite tikslią kainą. Trumpam klausimui – parašykite WhatsApp.</p>
<div class="btns">{tel_link("cta")}{mail_link("cta")}{wa_link("cta")}<a class="btn btn-ghost" href="{SITE["viber"]}" data-loc="cta">Viber</a></div>
</div></section>
'''
    pages.append(page("/", SITE["home_title"], SITE["home_desc"], home,
        ld=[business_ld(), faq_ld([(q, html.unescape(a)) for q,a in FAQ_HOME])]))

    # ---------- SERVICE PAGES ----------
    for s in SERVICES:
        others = "".join(f'<a class="card" href="/{o["slug"]}/"><h3>{E(o["h1"])}</h3><span class="more">Plačiau →</span></a>' for o in SERVICES if o is not s)[:]
        body = f'''
<section class="hero"><div class="wrap">
<div>
<p class="crumbs"><a href="/">Pradžia</a> › {E(s["short"])}</p>
<h1>{E(s["h1"])}</h1>
<p class="lead">{E(s["lead"])}</p>
{ctas("service_hero")}
<ul class="trust"><li>{E(s["price_short"])}</li><li><span class="stars">★★★★★</span> 5,0 Google</li><li>Dirbame nuo {SITE["since"]} m.</li></ul>
</div>
{img(s["image"], s["image_alt"], lazy=False)}
</div></section>
<section><div class="wrap two">
<div class="article">{s["body"]}</div>
<aside class="card"><h3>Kaina</h3><p>{s["price_detail"]}</p><div class="notice">{SITE["notice"]}</div><div class="stack">{tel_link("service_aside")}{mail_link("service_aside")}{wa_link("service_aside")}</div></aside>
</div></section>
<section class="alt"><div class="wrap">
<h2>Klausimai</h2>
{faq_html(s["faq"])}
</div></section>
<section><div class="wrap">
<h2>Kitos paslaugos</h2>
<div class="grid g3">{others}</div>
</div></section>
'''
        pages.append(page(f'/{s["slug"]}/', s["title"], s["desc"], body, og_img="og.jpg",
            ld=[business_ld(),
                {"@context":"https://schema.org","@type":"Service","name":s["h1"],"serviceType":s["short"],
                 "provider":{"@id":BASE+"/#business"},"areaServed":"Vilnius","url":BASE+f'/{s["slug"]}/'},
                crumbs_ld([("Pradžia","/"),(s["short"],f'/{s["slug"]}/')]),
                faq_ld([(q, html.unescape(a)) for q,a in s["faq"]])]))

    # ---------- ARTICLES ----------
    cards = ""
    for a in ARTICLES:
        body = f'''<section><div class="wrap article">
<p class="crumbs"><a href="/">Pradžia</a> › <a href="/papildoma-informacija/">Patarimai</a> › {E(a["title"])}</p>
<h1>{E(a["title"])}</h1>
<p class="small">{E(a["author"])} · {a["date"]}</p>
{a["body"]}
<div class="card" style="margin-top:28px"><h3>Norite, kad langai žvilgėtų?</h3><p>Paskambinkite arba atsiųskite nuotraukas – pasakysime kainą.</p>{ctas("article")}</div>
</div></section>'''
        pages.append(page(f'/{a["slug"]}/', a["title"] + " | " + SITE["name"], a["desc"], body,
            ld=[{"@context":"https://schema.org","@type":"Article","headline":a["title"],"datePublished":a["date"],
                 "author":{"@type":"Person","name":a["author"]},"publisher":{"@id":BASE+"/#business"},"mainEntityOfPage":BASE+f'/{a["slug"]}/'},
                crumbs_ld([("Pradžia","/"),("Patarimai","/papildoma-informacija/"),(a["title"],f'/{a["slug"]}/')])]))
        cards += f'<a class="card" href="/{a["slug"]}/"><h3>{E(a["title"])}</h3><p>{E(a["desc"])}</p><span class="more">Skaityti →</span></a>'
    pages.append(page("/papildoma-informacija/", "Patarimai apie langų priežiūrą | " + SITE["name"],
        "Patarimai apie langų valymą ir priežiūrą Vilniuje: kodėl verta valyti langus reguliariai, kaip išvengti kalkių dėmių.",
        f'<section><div class="wrap"><p class="crumbs"><a href="/">Pradžia</a> › Patarimai</p><h1>Patarimai</h1><div class="grid g2">{cards}</div></div></section>'))

    # ---------- PRIVACY ----------
    pages.append(page("/privatumo-politika/", "Privatumo politika | " + SITE["name"],
        "Kaip " + SITE["name"] + " tvarko asmens duomenis ir naudoja slapukus.", SITE["privacy_html"]))

    # ---------- 404 ----------
    body404 = f'<section><div class="wrap center"><h1>Puslapis nerastas</h1><p class="lead">Tokio puslapio nėra. Grįžkite į <a href="/">pradžią</a> arba susisiekite:</p><div class="btns" style="justify-content:center">{tel_link("404")}{wa_link("404")}</div></div></section>'
    page("/404-page/", "Puslapis nerastas | " + SITE["name"], "Puslapis nerastas.", body404)
    os.replace(os.path.join(ROOT, "404-page", "index.html"), os.path.join(ROOT, "404.html")); os.rmdir(os.path.join(ROOT, "404-page"))

    # ---------- sitemap / robots ----------
    today = datetime.date.today().isoformat()
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
         "".join(f"  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod></url>\n" for p in pages) + "</urlset>\n"
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(sm)
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("built", len(pages), "pages")

if __name__ == "__main__":
    build()
