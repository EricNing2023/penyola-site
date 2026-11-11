#!/usr/bin/env python3
"""Make every website image: web-sized, with an invisible TrustMark watermark and a copyright tag.

Run with the site's own venv (TrustMark needs PyTorch):  .venv/bin/python images.py
then `python3 build.py`. Sources stay outside this public repository: map packages under
../penyola/maps, building art in the app, and a one-time backup of the older site images in
../penyola-artifacts/site-image-originals/. Only the reduced copies are published.

The watermark is the text PENYOLA. It survives WebP/JPEG recompression and downscaling, not
heavy cropping; check a suspect copy with  .venv/bin/python images.py --check FILE.
"""
import json, pathlib, shutil, sys
from PIL import Image

SITE = pathlib.Path(__file__).resolve().parent
AI = SITE.parent
IMG = SITE / 'assets/img'
ORIGINALS = AI / 'penyola-artifacts/site-image-originals'
MAPS = AI / 'penyola/maps'
APP = AI / 'penyola-release/app/engine/iphone/Maps/ScenicResources'
MARK = 'PENYOLA'
COPYRIGHT = 'Copyright (c) Penyola, penyola.com. All rights reserved.'
Image.MAX_IMAGE_PIXELS = None

# Showcase panoramas (wide) and the "In the works" cards (square crops around the pins).
# Pins are POIs from each package, only a few per map: they are there to look good, not to be complete.
MAP_CARDS = {
    'longmen':   ('wide', 'longmen-west/candidates/1.1.5/payload', ['Fengxian Temple']),
    'yungang':   ('wide', 'yungang-grottoes/local-integration-candidates/0.4.5/payload',
                  ['Cave Twenty: The Open-Air Buddha', 'Cave Five: Monument and Later Layers']),
    'badaling':  ('square', 'badaling/local-integration-candidates/0.6.17/payload', ['Heritage protection stele']),
    'huangshan': ('square', 'huangshan/candidates/1.0.21/payload', ['Greeting Pine', 'Bright Summit', 'Lotus Peak']),
    'elephant-trunk-hill': ('square', 'elephant-trunk-hill/candidates/0.1.13/payload',
                            ['Elephant Trunk Hill', 'Yunfeng Temple · Taiping Exhibition']),
    'jiuzhaigou': ('square', 'jiuzhaigou/candidates/1.0.16/payload', ['Five Flower Lake', 'Long Lake', 'Mirror Lake']),
    'tianmen':   ('square', 'tianmen-mountain/candidates/0.1.13/payload', ['Love Between Tree and Rock', 'Child-Wishing Cave']),
    'mount-hua': ('square', 'mount-hua/candidates/1.0.13/payload', ['North Peak', 'South Peak']),
}
NO_ART = {'longmen'}  # Longmen's POI art is drawn after photographs, so its pin shows the name only
LABELS = {'Fengxian Temple': 'Fengxian Temple · Vairocana Buddha'}
# Gallery: the app's own building art (no photo-derived drawings).
GALLERY_ART = {
    'foxiang-tower': 'summerpalace/building-art/foxiang-tower.png',
    'seventeen-arch-bridge': 'summerpalace/building-art/seventeen-arch-bridge.png',
    'marble-boat': 'summerpalace/building-art/marble-boat.png',
    'long-corridor': 'summerpalace/building-art/long-corridor.png',
    'bronze-ox': 'summerpalace/building-art/bronze-ox.png',
    'imperial-garden': 'forbiddencity/building-art/imperial-garden.png',
}
WIDE_W, SQUARE_W, THUMB_W, BLD_W = 1400, 900, 160, 640


def pois(payload):
    """(name, anchor, art path or None) for every anchored POI in a package."""
    pres = {p['id']: p for p in json.loads((payload / 'presentation-en.json').read_text())['pois']}
    guide = payload / 'image-guide.json'
    if guide.exists():
        g = json.loads(guide.read_text())
        image, items = g['image']['path'], g['pois']
    else:  # older packages: image-pois.json with Chinese names, English in the presentation
        g = json.loads((payload / 'image-pois.json').read_text())
        image, items = g['image']['path'], g['pois']
    out = {}
    for q in items:
        if q.get('anchor'):
            p = pres.get(q['id'], {})
            out[p.get('name') or q['name']] = (q['anchor'], p.get('art'))
    return payload / image, out


