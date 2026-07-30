#!/usr/bin/env python3
"""Generate all TFT Legal Service HTML pages with enterprise SEO + shared chrome."""

from pathlib import Path

ROOT = Path("/workspace/TFT-SITE")
SITE = "https://www.tftlegalservice.com"
ORG_PHONE = ""  # not published on source site
EMAIL = "info@tftlegalservice.com"

BRAND_SVG = """<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">
  <g fill="none" stroke="#C6A15B" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
    <path d="M32 12v40"/><path d="M24 52h16"/><path d="M16 20h32"/>
    <path d="M22 20l-7 14a7.5 7.5 0 0 0 15 0l-7-14"/>
    <path d="M42 20l-7 14a7.5 7.5 0 0 0 15 0l-7-14"/>
  </g>
  <circle cx="32" cy="12" r="2.6" fill="#C6A15B"/>
</svg>"""

ICON_ARROW = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>"""
ICON_PLUS = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>"""
ICON_CHECK = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>"""


def head(meta: dict) -> str:
    title = meta["title"]
    desc = meta["description"]
    path = meta["path"]
    canon = f"{SITE}{path}"
    og_type = meta.get("og_type", "website")
    keywords = meta.get("keywords", "")
    robots = meta.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")
    jsonld = meta.get("jsonld", [])
    extra = meta.get("extra_head", "")

    scripts = "\n".join(
        f'<script type="application/ld+json">\n{j}\n</script>' for j in jsonld
    )

    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="TFT Legal Service">
  <meta name="publisher" content="TFT Legal Service">
  <meta name="robots" content="{robots}">
  <meta name="googlebot" content="{robots}">
  <meta name="bingbot" content="index, follow">
  <meta name="language" content="English">
  <meta name="geo.region" content="US">
  <meta name="rating" content="general">
  <meta name="referrer" content="strict-origin-when-cross-origin">
  <meta name="theme-color" content="#0c1b33">
  <meta name="color-scheme" content="light">
  <meta name="format-detection" content="telephone=yes">
  <link rel="canonical" href="{canon}">
  <link rel="alternate" hreflang="en-us" href="{canon}">
  <link rel="alternate" hreflang="x-default" href="{canon}">
  <link rel="author" href="/humans.txt">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">

  <!-- Open Graph -->
  <meta property="og:type" content="{og_type}">
  <meta property="og:site_name" content="TFT Legal Service">
  <meta property="og:locale" content="en_US">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canon}">
  <meta property="og:image" content="{SITE}/assets/img/og-share.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="TFT Legal Service — Connecting people with trusted legal representation">

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{SITE}/assets/img/og-share.jpg">
  <meta name="twitter:image:alt" content="TFT Legal Service">

  <!-- AI / discovery hints -->
  <link rel="describedby" href="/llms.txt" type="text/plain" title="LLM / AI site summary">
  <meta name="ai-content-declaration" content="human-authored company website content">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css">
{extra}
{scripts}
</head>
"""


ORG_JSONLD = """{
  "@context": "https://schema.org",
  "@type": ["Organization", "ProfessionalService"],
  "@id": "https://www.tftlegalservice.com/#organization",
  "name": "TFT Legal Service",
  "alternateName": ["TFT Legal", "TFT Legal Services"],
  "url": "https://www.tftlegalservice.com/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.tftlegalservice.com/assets/img/icon-512.png",
    "width": 512,
    "height": 512
  },
  "image": "https://www.tftlegalservice.com/assets/img/og-share.jpg",
  "description": "TFT Legal Service is a lead generation and legal marketing company that connects individuals with qualified law firms specializing in mass torts, motor vehicle accidents, SSDI, and related practice areas.",
  "email": "info@tftlegalservice.com",
  "sameAs": [
    "https://www.instagram.com/tftlegalservice"
  ],
  "foundingDate": "2024",
  "founder": {
    "@type": "Person",
    "name": "Giselle Leite",
    "jobTitle": "Founder",
    "description": "Brazilian-American entrepreneur and law graduate who founded TFT Legal Service to connect people with accessible, reputable legal representation."
  },
  "employee": [
    {
      "@type": "Person",
      "name": "Giselle Leite",
      "jobTitle": "Founder"
    },
    {
      "@type": "Person",
      "name": "Dr. Gabriel Saboia",
      "jobTitle": "Legal Marketing Partner"
    }
  ],
  "areaServed": {
    "@type": "Country",
    "name": "United States"
  },
  "knowsAbout": [
    "Mass Tort Lead Generation",
    "Motor Vehicle Accident Referrals",
    "Social Security Disability Insurance",
    "Legal Marketing Compliance",
    "TCPA Compliance"
  ],
  "slogan": "Connecting people with trusted legal representation",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "info@tftlegalservice.com",
    "availableLanguage": ["English", "Portuguese"],
    "hoursAvailable": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "19:00"
    }
  },
  "disclaimer": "TFT Legal Service is a lead generation company and does not provide legal services. No attorney-client relationship is formed through use of this website."
}"""

WEBSITE_JSONLD = """{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.tftlegalservice.com/#website",
  "url": "https://www.tftlegalservice.com/",
  "name": "TFT Legal Service",
  "description": "Official website of TFT Legal Service — connecting individuals with qualified law firms for mass torts, MVA, SSDI, and more.",
  "publisher": { "@id": "https://www.tftlegalservice.com/#organization" },
  "inLanguage": "en-US",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://www.tftlegalservice.com/contact.html?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}"""


def breadcrumb(items):
    """items: list of (name, url)"""
    els = []
    for i, (name, url) in enumerate(items, 1):
        els.append(
            f"""{{
      "@type": "ListItem",
      "position": {i},
      "name": "{name}",
      "item": "{SITE}{url}"
    }}"""
        )
    return (
        '{\n  "@context": "https://schema.org",\n  "@type": "BreadcrumbList",\n  "itemListElement": [\n    '
        + ",\n    ".join(els)
        + "\n  ]\n}"
    )


NAV = [
    ("Home", "/", "index"),
    ("Mass Torts", "/torts.html", "torts"),
    ("MVA", "/mva.html", "mva"),
    ("SSDI", "/ssdi.html", "ssdi"),
    ("Mortgage", "/mortgage.html", "mortgage"),
    ("About", "/about.html", "about"),
    ("Contact", "/contact.html", "contact"),
]


def header(active: str) -> str:
    links = []
    for label, href, key in NAV:
        if key == "contact":
            continue
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'      <a href="{href}"{cur}>{label}</a>')
    cta_cur = ' aria-current="page"' if active == "contact" else ""
    return f"""<a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header" role="banner">
    <div class="container header-inner">
      <a class="brand" href="/" aria-label="TFT Legal Service — Home">
        <span class="brand-mark">{BRAND_SVG}</span>
        <span class="brand-text">
          <span class="brand-name">TFT <em>Legal</em></span>
          <span class="brand-sub">Service</span>
        </span>
      </a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open menu">
        <span></span>
      </button>
      <nav class="main-nav" id="primary-nav" aria-label="Primary">
{chr(10).join(links)}
        <a class="btn btn--gold btn--sm nav-cta" href="/contact.html"{cta_cur}>Get Connected</a>
      </nav>
    </div>
  </header>
"""


