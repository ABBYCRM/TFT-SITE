# TFT Legal Service — Official Website

Enterprise rebuild of [tftlegalservice.com](https://www.tftlegalservice.com).

## Stack

- Static HTML5 / CSS3 / vanilla JS (no framework lock-in)
- Schema.org JSON-LD on every page
- `robots.txt` with explicit AI crawler allow rules
- `llms.txt` for LLM / answer-engine discovery
- XML sitemap with image extensions
- Open Graph + Twitter cards
- PWA manifest + security headers (Netlify)

## Local preview

```bash
cd TFT-SITE
python3 -m http.server 8080
# open http://localhost:8080
```

## Pages

| Path | Purpose |
|------|---------|
| `/` | Home |
| `/about.html` | Company + founders |
| `/torts.html` | Mass tort pathways |
| `/mva.html` | Motor vehicle accidents |
| `/ssdi.html` | SSDI |
| `/mortgage.html` | Mortgage refinancing |
| `/contact.html` | Contact / intake |
| `/compliance.html` | Compliance policy |
| `/privacy.html` | Privacy policy |

## SEO / AI crawl assets

- `/robots.txt`
- `/sitemap.xml`
- `/llms.txt`
- `/humans.txt`
- `/.well-known/security.txt`
- `/site.webmanifest`

## Brand

- **Company:** TFT Legal Service
- **Email:** info@tftlegalservice.com
- **Instagram:** [@tftlegalservice](https://www.instagram.com/tftlegalservice)
- **Founders:** Giselle Leite; Dr. Gabriel Saboia (Legal Marketing Partner)

## Regenerating pages

Shared chrome + SEO meta are produced by:

```bash
python3 scripts/generate_pages.py
```

## Disclaimer

TFT Legal Service is a lead generation company and does not provide legal services. No attorney-client relationship is formed through this website.