def save(im, path, tm, quality=80):
    """Watermark, tag and write one web image (WebP or JPEG by extension). Transparency is kept."""
    alpha = im.getchannel('A') if 'A' in im.mode else None
    im = tm.encode(im.convert('RGB'), MARK, MODE='text')
    if alpha:
        im.putalpha(alpha)
    exif = Image.Exif()
    exif[0x8298] = COPYRIGHT  # Copyright
    exif[0x013B] = 'Penyola'  # Artist
    path.parent.mkdir(parents=True, exist_ok=True)
    fmt = 'JPEG' if path.suffix == '.jpg' else 'WEBP'
    im.save(path, fmt, quality=quality, exif=exif.tobytes(), method=6 if fmt == 'WEBP' else None, **({'exact': True} if alpha else {}))


def short(name):
    name = LABELS.get(name, name)
    return name.split(':')[0].split(' · ')[0].replace('Cave Twenty', 'Cave 20').replace('Cave Five', 'Cave 5').replace('Cave Six', 'Cave 6')


def map_cards(tm):
    data = {}
    for key, (kind, rel, wanted) in MAP_CARDS.items():
        payload = MAPS / rel
        src, found = pois(payload)
        im = Image.open(src).convert('RGB')
        picked = [(n, *found[n]) for n in wanted]
        if kind == 'square':  # square crop around the pins, clamped to the image
            side = min(im.size)
            cx = sum(a['u'] for _, a, _ in picked) / len(picked) * im.width
            cy = sum(a['v'] for _, a, _ in picked) / len(picked) * im.height
            x0 = int(min(max(cx - side / 2, 0), im.width - side))
            y0 = int(min(max(cy - side / 2, 0), im.height - side))
            box, width = (x0, y0, x0 + side, y0 + side), SQUARE_W
        else:
            box, width = (0, 0, *im.size), WIDE_W
        crop = im.crop(box)
        crop = crop.resize((width, round(crop.height * width / crop.width)), Image.LANCZOS)
        save(crop, IMG / f'next-{key}.webp', tm)
        pins = []
        for i, (name, a, art) in enumerate(picked):
            u = (a['u'] * im.width - box[0]) / (box[2] - box[0])
            v = (a['v'] * im.height - box[1]) / (box[3] - box[1])
            thumb = None
            if art and key not in NO_ART:
                t = Image.open(payload / art).convert('RGB')
                s = min(t.size)
                t = t.crop(((t.width - s) // 2, (t.height - s) // 2, (t.width + s) // 2, (t.height + s) // 2)).resize((THUMB_W, THUMB_W), Image.LANCZOS)
                thumb = f'assets/img/poi/{key}-{i + 1}.webp'
                save(t, SITE / thumb, tm)
            pins.append({'name': short(name), 'u': round(u, 4), 'v': round(v, 4), 'art': thumb})
        data[key] = {'width': crop.width, 'height': crop.height, 'pins': pins}
        print(key, crop.size, [p['name'] for p in pins])
    return data


def gallery(tm):
    for key, rel in GALLERY_ART.items():
        im = Image.open(APP / rel).convert('RGB').resize((BLD_W, BLD_W), Image.LANCZOS)
        save(im, IMG / f'bld-{key}.webp', tm)


def older_images(tm):
    """Watermark the images the site already had, always from the backed-up originals."""
    keep = ['art-*.webp', 'map-*.webp', 'bld-hall-of-supreme-harmony.webp', 'bld-wanchun.webp', 'bld-stone-forest.webp', 'og.jpg']
    for pattern in keep:
        for p in sorted(IMG.glob(pattern)):
            orig = ORIGINALS / p.name
            if not orig.exists():
                ORIGINALS.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, orig)
            save(Image.open(orig), p, tm, quality=85 if p.suffix == '.jpg' else 82)
    demo = SITE / 'assets/demo/art'
    for p in sorted(demo.glob('*.webp')):
        orig = ORIGINALS / 'demo-art' / p.name
        if not orig.exists():
            orig.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, orig)
        save(Image.open(orig), p, tm)