def footer() -> str:
    return f"""  <footer class="site-footer" role="contentinfo">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="/" aria-label="TFT Legal Service">
            <span class="brand-mark">{BRAND_SVG}</span>
            <span class="brand-text">
              <span class="brand-name" style="color:#fff">TFT <em>Legal</em></span>
              <span class="brand-sub">Service</span>
            </span>
          </a>
          <p style="margin-top:1.2rem">We connect individuals with reputable, experienced law firms across mass torts, motor vehicle accidents, SSDI, and more — with ethics and compliance at the core.</p>
          <a class="social-link" href="https://www.instagram.com/tftlegalservice" target="_blank" rel="noopener noreferrer me" aria-label="TFT Legal Service on Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>
            @tftlegalservice
          </a>
        </div>
        <div>
          <h4>Practice Areas</h4>
          <ul class="footer-links">
            <li><a href="/torts.html">Mass Torts</a></li>
            <li><a href="/mva.html">Motor Vehicle Accidents</a></li>
            <li><a href="/ssdi.html">SSDI Benefits</a></li>
            <li><a href="/mortgage.html">Mortgage Refinancing</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul class="footer-links">
            <li><a href="/about.html">About Us</a></li>
            <li><a href="/contact.html">Contact</a></li>
            <li><a href="/compliance.html">Compliance Policy</a></li>
            <li><a href="/privacy.html">Privacy Policy</a></li>
          </ul>
        </div>
        <div>
          <h4>Contact</h4>
          <div class="footer-contact">
            <div><a href="mailto:{EMAIL}">{EMAIL}</a></div>
            <div>Mon–Fri · 9:00 am – 7:00 pm</div>
            <div>Saturday &amp; Sunday · Closed</div>
          </div>
        </div>
      </div>
      <div class="footer-legal">
        <div class="disclaimer">
          <strong>ATTORNEY ADVERTISING · LEGAL DISCLAIMER</strong><br>
          TFT Legal Service is a lead generation company and does not provide legal services. We connect individuals with qualified law firms specializing in mass tort cases and related matters. By using our services, you acknowledge that TFT Legal Service is not acting as your attorney and that no attorney-client relationship is formed. The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. Prior results do not guarantee a similar outcome. Consent to communications is not a condition of receiving services and may be revoked at any time.
        </div>
        <div class="footer-bottom">
          <p>© <span data-year>2026</span> TFT Legal Service. All rights reserved.</p>
          <nav aria-label="Legal">
            <a href="/compliance.html">Compliance</a>
            <a href="/privacy.html">Privacy</a>
            <a href="/llms.txt">AI / LLM Info</a>
          </nav>
        </div>
      </div>
    </div>
  </footer>

  <div class="cookie-banner" role="dialog" aria-label="Cookie notice" aria-live="polite">
    <p>We use cookies to analyze traffic and improve your experience. By continuing, you agree to aggregated analytics. See our <a href="/privacy.html">Privacy Policy</a>.</p>
    <button class="btn btn--gold btn--sm" type="button" data-cookie-accept>Accept</button>
  </div>
  <script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(crumbs, title, lede, eyebrow="TFT Legal Service"):
    crumbs_html = []
    for i, (name, href) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            crumbs_html.append(f'<li aria-current="page">{name}</li>')
        else:
            crumbs_html.append(f'<li><a href="{href}">{name}</a></li>')
    return f"""  <section class="page-hero">
    <div class="container">
      <nav aria-label="Breadcrumb">
        <ol class="breadcrumbs">
          {''.join(crumbs_html)}
        </ol>
      </nav>
      <p class="eyebrow">{eyebrow}</p>
      <h1 class="display-lg">{title}</h1>
      <p class="lede">{lede}</p>
    </div>
  </section>
