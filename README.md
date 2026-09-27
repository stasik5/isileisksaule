# isileisksaule.lt

Static website for Įsileisk Saulę (window cleaning, Vilnius). Hosted on Hostinger, deployed from this repo.

## Editing
All texts, prices, services, reviews and FAQs live in `_build/content.py`. The page layout is in `_build/build.py`.

```bash
python3 _build/build.py   # regenerates index.html and all page folders
git add -A && git commit -m "..." && git push
```

Needs Python 3 with Pillow (`pip install pillow`).

## Structure
- `/` – home; one folder per service page (`/balkono-langu-valymas/` …)
- `/papildoma-informacija/` – tips list; articles have their own folders
- `assets/` – CSS + JS (consent banner, GA4 click tracking)
- `img/` – photos (WebP), logo, og image
- `.htaccess` – HTTPS, www→non-www, caching, noindex on non-live hosts

## Tracking
GA4 `G-DL4VGZ7YQM` with Consent Mode v2 (default denied, banner on first visit).
Click events: `click_call`, `click_whatsapp`, `click_viber`, `click_email`, plus `generate_lead` (param `method`).
Mark `generate_lead` as a key event in GA4 and import it into Google Ads as a conversion.
