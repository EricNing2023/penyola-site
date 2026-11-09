"""Third-party photos and videos shown on or linked from the planning guides, rendered by build.py.

Photos are Wikimedia Commons files under public domain, CC0, CC BY or CC BY-SA only (TEAM.md, long-term
website authorisation). Each is credited on the page that uses it, or whose social posts point to it,
and on credits.html. They are never watermarked. Check the file page again before adding one.
"""

COMMONS = 'https://commons.wikimedia.org/wiki/File:'
LICENCES = {
    'CC0': 'https://creativecommons.org/publicdomain/zero/1.0/',
    'CC BY 2.0': 'https://creativecommons.org/licenses/by/2.0/',
    'CC BY 3.0': 'https://creativecommons.org/licenses/by/3.0/',
    'CC BY 4.0': 'https://creativecommons.org/licenses/by/4.0/',
    'CC BY-SA 2.5': 'https://creativecommons.org/licenses/by-sa/2.5/',
    'CC BY-SA 3.0': 'https://creativecommons.org/licenses/by-sa/3.0/',
    'CC BY-SA 4.0': 'https://creativecommons.org/licenses/by-sa/4.0/',
}

# Commons file name: (author as the file page gives it, licence). Checked 2026-11-08.
PHOTOS = {
    'Views of the Forbidden City from Jingshan Park 1.jpg': ('EditQ', 'CC BY-SA 4.0'),
    'Wumen.jpg': ('Shizhao', 'CC BY-SA 2.5'),
    'Hall of Supreme Harmony.JPG': ('Gisling', 'CC BY 3.0'),
    'Beijing China Forbidden-City-03.jpg': ('CEphoto, Uwe Aranas', 'CC BY-SA 3.0'),
    'Beijing Forbidden City Hall of Central Harmony terraces-20071018-RM-143613.jpg': ('Reinhold Möller Ermell', 'CC BY-SA 4.0'),
    '保和殿 Baohe Hall - panoramio.jpg': ('lienyuan lee', 'CC BY 3.0'),
    'Palace of Heavenly Purity (20220218132818).jpg': ('N509FZ', 'CC BY-SA 4.0'),
    '交泰殿 Jiaotai Hall - panoramio.jpg': ('lienyuan lee', 'CC BY 3.0'),
    'Palace of Earthly Tranquility (20220218133044).jpg': ('N509FZ', 'CC BY-SA 4.0'),
    'Imperial Garden (54448349292).jpg': ('xiquinhosilva', 'CC BY 2.0'),
    'Forbidden City Beijing Shenwumen Gate.JPG': ('kallgan', 'CC BY-SA 3.0'),
    'Wanchun Pavilion, Jingshan Park, Beijing - November 2016 - 113.jpg': ('Another Believer', 'CC BY-SA 4.0'),
    'Jingshan (Coal Hill) Qiwang Tower (9869109674).jpg': ('Gary Todd', 'CC0'),
    # First Time in Beijing videos (marketing/video/first-time/commons/credits.json). Checked 2026-11-09.
    'Corner Tower of the Forbidden City, Beijing.jpg': ('ZhengZhou', 'CC BY-SA 4.0'),
    '北京大兴国际机场 2024-05-15.jpg': ('xiquinhosilva', 'CC BY 4.0'),
    'Beijing Daxing International Airport Terminal 20191005.jpg': ('Tyg728', 'CC BY-SA 4.0'),
    'Beijing Capital International Airport Terminal 3 Interior 20090818.jpg': ('颐园新居', 'CC BY-SA 3.0'),
}

# Long video C (video group, marketing/video/v2/seo-handoff/). It appears on the page only once
# youtube_id is set; the transcript is read from the hand-over folder at build time.
FC_ROUTE_VIDEO = {
    'youtube_id': None,  # set after upload, with upload_date
    'upload_date': None,
    'name': 'Forbidden City Walking Route: Meridian Gate to the Gate of Divine Might in 9 Stops',
    'description': "A stop-by-stop walk along the Forbidden City's central axis, from the Meridian Gate in the south to the Gate of Divine Might in the north, about 1.8 km, with the details worth stopping for on the way.",
    'duration': 'PT6M42S',
    'transcript': 'penyola-artifacts/marketing/video/v2/seo-handoff/c-fc-route-long.transcript.txt',
    'draft': 'penyola-artifacts/marketing/video/v2/seo-handoff/videoobject-draft.json',  # chapters
}