"""


def write(name: str, html: str):
    path = ROOT / name
    path.write_text(html, encoding="utf-8")
    print("wrote", path.name, len(html), "bytes")


# ---------------------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------------------
index_faq = """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Is TFT Legal Service a law firm?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. TFT Legal Service is a lead generation and legal marketing company. We connect individuals with qualified partner law firms. We do not provide legal advice and no attorney-client relationship is formed through our website."
      }
    },
    {
      "@type": "Question",
      "name": "What practice areas does TFT Legal Service cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We connect people with counsel for mass tort litigation (including rideshare abuse, social media and video game addiction, Roblox abuse, Depo-Provera, and institutional sexual abuse cases), motor vehicle accidents (MVA), Social Security Disability Insurance (SSDI), and mortgage refinancing referrals."
      }
    },
    {
      "@type": "Question",
      "name": "How does the referral process work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "We use targeted digital marketing and a comprehensive intake process to identify and screen potential clients, then refer qualified leads exclusively to partner law firms in real time — in compliance with TCPA and ethical advertising standards."
      }
    },
    {
      "@type": "Question",
      "name": "How can I contact TFT Legal Service?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Email info@tftlegalservice.com or use the contact form on tftlegalservice.com. Hours are Monday through Friday, 9:00 am to 7:00 pm."
      }
    }
  ]
}"""

index_html = head({
    "title": "TFT Legal Service | Mass Tort Lead Generation & Legal Marketing",
    "description": "TFT Legal Service connects individuals with qualified law firms for mass torts, motor vehicle accidents, SSDI, and more. Ethical, TCPA-compliant legal marketing founded by Giselle Leite.",
    "path": "/",
    "keywords": "TFT Legal Service, mass tort lead generation, legal marketing, motor vehicle accident lawyer referral, SSDI help, rideshare abuse lawsuit, Depo-Provera lawsuit, TCPA compliant leads, Giselle Leite",
    "jsonld": [ORG_JSONLD, WEBSITE_JSONLD, index_faq],
}) + f"""<body>
{header("index")}
  <main id="main">
    <section class="hero" aria-label="Hero">
      <div class="hero-media" aria-hidden="true">
        <img src="/assets/img/hero-scales.jpg" width="1600" height="1067" alt="" decoding="async" fetchpriority="high">
      </div>
      <div class="container">
        <p class="hero-brand-lockup">TFT Legal<span>Service</span></p>
        <h1 class="display-xl">Connecting people with <span class="accent">trusted legal</span> representation</h1>
        <p class="lede">Ethical legal marketing that identifies, screens, and refers qualified clients to reputable law firms nationwide.</p>
        <div class="hero-actions">
          <a class="btn btn--gold" href="/contact.html">Get Connected {ICON_ARROW}</a>
          <a class="btn btn--ghost-light" href="/torts.html">Explore Mass Torts</a>
        </div>
      </div>
      <div class="scroll-hint" aria-hidden="true"></div>
    </section>

    <section class="section" id="practice-areas">
      <div class="container">
        <div class="section-head section-head--center reveal">
          <p class="eyebrow eyebrow--center">Practice Areas</p>
          <h2 class="display-md">Where we connect people with counsel</h2>
          <p class="lede">Focused pathways across mass tort litigation, injury claims, disability benefits, and financial referrals — each with dedicated intake and partner firms.</p>
        </div>
        <div class="grid grid--2" data-stagger>
          <article class="card reveal">
            <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 3v18M8 21h8M4 7h16"/><path d="m7 7-3 6a3.5 3.5 0 1 0 7 0L8 7"/><path d="m17 7-3 6a3.5 3.5 0 1 0 7 0l-3-6"/></svg></div>
            <span class="tag">High Priority</span>
            <h3>Mass Torts</h3>
            <p>Rideshare abuse, social media &amp; video game addiction, Roblox abuse, Depo-Provera, and institutional sexual abuse litigation across California and Illinois.</p>
            <a class="card-link" href="/torts.html">View mass tort cases {ICON_ARROW}</a>
          </article>
          <article class="card reveal">
            <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 17h14l-1.5-5H6.5L5 17Z"/><path d="M7 17v2M17 17v2M8 12V8l3-3h5l2 3v4"/></svg></div>
            <span class="tag">Injury Claims</span>
            <h3>Motor Vehicle Accidents</h3>
            <p>Legal claims after car, truck, or rideshare crashes — connecting injured parties with attorneys who pursue damages for medical costs, lost wages, and pain.</p>
            <a class="card-link" href="/mva.html">Learn about MVA claims {ICON_ARROW}</a>
          </article>
          <article class="card reveal">
            <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h10M7 13h6"/></svg></div>
            <span class="tag">Federal Benefits</span>
            <h3>Social Security Disability</h3>
            <p>SSDI provides monthly support for people unable to work due to serious long-term conditions. We help connect applicants with experienced disability counsel.</p>
            <a class="card-link" href="/ssdi.html">Explore SSDI support {ICON_ARROW}</a>
          </article>
          <article class="card reveal">
            <div class="card-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 10.5 12 4l9 6.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1v-9.5Z"/></svg></div>
            <span class="tag">Home Finance</span>
            <h3>Mortgage Refinancing</h3>
            <p>When rates, terms, or equity access can improve cash flow, we help homeowners explore refinancing options through trusted referral partners.</p>
            <a class="card-link" href="/mortgage.html">See refinancing options {ICON_ARROW}</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--tight stats-band">
      <div class="container">
        <div class="stats-grid" data-stagger>
          <div class="stat reveal"><strong data-count="100" data-suffix="%">0%</strong><span>Ethical screening focus</span></div>
          <div class="stat reveal"><strong>TCPA</strong><span>Aligned outreach practices</span></div>
          <div class="stat reveal"><strong data-count="7" data-suffix="+">0+</strong><span>Active tort categories</span></div>
          <div class="stat reveal"><strong>Excl.</strong><span>Partner firm referrals</span></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container split">
        <div class="media-frame reveal">
          <img src="/assets/img/hero-scales.jpg" width="1600" height="1067" alt="Scales of justice representing ethical legal marketing and client advocacy" loading="lazy" decoding="async">
          <div class="media-badge"><strong>Ethics first</strong> Transparent advertising. Informed consent. No guaranteed outcomes.</div>
        </div>
        <div class="reveal">
          <p class="eyebrow">Our Mission</p>
          <h2 class="display-md">Exceptional connections, tailored to each case</h2>
          <p class="lede" style="margin-bottom:1.5rem">At TFT Legal, we strive to provide exceptional legal connections tailored to your needs — matching people with firms prepared to pursue justice against corporate negligence and serious injury.</p>
          <ul class="check-list">
            <li>{ICON_CHECK}<div><strong>Expertise from media &amp; law</strong><span>Founded by Giselle Leite — entrepreneur, law graduate, and former media personality — with deep insight into how people find help.</span></div></li>
            <li>{ICON_CHECK}<div><strong>Quality over volume</strong><span>Rigorous screening so only qualified leads reach partner law firms.</span></div></li>
            <li>{ICON_CHECK}<div><strong>Compliance by design</strong><span>TCPA adherence, data privacy, and ABA-aligned ethical standards.</span></div></li>
          </ul>
          <div style="margin-top:2rem;display:flex;flex-wrap:wrap;gap:0.9rem">
            <a class="btn btn--navy" href="/about.html">About TFT Legal {ICON_ARROW}</a>
            <a class="btn btn--ghost" href="/compliance.html">Compliance Policy</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow" style="color:var(--gold-light)">The Process</p>
          <h2 class="display-md">Three steps. One standard of care.</h2>
          <p class="lede">A clear path from first outreach to a connection with qualified counsel — built for people seeking justice and for firms that demand quality.</p>
        </div>
        <ol class="timeline" data-stagger>
          <li class="reveal">
            <h3>Identify &amp; reach</h3>
            <p>Advanced digital marketing identifies individuals who may have been harmed by specific products, platforms, or incidents — with truthful, non-misleading creative.</p>
          </li>
          <li class="reveal">
            <h3>Screen &amp; qualify</h3>
            <p>Our intake team conducts thorough screenings against partner law firm criteria, elevating relevance and readiness before any referral is made.</p>
          </li>
          <li class="reveal">
            <h3>Connect exclusively</h3>
            <p>Qualified leads are delivered exclusively and in real time to partner firms — giving counsel a competitive edge while giving people a clear next step toward justice.</p>
          </li>
        </ol>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head section-head--center reveal">
          <p class="eyebrow eyebrow--center">Common Questions</p>
          <h2 class="display-md">Clarity before you reach out</h2>
        </div>
        <div class="faq" style="max-width:820px;margin-inline:auto" data-stagger>
          <div class="faq-item reveal">
            <button class="faq-q" type="button" aria-expanded="false">Is TFT Legal Service a law firm? {ICON_PLUS}</button>
            <div class="faq-a"><div class="faq-a-inner">No. We are a lead generation and legal marketing company. We connect you with qualified partner law firms. We do not give legal advice, and contacting us does not create an attorney-client relationship.</div></div>
          </div>
          <div class="faq-item reveal">
            <button class="faq-q" type="button" aria-expanded="false">What kinds of cases do you handle referrals for? {ICON_PLUS}</button>
            <div class="faq-a"><div class="faq-a-inner">Mass torts (rideshare abuse, social media and video game addiction, Roblox abuse, Depo-Provera, institutional sexual abuse), motor vehicle accidents, SSDI claims, and mortgage refinancing referrals.</div></div>
          </div>
          <div class="faq-item reveal">
            <button class="faq-q" type="button" aria-expanded="false">Do you guarantee a settlement or outcome? {ICON_PLUS}</button>
            <div class="faq-a"><div class="faq-a-inner">Never. We do not guarantee legal outcomes or financial compensation. Prior results of any firm do not guarantee a similar outcome in your matter.</div></div>
          </div>
          <div class="faq-item reveal">
            <button class="faq-q" type="button" aria-expanded="false">How do I get started? {ICON_PLUS}</button>
            <div class="faq-a"><div class="faq-a-inner">Email <a href="mailto:{EMAIL}">{EMAIL}</a> or use our <a href="/contact.html">contact form</a>. Our team is available Monday–Friday, 9:00 am – 7:00 pm.</div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <p class="eyebrow" style="color:var(--gold-light);justify-content:center">Ready when you are</p>
          <h2 class="display-md">Take the first step toward the right counsel</h2>
          <p>Whether you need help after an injury, a mass tort inquiry, or an SSDI question — tell us your situation and we will help connect you with a qualified firm.</p>
          <div class="hero-actions">
            <a class="btn btn--gold" href="/contact.html">Contact TFT Legal {ICON_ARROW}</a>
            <a class="btn btn--ghost-light" href="mailto:{EMAIL}">Email {EMAIL}</a>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("index.html", index_html)

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------
about_jsonld = """{
  "@context": "https://schema.org",
  "@type": "AboutPage",
  "@id": "https://www.tftlegalservice.com/about.html#aboutpage",
  "url": "https://www.tftlegalservice.com/about.html",
  "name": "About TFT Legal Service",
  "description": "Learn about TFT Legal Service, founded by Giselle Leite with legal marketing partner Dr. Gabriel Saboia.",
  "isPartOf": { "@id": "https://www.tftlegalservice.com/#website" },
  "about": { "@id": "https://www.tftlegalservice.com/#organization" },
  "mainEntity": { "@id": "https://www.tftlegalservice.com/#organization" }
}"""