# Planning guides and the press kit: one illustration per guide, three App Store screenshots.
PAGE_ART = {
    'page-wanchun-pavilion': APP / 'jingshan/cultural/wanchun-v2.png',
    'page-meridian-gate': APP / 'forbiddencity/building-art/meridian-gate.png',
    'page-gate-of-divine-might': APP / 'forbiddencity/building-art/gate-of-divine-might.png',
    'page-palace-of-heavenly-purity': APP / 'forbiddencity/building-art/palace-of-heavenly-purity.png',
    'page-hall-of-central-harmony': APP / 'forbiddencity/building-art/hall-of-central-harmony.png',
    'page-hall-of-preserving-harmony': APP / 'forbiddencity/building-art/hall-of-preserving-harmony.png',
    'page-roof-beasts': APP / 'forbiddencity/cultural/illustrations/fc-d014.png',
}
SCREENSHOTS = AI / 'penyola-artifacts/app-store/marketing-6.9-final'
PRESS_SHOTS = {'press-screen-map': '01.png', 'press-screen-story': '03.png', 'press-screen-route': '04.png'}
SHOT_W = 400


# The whole Forbidden City map (Pinterest artwork, approved): a web copy for the page and the full-size original
# behind a link, both watermarked only. Source stays in penyola-artifacts.
FC_MAP = AI / 'penyola-artifacts/marketing/pinterest/images/map-fc-whole-3000.jpg'
FC_MAP_WEB_W = 1200


FC_AREAS = ['outer', 'inner', 'west', 'east']  # 2:3 area maps, 1000 x 1500, shown as they are


def fc_map(tm):
    for area in FC_AREAS:
        save(Image.open(FC_MAP.parent / f'fc-area-{area}-2x3.jpg').convert('RGB'), IMG / f'fc-area-{area}.webp', tm, quality=85)
    im = Image.open(FC_MAP).convert('RGB')
    save(im.resize((FC_MAP_WEB_W, round(im.height * FC_MAP_WEB_W / im.width)), Image.LANCZOS), IMG / 'fc-map.webp', tm, quality=82)
    save(im, IMG / 'fc-map-full.jpg', tm, quality=85)


def page_images(tm):
    for name, src in PAGE_ART.items():
        im = Image.open(src)
        im = im.convert('RGBA' if 'A' in im.getbands() else 'RGB').resize((BLD_W, round(im.height * BLD_W / im.width)), Image.LANCZOS)
        save(im, IMG / f'{name}.webp', tm)
    for name, file in PRESS_SHOTS.items():
        im = Image.open(SCREENSHOTS / file).convert('RGB')
        save(im.resize((SHOT_W, round(im.height * SHOT_W / im.width)), Image.LANCZOS), IMG / f'{name}.webp', tm)


def main():
    from trustmark import TrustMark
    tm = TrustMark(verbose=False, model_type='Q', encoding_type=TrustMark.Encoding.BCH_5)
    if sys.argv[1:2] == ['--check']:
        for f in sys.argv[2:]:
            text, found, _ = tm.decode(Image.open(f).convert('RGB'), MODE='text')
            print(f, 'PENYOLA watermark found' if found and text == MARK else 'no watermark found')
        return
    if sys.argv[1:2] == ['--map']:  # only the Forbidden City map
        fc_map(tm)
        return
    page_images(tm)
    fc_map(tm)
    if sys.argv[1:2] == ['--pages']:  # only the guide and press images, leaving the others untouched
        return
    data = map_cards(tm)
    (IMG / 'map-cards.json').write_text(json.dumps(data, indent=1))
    gallery(tm)
    older_images(tm)


if __name__ == '__main__':
    main()
