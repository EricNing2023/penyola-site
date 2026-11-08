#!/usr/bin/env python3
"""Build the Penyola website (GitHub Pages serves the repository root as-is).

Privacy, terms and credits pages reuse the body of the legal files the app bundles, so the
published text never drifts from what users read in the app. Run after those files change:

    python3 build.py [path/to/penyola-release]
"""
import hashlib, json, pathlib, re, sys
from articles import ARTICLES, CHECK, CHECKED

SITE = pathlib.Path(__file__).resolve().parent
RELEASE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else SITE.parent / 'penyola-release')
LEGAL = RELEASE / 'app/engine/iphone/Maps/ScenicResources/legal'
config = json.loads((RELEASE / 'release-config.json').read_text())
EMAIL = config['support_email']
APP_STORE = 'https://apps.apple.com/app/id6821783513'
BASE = 'https://penyola.com/'
RELEASED = True  # live on the App Store since 2026-11-06

CSS_VERSION = hashlib.sha1((SITE / 'assets/site.css').read_bytes()).hexdigest()[:8]  # busts the Pages cache

# Cloudflare Web Analytics: cookieless page counts. Stays off (no script, no privacy note) until the beacon token is set.
CF_BEACON_TOKEN = None
ANALYTICS = (f'\n<script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon=\'{{"token": "{CF_BEACON_TOKEN}"}}\'></script>'
             if CF_BEACON_TOKEN else '')
SITE_PRIVACY_NOTE = ('\n<h2>This website</h2>\n<p>penyola.com counts page visits with Cloudflare Web Analytics, which uses no cookies and does not identify or follow you across sites. '
                     'The app itself collects no data.</p>') if CF_BEACON_TOKEN else ''

NAV = [('index.html', 'Home'), ('demo.html', 'Try it'), ('support.html', 'Support'), ('privacy.html', 'Privacy'), ('credits.html', 'Credits')]


def legal_body(name):
    html = (LEGAL / f'{name}.html').read_text()
    if '{SUPPORT_EMAIL}' in html:
        sys.exit(f'{name}.html still has the {{SUPPORT_EMAIL}} placeholder')
    return re.search(r'<body>(.*)</body>', html, re.S).group(1).strip()