about_people = """{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "TFT Legal Service Leadership",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Person",
        "name": "Giselle Leite",
        "jobTitle": "Founder",
        "worksFor": { "@id": "https://www.tftlegalservice.com/#organization" },
        "image": "https://www.tftlegalservice.com/assets/img/giselle-leite.jpg",
        "description": "Brazilian-American entrepreneur and law graduate who founded TFT Legal Service after recognizing a growing need for accessible legal assistance among her audience."
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Person",
        "name": "Dr. Gabriel Saboia",
        "jobTitle": "Legal Marketing Partner",
        "worksFor": { "@id": "https://www.tftlegalservice.com/#organization" },
        "image": "https://www.tftlegalservice.com/assets/img/gabriel-saboia.jpg",
        "description": "Brazilian surgeon and cancer survivor dedicated to mass tort legal marketing — connecting victims and families with opportunities to seek justice against corporate negligence. He does not provide medical services through TFT Legal Service."
      }
    }
  ]
}"""

about_html = head({
    "title": "About Us | TFT Legal Service — Giselle Leite & Dr. Gabriel Saboia",
    "description": "TFT Legal Service was founded by Giselle Leite, a Brazilian-American entrepreneur and law graduate. Partner Dr. Gabriel Saboia brings a unique perspective to mass tort legal marketing.",
    "path": "/about.html",
    "keywords": "Giselle Leite TFT Legal, Gabriel Saboia, about TFT Legal Service, legal marketing company founders, mass tort lead generation company",
    "jsonld": [ORG_JSONLD, about_jsonld, about_people, breadcrumb([("Home", "/"), ("About Us", "/about.html")])],
}) + f"""<body>
{header("about")}
  <main id="main">
{page_hero([("Home", "/"), ("About Us", "#")], "Built to connect people with justice", "From media and medicine to ethical legal marketing — the story behind TFT Legal Service.")}

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow">Our Story</p>
          <h2 class="display-md">Why TFT Legal Service exists</h2>
          <p>TFT Legal Service was founded by <strong>Giselle Leite</strong>, a Brazilian-American entrepreneur and law graduate in Brazil, who began her career as a media personality and later recognized a growing need for accessible legal assistance among her audience.</p>
          <p>With a strong foundation in law, communications, and a deep commitment to helping others, Giselle transitioned from hosting a widely followed YouTube channel in Brazil to establishing TFT Legal Service — a company dedicated to connecting individuals with reputable and experienced legal representation across various practice areas.</p>
          <div class="notice" style="margin-top:1.5rem"><strong>Important:</strong> TFT Legal Service is a lead generation company and does not provide legal services. We connect individuals with qualified law firms. No attorney-client relationship is formed through this website.</div>
        </div>
        <div class="media-frame reveal">
          <img src="/assets/img/about-mission.jpg" width="1400" height="933" alt="Professional workspace representing TFT Legal Service operations" loading="lazy" decoding="async">
        </div>
      </div>
    </section>

    <section class="section section--tight" style="background:linear-gradient(180deg,#fff,var(--ivory))">
      <div class="container">
        <div class="section-head section-head--center reveal">
          <p class="eyebrow eyebrow--center">Leadership</p>
          <h2 class="display-md">The people behind the mission</h2>
          <p class="lede">Experience in law, media, and medicine — united by a commitment to turn hardship into a path toward justice.</p>
        </div>
        <div class="grid grid--2" data-stagger>
          <article class="team-card reveal">
            <div class="team-photo">
              <img src="/assets/img/giselle-leite.jpg" width="800" height="823" alt="Giselle Leite, Founder of TFT Legal Service" loading="lazy" decoding="async">
            </div>
            <div class="team-body">
              <span class="role">Founder</span>
              <h3>Giselle Leite</h3>
              <p>Brazilian-American entrepreneur and law graduate. After building a widely followed media presence in Brazil, she founded TFT Legal Service to make reputable legal representation more accessible to people who need it.</p>
            </div>
          </article>
          <article class="team-card reveal">
            <div class="team-photo">
              <img src="/assets/img/gabriel-saboia.jpg" width="800" height="1067" alt="Dr. Gabriel Saboia, Legal Marketing Partner at TFT Legal Service" loading="lazy" decoding="async">
            </div>
            <div class="team-body">
              <span class="role">Legal Marketing Partner</span>
              <h3>Dr. Gabriel Saboia</h3>
              <p>Brazilian surgeon and cancer survivor with a unique understanding of the emotional, financial, and social impact illness can have on families. He dedicates part of his career to mass torts through legal marketing — not medical services — connecting victims and families with opportunities to seek justice against corporate negligence. For him, every connection is more than a lead: it is the first step toward transforming pain into justice.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">What We Deliver</p>
          <h2 class="display-md">Services built for law firms &amp; clients</h2>
        </div>
        <div class="grid grid--3" data-stagger>
          <article class="card reveal">
            <div class="card-icon">{ICON_CHECK}</div>
            <h3>Targeted Lead Generation</h3>
            <p>Advanced digital marketing strategies to identify and reach individuals who may have been harmed by specific products or substances.</p>
          </article>
          <article class="card reveal">
            <div class="card-icon">{ICON_CHECK}</div>
            <h3>Comprehensive Intake</h3>
            <p>Thorough screenings so leads meet the specific criteria set by partner law firms — elevating quality and relevance of every referral.</p>
          </article>
          <article class="card reveal">
            <div class="card-icon">{ICON_CHECK}</div>
            <h3>Exclusive Partnerships</h3>
            <p>We work closely with law firms to provide exclusive, real-time leads — a competitive edge in acquiring new cases.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow" style="color:var(--gold-light)">Compliance &amp; Ethics</p>
          <h2 class="display-md">Standards that withstand scrutiny</h2>
          <p>We understand the importance of maintaining ethical standards and complying with legal regulations in the lead generation industry. Our practices adhere to the Telephone Consumer Protection Act (TCPA) and other relevant state and federal laws.</p>
          <p>We prioritize transparency, consent, and data privacy. All advertising materials are truthful and not misleading — avoiding any guarantees of financial compensation or outcomes.</p>
          <a class="btn btn--gold" href="/compliance.html" style="margin-top:1rem">Read Compliance Policy {ICON_ARROW}</a>
        </div>
        <ul class="check-list reveal">
          <li>{ICON_CHECK}<div><strong>TCPA aligned</strong><span>Lawful generation of leads with informed consent.</span></div></li>
          <li>{ICON_CHECK}<div><strong>No outcome guarantees</strong><span>Honest advertising that never promises settlements.</span></div></li>
          <li>{ICON_CHECK}<div><strong>Data privacy</strong><span>Respect for personal information throughout intake.</span></div></li>
          <li>{ICON_CHECK}<div><strong>ABA-conscious</strong><span>Practices designed to uphold the integrity of the legal profession.</span></div></li>
        </ul>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <h2 class="display-md">Partner with TFT Legal Service</h2>
          <p>Law firms seeking exclusive, screened referrals — or individuals looking for a path to counsel — can reach us anytime.</p>
          <div class="hero-actions">
            <a class="btn btn--gold" href="/contact.html">Contact Us {ICON_ARROW}</a>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("about.html", about_html)

print("phase1 done")

# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------
contact_jsonld = """{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "url": "https://www.tftlegalservice.com/contact.html",
  "name": "Contact TFT Legal Service",
  "description": "Contact TFT Legal Service by email or form. Hours Monday–Friday 9:00 am – 7:00 pm.",
  "mainEntity": { "@id": "https://www.tftlegalservice.com/#organization" }
}"""

contact_html = head({
    "title": "Contact Us | TFT Legal Service — Get Connected with Counsel",
    "description": "Contact TFT Legal Service at info@tftlegalservice.com. Hours Mon–Fri 9am–7pm. Tell us about your situation and we will help connect you with a qualified law firm.",
    "path": "/contact.html",
    "keywords": "contact TFT Legal Service, info@tftlegalservice.com, legal lead generation contact, mass tort intake",
    "jsonld": [ORG_JSONLD, contact_jsonld, breadcrumb([("Home", "/"), ("Contact", "/contact.html")])],
}) + f"""<body>
{header("contact")}
  <main id="main">
{page_hero([("Home", "/"), ("Contact", "#")], "Get in touch", "Share your situation. Our team will help connect you with qualified legal representation — or discuss partnership opportunities with your firm.")}

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow">Direct Lines</p>
          <h2 class="display-md">We respond during business hours</h2>
          <ul class="info-list" style="margin:2rem 0">
            <li>
              <span class="info-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 6h16v12H4z"/><path d="m4 7 8 6 8-6"/></svg></span>
              <div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
            </li>
            <li>
              <span class="info-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></span>
              <div><strong>Hours</strong><span class="val">Monday – Friday · 9:00 am – 7:00 pm</span></div>
            </li>
            <li>
              <span class="info-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/></svg></span>
              <div><strong>Instagram</strong><a href="https://www.instagram.com/tftlegalservice" target="_blank" rel="noopener noreferrer">@tftlegalservice</a></div>
            </li>
          </ul>
          <table class="hours-table" aria-label="Business hours">
            <tbody>
              <tr><td>Monday</td><td>09:00 am – 07:00 pm</td></tr>
              <tr><td>Tuesday</td><td>09:00 am – 07:00 pm</td></tr>
              <tr><td>Wednesday</td><td>09:00 am – 07:00 pm</td></tr>
              <tr><td>Thursday</td><td>09:00 am – 07:00 pm</td></tr>
              <tr><td>Friday</td><td>09:00 am – 07:00 pm</td></tr>
              <tr class="is-closed"><td>Saturday</td><td>Closed</td></tr>
              <tr class="is-closed"><td>Sunday</td><td>Closed</td></tr>
            </tbody>
          </table>
        </div>
        <div class="form-card reveal">
          <h2 class="display-md" style="font-size:1.8rem;margin-bottom:0.4rem">Drop us a line</h2>
          <p style="color:var(--muted);margin-top:0;margin-bottom:1.5rem">Fields marked with <span style="color:var(--gold-strong)">*</span> are required.</p>
          <form data-intake-form action="mailto:{EMAIL}" method="post" enctype="text/plain">
            <div class="form-grid">
              <div class="form-field">
                <label for="name">Full name <span class="req">*</span></label>
                <input id="name" name="name" type="text" autocomplete="name" required placeholder="Your name">
                <span class="field-error">Please enter your name.</span>
              </div>
              <div class="form-field">
                <label for="email">Email <span class="req">*</span></label>
                <input id="email" name="email" type="email" autocomplete="email" required placeholder="you@example.com">
                <span class="field-error">Please enter a valid email.</span>
              </div>
              <div class="form-field">
                <label for="phone">Phone</label>
                <input id="phone" name="phone" type="tel" autocomplete="tel" placeholder="(555) 000-0000">
              </div>
              <div class="form-field">
                <label for="topic">Topic</label>
                <select id="topic" name="topic">
                  <option value="Mass Torts">Mass Torts</option>
                  <option value="Motor Vehicle Accident">Motor Vehicle Accident</option>
                  <option value="SSDI">SSDI</option>
                  <option value="Mortgage">Mortgage Refinancing</option>
                  <option value="Law Firm Partnership">Law Firm Partnership</option>
                  <option value="General inquiry">General Inquiry</option>
                </select>
              </div>
              <div class="form-field form-field--full">
                <label for="message">How can we help? <span class="req">*</span></label>
                <textarea id="message" name="message" required placeholder="Briefly describe your situation or partnership interest…"></textarea>
                <span class="field-error">Please share a short message.</span>
              </div>
              <label class="consent">
                <input type="checkbox" name="consent" required>
                <span>I agree to be contacted by TFT Legal Service at the email/phone provided about my inquiry. Consent is not a condition of receiving services and may be revoked at any time. I understand TFT Legal Service is not a law firm and does not provide legal advice. I have read the <a href="/privacy.html">Privacy Policy</a>.</span>
              </label>
              <div class="form-field form-field--full" style="margin-top:0.4rem">
                <button class="btn btn--gold" type="submit">Send Message {ICON_ARROW}</button>
              </div>
              <p class="form-status" role="status" aria-live="polite"></p>
            </div>
          </form>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("contact.html", contact_html)

