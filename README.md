# Penyola website

Public site for the Penyola iOS app, pushed to the EricNing2023/penyola-site repository and served by GitHub Pages
from the root of `main` at the custom domain
https://penyola.com (the `CNAME` file sets it; DNS is at Cloudflare, records DNS-only).
The old EricNing2023/penyola repository (https://ericning2023.github.io/penyola/) is frozen as the support site the
1.0 App Store listing points to; this checkout keeps it as the `legacy` remote with pushing disabled.

- `demo.html` in-browser demo of the free Jingshan guide (data exported from penyola-release by `build_demo()`)
- `index.html` home · `support.html` support + FAQ (App Store Support URL is the site root)
- `privacy.html` (App Store Privacy Policy URL) · `terms.html` · `credits.html`

The HTML files are generated. Edit `build.py` (home and support copy) or `assets/site.css`, then run:

    python3 build.py            # reads ../penyola-release by default

`support.html` is frozen at the published version by the user's decision: `build.py` skips writing it (`FROZEN`),
so its copy and footer in `build.py` no longer reach the live page. Never commit a change to it without the user's
approval; if it ever shows as modified, restore it with `git checkout -- support.html` before committing.

Planning guides: copy in `articles.py`, rendered by `build.py` into folder URLs (`forbidden-city/…/`, `/guides/` hub, `/press/`).
Every ticket, hours or timing fact needs an official source; mark unchecked ones `[[…]]` and set `CHECK = True` to highlight them locally.

Privacy, terms and credits take their text from the legal files the app bundles
(`penyola-release/app/engine/iphone/Maps/ScenicResources/legal/`), so rebuild whenever those change.
The support email comes from `penyola-release/release-config.json`.

This repository replaces the output of `penyola-release/tools/build_site.py`
(`penyola-artifacts/site/`). Do not push from that older checkout, or the site reverts to the plain version.

Fonts: Manrope, SIL Open Font License 1.1 (`assets/fonts/OFL.txt`).

`RELEASED = True` in `build.py` (live since 2026-11-06): the badges link to the App Store and pages carry the Smart App Banner.
The build also writes `robots.txt`, `sitemap.xml` and the IndexNow key file; after a push run
`python3 ../penyola-release/tools/ping_indexnow.py`.

The "In the works" section on the home page (`NEXT` in `build.py`) previews maps still in development (area-focused site maps only, no mountain landscapes),
from `penyola-artifacts/test-catalog/`. It promises no dates. Update it as guides ship.