def page(file, title, description, main, body_class='', scripts='', head='', image='assets/img/og.jpg'):
    root = '../' * file.count('/')  # pages in folders (press/index.html) still use relative links
    nav = ''.join(f'<a href="{root}{href}"{" aria-current=\"page\"" if href == file else ""}>{label}</a>'
                  for href, label in NAV)
    url = BASE + file.removesuffix('index.html')
    extra = f'\n<meta name="apple-itunes-app" content="app-id={APP_STORE.rsplit("id", 1)[1]}">' if RELEASED else ''
    if file == 'index.html':
        app = {'@context': 'https://schema.org', '@type': 'MobileApplication', 'name': 'Penyola', 'operatingSystem': 'iOS',
               'applicationCategory': 'TravelApplication', 'url': BASE, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'}}
        if RELEASED:
            app['installUrl'] = APP_STORE
        extra += f'\n<script type="application/ld+json">{json.dumps(app)}</script>'
    extra += head
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{'article' if head else 'website'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#f8f3ea">
<link rel="icon" type="image/png" href="{root}favicon.png">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<link rel="stylesheet" href="{root}assets/site.css?v={CSS_VERSION}">{extra}{ANALYTICS}
</head>
<body class="{body_class}">
<header class="top">
  <div class="wrap top-inner">
    <a class="brand" href="{root}index.html"><img src="{root}assets/img/icon-256.png" alt="" width="32" height="32">Penyola</a>
    <nav aria-label="Main">{nav}</nav>
  </div>
</header>
<main>
{main}
</main>
<footer class="foot">
  <div class="wrap foot-inner">
    <p><strong>Penyola</strong> · offline guides to Beijing's imperial sights<br>
    Support: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p><a href="{root}guides/">Planning guides</a> · <a href="{root}support.html">Support</a> · <a href="{root}press/">Press</a> · <a href="{root}privacy.html">Privacy Policy</a> · <a href="{root}terms.html">Terms of Use</a> · <a href="{root}credits.html">Credits</a></p>
    <p class="fine">Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a>. Penyola is an independent guide and is not affiliated with the management of these sites. © 2026 Hong Ning.</p>
  </div>
</footer>
{scripts}</body>
</html>
'''


APPLE_LOGO = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M16.37 12.6c-.02-2.3 1.88-3.4 1.96-3.46-1.07-1.56-2.73-1.77-3.32-1.8-1.41-.14-2.76.83-3.48.83-.72 0-1.82-.81-3-.79-1.54.02-2.96.9-3.76 2.27-1.6 2.78-.41 6.9 1.15 9.16.76 1.1 1.67 2.34 2.86 2.3 1.15-.05 1.58-.74 2.97-.74 1.38 0 1.77.74 2.98.72 1.23-.02 2.01-1.12 2.76-2.23.87-1.28 1.23-2.52 1.25-2.58-.03-.01-2.4-.92-2.42-3.66zM14.1 5.84c.63-.77 1.06-1.83.94-2.89-.91.04-2.01.61-2.66 1.37-.58.67-1.1 1.76-.96 2.8 1.01.08 2.05-.52 2.68-1.28z"/></svg>'


def store_button():
    # Until the app is live the App Store link 404s, so show a non-link badge instead.
    if RELEASED:
        return f'<a class="store" href="{APP_STORE}">{APPLE_LOGO}<span><small>Download on the</small>App Store</span></a>'
    return f'<span class="store soon">{APPLE_LOGO}<span><small>Coming soon to the</small>App Store</span></span>'


GUIDES = [
    ('jingshan', 'Jingshan Park', '景山公园', 'Free', 'Climb to the hilltop pavilions for the classic view over the Forbidden City.'),
    ('forbiddencity', 'Forbidden City', '故宫', 'Unlock All Guides', 'Courtyards, halls, carved guardians and the stories behind them, with routes for a short visit or a full day.'),
    ('summerpalace', 'Summer Palace', '颐和园', 'Unlock All Guides', 'Kunming Lake, Longevity Hill and the Long Corridor, with walking routes around the lake.'),
]

# Illustrations from the guides and from guides in development. Ones drawn after a photograph carry
# the photo's credit (author, licence, source), as the licences require.
GALLERY = [
    ('hall-of-supreme-harmony', 'Hall of Supreme Harmony', 'Forbidden City', None),
    ('foxiang-tower', 'Tower of Buddhist Incense', 'Summer Palace', None),
    ('seventeen-arch-bridge', 'Seventeen-Arch Bridge', 'Summer Palace', None),
    ('wanchun', 'Wanchun Pavilion', 'Jingshan Park', None),
    ('marble-boat', 'Marble Boat', 'Summer Palace', None),
    ('long-corridor', 'Long Corridor', 'Summer Palace', None),
    ('bronze-ox', 'Bronze Ox', 'Summer Palace', None),
    ('imperial-garden', 'Imperial Garden', 'Forbidden City', None),
    ('stone-forest', 'Stone Forest', 'Yunnan', None),
]

FEATURES = [
    ('Hand-drawn maps', 'Every site is drawn by hand. Pinch, zoom and tap any building.'),
    ('Stories for every highlight', '129 illustrated highlights, from throne halls to the roof beasts most visitors miss.'),
    ('Narrated audio', '150+ audio stories in two English voices, to play as you walk.'),
    ('Ready-made routes', 'Suggested walks with times and distances between stops.'),
    ('Visitor essentials', 'Opening hours, ticket notes, entrances and a Chinese address card for your taxi driver.'),
    ('Works offline', 'Everything is on your phone. No account, no sign-in, no ads.'),
]

# Maps in development, chosen from the most complete packages; previews only, no dates promised.
# Map cards (images, crops and POI pins) come from images.py, which writes assets/img/map-cards.json.
MAP_CARDS = json.loads((SITE / 'assets/img/map-cards.json').read_text())
SHOWCASE = [
    ('longmen', 'Longmen Grottoes, West Hill', 'Luoyang', '龙门石窟', 'Cliffs of carved Buddhas above the Yi River, with the great Vairocana at Fengxian Temple.'),
    ('yungang', 'Yungang Grottoes', 'Datong', '云冈石窟', 'Fifth-century caves cut into a sandstone ridge, from the open-air Buddha of Cave 20 to the giant seated Buddha of Cave 5.'),
]
NEXT = [
    ('badaling', 'Badaling Great Wall', 'Beijing', '八达岭长城'),
    ('huangshan', 'Huangshan', 'Anhui', '黄山'),
    ('elephant-trunk-hill', 'Elephant Trunk Hill', 'Guilin', '象鼻山'),
    ('jiuzhaigou', 'Jiuzhaigou Valley', 'Sichuan', '九寨沟'),
    ('tianmen', 'Tianmen Mountain', 'Zhangjiajie', '天门山'),
    ('mount-hua', 'Mount Hua', 'Shaanxi', '华山'),
]

guides = ''.join(f"""
      <article class="guide">
        <div class="guide-map"><img src="assets/img/map-{key}.webp" alt="Hand-drawn map of {name}" loading="lazy" width="{w}" height="{h}"></div>
        <div class="guide-text">
          <p class="tag{' free' if tag == 'Free' else ''}">{tag}</p>
          <h3>{name} <span class="zh" lang="zh-Hans">{zh}</span></h3>
          <p>{text}</p>
        </div>
      </article>""" for (key, name, zh, tag, text), (w, h) in zip(GUIDES, ((1000, 1202), (1100, 1374), (1000, 1168))))

features = ''.join(f"""
      <li><h3>{title}</h3><p>{text}</p></li>""" for title, text in FEATURES)

def gallery_credit(credit):
    if not credit:
        return ''
    author, licence, licence_url, source = credit
    return (f'<small class="credit">Drawn after a <a href="{source}">photo</a> by {author}, '
            f'<a href="{licence_url}">{licence}</a></small>')


gallery = ''.join(f"""
      <figure class="bld{' fit' if key == 'wanchun' else ''}"><img src="assets/img/bld-{key}.webp" alt="Illustration of {name}" loading="lazy" width="800" height="600"><figcaption><strong>{name}</strong>{place}{gallery_credit(credit)}</figcaption></figure>"""
                  for key, name, place, credit in GALLERY)

def pins(key):
    return ''.join(f'''<span class="pin{' art' if p['art'] else ''}" style="left:{p['u'] * 100:.2f}%;top:{p['v'] * 100:.2f}%">{f'<img src="{p["art"]}" alt="" width="160" height="160" loading="lazy">' if p['art'] else ''}<b>{p['name']}</b></span>'''
                   for p in MAP_CARDS[key]['pins'])


def pin_map(key, name, extra=''):
    c = MAP_CARDS[key]
    return (f'<div class="pinmap"><img src="assets/img/next-{key}.webp" alt="Hand-drawn map of {name}, in development" '
            f'loading="lazy" width="{c["width"]}" height="{c["height"]}">{pins(key)}</div>')


upcoming = ''.join(f"""
      <figure class="next">
        {pin_map(key, name)}
        <figcaption><strong>{name}</strong><span>{region} · <span lang="zh-Hans">{zh}</span></span></figcaption>
      </figure>""" for key, name, region, zh in NEXT)

showcase = ''.join(f"""
      <figure class="show">
        {pin_map(key, name)}
        <figcaption><strong>{name}</strong> <span>{region} · <span lang="zh-Hans">{zh}</span></span><p>{text}</p></figcaption>
      </figure>""" for key, name, region, zh, text in SHOWCASE)

HOME = f"""
<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-text">
      <p class="eyebrow">Offline audio guide · Beijing</p>
      <h1>Beijing's imperial sights, beautifully drawn.</h1>
      <p class="lede">An English guide for international visitors to Jingshan Park, the Forbidden City and the Summer Palace. Hand-drawn maps, narrated stories and ready-made walking routes, all on your iPhone, with no connection needed.</p>
      <div class="cta">{store_button()}<a class="text-link" href="demo.html">Try the free guide →</a></div>
      <p class="note">{'Free to download for iPhone.' if RELEASED else 'Launching soon for iPhone.'} Jingshan Park is free; one purchase unlocks the rest.</p>
    </div>
    <div class="hero-art">
      <img class="hero-lion" src="assets/img/art-lion.webp" alt="" width="600" height="727">
      <div class="hero-map"><img src="assets/img/map-forbiddencity.webp" alt="Hand-drawn map of the Forbidden City" width="1100" height="1374"></div>
    </div>
  </div>
</section>

<section class="stats" aria-label="At a glance">
  <div class="wrap stats-inner">
    <p><strong>3</strong>guides</p>
    <p><strong>129</strong>illustrated highlights</p>
    <p><strong>150+</strong>audio stories</p>
    <p><strong>0</strong>bars of signal needed</p>
  </div>
</section>

<section class="tryit">
  <div class="wrap tryit-inner">
    <img src="assets/img/map-jingshan.webp" alt="" loading="lazy" width="1000" height="1202">
    <div>
      <p class="eyebrow">Try it now</p>
      <h2>Walk Jingshan Park in your browser</h2>
      <p>Open the free Jingshan Park guide right here: tap places on the hand-drawn map, listen to the audio stories and follow a suggested route.</p>
      <a class="btn" href="demo.html">Open the guide →</a>
    </div>
  </div>
</section>

<section class="band" id="guides">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">The guides</p>
      <h2>Three of Beijing's great sites, in one app</h2>
    </div>
    <div class="guides">{guides}
    </div>
  </div>
</section>

<section class="band dark showcase">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Being drawn now</p>
      <h2>China's great grottoes, by hand</h2>
      <p class="lede">The next guides take you to the cave temples of Longmen and Yungang: every niche and carved Buddha on a hand-drawn panorama, with the same stories and audio as the Beijing guides.</p>
    </div>
    <div class="shows">{showcase}
    </div>
  </div>
</section>

<section class="band paper">
  <div class="wrap story">
    <div class="story-text">
      <p class="eyebrow">Every detail has a story</p>
      <h2>See what most visitors walk past</h2>
      <p>Bronze lions guarding the gates, the crane and tortoise before the throne hall, a golden celestial globe, the sundial that told imperial time. Penyola points them out on the map and tells you why they are there.</p>
    </div>
    <div class="relics" aria-hidden="true">
      <img src="assets/img/art-crane.webp" alt="" loading="lazy" width="600" height="600">
      <img src="assets/img/art-tortoise.webp" alt="" loading="lazy" width="600" height="600">
      <img src="assets/img/art-globe.webp" alt="" loading="lazy" width="600" height="600">
      <img src="assets/img/art-sundial.webp" alt="" loading="lazy" width="600" height="600">
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">What's inside</p>
      <h2>Made for walking around, not reading at home</h2>
    </div>
    <ul class="features">{features}
    </ul>
  </div>
</section>

<section class="band paper">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">Drawn by hand</p>
      <h2>Halls, bridges, pavilions and bronze beasts</h2>
      <p class="lede">Every guide comes with watercolour-style drawings of what you'll see, from throne halls and lakeside pavilions to the bronze ox that guards Kunming Lake.</p>
    </div>
    <div class="blds">{gallery}
    </div>
  </div>
</section>

<section class="band dark" id="coming">
  <div class="wrap">
    <div class="head">
      <p class="eyebrow">In the works</p>
      <h2>More of China, being drawn</h2>
      <p class="lede">We're drawing guides to more than 30 other sites across China. Here are a few of the maps in progress. <strong>Unlock All Guides includes every guide we add</strong>, at no extra cost.</p>
    </div>
    <div class="nexts">{upcoming}
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap price">
    <div class="price-card">
      <p class="eyebrow">Pay once</p>
      <h2>Free to start. One purchase for every guide.</h2>
      <p>Jingshan Park is free and complete. You can open the Forbidden City and Summer Palace maps before you buy. A single in-app purchase, <strong>Unlock All Guides</strong>, unlocks their stories, audio and routes, plus every guide added later.</p>
      <p class="price-line"><strong>US$6.99</strong> one time · no subscription · nothing renews</p>
      <div class="cta">{store_button()}</div>
    </div>
    <img class="price-art" src="assets/img/art-throne.webp" alt="" loading="lazy" width="600" height="600">
  </div>
</section>
"""


SUPPORT = f'''
<section class="doc wrap">
  <h1>Support</h1>
  <p class="lede">Questions, problems or feedback: write to <a href="mailto:{EMAIL}">{EMAIL}</a>. We usually reply within two business days.</p>
  <p>If something isn't working, it helps to tell us your iPhone model, iOS version and which guide you were using.</p>

  <h2>Frequently asked questions</h2>

  <details open><summary>Does Penyola work offline?</summary>
  <p>Yes. All maps, texts and audio are included in the app when you install it, so nothing needs to be downloaded at the site. You only need an internet connection to buy or restore the purchase.</p></details>

  <details><summary>What is free, and what do I pay for?</summary>
  <p>The app is free to download and the Jingshan Park guide is free and complete. The Forbidden City and Summer Palace show a map preview. One non-consumable in-app purchase, <strong>Unlock All Guides</strong>, unlocks their stories, audio and routes, and covers guides added later. It is a one-time purchase, not a subscription.</p></details>

  <details><summary>How do I buy Unlock All Guides?</summary>
  <p>On the home screen, open the Forbidden City (or the Summer Palace), tap <strong>Open guide map</strong>, then tap <strong>Unlock full guide</strong> at the bottom of the map. Apple's purchase sheet handles the payment; Penyola never sees your payment details.</p></details>

  <details><summary>How do I restore my purchase on a new iPhone?</summary>
  <p>Sign in with the same Apple Account you bought with. Tap the gear icon on the home screen, open <strong>Purchases &amp; restore</strong> and tap <strong>Restore Purchases</strong>. The Restore button is also on the purchase sheet.</p></details>

  <details><summary>Does Penyola use my location?</summary>
  <p>No. Penyola never asks for location access. You follow the map and choose stops yourself.</p></details>

  <details><summary>In which countries is Penyola available?</summary>
  <p>Penyola is on the App Store in every region except mainland China, Hong Kong and Taiwan. The app is the same everywhere: all content is in English and works offline. It runs on iPhone.</p></details>

  <details><summary>Are opening hours and tickets always up to date?</summary>
  <p>We check them carefully, but sites change their hours, routes and closures. Always follow official signs and staff on the day.</p></details>

  <details><summary>I found a mistake in a guide.</summary>
  <p>Thank you. Please email us with the guide, the place and what looks wrong, and we'll fix it in an update.</p></details>
</section>
'''


def legal_page(main_html, extra_class='legal'):
    return f'<section class="doc wrap {extra_class}">\n{main_html}\n</section>'



def build_demo():
    """Export the free Jingshan Park guide for the in-browser demo (demo.html).

    Positions come from the app's own data: cultural anchors where the guide has them, otherwise
    the route graph's endpoints projected onto the hand-drawn map (Web Mercator over manifest bounds).
    """
    import math, shutil, subprocess
    src = RELEASE / 'app/engine/iphone/Maps/ScenicResources/jingshan'
    out = SITE / 'assets/demo'
    load = lambda name: json.loads((src / name).read_text())
    manifest, routes = load('manifest.json'), load('routes.json')
    details, guide = load('historical_details.json'), load('cultural/guide.json')
    presentation, audio, info = load('cultural/presentation.json'), load('audio/index.json'), load('site_information.json')
    west, south, east, north = manifest['bounds']
    merc = lambda lat: math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))

    def uv(lon, lat):
        return [round((lon - west) / (east - west), 5), round((merc(north) - merc(lat)) / (merc(north) - merc(south)), 5)]

    segments, alias = routes['segments'], routes['stop_aliases']
    endpoint = {}
    for key, seg in segments.items():
        a, b = key.split('|')
        coords = seg['recommended']['coordinates']
        endpoint.setdefault(a, coords[0]); endpoint.setdefault(b, coords[-1])
    places = {pl['id']: pl for pl in routes['places']}
    anchors = {poi['id']: [round(poi['anchor']['u'], 5), round(poi['anchor']['v'], 5)] for poi in guide['pois']}
    pres = {poi['id']: poi for poi in presentation['pois']}

    def position(pid):
        if pid in anchors:
            return anchors[pid]
        c = endpoint.get(pid) or endpoint.get(alias.get(pid, ''))
        if c:
            return uv(*c)
        pl = places.get(pid)
        return uv(pl['lon'], pl['lat']) if pl else None

    (out / 'art').mkdir(parents=True, exist_ok=True)
    pois, intro = [], None
    for d in details:
        pid, key = d['poi_id'], d['poi_id'].replace('/', '-')
        pr = pres.get(pid, {})
        clip = audio['clips'].get(key)
        item = {'id': pid, 'name': d['title'], 'category': pr.get('category') or d['category'],
                'summary': pr.get('summary') or d['summary'], 'story': pr.get('story') or d['story'],
                'source': d.get('source_url'), 'pos': position(pid)}
        if clip:
            item['audio'] = {}
            for voice, c in clip.items():
                dst = out / 'audio' / voice / f'{key}.mp3'
                if not dst.exists():
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(src / c['path']), '-ac', '1', '-b:a', '64k', str(dst)], check=True)
                item['audio'][voice] = {'src': f'assets/demo/audio/{voice}/{key}.mp3', 'seconds': round(c['seconds'])}
        if pr.get('art'):
            art = pathlib.Path(pr['art']).stem
            dst = out / 'art' / f'{art}.webp'
            if not dst.exists():
                subprocess.run(['cwebp', '-quiet', '-q', '80', '-resize', '640', '0', str(src / pr['art']), '-o', str(dst)], check=True)
            item['art'] = f'assets/demo/art/{art}.webp'
        if pid == 'way/29201967':
            intro = item
        elif item['pos']:
            pois.append(item)

    def leg(a, b):
        for x, y, flip in ((a, b, False), (b, a, True), (alias.get(a, a), alias.get(b, b), False), (alias.get(b, b), alias.get(a, a), True)):
            seg = segments.get(f'{x}|{y}')
            if seg:
                rec = seg['recommended']
                coords = rec['coordinates'][::-1] if flip else rec['coordinates']
                return {'distance_m': rec['distance_m'], 'path': [uv(*c) for c in coords]}
        return None

    names = {pl['id']: pl['name'] for pl in routes['places']}
    names.update({d['poi_id']: d['title'] for d in details})
    demo_routes = []
    for preset in routes['presets']:
        stops = [{'id': sid, 'name': names.get(sid, 'Stop'), 'pos': position(sid)} for sid in preset['stop_ids']]
        legs = [leg(a['id'], b['id']) for a, b in zip(stops, stops[1:])]
        if all(legs) and all(st['pos'] for st in stops):
            for st, lg in zip(stops[1:], legs):
                st['pos'] = lg['path'][-1]
            stops[0]['pos'] = legs[0]['path'][0]
            demo_routes.append({'id': preset['id'], 'title': preset['title'], 'minutes': preset['estimated_minutes'],
                                'stops': stops, 'legs': legs})
    entrances = [{'name': names[e], 'pos': position(e)} for e in ('node/1382551889', 'node/733788771', 'node/733788916')]
    data = {
        'name': manifest['name'], 'map': {'src': 'assets/img/map-jingshan.webp', 'width': 1000, 'height': 1202},
        'intro': intro, 'pois': pois, 'entrances': entrances, 'routes': demo_routes,
        'route_note': routes['access_review']['notice'] + ' Times assume walking at 65 m/min plus 10 minutes per sight.',
        'info': {k: info[k] for k in ('address', 'address_chinese', 'opening_hours', 'ticket_prices', 'public_transport', 'reservation')},
    }
    (out / 'jingshan.json').write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    return len(pois), len(demo_routes)


DEMO_STATS = build_demo()

DEMO = f"""
<section class="demo-head wrap">
  <p class="eyebrow">Try it in your browser</p>
  <h1>Jingshan Park, the free guide</h1>
  <p class="lede">This is the real Jingshan Park guide from the app: the hand-drawn map, {DEMO_STATS[0]} highlights with narrated audio stories, {DEMO_STATS[1]} suggested walking routes and the visitor information. In the app it all works offline.</p>
</section>
<section class="wrap">
  <div id="demo" class="demo">
    <div class="dm-map" aria-label="Hand-drawn map of Jingshan Park">
      <div class="dm-stage">
        <img class="dm-map-img" alt="" width="1000" height="1202" draggable="false">
        <svg class="dm-route" preserveAspectRatio="none" aria-hidden="true"></svg>
        <div class="dm-markers"></div>
      </div>
      <div class="dm-zoom">
        <button data-zoom="in" aria-label="Zoom in">+</button>
        <button data-zoom="out" aria-label="Zoom out">−</button>
        <button data-zoom="reset" aria-label="Show whole map">⤢</button>
      </div>
    </div>
    <div class="dm-panel">
      <div class="dm-tabs" role="tablist">
        <button data-tab="highlights" role="tab" aria-selected="true">Highlights</button>
        <button data-tab="routes" role="tab">Routes</button>
        <button data-tab="info" role="tab">Visit info</button>
      </div>
      <div class="dm-panel-body"><p class="dm-hint">Loading the guide…</p></div>
      <div class="dm-player" hidden>
        <span class="dm-player-name"></span><span class="dm-player-time"></span>
        <div class="dm-progress"><i></i></div>
        <button class="dm-player-toggle">Pause</button><button class="dm-player-close" aria-label="Stop">✕</button>
      </div>
    </div>
  </div>
  <div class="demo-cta">
    <p><strong>The Forbidden City and the Summer Palace</strong> work the same way, with more highlights, longer routes and their own illustrations. {'Get Penyola on the App Store.' if RELEASED else 'Penyola is coming soon to the App Store.'}</p>
    {store_button()}
  </div>
</section>
"""


SITE_CREDITS = ('<h2>Website illustrations</h2>\n  <p>Some illustrations on this website come from guides still in development. Where one was drawn after a photograph, the photographer and licence are credited below; each adapted illustration is shared under the same licence as its source.</p>\n  <ul>' + ''.join(
    f'\n    <li><strong>{name}</strong> &mdash; drawn after a <a href="{c[3]}">photograph</a> by {c[0]}, Wikimedia Commons, <a href="{c[2]}">{c[1]}</a></li>'
    for _, name, _, c in GALLERY if c) + '\n  </ul>'
                if any(c for *_, c in GALLERY) else '')

PRESS_SHOTS = [('press-screen-map.webp', 'The hand-drawn Forbidden City map'),
               ('press-screen-story.webp', 'A highlight story with narrated audio'),
               ('press-screen-route.webp', 'A suggested walk with times and stops')]
press_shots = ''.join(f'\n    <figure><img src="../assets/img/{f}" alt="{alt}" width="400" height="869" loading="lazy"><figcaption>{alt}</figcaption></figure>'
                      for f, alt in PRESS_SHOTS)

PRESS = f'''
<section class="doc wrap press">
  <p class="eyebrow">Press</p>
  <h1>Penyola press kit</h1>
  <p class="lede">Penyola is an offline iPhone guide to Beijing's Forbidden City, Summer Palace and Jingshan Park, with hand-drawn maps, audio stories and walking routes.</p>

  <p>Penyola is made for international visitors who want to understand what they are looking at. Each site has its own hand-drawn map: tap a hall, gate, tree or carved beast to read its story or hear it narrated in English. Suggested walks give times and stops, and the visitor information (hours, tickets, entrances and a Chinese address card for taxis) is in the same place.</p>
  <p>Everything is stored on the phone, so the guide works with no signal, no roaming plan and no VPN. There is no account, no sign-in and no advertising, and the app collects no data. The maps and the illustrations of buildings and relics are drawn for Penyola.</p>
  <p>Penyola is free to download, and the Jingshan Park guide is free and complete. One in-app purchase of US$6.99, Unlock All Guides, unlocks the Forbidden City and the Summer Palace and every guide added later, with no subscription. Penyola launched on 6 November 2026, in English, for iPhone, on the App Store in every region except mainland China, Hong Kong and Taiwan.</p>

  <h2>Key facts</h2>
  <ul class="facts">
    <li><strong>3</strong> guides: Jingshan Park (free), the Forbidden City, the Summer Palace</li>
    <li><strong>129</strong> illustrated highlights</li>
    <li><strong>150+</strong> audio stories in English</li>
    <li><strong>Offline</strong> everything is on the phone</li>
    <li><strong>US$6.99</strong> one time for every guide, no subscription</li>
    <li><strong>No data</strong> collected: no account, no ads, no analytics in the app</li>
  </ul>

  <h2>Images</h2>
  <div class="press-shots">
    <figure><img src="../assets/img/icon-256.png" alt="Penyola app icon" width="256" height="256" loading="lazy"><figcaption>App icon</figcaption></figure>{press_shots}
  </div>
  <p>These images and the illustrations on the <a href="../index.html">home page</a> may be used in coverage of Penyola. Larger files on request.</p>

  <h2>Links and contact</h2>
  <ul>
    <li>App Store: <a href="{APP_STORE}">{APP_STORE.removeprefix('https://')}</a></li>
    <li>Free Jingshan Park guide in the browser: <a href="../demo.html">penyola.com/demo.html</a></li>
    <li>Press and partnerships: <a href="mailto:{EMAIL}">{EMAIL}</a></li>
  </ul>
</section>
'''


VERIFY = []
MONTHS = 'January February March April May June July August September October November December'.split()


def claims(html):
    """[[...]] marks a ticket, hours or timing claim: highlighted while CHECK is on, plain text once checked."""
    def mark(m):
        VERIFY.append(re.sub(r'<[^>]+>', '', m.group(1)))
        return f'<mark class="chk">{m.group(1)}</mark>' if CHECK else m.group(1)
    return re.sub(r'\[\[(.+?)\]\]', mark, html, flags=re.S)


def article_page(a):
    root = '../' * a.path.count('/')
    by_path = {x.path: x for x in ARTICLES}
    related = ''.join(f'\n    <li><a href="{root}{p}">{by_path[p].h1}</a></li>' for p in a.related)
    checked = f'{int(CHECKED[8:])} {MONTHS[int(CHECKED[5:7]) - 1]} {CHECKED[:4]}'
    main = f'''
<article class="doc wrap guide-page">
  <p class="eyebrow">{a.eyebrow}</p>
  <h1>{a.h1}</h1>
  <p class="checked">Last checked: <time datetime="{CHECKED}">{checked}</time></p>
  <figure class="guide-art"><img src="{root}assets/img/{a.image}" alt="{a.image_alt}" width="640" height="640"></figure>
{claims(a.body).replace('@ROOT@', root)}
  <aside class="guide-cta">
    <p><strong>Penyola</strong> puts these sights on hand-drawn maps with audio stories and walking routes, offline on your iPhone. The Jingshan Park guide is free.</p>
    <div class="cta">{store_button()}<a class="text-link" href="{root}demo.html">Try the free guide →</a></div>
  </aside>
  <h2>More planning guides</h2>
  <ul>{related}
  </ul>
</article>
'''
    data = {'@context': 'https://schema.org', '@type': 'Article', 'headline': a.h1, 'description': a.description,
            'image': BASE + 'assets/img/' + a.image, 'datePublished': CHECKED, 'dateModified': CHECKED,
            'author': {'@type': 'Organization', 'name': 'Penyola', 'url': BASE},
            'publisher': {'@type': 'Organization', 'name': 'Penyola', 'url': BASE, 'logo': {'@type': 'ImageObject', 'url': BASE + 'assets/img/icon-256.png'}},
            'mainEntityOfPage': BASE + a.path, 'about': a.about}
    return main, f'\n<script type="application/ld+json">{json.dumps(data, ensure_ascii=False)}</script>'


pages = {
    'index.html': ("Penyola – Offline guide to Beijing's imperial sights",
                   'Hand-drawn maps, audio stories and walking routes for Jingshan Park, the Forbidden City and the Summer Palace. Works offline. Jingshan Park is free.',
                   HOME, 'home'),
    'demo.html': ('Try the Jingshan Park guide – Penyola', 'Try the free Jingshan Park guide from Penyola in your browser: hand-drawn map, audio stories and suggested walking routes.', DEMO, 'demo-page'),
    'support.html': ('Support – Penyola', 'Contact Penyola support and answers to common questions about offline use, purchases and restoring.', SUPPORT, ''),
    'privacy.html': ('Privacy Policy – Penyola', 'Penyola collects no data: no accounts, no analytics, no ads.', legal_page(legal_body('privacy') + SITE_PRIVACY_NOTE), ''),
    'terms.html': ('Terms of Use – Penyola', 'Terms of use for the Penyola app.', legal_page(legal_body('terms')), ''),
    'credits.html': ('Credits – Penyola', 'Content credits, map data attribution and open-source notices for Penyola.',
                     legal_page(legal_body('content-credits') + '\n<hr>\n' + (SITE_CREDITS + '\n<hr>\n' if SITE_CREDITS else '') + legal_body('notice')), ''),
}
GROUPS = [('Forbidden City', 'forbidden-city/'), ('Jingshan Park', 'jingshan-park/'), ('Summer Palace', 'summer-palace/'), ('Beijing', 'beijing/')]
GUIDES_HUB = '\n<section class="doc wrap">\n  <p class="eyebrow">Plan your visit</p>\n  <h1>Planning guides</h1>\n  <p class="lede">Tickets, routes, timing and the stories behind the sights, for the Forbidden City, Jingshan Park and the Summer Palace.</p>' + ''.join(
    f'\n  <h2>{name}</h2>\n  <ul>' + ''.join(f'\n    <li><a href="../{a.path}">{a.h1}</a></li>' for a in ARTICLES if a.path.startswith(prefix)) + '\n  </ul>'
    for name, prefix in GROUPS) + '\n</section>\n'
pages['guides/index.html'] = ('Planning guides – Penyola', 'Planning guides for Beijing: Forbidden City tickets and routes, Jingshan Park, the Summer Palace, and getting around without Google.', GUIDES_HUB, '')
pages['press/index.html'] = ('Press kit – Penyola', 'Penyola press kit: one-line description, key facts, app icon and screenshots, and contact for press and partnerships.', PRESS, '')
heads, images = {}, {}
for a in ARTICLES:
    main, heads[a.path + 'index.html'] = article_page(a)
    images[a.path + 'index.html'] = 'assets/img/' + a.image
    pages[a.path + 'index.html'] = (a.title, a.description, main, 'guide-doc')
for file, (title, desc, main, cls) in pages.items():
    scripts = '<script src="assets/demo.js?v=' + hashlib.sha1((SITE / 'assets/demo.js').read_bytes()).hexdigest()[:8] + '" defer></script>\n' if file == 'demo.html' else ''
    (SITE / file).parent.mkdir(parents=True, exist_ok=True)
    (SITE / file).write_text(page(file, title, desc, main, cls, scripts, heads.get(file, ''), images.get(file, 'assets/img/og.jpg')))
(SITE / '.nojekyll').write_text('')

# Crawlers: everything is open to search and AI assistants; the sitemap lists every page.
(SITE / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n')
(SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                                  + ''.join(f'  <url><loc>{BASE}{f.removesuffix("index.html")}</loc></url>\n' for f in pages) + '</urlset>\n')
# IndexNow key file, so penyola-release/tools/ping_indexnow.py can tell Bing about changes.
if key := config.get('indexnow_key'):
    (SITE / f'{key}.txt').write_text(key)
# Claims still to check on the official sites before CHECK is turned off (kept out of the repository by .gitignore).
(SITE / 'verify-claims.txt').write_text(''.join(f'- {c}\n' for c in VERIFY))
print(json.dumps(sorted(pages)))