# ---------------------------------------------------------------------------
# TORTS
# ---------------------------------------------------------------------------
torts_cases = [
    ("Rideshare Abuse", "The largest current wave of litigation involves thousands of consolidated federal multidistrict litigation (MDL) cases alleging that Uber and Lyft systemically failed to implement basic safety measures to protect passengers from driver sexual assault.", "https://www.claimresolutionscenter.com", "MDL"),
    ("Video Game Addiction", "Lawsuits allege that major developers intentionally design games to foster compulsive behavior. Key targets include Epic Games, Roblox Corporation, and Activision Blizzard — with titles like Fortnite, Roblox, and Call of Duty named in complaints.", "https://www.fight4myrights.net", "Litigation"),
    ("Social Media Addiction", "Thousands of consolidated actions allege that Meta, ByteDance (TikTok), Alphabet (YouTube), and Snap Inc. used manipulative design — infinite scroll, push notifications, and algorithms — contributing to severe mental health harm among adolescents.", "#", "Litigation"),
    ("Roblox Abuse", "Families and government entities accuse the platform of failing to protect minors from sexual exploitation, grooming, and human trafficking — one of the most significant legal actions against Roblox today.", "https://www.gettingjusticenow.com", "Minors"),
    ("CA Sexual Abuse", "Institutional sexual abuse of minors in California settings — organizations that had a duty to supervise and protect children but failed to prevent abuse by staff, volunteers, or authority figures.", "https://www.standagainstabuse.com", "California"),
    ("Depo-Provera", "Thousands of lawsuits have been filed against Pfizer regarding Depo-Provera, focusing on meningioma brain tumors, failure to warn, and related claims.", "https://www.depohelp.org", "Pharma"),
    ("Illinois Sexual Abuse", "Victims of sexual abuse in Illinois can pursue civil lawsuits. Cases often involve institutions and authority figures who exploited positions of power over minors.", "https://www.justiceroute.com", "Illinois"),
]

cases_html = []
for title, desc, url, tag in torts_cases:
    target = ' target="_blank" rel="noopener noreferrer"' if url.startswith("http") else ""
    cases_html.append(f"""          <article class="case-card reveal">
            <div class="meta"><span class="tag" style="margin:0">{tag}</span></div>
            <h3>{title}</h3>
            <p>{desc}</p>
            <a class="btn btn--navy btn--sm" href="{url}"{target}>Read More {ICON_ARROW}</a>
          </article>""")

torts_faq = """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is a mass tort?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A mass tort is a civil action involving numerous plaintiffs against one or more corporate defendants, often arising from the same product, drug, platform, or pattern of alleged negligence. TFT Legal Service connects potential claimants with qualified mass tort law firms."
      }
    },
    {
      "@type": "Question",
      "name": "Which mass tort cases does TFT Legal Service cover?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Current pathways include rideshare abuse (Uber/Lyft), video game addiction, social media addiction, Roblox abuse, California institutional sexual abuse, Depo-Provera litigation, and Illinois sexual abuse cases."
      }
    }
  ]
}"""

torts_html = head({
    "title": "Mass Torts | TFT Legal Service — Rideshare, Social Media, Depo-Provera & More",
    "description": "Explore mass tort pathways including rideshare abuse, social media and video game addiction, Roblox abuse, Depo-Provera, and institutional sexual abuse. TFT Legal Service connects you with qualified counsel.",
    "path": "/torts.html",
    "keywords": "mass torts, rideshare abuse lawsuit, Uber Lyft sexual assault MDL, social media addiction lawsuit, video game addiction lawsuit, Roblox abuse lawsuit, Depo-Provera lawsuit, California sexual abuse lawsuit, Illinois sexual abuse",
    "jsonld": [ORG_JSONLD, torts_faq, breadcrumb([("Home", "/"), ("Mass Torts", "/torts.html")])],
}) + f"""<body>
{header("torts")}
  <main id="main">
{page_hero([("Home", "/"), ("Mass Torts", "#")], "Mass Tort Litigation Pathways", "When corporate negligence harms many, coordinated litigation can open a path to accountability. We connect potential claimants with experienced mass tort firms.")}

    <section class="section section--tight">
      <div class="container split">
        <div class="media-frame reveal">
          <img src="/assets/img/torts-hero.jpg" width="1400" height="933" alt="Legal books representing mass tort litigation research" loading="eager" decoding="async" fetchpriority="high">
        </div>
        <div class="reveal">
          <p class="eyebrow">Overview</p>
          <h2 class="display-md">Justice at scale</h2>
          <p class="lede">Mass torts consolidate claims of individuals harmed by the same product, platform, or institutional failure. TFT Legal Service helps identify potential claimants and connects them with firms prepared to pursue these complex cases.</p>
          <div class="notice" style="margin-top:1.4rem"><strong>Attorney Advertising:</strong> Information is general only. Not legal advice. Prior results do not guarantee similar outcomes.</div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Active Categories</p>
          <h2 class="display-md">Current mass tort focus areas</h2>
          <p class="lede">Select a category to learn more. External partner sites provide additional case detail and intake options.</p>
        </div>
        <div class="grid grid--2" data-stagger>
{chr(10).join(cases_html)}
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <h2 class="display-md">Think you may have a claim?</h2>
          <p>Tell us about your situation. We will help determine whether a partner firm may be able to evaluate your case.</p>
          <div class="hero-actions">
            <a class="btn btn--gold" href="/contact.html">Start a Conversation {ICON_ARROW}</a>
          </div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("torts.html", torts_html)

# ---------------------------------------------------------------------------
# MVA
# ---------------------------------------------------------------------------
mva_html = head({
    "title": "Motor Vehicle Accident Claims | TFT Legal Service — MVA Lawyer Referral",
    "description": "Injured in a car, truck, or rideshare crash? TFT Legal Service connects motor vehicle accident victims with qualified personal injury attorneys. Learn how an MVA lawsuit works.",
    "path": "/mva.html",
    "keywords": "motor vehicle accident lawsuit, MVA claim, car accident lawyer referral, rideshare accident attorney, personal injury lead generation",
    "jsonld": [
        ORG_JSONLD,
        breadcrumb([("Home", "/"), ("Motor Vehicle Accidents", "/mva.html")]),
        """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is an MVA lawsuit?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "An MVA (motor vehicle accident) lawsuit is a legal claim filed after a car, truck, motorcycle, or similar crash seeking damages for injuries, medical expenses, lost wages, and related losses. TFT Legal Service connects injured individuals with qualified personal injury law firms."
    }
  }]
}""",
    ],
}) + f"""<body>
{header("mva")}
  <main id="main">
{page_hero([("Home", "/"), ("MVA", "#")], "Motor Vehicle Accident Claims", "An MVA lawsuit is a legal claim filed after a motor vehicle accident for damages or injuries. We connect injured people with attorneys who evaluate these cases.")}

    <section class="section">
      <div class="container split">
        <div class="media-frame reveal">
          <img src="/assets/img/mva-hero.jpg" width="1400" height="934" alt="Roadway representing motor vehicle accident claim pathways" loading="eager" decoding="async" fetchpriority="high">
        </div>
        <div class="reveal">
          <p class="eyebrow">MVA Overview</p>
          <h2 class="display-md">After a crash, the next step matters</h2>
          <p>Motor vehicle accidents can leave lasting physical, financial, and emotional damage. Whether the collision involved a passenger car, commercial truck, motorcycle, or rideshare vehicle, injured parties may have grounds to pursue compensation.</p>
          <p>TFT Legal Service does not represent clients in court. We help connect you with experienced personal injury counsel who can review your accident, injuries, and insurance landscape.</p>
          <div style="margin-top:1.8rem;display:flex;flex-wrap:wrap;gap:0.9rem">
            <a class="btn btn--gold" href="https://www.fastclaimassist.com" target="_blank" rel="noopener noreferrer">Read More {ICON_ARROW}</a>
            <a class="btn btn--ghost" href="/contact.html">Talk to Our Team</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow" style="color:var(--gold-light)">What Claims May Cover</p>
          <h2 class="display-md">Common damages in MVA cases</h2>
        </div>
        <div class="grid grid--3" data-stagger>
          <article class="card card--navy reveal"><h3>Medical Costs</h3><p>Emergency care, surgery, rehabilitation, and ongoing treatment related to crash injuries.</p></article>
          <article class="card card--navy reveal"><h3>Lost Income</h3><p>Wages and earning capacity reduced by recovery time or permanent limitation.</p></article>
          <article class="card card--navy reveal"><h3>Pain &amp; Suffering</h3><p>Non-economic harm including physical pain and diminished quality of life.</p></article>
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <h2 class="display-md">Injured in an accident?</h2>
          <p>Reach out today. We will help connect you with a firm that can evaluate your claim.</p>
          <div class="hero-actions"><a class="btn btn--gold" href="/contact.html">Get Connected {ICON_ARROW}</a></div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("mva.html", mva_html)

# ---------------------------------------------------------------------------
# SSDI
# ---------------------------------------------------------------------------
ssdi_html = head({
    "title": "Social Security Disability Insurance (SSDI) | TFT Legal Service",
    "description": "Learn how SSDI works and connect with experienced disability counsel through TFT Legal Service. Monthly benefits for people unable to work due to serious long-term medical conditions.",
    "path": "/ssdi.html",
    "keywords": "SSDI, Social Security Disability Insurance, disability benefits lawyer referral, SSDI application help, disability legal marketing",
    "jsonld": [
        ORG_JSONLD,
        breadcrumb([("Home", "/"), ("SSDI", "/ssdi.html")]),
        """{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Social Security Disability Insurance (SSDI)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SSDI is a federal benefit program that provides monthly financial support to individuals unable to work due to a serious, long-term, or permanent medical condition. To qualify, the person must have previously worked and contributed to Social Security through payroll taxes. Approved individuals may also become eligible for Medicare after a waiting period."
      }
    },
    {
      "@type": "Question",
      "name": "How can TFT Legal Service help with SSDI?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TFT Legal Service connects individuals with attorneys and advocates experienced in SSDI claims. We do not decide benefits and do not provide legal advice; we facilitate the connection to qualified counsel who can develop tailored strategies for your situation."
      }
    }
  ]
}""",
    ],
}) + f"""<body>
{header("ssdi")}
  <main id="main">
{page_hero([("Home", "/"), ("SSDI", "#")], "Social Security Disability Insurance", "Federal monthly support for people unable to work due to a serious, long-term medical condition — and a pathway to counsel who understand the process.")}

    <section class="section">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow">SSDI Explained</p>
          <h2 class="display-md">Benefits when work is no longer possible</h2>
          <p>Social Security Disability Insurance (SSDI) is a federal benefit program that provides monthly financial support to individuals who are unable to work due to a serious, long-term, or permanent medical condition. To qualify, the person must have previously worked and contributed to the Social Security system through payroll taxes.</p>
          <p>Monthly benefit amounts vary depending on work and earnings history. In addition to financial support, individuals approved for SSDI may become eligible for Medicare coverage after a qualifying waiting period.</p>
        </div>
        <div class="media-frame reveal">
          <img src="/assets/img/ssdi-hero.jpg" width="1400" height="933" alt="Professional reviewing documents related to disability benefits" loading="eager" decoding="async" fetchpriority="high">
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container split">
        <div class="reveal">
          <p class="eyebrow" style="color:var(--gold-light)">Tailored Strategies</p>
          <h2 class="display-md">Every disability case is unique</h2>
          <p>We understand that each case is unique at TFT Legal. That’s why partner counsel develops personalized legal strategies that cater to specific needs and objectives — maximizing the chance of a complete, well-documented claim.</p>
        </div>
        <ul class="check-list reveal">
          <li>{ICON_CHECK}<div><strong>Work history matters</strong><span>SSDI eligibility depends on prior contributions to Social Security.</span></div></li>
          <li>{ICON_CHECK}<div><strong>Medical evidence</strong><span>Serious, long-term conditions must be thoroughly documented.</span></div></li>
          <li>{ICON_CHECK}<div><strong>Medicare pathway</strong><span>Approved beneficiaries may qualify for Medicare after a waiting period.</span></div></li>
          <li>{ICON_CHECK}<div><strong>Experienced counsel</strong><span>We connect you with advocates who navigate denials and appeals.</span></div></li>
        </ul>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <h2 class="display-md">Need help with an SSDI matter?</h2>
          <p>Contact TFT Legal Service and we will help connect you with qualified disability counsel.</p>
          <div class="hero-actions"><a class="btn btn--gold" href="/contact.html">Contact Us {ICON_ARROW}</a></div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("ssdi.html", ssdi_html)

# ---------------------------------------------------------------------------
# MORTGAGE
# ---------------------------------------------------------------------------
mortgage_html = head({
    "title": "Mortgage Refinancing | TFT Legal Service — Optimize Your Home Loan",
    "description": "It may be time to refinance your mortgage. Learn how refinancing can lower payments, reduce rates, or unlock equity. TFT Legal Service connects homeowners with trusted referral partners.",
    "path": "/mortgage.html",
    "keywords": "mortgage refinancing, refinance home loan, lower mortgage rate, cash-out refinance, home equity",
    "jsonld": [ORG_JSONLD, breadcrumb([("Home", "/"), ("Mortgage Refinancing", "/mortgage.html")])],
}) + f"""<body>
{header("mortgage")}
  <main id="main">
{page_hero([("Home", "/"), ("Mortgage", "#")], "It may be time to refinance your mortgage", "Replace your current home loan with one that better fits your goals — lower payments, better rates, or access to equity.")}

    <section class="section">
      <div class="container split">
        <div class="media-frame reveal">
          <img src="/assets/img/mortgage-hero.jpg" width="1400" height="933" alt="House keys representing mortgage refinancing opportunities" loading="eager" decoding="async" fetchpriority="high">
        </div>
        <div class="reveal">
          <p class="eyebrow">Refinancing</p>
          <h2 class="display-md">Optimize your finances</h2>
          <p>Mortgage refinancing is the process of replacing your current home loan with a new one — often with better terms. Homeowners choose to refinance for several reasons, including lowering monthly payments, reducing interest rates, or accessing equity built in their property.</p>
          <p>Refinancing can be a smart financial move if you’re looking to improve cash flow, consolidate debt, or shorten the term of your loan. By securing a lower interest rate, you may save thousands over the life of the mortgage. Cash-out refinancing can convert part of your home equity into cash for improvements, investments, or other needs.</p>
          <p>Every situation is unique. Exploring options today could put you in a stronger financial position tomorrow.</p>
        </div>
      </div>
    </section>

    <section class="section section--dark">
      <div class="container">
        <div class="grid grid--3" data-stagger>
          <article class="card card--navy reveal"><h3>Lower Payments</h3><p>A better rate or longer term can free monthly cash flow for other priorities.</p></article>
          <article class="card card--navy reveal"><h3>Rate Reduction</h3><p>Market shifts may allow you to lock a meaningfully lower interest rate.</p></article>
          <article class="card card--navy reveal"><h3>Equity Access</h3><p>Cash-out refinance can fund renovations, consolidation, or other goals.</p></article>
        </div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="container">
        <div class="cta-band reveal">
          <h2 class="display-md">Ready to explore refinancing?</h2>
          <p>Contact TFT Legal Service and we will help connect you with a trusted referral partner.</p>
          <div class="hero-actions"><a class="btn btn--gold" href="/contact.html">Get Started {ICON_ARROW}</a></div>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("mortgage.html", mortgage_html)

# ---------------------------------------------------------------------------
# COMPLIANCE
# ---------------------------------------------------------------------------
compliance_html = head({
    "title": "Compliance Policy | TFT Legal Service — TCPA & Ethical Lead Generation",
    "description": "TFT Legal Service compliance policy: TCPA adherence, ABA-aligned ethics, transparent advertising, informed consent, and data privacy in legal lead generation.",
    "path": "/compliance.html",
    "keywords": "TFT Legal compliance, TCPA lead generation, ethical legal marketing, ABA advertising guidelines",
    "jsonld": [ORG_JSONLD, breadcrumb([("Home", "/"), ("Compliance Policy", "/compliance.html")])],
}) + f"""<body>
{header("index")}
  <main id="main">
{page_hero([("Home", "/"), ("Compliance Policy", "#")], "Compliance Policy", "Ethical conduct and full compliance with U.S. law — non-negotiable in everything we do.")}

    <section class="section">
      <div class="container">
        <article class="prose reveal" style="margin-inline:auto">
          <p>We are firmly committed to upholding the highest standards of ethical conduct and full compliance with U.S. laws and the American Bar Association (ABA) guidelines. We ensure that every aspect of our lead generation process strictly adheres to applicable state and federal regulations, including the Telephone Consumer Protection Act (TCPA).</p>
          <h2>Core principles</h2>
          <ul>
            <li><strong>Transparency</strong> — Clear communication about who we are and how we operate.</li>
            <li><strong>Informed consent</strong> — Outreach grounded in lawful, documented consent practices.</li>
            <li><strong>Data privacy</strong> — Rigorous protections for personal information.</li>
            <li><strong>Honest advertising</strong> — No guarantees of legal outcomes or financial compensation; materials that are truthful and not misleading.</li>
          </ul>
          <p>By adhering to these principles, we offer law firms and clients the assurance that they are working with a reputable, ethically sound, and professionally responsible organization. Our lead generation processes are designed to withstand regulatory scrutiny and uphold the integrity of the legal profession.</p>
          <h2>Attorney advertising notice</h2>
          <p>The information on this website is for general information purposes only. Nothing on this site should be taken as legal advice for any individual case or situation. Prior results do not guarantee a similar outcome.</p>
          <div class="notice" style="margin-top:2rem"><strong>Disclaimer:</strong> TFT Legal Service is a lead generation company and does not provide legal services. No attorney-client relationship is formed through use of this website or our referral process.</div>
        </article>
      </div>
    </section>
  </main>
{footer()}"""

write("compliance.html", compliance_html)

# ---------------------------------------------------------------------------
# PRIVACY
# ---------------------------------------------------------------------------
privacy_html = head({
    "title": "Privacy Policy | TFT Legal Service",
    "description": "Privacy policy for TFT Legal Service: how we collect, use, and protect personal information submitted through tftlegalservice.com.",
    "path": "/privacy.html",
    "keywords": "TFT Legal privacy policy, data privacy legal marketing",
    "jsonld": [ORG_JSONLD, breadcrumb([("Home", "/"), ("Privacy Policy", "/privacy.html")])],
}) + f"""<body>
{header("index")}
  <main id="main">
{page_hero([("Home", "/"), ("Privacy Policy", "#")], "Privacy Policy", "How TFT Legal Service handles personal information.", "Last updated July 30, 2026")}

    <section class="section">
      <div class="container">
        <article class="prose reveal" style="margin-inline:auto">
          <p>TFT Legal Service (“we,” “us,” or “our”) respects your privacy. This policy describes how we collect, use, and protect information when you visit <strong>www.tftlegalservice.com</strong> or contact us.</p>
          <h2>Information we collect</h2>
          <ul>
            <li>Contact details you submit (name, email, phone, message content).</li>
            <li>Technical data such as IP address, browser type, and pages visited (via cookies or analytics, if enabled).</li>
            <li>Communications preferences and consent records related to outreach.</li>
          </ul>
          <h2>How we use information</h2>
          <ul>
            <li>To respond to inquiries and facilitate connections with partner law firms when appropriate.</li>
            <li>To operate, secure, and improve our website and intake processes.</li>
            <li>To comply with legal obligations, including TCPA and related regulations.</li>
          </ul>
          <h2>Sharing</h2>
          <p>We may share relevant inquiry information with partner law firms for referral purposes, with service providers who support our operations, or when required by law. We do not sell personal information as a standalone consumer data product.</p>
          <h2>Cookies</h2>
          <p>We may use cookies to analyze website traffic and optimize experience. Aggregate analytics may be used. You can control cookies through your browser settings.</p>
          <h2>Your choices</h2>
          <p>You may revoke communication consent at any time and request access or deletion of personal information we hold, subject to legal retention requirements, by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
          <h2>Contact</h2>
          <p>Privacy questions: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
        </article>
      </div>
    </section>
  </main>
{footer()}"""

write("privacy.html", privacy_html)

# ---------------------------------------------------------------------------
# 404
# ---------------------------------------------------------------------------
notfound = head({
    "title": "Page Not Found | TFT Legal Service",
    "description": "The page you requested could not be found on TFT Legal Service.",
    "path": "/404.html",
    "keywords": "404",
    "robots": "noindex, follow",
    "jsonld": [ORG_JSONLD],
}) + f"""<body>
{header("index")}
  <main id="main">
    <section class="page-hero">
      <div class="container">
        <p class="eyebrow">Error 404</p>
        <h1 class="display-lg">This page could not be found</h1>
        <p class="lede">The link may be outdated or mistyped. Return home or contact our team for help.</p>
        <div class="hero-actions" style="margin-top:2rem">
          <a class="btn btn--gold" href="/">Back to Home {ICON_ARROW}</a>
          <a class="btn btn--ghost-light" href="/contact.html">Contact Us</a>
        </div>
      </div>
    </section>
  </main>
{footer()}"""

write("404.html", notfound)

print("ALL PAGES GENERATED")
