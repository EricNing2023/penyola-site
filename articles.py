"""Planning guides (landing pages) for penyola.com, rendered by build.py.

Bodies are HTML with three tokens: @ROOT@ (relative path to the site root), @STORE@ (App Store badge)
and [[...]] around every ticket, hours or timing claim. While CHECK is true those claims are highlighted
for review and listed in verify-claims.txt; set it to False once they have been checked on the official sites.
Facts come from the app's own site data (penyola-release ScenicResources) unless a source is named.
"""
from dataclasses import dataclass, field

from media import FC_ROUTE_VIDEO

CHECK = False
CHECKED = '2026-11-06'  # "Last checked" date shown on every guide


@dataclass
class Article:
    path: str          # folder URL, e.g. 'forbidden-city/tickets-for-foreigners/'
    short: str         # footer link text
    title: str         # <title>, 60 characters or fewer
    description: str   # meta description, 155 characters or fewer
    eyebrow: str
    h1: str
    image: str         # under assets/img/, or None for no illustration
    image_alt: str
    about: dict        # schema.org TouristAttraction
    body: str
    related: list = field(default_factory=list)
    photos: list = field(default_factory=list)  # Commons files from media.PHOTOS, credited at the end
    video: dict = None  # e.g. media.FC_ROUTE_VIDEO; shown once it has a youtube_id
    checked: str = CHECKED  # date the facts on this page were last checked on the official sources
    published: str = None  # first publication date, if earlier than checked (datePublished)
    sources: list = field(default_factory=list)  # (label, official URL), listed at the end of the page
    city: str = None  # part of that city's "first time" series (CITY_HUBS), e.g. 'beijing'
    cta: bool = True  # False on pages about sights the app does not cover yet
    og_image: str = None  # share image under assets/img/ when it is not the illustration
    extra_ld: list = field(default_factory=list)  # more schema.org objects, e.g. an ImageObject


# Official pages behind the facts on the older guides (listed under "Sources" on each page).
DPM_VISIT = ('Palace Museum: visiting information', 'https://www.dpm.org.cn/Visit.html')
DPM_RULES = ('Palace Museum: visitor rules (booking, sessions, refunds, bags)', 'https://www.dpm.org.cn/singles_detail/259831.html')
DPM_BOOKING = ('Palace Museum: official ticket booking', 'https://bookingticket.dpm.org.cn/')
DPM_GATE = ('Palace Museum: Gate of Supreme Harmony works notice', 'https://www.dpm.org.cn/announce_detail/379422.html')
DPM_HALL = ('Palace Museum: Hall of Supreme Harmony', 'https://www.dpm.org.cn/explore/building/236465.html')
DPM_GUIDES = ('Palace Museum: guided tour routes and fees', 'https://www.dpm.org.cn/announce_detail/239321.html')
JS_PARK = ('Beijing Municipal Government: Jingshan Park', 'https://english.beijing.gov.cn/specials/parktours/guidevisitors/jingshanpark/')
JS_TICKETS = ('Beijing Municipal Government: Jingshan Park tickets', 'https://english.beijing.gov.cn/specials/ticketing/parks/202407/t20240719_3753324.html')
JS_PARKS_CENTRE = ('Beijing Municipal Administration Center of Parks: Jingshan Park', 'https://gygl.beijing.gov.cn/mlgy/mlgy_lsmy/201911/t20191129_732675.html')
SP_GOV = ('Beijing Municipal Government: Summer Palace', 'https://english.beijing.gov.cn/specials/parktours/guidevisitors/summerpalace/')
SP_SITE = ('Summer Palace official site: hours, tickets and boats', 'https://www.summerpalace.net.cn/')
NIA_TRANSIT = ('National Immigration Administration: visa-free transit', 'https://www.nia.gov.cn/n741440/n741577/c1731205/content.html')

FORBIDDEN_CITY = {
    '@type': 'TouristAttraction', 'name': 'Forbidden City (Palace Museum)', 'alternateName': '故宫',
    'address': {'@type': 'PostalAddress', 'streetAddress': '4 Jingshan Front Street', 'addressLocality': 'Dongcheng District, Beijing', 'addressCountry': 'CN'},
    'geo': {'@type': 'GeoCoordinates', 'latitude': 39.91657, 'longitude': 116.39078},
    'sameAs': 'https://www.dpm.org.cn/',
}
JINGSHAN = {
    '@type': 'TouristAttraction', 'name': 'Jingshan Park', 'alternateName': '景山公园',
    'address': {'@type': 'PostalAddress', 'streetAddress': '44 Jingshan West Street', 'addressLocality': 'Xicheng District, Beijing', 'addressCountry': 'CN'},
    'geo': {'@type': 'GeoCoordinates', 'latitude': 39.92442, 'longitude': 116.39038},
    'isAccessibleForFree': False,
}

JINGSHAN_VIEW = Article(
    path='jingshan-park/best-view-of-the-forbidden-city/',
    short='Jingshan Park view',
    title='Jingshan Park: the best view of the Forbidden City',
    description='Climb 10–20 minutes to Wanchun Pavilion for the classic view over the Forbidden City. Tickets, hours, best time and a free offline audio guide.',
    eyebrow='Jingshan Park · free guide',
    h1='Jingshan Park: the best view of the Forbidden City',
    image='page-wanchun-pavilion.webp',
    image_alt='Hand-drawn illustration of Wanchun Pavilion on top of Jingshan Hill',
    about=JINGSHAN,
    related=['forbidden-city/half-day-route/', 'forbidden-city/tickets-for-foreigners/'],
    photos=['Jingshan (Coal Hill) Qiwang Tower (9869109674).jpg', 'Wanchun Pavilion, Jingshan Park, Beijing - November 2016 - 113.jpg', 'Views of the Forbidden City from Jingshan Park 1.jpg'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[JS_TICKETS, JS_PARK, JS_PARKS_CENTRE, DPM_VISIT],
    body='''
<h2>Where is the best view of the Forbidden City?</h2>
<p>The best view is from Wanchun Pavilion on top of Jingshan Hill, 94.2 metres above sea level and roughly 45 metres above the streets around it, directly north of the palace: a 10–20 minute climb on stone paths and steps gives you the whole run of golden roofs from the Gate of Divine Might down to the Meridian Gate. Entry costs ¥2, and the park's South Gate is just across the road from the Forbidden City's north exit.</p>
<p>Wanchun is the middle and highest of the hill's five pavilions, the one with three tiers of yellow-glazed roofs edged in green. Stand on its south terrace and the palace lies along Beijing's north–south Central Axis, which UNESCO inscribed as a World Heritage property in 2024. Turn round and the same axis continues north to the Drum and Bell Towers.</p>

<h2>How much does Jingshan Park cost, and do I need to book?</h2>
<ul>
  <li>Adult ticket: ¥2; students ¥1. During the park's cultural seasons (usually spring and midsummer) the adult price is ¥10.</li>
  <li>Book online up to 7 days ahead on the official "Visiting Beijing Parks" WeChat account, with your passport.</li>
</ul>

<h2>What are the opening hours?</h2>
<ul>
  <li>1 April – 31 October: 06:00–21:00, last entry 20:30.</li>
  <li>1 November – 31 March: 06:30–20:00, last entry 19:30.</li>
  <li>Some halls inside the park keep shorter hours.</li>
</ul>

<h2>Is Jingshan Park worth it after the Forbidden City?</h2>
<p>Yes, and the timing works: the Forbidden City's main visitor exit, the Gate of Divine Might, is just across the road from Jingshan's South Gate. After two or three hours walking through courtyards at ground level, the hilltop shows you how the whole palace fits together, which is hard to picture from inside. It is also open long after the palace closes (16:30 or 17:00 depending on the season), so you can rest, then climb for the late light.</p>

<h2>When is the best time to go up?</h2>
<p>Late afternoon is the favourite: the sun drops in the west and lights the palace roofs from the side. Arrive about 30 minutes before sunset in spring and autumn, when the terrace gets crowded. Early morning, soon after the 06:00 or 06:30 opening, is quieter and you will share the paths with locals doing tai chi and singing. Clear days after wind or rain give the sharpest views across the city.</p>

<h2>How long do you need in Jingshan Park?</h2>
<ul>
  <li><strong>About 50 minutes</strong> for the hilltop and the memorial site: the shortest route in the Penyola guide is 52 minutes.</li>
  <li><strong>About 1 hour 40 minutes</strong> to add the pavilions along the ridge and Shouhuang Hall at the north end of the park.</li>
  <li><strong>About 2½ hours</strong> to see all five pavilions, the halls and the gardens at an easy pace.</li>
</ul>
<p>The times assume walking at an easy pace plus ten minutes at each sight.</p>

<h2>What else is there to see on the hill?</h2>
<p>Four smaller pavilions flank Wanchun on the ridge, two on each side: the inner pair with octagonal roofs, the outer pair with round ones. On the eastern slope, two stone steles mark where the last Ming emperor, Chongzhen, died in 1644 as rebel armies entered Beijing; the scholar tree beside them is a replacement planted in 1996. At the north end of the park, Shouhuang Hall once held the Qing emperors' ancestral portraits.</p>

<h2>How do I get to Jingshan Park?</h2>
<ul>
  <li><strong>From the Forbidden City:</strong> leave by the Gate of Divine Might and cross the road to the South Gate.</li>
  <li><strong>By bus:</strong> 58, 101, 103, 109 or 124 to Gugong, then walk about 200 metres to the South Gate.</li>
  <li><strong>By metro:</strong> Line 8 to National Art Museum, then bus 109 or 191; or Line 1 to Tian'anmen West, then bus 5 to Xibanqiao, by the West Gate.</li>
  <li><strong>For a taxi:</strong> show the driver <span lang="zh-Hans">北京市西城区景山西街44号 景山公园</span>.</li>
</ul>

<h2>Is there a free audio guide for Jingshan Park?</h2>
<p>Yes. The Jingshan Park guide in Penyola is free and complete: a hand-drawn map of the park, the pavilions, halls and memorials with narrated stories in English, and three suggested walks. It works without a phone signal once the app is installed. You can <a href="@ROOT@demo.html">try it in your browser</a> before you go.</p>
''')

HALF_DAY = Article(
    path='forbidden-city/half-day-route/',
    short='Forbidden City in half a day',
    title='Forbidden City in half a day: a 3–4 hour route',
    description='A 3–4 hour Forbidden City route from the Meridian Gate to the Gate of Divine Might: what to see on the central axis, what to add, and what to skip.',
    eyebrow='Forbidden City · route',
    h1='The Forbidden City in half a day',
    image='page-palace-of-heavenly-purity.webp',
    image_alt='Hand-drawn illustration of the Palace of Heavenly Purity',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/map/', 'forbidden-city/tickets-for-foreigners/', 'forbidden-city/entrance-and-exit/', 'forbidden-city/hall-of-supreme-harmony/', 'jingshan-park/best-view-of-the-forbidden-city/'],
    photos=['Views of the Forbidden City from Jingshan Park 1.jpg', 'Wumen.jpg', 'Hall of Supreme Harmony.JPG', 'Beijing China Forbidden-City-03.jpg', 'Beijing Forbidden City Hall of Central Harmony terraces-20071018-RM-143613.jpg', '保和殿 Baohe Hall - panoramio.jpg', 'Palace of Heavenly Purity (20220218132818).jpg', '交泰殿 Jiaotai Hall - panoramio.jpg', 'Palace of Earthly Tranquility (20220218133044).jpg', 'Imperial Garden (54448349292).jpg', 'Forbidden City Beijing Shenwumen Gate.JPG', 'Wanchun Pavilion, Jingshan Park, Beijing - November 2016 - 113.jpg'],
    video=FC_ROUTE_VIDEO,
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_VISIT, DPM_RULES],
    body='''
<h2>How long do you need in the Forbidden City?</h2>
<p>Half a day is enough: allow 3–4 hours, which covers the central axis from the Meridian Gate to the Gate of Divine Might (about 1 hour 40 minutes of walking and short stops before queues) plus one side area such as the Clock Gallery or the Treasure Gallery. A full day lets you add both galleries and the quieter western palaces.</p>
<p>The palace is one-way: you enter from the south through the Meridian Gate and leave from the north or east. Plan the route as a single walk north, with side trips to the east or west on the way. The <a href="@ROOT@forbidden-city/map/">Forbidden City map</a> shows both routes and 21 spots on one page.</p>

<h2>What should I do before I go?</h2>
<ul>
  <li>Book a ticket online: sales open at 20:00 Beijing time seven days before your visit, and no tickets are sold on the day. See <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book with a passport</a>.</li>
  <li>Bring the original passport you booked with; a photo or copy will not do.</li>
  <li>Check the day: the palace is closed on Mondays except public holidays.</li>
  <li>Choose your session: morning tickets must check in by 12:00; afternoon tickets from 11:00.</li>
</ul>

<h2>What is the best half-day route?</h2>
<ol>
  <li><strong>Meridian Gate (0:00).</strong> Security and ticket check. The U-shaped gate is the largest in the palace; once through, cross the Inner Golden Water Bridges.</li>
  <li><strong>Gate of Supreme Harmony.</strong> Closed for conservation since 3 August 2026: walk round it by the side passages. Its bronze lions are still visible outside the works fence.</li>
  <li><strong>Hall of Supreme Harmony (about 0:20).</strong> The throne hall on its three-tier marble terrace. Before you climb, find the bronze tortoise and crane, the sundial and the small grain measure on the terrace, and count the ten beasts on the roof ridge.</li>
  <li><strong>Halls of Central and Preserving Harmony.</strong> Two smaller halls behind it, where the emperor prepared for ceremonies and held palace examinations. Behind the last one, a huge carved marble ramp runs down the middle of the stairs.</li>
  <li><strong>Palace of Heavenly Purity, Hall of Union, Palace of Earthly Tranquility (about 1:00).</strong> The Inner Court, where the emperors lived. The Hall of Union holds the imperial seals and a water clock.</li>
  <li><strong>Side trip (about 1:15–2:30).</strong> East to the Clock Gallery and the Treasure Gallery (¥10 each, bought separately), or west to the Six Western Palaces, where consorts lived.</li>
  <li><strong>Imperial Garden (about 2:45).</strong> Old cypresses, rockeries and pavilions at the north end, including a pair of intertwined cypresses.</li>
  <li><strong>Gate of Divine Might (about 3:15).</strong> Exit north. Jingshan Park is across the road.</li>
</ol>
<p>Times are from the gate and assume an unhurried pace. The Penyola guide's Classic Highlights walk covers steps 1–5, 7 and 8 in about 1 hour 36 minutes without queues; its Full Exploration walk, with the galleries and side palaces, takes about 4 hours.</p>

<h2>What can I skip if I am short of time?</h2>
<p>If you have only two hours, stay on the central axis and skip the side trip. The halls along the axis are viewed from their doorways, so you lose little by not queuing at each one: look in, then move on. The galleries are worth the extra ticket only if you have at least an hour left.</p>

<h2>Morning or afternoon?</h2>
<p>Go early. The first entry is 08:30, and the central axis is quietest in the first hour before tour groups arrive. In the afternoon, remember last entry is 16:00 from April to October and 15:30 from November to March, and the galleries take their last visitors ten minutes later.</p>

<h2>Where do I go after the Forbidden City?</h2>
<p>Cross to <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a> and climb to Wanchun Pavilion. After half a day inside the walls, the hilltop shows you the whole palace you have just walked through. If you leave by the East Glorious Gate instead, you come out near Wangfujing.</p>

<h2>Can I follow this route offline?</h2>
<p>Yes. Penyola has both walks on a hand-drawn map of the palace, with stories and narrated audio for the halls, beasts, trees and inscriptions along the way, all stored on your iPhone. Compare it with the other ways to hear the palace's stories in <a href="@ROOT@forbidden-city/audio-guide-options/">Forbidden City audio guide options</a>.</p>
''')

TICKETS = Article(
    path='forbidden-city/tickets-for-foreigners/',
    short='Forbidden City tickets',
    title='Forbidden City tickets for foreigners: booking with a passport',
    description='How foreign visitors book Forbidden City tickets with a passport: when sales open, prices (¥60 or ¥40), the rules at the gate and what to do if tickets sell out.',
    eyebrow='Forbidden City · tickets',
    h1='Forbidden City tickets for foreigners',
    image='page-meridian-gate.webp',
    image_alt='Hand-drawn illustration of the Meridian Gate, the entrance to the Forbidden City',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/half-day-route/', 'forbidden-city/audio-guide-options/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_RULES, DPM_VISIT, DPM_BOOKING],
    body='''
<h2>How do foreigners book Forbidden City tickets?</h2>
<p>Book online with your passport number: tickets go on sale at 20:00 Beijing time, seven days before the visit, cost ¥60 from April to October and ¥40 from November to March, and are not sold at the gate. Your passport is your ticket; you show it at the Meridian Gate.</p>

<h2>Where do I book?</h2>
<ul>
  <li>The Palace Museum's English booking site, bookingticket.dpm.org.cn, which takes international cards. The Chinese site is ticket.dpm.org.cn.</li>
  <li>The museum's official WeChat mini program, <span lang="zh-Hans">故宫博物院</span>, if you already use WeChat.</li>
</ul>
<p>The museum says it has not authorised any third-party ticket agents. Tour companies that include tickets book them in your name with your passport details, so give your passport number only to a company you trust.</p>

<h2>How much are Forbidden City tickets?</h2>
<table>
  <thead><tr><th>Ticket</th><th>Price</th></tr></thead>
  <tbody>
    <tr><td>Adult, 1 April – 31 October</td><td>¥60</td></tr>
    <tr><td>Adult, 1 November – 31 March</td><td>¥40</td></tr>
    <tr><td>Students aged 18 and over, in undergraduate study or below, with proof</td><td>¥20</td></tr>
    <tr><td>Visitors aged 60 and over</td><td>¥30 (April–October) or ¥20 (November–March)</td></tr>
    <tr><td>Treasure Gallery or Clock Gallery, each</td><td>¥10</td></tr>
  </tbody>
</table>
<p>Free entry for under-18s applies to Chinese citizens and foreign permanent residents; check the price for other children when you book. Children under 14 must come with an adult, up to three per adult. ¥60 is about US$8.</p>

<h2>What do I need to book?</h2>
<ul>
  <li>The passport each visitor will carry. One ticket per passport per day, and a ticket cannot be moved to another person, date or session.</li>
  <li>A morning or afternoon session. Morning tickets check in by 12:00; afternoon tickets from 11:00.</li>
  <li>A way to pay: the English booking site accepts international cards.</li>
</ul>

<h2>What happens at the gate?</h2>
<p>Go to the Meridian Gate, the only visitor entrance, on the south side. The nearest metro stations are Tian'anmen East and Tian'anmen West on Line 1; see <a href="@ROOT@forbidden-city/entrance-and-exit/">entrance and exits</a> for the walk. Show the original passport you booked with, not a photo or copy, and expect a security check. You leave by the Gate of Divine Might (north) or the East Glorious Gate (east), not by the Meridian Gate.</p>

<h2>When is the Forbidden City open?</h2>
<ul>
  <li>1 April – 31 October: 08:30–17:00, last entry 16:00.</li>
  <li>1 November – 31 March: 08:30–16:30, last entry 15:30.</li>
  <li>Closed on Mondays, except public holidays.</li>
</ul>

<h2>What if tickets are sold out?</h2>
<ul>
  <li>Be online at 20:00 Beijing time seven days ahead; weekend and holiday dates go first, especially during the Chinese national holidays in early May and early October.</li>
  <li>Check again the evening before: visitors can cancel until midnight before their visit.</li>
  <li>Choose a weekday or an afternoon session.</li>
  <li>If the palace is full, <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a> shows you the whole palace from above.</li>
</ul>

<h2>Can I cancel?</h2>
<p>Yes, through the channel you booked with, until midnight before your visit. Later cancellations and no-shows count as missed visits: three in 180 days and you cannot book for 60 days.</p>

<h2>What is there to see once I am in?</h2>
<p>Plan 3–4 hours. Our <a href="@ROOT@forbidden-city/half-day-route/">half-day route</a> follows the central axis from the Meridian Gate to the Gate of Divine Might, with the stops worth slowing down for. Penyola has the route on a hand-drawn map with audio stories, and the ticket notes, hours and a Chinese address card for your taxi, all offline.</p>
''')

AUDIO = Article(
    path='forbidden-city/audio-guide-options/',
    short='Forbidden City audio guides',
    title='Forbidden City audio guide options compared',
    description='The official audio guide, the museum’s English guides (from ¥600) and phone apps for the Forbidden City compared: cost, offline use, and who each suits.',
    eyebrow='Forbidden City · audio guides',
    h1='Forbidden City audio guide options, compared',
    image='bld-imperial-garden.webp',
    image_alt='Hand-drawn illustration of the Imperial Garden in the Forbidden City',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/half-day-route/', 'forbidden-city/tickets-for-foreigners/'],
    published='2026-11-07',
    sources=[DPM_GUIDES, DPM_VISIT],
    body='''
<h2>What are the options for an English audio guide?</h2>
<p>There are four: the museum's own rental audio guide, a human guide, a phone app, or a web-link guide bundled with some tickets. Most visitors are well served by either the official device or an offline app; a human guide is worth it if you want to ask questions.</p>

<h2>How do they compare?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th>Option</th><th>Cost</th><th>Works offline</th><th>Best for</th><th>Watch out for</th></tr></thead>
  <tbody>
    <tr><td>Official audio guide (rental device)</td><td>Rental fee</td><td>Yes</td><td>Anyone who wants the museum's own commentary without using their phone</td><td>Queue at pickup; return it on your way out</td></tr>
    <tr><td>Human guide (private or small group)</td><td>Museum English guides: ¥600 (1 hour) to ¥1,500 (2.5 hours) for up to 5 people; agencies vary</td><td>Yes</td><td>First-time visitors who want context and questions answered</td><td>Set pace and route; book ahead; agree what is included</td></tr>
    <tr><td>Phone apps</td><td>From free to a few dollars</td><td>Depends on the app</td><td>Independent visitors who like to choose what to hear</td><td>Some need a data connection, which needs a working roaming plan in China</td></tr>
    <tr><td>Web-link guide sold with a ticket</td><td>Included in the bundle</td><td>Usually not</td><td>Visitors booking a ticket package anyway</td><td>Needs mobile data and a charged phone throughout</td></tr>
  </tbody>
</table>
</div>

<h2>Is the official Forbidden City audio guide any good?</h2>
<p>It is the safe default: the museum's own commentary, in several languages, on a handheld device. Its limits are the queue at busy times and that it follows the main halls, so the smaller details in the courtyards get little time.</p>

<h2>Should I hire a human guide?</h2>
<p>A good guide is the best way to understand the palace if you want stories told around your questions, and the only option that can steer you through crowds and closures on the day. The museum runs its own English-language tours for groups of one to five: ¥600 for an hour on the central axis, ¥1,200 for two hours with the Treasure Gallery, ¥1,500 for two and a half hours, with gallery tickets extra. Agencies and independent guides are the alternative; agree in advance whether tickets are included and how long the tour lasts.</p>

<h2>Which apps cover the Forbidden City in English?</h2>
<p>Several apps on the App Store cover the Forbidden City in English. They differ mainly in whether the content is stored on your phone and in how it is organised. Check that the app works offline before you rely on it: mobile data from a foreign SIM in China can be slow or unreliable. Read recent reviews too, since some city guides cover the palace in only a few stops.</p>
<p><strong>Penyola</strong>, our own app, is one of them. It is built around a hand-drawn map of the palace on which you tap any hall, gate or carved detail to read its story or hear it narrated in English. It suggests walks with times, and keeps the visitor information to hand. Everything is stored on the iPhone, so it works with no signal. The Forbidden City and Summer Palace guides are unlocked together with one purchase of US$6.99; the Jingshan Park guide is free. What it does not do: it does not use your location, so it will not play automatically as you walk; it is in English only; and it is for iPhone only.</p>

<h2>Which option should I choose?</h2>
<ul>
  <li><strong>You want no planning and no phone:</strong> the official audio guide.</li>
  <li><strong>You want someone to ask:</strong> a human guide.</li>
  <li><strong>You want to choose your own pace and keep it after the visit:</strong> an offline app.</li>
  <li><strong>You are short of time:</strong> any of them, on the <a href="@ROOT@forbidden-city/half-day-route/">half-day route</a>.</li>
</ul>
<p>Whichever you choose, bring headphones, a charged phone for your ticket booking and the passport you booked with. If you have not booked yet, see <a href="@ROOT@forbidden-city/tickets-for-foreigners/">Forbidden City tickets for foreigners</a>.</p>
''')


SUMMER_PALACE = {
    '@type': 'TouristAttraction', 'name': 'Summer Palace', 'alternateName': '颐和园',
    'address': {'@type': 'PostalAddress', 'streetAddress': '19 Xinjiangongmen Road', 'addressLocality': 'Haidian District, Beijing', 'addressCountry': 'CN'},
    'geo': {'@type': 'GeoCoordinates', 'latitude': 39.99041, 'longitude': 116.26593},
}
BEIJING = {'@type': 'City', 'name': 'Beijing', 'alternateName': '北京'}

ENTRANCE = Article(
    path='forbidden-city/entrance-and-exit/',
    short='Forbidden City entrance and exits',
    title='Forbidden City entrance and exit: Meridian Gate to Jingshan',
    description='The Forbidden City has one entrance, the Meridian Gate, and two exits. How to reach the entrance by metro or taxi, and where each exit leaves you.',
    eyebrow='Forbidden City · getting in and out',
    h1='Forbidden City entrance and exits',
    image='page-gate-of-divine-might.webp',
    image_alt='Hand-drawn illustration of the Gate of Divine Might, the north exit of the Forbidden City',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/tickets-for-foreigners/', 'forbidden-city/half-day-route/', 'jingshan-park/best-view-of-the-forbidden-city/', 'beijing/chinese-address-cards/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_VISIT, DPM_RULES],
    body='''
<h2>Where is the entrance to the Forbidden City?</h2>
<p>There is one visitor entrance, the Meridian Gate (<span lang="zh-Hans">午门</span>, Wumen) on the south side, and two exits: the Gate of Divine Might (<span lang="zh-Hans">神武门</span>) to the north, opposite Jingshan Park, and the East Glorious Gate (<span lang="zh-Hans">东华门</span>) to the east. The palace is about 960 metres from south to north, and you cannot come back in once you leave.</p>

<h2>How do I get to the Meridian Gate by metro?</h2>
<p>The nearest stations are Tian'anmen East and Tian'anmen West on Line 1. From there, the museum gives two ways in:</p>
<ul>
  <li><strong>If you have booked only the Forbidden City:</strong> walk along the moat-side roads, from the East or the West Glorious Gate, south to the Meridian Gate. This avoids the Tian'anmen Square security queues.</li>
  <li><strong>If you have also booked Tiananmen Square:</strong> go through the square's security checks, then north through Tian'anmen and the Duanmen gate to the Meridian Gate. This passage is open Tuesday to Sunday, 08:00–16:00, and runs one way, north.</li>
</ul>
<p>Leave plenty of time: queues for security are longest on weekend and holiday mornings.</p>

<h2>Can a taxi drop me at the entrance?</h2>
<p>Not right at it: the museum has no car park, and the Meridian Gate is reached on foot. Ask to be dropped at the East Glorious Gate (<span lang="zh-Hans">故宫东华门</span>) and walk south along the moat-side road to the Meridian Gate. The East Glorious Gate is an exit only, so do not queue there. Show the driver the name in Chinese; there are printable cards in <a href="@ROOT@beijing/chinese-address-cards/">Chinese address cards for Beijing sights</a>.</p>

<h2>What do I need at the gate?</h2>
<ul>
  <li>The original passport you booked with: your passport is your ticket.</li>
  <li>A booking for today: tickets are not sold at the gate. See <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book</a>.</li>
  <li>Time for a security check of bags. Suitcases and bags of 20 inches or more must be left at the bag store on the west side of the Duanmen square, and are collected at the exits, outside the Gate of Divine Might or the East Glorious Gate.</li>
</ul>

<h2>Which exit should I use?</h2>
<p><strong>The Gate of Divine Might (north)</strong> is the natural end of a walk along the central axis. Across the road is the South Gate of <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a>, the best view of the palace you have just walked through. Buses 58, 101, 103, 109 and 124 stop outside at Shenwumen. There is no metro station next to it.</p>
<p><strong>The East Glorious Gate (east)</strong> suits you if you finish in the east of the palace, near the Treasure Gallery, or want to go on to Wangfujing for food and shopping. Wangfujing's main street is about 800 metres east along Dong'anmen Street.</p>
<p>The West Glorious Gate is staff only, and you cannot leave by the Meridian Gate.</p>

<h2>How long is it from the entrance to the exit?</h2>
<p>Walking straight up the central axis with no stops takes about a quarter of an hour; nobody does that. A visit along the axis with short stops takes about 1 hour 40 minutes before queues, and 3–4 hours with a side trip; see <a href="@ROOT@forbidden-city/half-day-route/">the half-day route</a>. Toilets, cafés and mother-and-baby rooms are spaced along the route; bring water anyway.</p>

<h2>Which way round should I visit with Jingshan Park?</h2>
<p>The palace is strictly one-way, south to north, so the order is fixed: Forbidden City first, then out through the Gate of Divine Might and across to Jingshan. Jingshan stays open long after the palace closes (until 20:00 or 21:00 depending on the season), so finishing on the hilltop near sunset works well.</p>

<h2>Can I see the gates on a map offline?</h2>
<p>Yes. Penyola's Forbidden City map shows the entrance, both visitor exits and the walks between them, and the visitor information with the address in Chinese, all stored on the phone.</p>
''')

HALL = Article(
    path='forbidden-city/hall-of-supreme-harmony/',
    short='Hall of Supreme Harmony',
    title='Hall of Supreme Harmony: what to look for',
    description='The Hall of Supreme Harmony is the Forbidden City’s largest hall. What to look for on its terrace, roof and throne, and how long to spend there.',
    eyebrow='Forbidden City · highlight',
    h1='Hall of Supreme Harmony: what to look for',
    image='bld-hall-of-supreme-harmony.webp',
    image_alt='Hand-drawn illustration of the Hall of Supreme Harmony on its marble terrace',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/roof-guardians/', 'forbidden-city/half-day-route/', 'forbidden-city/audio-guide-options/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_HALL, DPM_GATE, DPM_VISIT, DPM_RULES],
    body='''
<h2>What is the Hall of Supreme Harmony?</h2>
<p>It is the largest and most important hall in the Forbidden City, the throne hall where emperors were enthroned, married and received the court on great occasions. It stands on a three-tier white marble terrace about 8 metres high, and the present building dates from a rebuilding in 1695 under the Kangxi Emperor, after earlier halls burned. Plan 20–30 minutes here: most of what is worth seeing is outside.</p>

<h2>Can you go inside?</h2>
<p>No. Visitors look in from the open doorway at the front. The view is worth the short wait at the rail: the gilded throne on its raised platform, six columns wrapped in golden dragons, and above them a coffered ceiling whose centre is a carved dragon holding a pearl. Take a look, then step aside for the next person.</p>

<h2>What should I look for on the terrace?</h2>
<p>Before climbing the last steps, walk along the terrace in front of the hall. Most visitors pass straight by four objects that explain what the building was for:</p>
<ul>
  <li><strong>A bronze tortoise and a bronze crane</strong> on each side, both symbols of long life. On ceremonial days, incense burned inside them.</li>
  <li><strong>A sundial</strong> on the east side: a stone disc tilted to the sky, with a bronze pointer at its centre.</li>
  <li><strong>A standard measure</strong>, the jialiang, on the west side: a small bronze vessel on a stone pavilion-shaped stand, a standard for measuring grain.</li>
</ul>
<p>Time and measure, placed in front of the throne: the message is that the emperor set the standards the empire ran on.</p>

<h2>What is on the roof?</h2>
<p>Look up at the lower corners of the roof. Each ridge carries a line of small figures led by a man riding a bird. The Hall of Supreme Harmony has ten beasts behind him, more than any other building in China, and the last of them, a winged figure holding a weapon, appears only here. At each end of the top ridge sits a much larger dragon-like ornament, the chiwen, 3.4 metres tall. Binoculars or a phone zoom help. There is more on the figures in <a href="@ROOT@forbidden-city/roof-guardians/">the roof guardians of the Forbidden City</a>.</p>

<h2>What about the terrace itself?</h2>
<p>The three halls of the Outer Court share one marble platform. Count its three tiers on the stairs, and look along the edges for the carved dragon heads below the balustrades: they are drainage spouts. In heavy summer rain, water pours from all of them at once, a sight the museum calls "a thousand dragons spouting water". Near the foot of the terrace, large metal vats once held water for fighting fires in a palace built of wood.</p>

<h2>Why is the courtyard so big?</h2>
<p>The square in front of the hall is the largest open space in the palace. On ceremonial days, officials lined up on it by rank, marked by small stone tablets set into the paving. The emptiness was the point: a vast, treeless court that made everyone in it look small before the throne.</p>

<h2>Is the Gate of Supreme Harmony open?</h2>
<p>The gate in front of the courtyard has been closed for conservation since 3 August 2026, with no reopening date announced. Visitors walk around it by the side passages; its bronze lions are still visible outside the works fence.</p>

<h2>When is the best time to see it?</h2>
<p>In the first hour after the 08:30 opening, before tour groups fill the doorway, or late in the afternoon, when the terrace gets the side light. Cloudy days are good for the roof details; on bright days the yellow tiles glare.</p>

<h2>Is there an audio story for the hall?</h2>
<p>Penyola has the hall and each of these details as separate points on its hand-drawn map, with illustrated stories and narration, so you can stand at the sundial and listen to the story of the sundial. It works offline.</p>
''')

ROOF = Article(
    path='forbidden-city/roof-guardians/',
    short='Roof guardians explained',
    title='The roof guardians of the Forbidden City explained',
    description='The small figures on Forbidden City roofs: what the ten beasts are, why their number changes from building to building, and where to see them best.',
    eyebrow='Forbidden City · details',
    h1='The roof guardians of the Forbidden City',
    image='page-roof-beasts.webp',
    image_alt='Hand-drawn illustration of the line of guardian figures on a Forbidden City roof ridge',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/hall-of-supreme-harmony/', 'forbidden-city/with-kids/', 'forbidden-city/half-day-route/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_HALL],
    body='''
<h2>What are the little figures on the roofs?</h2>
<p>They are ceramic guardians set in a line along the sloping ridges at the corners of the roofs: a man riding a bird at the front, followed by up to ten mythical beasts. The Hall of Supreme Harmony is the only building with all ten; most halls have nine, seven or five, and smaller gates fewer. The number tells you how important the building was.</p>

<h2>What do the ten beasts mean?</h2>
<p>In order from the front, behind the rider, the usual list is:</p>
<ol>
  <li><strong>Dragon</strong>, the emperor's own symbol.</li>
  <li><strong>Phoenix</strong>, linked with the empress and with virtue.</li>
  <li><strong>Lion</strong>, a guardian, as at the palace gates.</li>
  <li><strong>Heavenly horse</strong> and</li>
  <li><strong>Sea horse</strong>, which carry the emperor's authority across land and sea.</li>
  <li><strong>Suanni</strong>, a lion-like beast said to love smoke and fire, often seen on incense burners.</li>
  <li><strong>Yayu</strong>, a fish-tailed sea creature believed to bring rain and so to protect against fire.</li>
  <li><strong>Xiezhi</strong>, a one-horned beast that can tell the guilty from the innocent, a symbol of justice.</li>
  <li><strong>Douniu</strong>, a horned dragon-fish, another protector against fire and flood.</li>
  <li><strong>Xingshi</strong>, a winged, monkey-like figure holding a vajra, the "tenth" beast found only on the Hall of Supreme Harmony.</li>
</ol>
<p>Several of them have to do with water and fire. In a palace of wooden halls, fire was the greatest danger, and these figures were part of the defences, alongside the water vats in the courtyards.</p>

<h2>Who is the man riding a bird?</h2>
<p>He is usually called the immortal riding a phoenix, and he leads the procession to the edge of the roof. A popular story says he is a tyrant prince stranded at the edge with the beasts behind him to stop his escape; it is folklore, but guides like to tell it. The figures also had a practical job: they cover the nails that hold the ridge tiles in place.</p>

<h2>Why is the number different on each building?</h2>
<p>Under Qing building rules, the number of beasts matched the rank of the building, and it is usually odd. Walking north through the palace, you can watch it change: ten on the Hall of Supreme Harmony, fewer on the halls behind it, fewer still on side halls and gates. Counting them is a good game for children; see <a href="@ROOT@forbidden-city/with-kids/">the Forbidden City with kids</a>.</p>

<h2>Where can I see them best?</h2>
<ul>
  <li><strong>Hall of Supreme Harmony:</strong> stand at the east or west corner of the terrace and look up at the nearest roof corner. A phone zoom is enough to count to ten.</li>
  <li><strong>Side halls and gates:</strong> lower roofs, so the figures are closer and easier to photograph.</li>
  <li><strong>From Jingshan Park:</strong> not for the beasts, but for the whole sea of roofs they sit on; see <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">the best view of the Forbidden City</a>.</li>
</ul>

<h2>What about the big ornaments at the ends of the top ridge?</h2>
<p>Those are chiwen, dragon-like creatures with open mouths that seem to bite the ridge. On the Hall of Supreme Harmony each one is 3.4 metres tall and weighs about 4.3 tonnes, far bigger than they look from the ground. Like the small beasts, they were believed to protect the building from fire.</p>

<h2>Is there a story for the roof beasts in the app?</h2>
<p>Yes. In Penyola the Ten Roof-Ridge Beasts are a point of their own on the Forbidden City map, with an illustration and a narrated story, next to the other details of the Hall of Supreme Harmony.</p>
''')

WINTER = Article(
    path='forbidden-city/winter-and-snow/',
    short='Forbidden City in winter',
    title='The Forbidden City in winter and snow: a visitor’s guide',
    description='Visiting the Forbidden City from November to March: lower prices, shorter hours, cold courtyards, and how to see it under snow before the crowds.',
    eyebrow='Forbidden City · seasons',
    h1='The Forbidden City in winter and snow',
    image='page-hall-of-preserving-harmony.webp',
    image_alt='Hand-drawn illustration of the Hall of Preserving Harmony',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/crowds-and-best-time/', 'forbidden-city/tickets-for-foreigners/', 'jingshan-park/best-view-of-the-forbidden-city/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_VISIT, DPM_RULES, JS_PARK],
    body='''
<h2>Is the Forbidden City worth visiting in winter?</h2>
<p>Yes. From November to March tickets drop to ¥40 from ¥60, crowds are thinner outside Chinese New Year, and on the few days a year that it snows, the red walls and yellow roofs under white are the most photographed sight in Beijing. The trade-off is cold: daytime temperatures in January are often around or below freezing, and almost all of the visit is outdoors.</p>

<h2>What are the winter opening hours?</h2>
<ul>
  <li>1 November – 31 March: 08:30–16:30, last entry 15:30.</li>
  <li>Treasure and Clock Galleries: last entry 15:40.</li>
  <li>Closed on Mondays, except public holidays.</li>
</ul>
<p>With sunset around 17:00 in December, the light goes early. Start in the morning.</p>

<h2>How often does it snow in Beijing?</h2>
<p>Not often. Beijing winters are dry and sunny; snow falls on only a handful of days each winter, mostly between December and February, and it often melts within a day or two. You cannot plan a trip around it, but if snow is forecast while you are in town, book the next morning straight away.</p>

<h2>What happens when it snows?</h2>
<p>Everyone in Beijing has the same idea. Tickets for the first clear morning after snowfall sell out quickly, and photographers queue at the gate before opening. Some tips:</p>
<ul>
  <li>Book at 20:00 seven days ahead for several possible dates, then cancel the ones you do not need before midnight the day before.</li>
  <li>Be at the Meridian Gate before the 08:30 opening; the untouched snow on the courtyards goes first.</li>
  <li>Stone steps and marble terraces are slippery. Wear shoes with grip.</li>
  <li>If you cannot get in, climb <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a> for the view of the snow-covered roofs from Wanchun Pavilion; the park opens at 06:30.</li>
  <li>The moat by the northwest corner tower, outside the walls, is the classic snow photograph and needs no ticket.</li>
</ul>

<h2>Are the halls heated?</h2>
<p>No. You look into the halls from their doorways, and the exhibition galleries are the only indoor spaces. The Clock Gallery and the Treasure Gallery (¥10 each) make good warm-up stops in the east of the palace. Food outlets are spread out: bring a hot drink in a flask and snacks.</p>

<h2>What should I wear?</h2>
<p>Dress for standing still outside: a warm coat, hat, gloves and thick-soled shoes, as the cold comes up from the stone paving. Phone batteries drain fast in the cold; keep yours in an inside pocket, especially if your ticket and maps are on it.</p>

<h2>What about Chinese New Year?</h2>
<p>The Spring Festival holiday, in late January or February, is the exception to quiet winter: it is one of the busiest times of the year, with tickets gone the moment they are released. See <a href="@ROOT@forbidden-city/crowds-and-best-time/">when not to visit</a>.</p>

<h2>How long do I need on a cold day?</h2>
<p>Two to three hours is plenty in winter. Follow the central axis from the Meridian Gate to the Gate of Divine Might and add one gallery; the <a href="@ROOT@forbidden-city/half-day-route/">half-day route</a> has the order. Penyola keeps the map, stories and audio on your phone, so you are not hunting for a signal with cold fingers.</p>
''')

KIDS = Article(
    path='forbidden-city/with-kids/',
    short='Forbidden City with kids',
    title='The Forbidden City with kids: a family guide',
    description='Visiting the Forbidden City with children: how long to plan, children’s tickets, buggies and toilets, and things to spot that keep kids interested.',
    eyebrow='Forbidden City · families',
    h1='The Forbidden City with kids',
    image='art-tortoise.webp',
    image_alt='Hand-drawn illustration of a bronze tortoise from the Forbidden City',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/roof-guardians/', 'forbidden-city/entrance-and-exit/', 'jingshan-park/best-view-of-the-forbidden-city/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_VISIT, DPM_RULES],
    body='''
<h2>Is the Forbidden City good for kids?</h2>
<p>Yes, with a plan: keep it to 2–3 hours, give them things to find rather than things to read, and finish across the road in Jingshan Park, where they can climb a hill. The full walk from the entrance to the north exit is about 1 kilometre of courtyards and stone paving, plus steps up to every hall, so the youngest children will need carrying or a buggy for part of it.</p>

<h2>Do children need tickets?</h2>
<p>Every visitor, including children, needs a booking under their own ID: book your children with their passports at the same time as yours. Free entry for under-18s applies to Chinese citizens and foreign permanent residents, and the ¥20 student ticket is for students aged 18 and over; check the price for other children when you book. Children under 14 must come with an adult, up to three children per adult. Tickets open at 20:00 seven days ahead; see <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book</a>.</p>

<h2>Is the palace easy with a buggy?</h2>
<p>Not very: the main halls stand on terraces with stairs, and side routes have high thresholds and steps. A lightweight folding buggy or a carrier is easier than a big pushchair.</p>

<h2>What will kids enjoy spotting?</h2>
<ul>
  <li><strong>Roof beasts.</strong> Count the little figures on the roof corners; the Hall of Supreme Harmony has ten, more than anywhere else in China. See <a href="@ROOT@forbidden-city/roof-guardians/">the roof guardians explained</a>.</li>
  <li><strong>Bronze animals.</strong> A tortoise and a crane on the terrace of the Hall of Supreme Harmony, lions at the gates (the one with a cub under its paw is the female), and kneeling bronze elephants in the Imperial Garden.</li>
  <li><strong>Dragons.</strong> They are everywhere, on roofs, stairs, ceilings and drainage spouts. Ask for a count by the end.</li>
  <li><strong>Doors.</strong> The big red gates have rows of golden studs: nine rows of nine on the most important ones.</li>
  <li><strong>The Clock Gallery.</strong> Mechanical clocks with moving figures, birds and waterfalls, given to the emperors. ¥10 extra.</li>
  <li><strong>The Imperial Garden.</strong> Old twisted trees, a rock hill and pavilions at the north end, the best place to let them run a little.</li>
</ul>

<h2>Where are the toilets and food?</h2>
<p>Toilets are spaced along the central axis and in the side courtyards; the museum also has mother-and-baby rooms. Food is limited: cafés and kiosks sell snacks and drinks, so bring water and something to eat. There is very little shade in the big courtyards in summer.</p>

<h2>Which route works with children?</h2>
<p>Stay on the central axis from the Meridian Gate to the Gate of Divine Might, with one side trip at most. Penyola's shortest Forbidden City walk takes about 1 hour 40 minutes before queues; with children, allow 2–3 hours. The <a href="@ROOT@forbidden-city/half-day-route/">half-day route</a> lists the stops.</p>

<h2>When is the best time to go with kids?</h2>
<p>Weekday mornings, right at the 08:30 opening. Avoid Chinese school holidays (July and August) and national holidays if you can; summer afternoons in the open courtyards are very hot. See <a href="@ROOT@forbidden-city/crowds-and-best-time/">the best time to visit</a>.</p>

<h2>What next?</h2>
<p>Cross to Jingshan Park and climb to the top: 10–20 minutes of steps for the best view of the palace. Penyola's Jingshan Park guide is free; older children can follow the map and play the audio stories themselves, and it works without a signal.</p>
''')

CROWDS = Article(
    path='forbidden-city/crowds-and-best-time/',
    short='Crowds and best time',
    title='Forbidden City crowds: Golden Week and the best time to visit',
    description='When the Forbidden City is busiest (Golden Week, May Day, summer holidays, Chinese New Year) and the quietest days and hours to visit.',
    eyebrow='Forbidden City · timing',
    h1='Forbidden City crowds and the best time to visit',
    image='page-hall-of-central-harmony.webp',
    image_alt='Hand-drawn illustration of the Hall of Central Harmony',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/winter-and-snow/', 'forbidden-city/tickets-for-foreigners/', 'forbidden-city/half-day-route/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[DPM_VISIT, DPM_RULES],
    body='''
<h2>When is the Forbidden City most crowded?</h2>
<p>During China's national holidays: Golden Week (1–7 October), the May Day holiday (around 1–5 May) and Chinese New Year (late January or February), plus the summer school holidays in July and August. On those days tickets are gone within minutes of release, seven days ahead. The quietest times are weekday mornings from March to April and from late October to mid-December, outside the holidays.</p>

<h2>Does the palace get overcrowded?</h2>
<p>Not as badly as an unlimited site: every ticket is sold in advance, by name and for a morning or afternoon session, so the number of visitors is set by the booking system. That moves the problem to booking: on busy dates the challenge is getting a ticket, not the crowd inside. See <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book with a passport</a>.</p>

<h2>Which Chinese holidays should I avoid?</h2>
<table>
  <thead><tr><th>Holiday</th><th>When</th><th>Crowds</th></tr></thead>
  <tbody>
    <tr><td>Chinese New Year (Spring Festival)</td><td>Late January or February, about 8 days</td><td>Very busy</td></tr>
    <tr><td>Qingming Festival</td><td>Early April, about 3 days</td><td>Busy</td></tr>
    <tr><td>May Day</td><td>1–5 May</td><td>Very busy</td></tr>
    <tr><td>Dragon Boat Festival</td><td>June, about 3 days</td><td>Busy</td></tr>
    <tr><td>Summer school holidays</td><td>July and August</td><td>Busy every day</td></tr>
    <tr><td>Mid-Autumn Festival</td><td>September or early October</td><td>Busy</td></tr>
    <tr><td>National Day Golden Week</td><td>1–7 October</td><td>The busiest week of the year</td></tr>
  </tbody>
</table>
<p>The exact dates move each year with the lunar calendar and are announced by the State Council near the end of the previous year. Check them before you book flights.</p>

<h2>What is the best day of the week?</h2>
<p>Tuesday to Thursday. The palace is closed on Mondays (except public holidays), so Tuesdays catch some people who could not come the day before, and weekends are busier everywhere in Beijing. Avoid the day before or after a holiday too.</p>

<h2>What is the best time of day?</h2>
<p>The first hour after the 08:30 opening. Tour groups usually arrive mid-morning, and the doorway of the Hall of Supreme Harmony gets crowded from then on. A late start can also work: by mid-afternoon groups have moved on, but remember the last entry at 16:00 (April–October) or 15:30 (November–March).</p>

<h2>Which parts of the palace are quieter?</h2>
<p>The central axis is always the busiest. The side courtyards are calmer at any time: the Six Western Palaces where consorts lived, the Clock Gallery and the Treasure Gallery in the east (¥10 each), which also keep many people away. Even on a busy day, ten minutes' walk off the axis can feel like a different place.</p>

<h2>What if I can only go during a holiday?</h2>
<ul>
  <li>Be online at 20:00 Beijing time exactly seven days ahead.</li>
  <li>Check again the evening before your visit for cancellations.</li>
  <li>Take an afternoon session, which sells out later.</li>
  <li>Visit <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a> instead or as well, for the best view of the palace roofs.</li>
</ul>

<h2>Does the season matter?</h2>
<p>Spring and autumn have the best weather and the most visitors. Summer is hot and humid with afternoon storms; winter is cold, dry and quieter, with cheaper tickets. See <a href="@ROOT@forbidden-city/winter-and-snow/">the Forbidden City in winter</a>. Whenever you go, Penyola's map shows the side courtyards and quieter routes, offline.</p>
''')

SP_ROUTE = Article(
    path='summer-palace/one-day-route/',
    short='Summer Palace one-day route',
    title='Summer Palace in one day: a route around Kunming Lake',
    description='A 3–5 hour Summer Palace route from the East Palace Gate along the Long Corridor to the Marble Boat and the Seventeen-Arch Bridge, with tickets and hours.',
    eyebrow='Summer Palace · route',
    h1='The Summer Palace in one day',
    image='bld-foxiang-tower.webp',
    image_alt='Hand-drawn illustration of the Tower of Buddhist Incense on Longevity Hill',
    about=SUMMER_PALACE,
    related=['summer-palace/long-corridor-paintings/', 'summer-palace/marble-boat/', 'beijing/visa-free-transit-2-day-plan/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[SP_GOV, SP_SITE],
    body='''
<h2>How long do you need at the Summer Palace?</h2>
<p>Three to five hours. The classic route from the East Palace Gate along the Long Corridor to the Marble Boat, then round to the Seventeen-Arch Bridge, takes about 3 hours at an easy pace; a full day lets you add Suzhou Street and the back lake. The park covers about 3 square kilometres, three-quarters of it water, so most of the visit is walking along the shore.</p>

<h2>How do I get tickets?</h2>
<ul>
  <li>Park ticket: ¥30 from April to October, ¥20 from November to March.</li>
  <li>Combined ticket: ¥60 or ¥50, adding the Tower of Buddhist Incense, the Garden of Virtue and Harmony, Suzhou Street and the museum.</li>
  <li>Book on the official "Summer Palace" WeChat account with your passport.</li>
</ul>

<h2>What are the opening hours?</h2>
<ul>
  <li>Park: 06:00–20:00 (last entry 19:00) from April to October; 06:30–19:00 (last entry 18:00) from November to March.</li>
  <li>Halls and gardens inside: 08:00–18:00 in summer, 08:30–17:00 in winter, usually closed on Mondays except public holidays.</li>
</ul>

<h2>What is the best route?</h2>
<ol>
  <li><strong>East Palace Gate (0:00).</strong> The main gate, reached from Xiyuan station on metro Line 4.</li>
  <li><strong>Hall of Benevolence and Longevity.</strong> Where Empress Dowager Cixi and the Guangxu Emperor received officials and foreign envoys.</li>
  <li><strong>Garden of Virtue and Harmony.</strong> A three-storey opera stage built for Cixi in the 1890s (combined ticket).</li>
  <li><strong>Hall of Jade Ripples and Hall of Happiness and Longevity.</strong> The lakeside courtyards where Guangxu was confined after 1898 and where Cixi lived.</li>
  <li><strong>Long Corridor (about 0:50).</strong> 728 metres of painted walkway along the north shore. See <a href="@ROOT@summer-palace/long-corridor-paintings/">the stories behind the paintings</a>.</li>
  <li><strong>Hall of Dispelling Clouds and Tower of Buddhist Incense (about 1:30).</strong> Climb the stairs up Longevity Hill to the tower for the view over Kunming Lake. It is steep; skip it if you are short of time or energy.</li>
  <li><strong>Marble Boat (about 2:15).</strong> The stone boat at the west end of the corridor. See <a href="@ROOT@summer-palace/marble-boat/">the stone boat that never sails</a>.</li>
  <li><strong>Across the lake (about 2:30).</strong> In the boating season, a ¥40 electric boat runs from the Marble Boat to South Lake Island (the boats stopped for the winter on 2 November 2026); otherwise walk the West Causeway, past the high-arched Jade Belt Bridge.</li>
  <li><strong>Bronze Ox and Seventeen-Arch Bridge (about 3:00).</strong> A bronze ox cast in 1755 to guard against floods, and a long bridge with more than 500 carved lions on its balustrades.</li>
  <li><strong>Exit at the New Palace Gate</strong> on the east shore, or return to the East Palace Gate.</li>
</ol>
<p>Times assume an easy pace. Penyola's Summer Palace guide has this route as its Classic Highlights walk (about 3 hours 7 minutes), plus a shorter walk of about 1 hour 50 minutes and a full walk of about 5 hours.</p>

<h2>What if I have only two hours?</h2>
<p>Enter at the East Palace Gate, walk the Long Corridor to the Marble Boat and back along the shore. You see the corridor, the lake and the hill without the climb.</p>

<h2>When is the best time to go?</h2>
<p>Early morning on a weekday, when the park opens at 06:00 or 06:30 and the lake is calm; or late afternoon for sunset behind the Seventeen-Arch Bridge, especially around the winter solstice in late December, when the setting sun lines up with the bridge's arches. Avoid Chinese holidays.</p>

<h2>Can I follow the route offline?</h2>
<p>Yes. Penyola's Summer Palace guide puts the halls, bridges and pavilions on a hand-drawn map of the lake with illustrated stories and the suggested walks, stored on your phone.</p>
''')

CORRIDOR = Article(
    path='summer-palace/long-corridor-paintings/',
    short='Long Corridor paintings',
    title='The Long Corridor paintings of the Summer Palace',
    description='The Summer Palace Long Corridor runs 728 metres with thousands of painted scenes. What the paintings show, the stories to look for, and how to walk it.',
    eyebrow='Summer Palace · highlight',
    h1='The Long Corridor paintings: stories behind them',
    image='bld-long-corridor.webp',
    image_alt='Hand-drawn illustration of the Long Corridor at the Summer Palace',
    about=SUMMER_PALACE,
    related=['summer-palace/one-day-route/', 'summer-palace/marble-boat/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[SP_GOV],
    body='''
<h2>What is the Long Corridor?</h2>
<p>It is a covered walkway that runs 728 metres along the north shore of Kunming Lake, in 273 sections, from the Gate of Inviting the Moon in the east to the Marble Boat in the west. Every beam is painted, with pictures of landscapes, birds and flowers, and scenes from Chinese novels, legends and history. Walking it end to end takes 15–20 minutes; looking at the paintings can take as long as you like.</p>

<h2>Why was it built?</h2>
<p>The Qianlong Emperor built the corridor in the 1750s so that his mother and the court could walk beside the lake in any weather, in shade in summer and out of the rain. It was burned by British and French troops in 1860 and rebuilt in the 1880s. Four octagonal pavilions along the way mark the seasons, and break up the long perspective that makes the corridor such a famous photograph.</p>

<h2>What do the paintings show?</h2>
<p>Four kinds of picture repeat along the beams:</p>
<ul>
  <li><strong>Landscapes</strong>, many of them scenes of West Lake in Hangzhou, which the emperor admired on his tours of the south.</li>
  <li><strong>Flowers and birds</strong>: peonies for wealth, lotus for purity, cranes for long life.</li>
  <li><strong>Figures and stories</strong> from the classic novels, history and folk tales: the most fun to look for.</li>
  <li><strong>Architecture</strong>: imagined pavilions and gardens.</li>
</ul>

<h2>Which stories should I look for?</h2>
<p>You will not identify most of the scenes without help, but a few are easy to recognise once you know what to look for:</p>
<ul>
  <li><strong>Journey to the West.</strong> Look for a monkey with a staff, Sun Wukong, the Monkey King, usually beside a monk on a white horse, a pig-faced companion and a man carrying luggage. They are on their way to India to fetch Buddhist scriptures.</li>
  <li><strong>Romance of the Three Kingdoms.</strong> Warriors on horseback, often a red-faced general with a long beard and a halberd: Guan Yu, the model of loyalty. A scene of three men calling at a thatched cottage in the snow shows Liu Bei's three visits to win the strategist Zhuge Liang.</li>
  <li><strong>Dream of the Red Chamber.</strong> Elegant young women in gardens, often reading, playing music or burying flowers, from the great novel of a declining noble family.</li>
  <li><strong>Water Margin.</strong> Outlaws in action: a man fighting a tiger is Wu Song, who killed it with his bare hands.</li>
</ul>
<p>The same story may appear several times, painted by different artists in different repaintings over the years.</p>

<h2>How should I walk it?</h2>
<p>Start at the east end, near the Hall of Happiness and Longevity, and walk west toward the Marble Boat, with the lake on your left. Pick one kind of scene to look for, say the Monkey King, rather than trying to read every beam. Half-way along, the corridor passes the foot of the stairs up Longevity Hill to the Tower of Buddhist Incense.</p>

<h2>When is it least crowded?</h2>
<p>In the early morning, soon after the park opens at 06:00 or 06:30, before tour groups arrive around 09:00. The Long Corridor is inside the park ticket, with no extra charge.</p>

<h2>Is there more about the corridor in the app?</h2>
<p>Penyola's Summer Palace guide has the Long Corridor on its hand-drawn map of the lake, with an illustrated story, and it is a stop on all three suggested walks. See <a href="@ROOT@summer-palace/one-day-route/">the one-day route</a>.</p>
''')

MARBLE = Article(
    path='summer-palace/marble-boat/',
    short='The Marble Boat',
    title='The Marble Boat at the Summer Palace: the stone boat that never sails',
    description='The Marble Boat at the Summer Palace: a 1755 stone hull with a Western-style cabin from 1893. Its story, what to look for and how to get there.',
    eyebrow='Summer Palace · highlight',
    h1='The Marble Boat: the stone boat that never sails',
    image='bld-marble-boat.webp',
    image_alt='Hand-drawn illustration of the Marble Boat at the Summer Palace',
    about=SUMMER_PALACE,
    related=['summer-palace/long-corridor-paintings/', 'summer-palace/one-day-route/'],
    published='2026-11-07',
    checked='2026-11-09',
    sources=[SP_GOV, SP_SITE],
    body='''
<h2>What is the Marble Boat?</h2>
<p>It is a waterside pavilion in the shape of a boat, at the west end of the Long Corridor: a stone hull completed in 1755, with a two-storey cabin on top that was rebuilt in a Western style in 1893. It has never moved. Its Chinese name, Qingyan Fang (<span lang="zh-Hans">清晏舫</span>), means "boat of clear and peaceful seas".</p>

<h2>Why build a boat that cannot sail?</h2>
<p>A stone boat was a garden folly with a message. A well-known saying compares a ruler to a boat and the people to the water: water can carry a boat, and water can overturn it. A boat made of stone could never capsize, a wish for a dynasty that would last. It was also simply a fine place to sit, take tea and look out over the lake.</p>

<h2>Why does the cabin look European?</h2>
<p>The original cabin was Chinese in style. It was burned in 1860, when British and French troops destroyed the imperial gardens around Beijing. When Empress Dowager Cixi rebuilt the Summer Palace in the 1880s and 1890s, the cabin was redone in a Western style, with coloured glass, arched windows and paddle wheels on the sides, painted to look like marble. The result is a curious mix: an eighteenth-century Chinese hull carrying a late-nineteenth-century European steamer's deck.</p>

<h2>Was it paid for with navy money?</h2>
<p>That is the most famous story about it. Historians agree that funds meant for the navy were diverted to rebuild the Summer Palace in the 1880s, a few years before China's fleet was destroyed in the war with Japan in 1894–95. The Marble Boat has become the symbol of that story, though it was only one small part of the work.</p>

<h2>What should I look for?</h2>
<ul>
  <li>The contrast between the heavy stone hull and the light, glassy upper rooms.</li>
  <li>The paddle wheels on each side, a nod to the steamships of the 1890s.</li>
  <li>The carved stone details of the hull, from the original 1755 boat.</li>
  <li>The view east from the shore beside it, back along the lake toward Longevity Hill.</li>
</ul>

<h2>How do I get to the Marble Boat?</h2>
<p>Walk the full length of the Long Corridor west from the East Palace Gate, about 25–30 minutes without stops, or come in by the North Palace Gate (Beigongmen station, metro Line 4) and walk down past Suzhou Street and over the hill, about 15–20 minutes. In the boating season, a ¥40 boat runs from beside the Marble Boat to South Lake Island.</p>

<h2>Is it included in the ticket?</h2>
<p>Yes, it is in the open park, covered by the basic park ticket (¥30 or ¥20 depending on the season).</p>

<h2>What is nearby?</h2>
<p>The Long Corridor, whose painted beams end here (see <a href="@ROOT@summer-palace/long-corridor-paintings/">the stories behind the paintings</a>), and the West Causeway with its six bridges. Penyola's Summer Palace map has the Marble Boat as a stop with an illustrated story, on the <a href="@ROOT@summer-palace/one-day-route/">one-day route</a> round the lake.</p>
''')

VISA_FREE = Article(
    path='beijing/visa-free-transit-2-day-plan/',
    short='Beijing 2-day visa-free plan',
    title='Beijing on 240-hour visa-free transit: a 2-day plan',
    description='A 2-day Beijing plan for visa-free transit travellers: Forbidden City and Jingshan on day 1, the Great Wall and the Summer Palace on day 2, with booking tips.',
    eyebrow='Beijing · itinerary',
    h1='Beijing in 2 days on visa-free transit',
    image='bld-seventeen-arch-bridge.webp',
    image_alt='Hand-drawn illustration of the Seventeen-Arch Bridge at the Summer Palace',
    about=BEIJING,
    related=['forbidden-city/tickets-for-foreigners/', 'summer-palace/one-day-route/', 'beijing/without-google/'],
    checked='2026-11-09',
    city='beijing',
    published='2026-11-07',
    sources=[NIA_TRANSIT, DPM_VISIT, DPM_RULES],
    body='''
<h2>Can I see Beijing in 2 days on visa-free transit?</h2>
<p>Yes. Under China's 240-hour visa-free transit policy, travellers from 57 countries flying on to a third country can stay up to 10 days without a visa if they arrive through one of the 65 listed ports; check that your airport is on the official list. Two full days cover the essentials: the Forbidden City and Jingshan Park on day 1, the Great Wall and the Summer Palace on day 2. Book the Forbidden City before you fly, because tickets open seven days ahead and sell out.</p>

<h2>Who qualifies for 240-hour transit?</h2>
<ul>
  <li>Citizens of the eligible countries, travelling on an ordinary passport.</li>
  <li>A confirmed onward ticket to a third country or region (Hong Kong and Macau count): Beijing to your home country is not transit.</li>
  <li>A fixed date and itinerary on the onward ticket; allow extra time at immigration.</li>
</ul>
<p>The rules and the list of countries change; check the National Immigration Administration's current notice or your nearest Chinese embassy before booking.</p>

<h2>Day 1: the Forbidden City and Jingshan Park</h2>
<ul>
  <li><strong>08:00</strong> Head for the Meridian Gate for the 08:30 opening; see <a href="@ROOT@forbidden-city/entrance-and-exit/">entrance and exits</a> for the way in.</li>
  <li><strong>08:30–12:00</strong> The Forbidden City along the central axis, with one side trip. See <a href="@ROOT@forbidden-city/half-day-route/">the half-day route</a>.</li>
  <li><strong>12:00</strong> Out through the Gate of Divine Might; lunch nearby.</li>
  <li><strong>13:30</strong> <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a>: climb to Wanchun Pavilion for the view over the palace.</li>
  <li><strong>15:00</strong> Walk west to Beihai Park or north to the hutong lanes around Shichahai and the Drum and Bell Towers.</li>
  <li><strong>Evening</strong> Wangfujing or Qianmen for dinner.</li>
</ul>

<h2>Day 2: the Great Wall and the Summer Palace</h2>
<ul>
  <li><strong>07:30</strong> Leave for the Great Wall. Mutianyu has a cable car and is best reached by car; Badaling is on the S2 suburban line and the Beijing–Zhangjiakou high-speed railway. See <a href="@ROOT@beijing/great-wall-which-section/">which section to choose</a>.</li>
  <li><strong>09:00–12:30</strong> On the wall. Book Great Wall tickets online in advance.</li>
  <li><strong>14:30–17:30</strong> The <a href="@ROOT@summer-palace/one-day-route/">Summer Palace</a>, which lies on the way back into the city: East Palace Gate, the Long Corridor, the Marble Boat.</li>
  <li><strong>Evening</strong> Peking duck.</li>
</ul>
<p>If the Great Wall is too far for your timing, swap it for the Temple of Heaven in the morning and give the Summer Palace a full afternoon.</p>

<h2>What should I set up before I land?</h2>
<ul>
  <li>Forbidden City tickets, booked with your passport at 20:00 Beijing time, seven days ahead. See <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how</a>.</li>
  <li>A payment app: Alipay or WeChat Pay with a foreign card linked.</li>
  <li>Mobile data: an eSIM or roaming plan, since Google services do not work in mainland China. See <a href="@ROOT@beijing/without-google/">getting around Beijing without Google</a>.</li>
  <li>Offline guides and maps, so you are not depending on a connection on the day.</li>
</ul>

<h2>What if I only have one day?</h2>
<p>Do day 1. The Forbidden City and Jingshan are next to each other, in the centre of the city, and need no long transfers.</p>

<h2>Which guides cover these sights offline?</h2>
<p>Penyola covers three of them: Jingshan Park (free), the Forbidden City and the Summer Palace, with hand-drawn maps, stories and walking routes on your iPhone, no connection needed. It is a useful companion when your mobile data is slow or your roaming plan runs out.</p>
''')

NO_GOOGLE = Article(
    path='beijing/without-google/',
    short='Beijing without Google',
    title='Getting around Beijing without Google: maps, taxis, payment',
    description='Google does not work in mainland China. What to use instead in Beijing: maps, taxis, metro, payment and translation, and what to set up before you fly.',
    eyebrow='Beijing · practical',
    h1='Getting around Beijing without Google',
    image='art-globe.webp',
    image_alt='Hand-drawn illustration of a gilded celestial globe from the Forbidden City',
    about=BEIJING,
    related=['beijing/chinese-address-cards/', 'beijing/visa-free-transit-2-day-plan/', 'forbidden-city/entrance-and-exit/'],
    city='beijing',
    body='''
<h2>Does Google work in Beijing?</h2>
<p>No. Google Maps, Gmail, Search and YouTube are blocked in mainland China, and a VPN on hotel or local Wi-Fi is unreliable. The fixes are simple if you set them up before you fly: a mobile data plan that works in China, Apple Maps or Amap for directions, DiDi for taxis, and Alipay or WeChat Pay for paying. Roaming data and many travel eSIMs route through outside China, so some blocked apps work on them, but do not count on it.</p>

<h2>Which map app should I use?</h2>
<ul>
  <li><strong>Apple Maps</strong> works well in Beijing on iPhone, in English, with metro and walking directions. It uses Chinese map data, so locations line up correctly.</li>
  <li><strong>Amap</strong> (<span lang="zh-Hans">高德地图</span>) is the most detailed, and is good for buses and walking routes.</li>
  <li><strong>Google Maps</strong>, even with a connection, shows streets offset by a few hundred metres because of differences in coordinate systems. Do not navigate with it.</li>
</ul>
<p>Save your hotel's address in Chinese before you go; English names are often not understood by drivers.</p>

<h2>How do I take a taxi?</h2>
<p>DiDi is China's ride-hailing app, with an English version, and also available inside Alipay, and accepts linked foreign cards. Street taxis are plentiful and cheap; drivers rarely speak English, so show your destination in Chinese. Penyola keeps a Chinese address card for each sight it covers, and <a href="@ROOT@beijing/chinese-address-cards/">our address cards page</a> has the Forbidden City, Jingshan Park and Summer Palace ready to show.</p>

<h2>How do I pay?</h2>
<p>Most places in Beijing expect mobile payment. Alipay and WeChat Pay both let visitors link a foreign Visa or Mastercard after a passport check; set them up and make a small test payment before your trip. Carry some cash as a backup: businesses are required to accept it, though small stalls may have no change.</p>

<h2>How do I use the metro?</h2>
<p>The metro is fast, cheap and signed in English. Pay with the Beijing transit QR code inside Alipay or buy a single ticket from a machine. Every station has a security check of bags.</p>

<h2>What about translation?</h2>
<p>Apple Translate works offline once you download Chinese; Google Translate needs a connection that reaches Google. Baidu Translate and the translation inside WeChat work on local networks. Photo translation of menus and signs is the feature you will use most.</p>

<h2>What should I download before I go?</h2>
<ul>
  <li>Alipay and/or WeChat, with a card linked and a test payment made.</li>
  <li>DiDi, or use it inside Alipay.</li>
  <li>Amap, as a backup to Apple Maps.</li>
  <li>An offline translator with Chinese downloaded.</li>
  <li>Offline guides for the sights you plan to see, so a weak signal does not matter.</li>
</ul>

<h2>Which sightseeing apps work without a connection?</h2>
<p>Penyola is made for this situation: guides to the Forbidden City, the Summer Palace and Jingshan Park with hand-drawn maps, stories, audio and routes, stored entirely on your iPhone, so they work with no signal and no VPN. The Jingshan Park guide is free.</p>
''')

ADDRESS = Article(
    path='beijing/chinese-address-cards/',
    short='Chinese address cards',
    title='Chinese address cards for Beijing sights (printable)',
    description='Show these Chinese address cards to a taxi driver: the Forbidden City entrance and exits, Jingshan Park and the Summer Palace gates. Free to print or screenshot.',
    eyebrow='Beijing · printable',
    h1='Chinese address cards for Beijing sights',
    image='art-lion.webp',
    image_alt='Hand-drawn illustration of a bronze guardian lion from the Forbidden City',
    about=BEIJING,
    related=['beijing/without-google/', 'forbidden-city/entrance-and-exit/', 'summer-palace/one-day-route/'],
    city='beijing',
    body='''
<h2>How do I tell a taxi driver where to go in Beijing?</h2>
<p>Show the name and address in Chinese characters: most Beijing drivers do not read English or pinyin. The cards below give each sight's gate in large characters with the full address underneath. Screenshot them or print this page (it prints one card per row), then point to the line you need.</p>

<h2>Forbidden City</h2>
<div class="addr-cards">
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">故宫 东华门</p><p class="addr-sub" lang="zh-Hans">北京市东城区景山前街4号</p><p class="addr-en">Forbidden City, East Glorious Gate: nearest taxi drop-off; walk to the Meridian Gate entrance</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">天安门东 地铁站</p><p class="addr-sub" lang="zh-Hans">地铁1号线</p><p class="addr-en">Tian'anmen East metro station: walk north through Tian'anmen to the entrance</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">故宫 神武门</p><p class="addr-sub" lang="zh-Hans">北京市东城区景山前街4号</p><p class="addr-en">Forbidden City, Gate of Divine Might: north exit, for pick-up after your visit</p></div>
</div>
<p>The Meridian Gate (<span lang="zh-Hans">午门</span>), the only entrance, is reached on foot along the moat; see <a href="@ROOT@forbidden-city/entrance-and-exit/">entrance and exits</a>.</p>

<h2>Jingshan Park</h2>
<div class="addr-cards">
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">景山公园 南门</p><p class="addr-sub" lang="zh-Hans">北京市西城区景山西街44号</p><p class="addr-en">Jingshan Park, South Gate: opposite the Forbidden City's north exit</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">景山公园 东门</p><p class="addr-en">Jingshan Park, East Gate</p></div>
</div>

<h2>Summer Palace</h2>
<div class="addr-cards">
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">颐和园 东宫门</p><p class="addr-sub" lang="zh-Hans">北京市海淀区新建宫门路19号</p><p class="addr-en">Summer Palace, East Palace Gate: the main gate</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">颐和园 北宫门</p><p class="addr-sub" lang="zh-Hans">北京市海淀区新建宫门路19号</p><p class="addr-en">Summer Palace, North Palace Gate: closest to Suzhou Street and metro Line 4</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">颐和园 新建宫门</p><p class="addr-sub" lang="zh-Hans">北京市海淀区新建宫门路19号</p><p class="addr-en">Summer Palace, New Palace Gate: east shore, near the Seventeen-Arch Bridge</p></div>
</div>

<h2>Useful phrases</h2>
<div class="addr-cards">
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">请带我去这里</p><p class="addr-en">Please take me here.</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">请在这里停车</p><p class="addr-en">Please stop here.</p></div>
  <div class="addr-card"><p class="addr-zh" lang="zh-Hans">请打表</p><p class="addr-en">Please use the meter.</p></div>
</div>

<h2>Do I need a card if I use DiDi?</h2>
<p>Less often: you choose the destination in the app. Drivers still sometimes call or ask where exactly to stop, and the gate names here help. Pick the gate, not just the sight: the Summer Palace gates are far apart.</p>

<h2>Are the cards in the app too?</h2>
<p>Yes. Penyola's visitor information for each sight includes an address card in Chinese that you can show from your phone or save to your photos, offline. See also <a href="@ROOT@beijing/without-google/">getting around Beijing without Google</a>.</p>
''')

GREAT_WALL = Article(
    path='beijing/great-wall-which-section/',
    short='Which Great Wall section',
    title='Which Great Wall section to visit from Beijing',
    description='Mutianyu, Badaling, Juyongguan or Simatai: tickets, opening hours, booking and how to get there for the Great Wall sections near Beijing, from official sources.',
    eyebrow='Great Wall',
    h1='Which section of the Great Wall should I visit from Beijing?',
    image=None,
    image_alt='',
    about={'@type': 'TouristAttraction', 'name': 'Great Wall of China', 'alternateName': '长城', 'containedInPlace': {'@type': 'City', 'name': 'Beijing'}},
    related=['beijing/3-day-itinerary/', 'beijing/visa-free-transit-2-day-plan/', 'beijing/chinese-address-cards/'],
    city='beijing',
    cta=False,
    checked='2026-11-09',
    sources=[('Mutianyu Great Wall: visitor information', 'https://www.mutianyugreatwall.com/cnInformation'),
             ('Mutianyu Great Wall: official ticket booking', 'https://fx.mutianyugreatwall.com/fore/index?disCode=736798'),
             ('Badaling Great Wall: opening hours and booking notices', 'https://www.badaling.cn/'),
             ('Beijing Municipal Government: Badaling Great Wall', 'https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260320_4562521.html'),
             ('Beijing Municipal Government: Juyongguan Great Wall', 'https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260320_4562519.html'),
             ('Beijing Municipal Government: Mutianyu Great Wall', 'https://english.beijing.gov.cn/travellinginbeijing/attractions/202603/t20260325_4566115.html'),
             ('Gubei Water Town and Simatai: tickets and hours', 'https://www.wtown.com/pc/ticket/index.html'),
             ('Gubei Water Town and Simatai: questions and prices', 'https://www.wtown.com/pc/travel/question.html'),
             ('Gubei Water Town and Simatai: getting there', 'https://www.wtown.com/pc/travel/index.html')],
    body='''
<h2>Which section is best for a first visit?</h2>
<p>For most first-time visitors, Mutianyu: about 70 km from central Beijing, a restored wall with watchtowers along a wooded ridge, and a cable car that saves the steep climb. Badaling, about 60 km northwest, is the easiest to reach by public transport, by train. Juyongguan is a fortified pass with tickets at the gate, and Simatai is the one you can walk at night.</p>

<h2>How do they compare?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th>Section</th><th>Adult ticket</th><th>Booking</th><th>Best for</th></tr></thead>
  <tbody>
    <tr><td>Mutianyu</td><td>¥40; cable car ¥140 return</td><td>Online with your passport, up to 30 days ahead</td><td>A first visit with a car or tour; families who want the cable car</td></tr>
    <tr><td>Badaling</td><td>¥40 (¥35, 1 November–31 March)</td><td>Online booking or at the gate</td><td>Going by train</td></tr>
    <tr><td>Juyongguan</td><td>¥40 (¥35 off season)</td><td>At the gate</td><td>A shorter trip; a fortified pass in a valley</td></tr>
    <tr><td>Simatai</td><td>¥40 by day; ¥200 at night</td><td>Through Gubei Water Town</td><td>An evening on the wall, with a night in the water town</td></tr>
  </tbody>
</table>
</div>
<p>Prices are the official adult prices when we checked; each site also sells concession tickets.</p>

<h2>Mutianyu: what do I need to know?</h2>
<ul>
  <li>Tickets are sold by real-name booking, up to 30 days ahead; book with your passport and show the same passport at the gate. Each ID can book one ticket per day.</li>
  <li>The wall ticket is ¥40. The shuttle bus between the service area and the wall, a 6 km round trip, is ¥15 and recommended. The cable car is ¥140 return or ¥100 one way. The chairlift and toboggan are run by a separate company and need their own tickets.</li>
  <li>Opening hours: 16 March–15 November, 07:30–18:00 on weekdays and 07:30–18:30 at weekends; 16 November–15 March, 08:00–17:30. Ticket sales stop an hour before closing and entry half an hour before.</li>
  <li>Towers 1 to 20 are open by day.</li>
  <li>You can cancel or change a booking until midnight on the day of your visit, as long as you have not entered.</li>
  <li>By public transport: bus 916 from Dongzhimen to Huairou Beidajie, then bus H23, H3 or H71 to Mutianyujingqu.</li>
</ul>

<h2>Badaling: what do I need to know?</h2>
<ul>
  <li>Opening hours: 1 April–31 October, 06:30–16:30; 1 November–31 March, 07:30–16:00. The open section runs from North Tower 12 to South Tower 7.5.</li>
  <li>Booking ahead is encouraged, through the official Chinese-language channels, and tickets are also sold at the gate, including on public holidays.</li>
  <li>Getting there: the S2 suburban line or the Beijing–Zhangjiakou high-speed railway, or buses 919, 880 and 877. Check the railway timetable for the day.</li>
</ul>

<h2>Juyongguan: what do I need to know?</h2>
<p>Juyongguan is a pass in a valley in Changping District, where the wall climbs steeply up both hillsides from a fortified gate. Tickets are sold at the gate: ¥40 in peak season, ¥35 off season. Hours are 08:30–17:30 in peak season and 08:30–16:30 off season.</p>

<h2>Simatai: can I walk the Great Wall at night?</h2>
<p>Yes, at Simatai, which is entered through Gubei Water Town, a resort in Miyun District about 120 km and two hours' drive from central Beijing. Night visits run all year:</p>
<ul>
  <li>May–October: 18:00–21:40.</li>
  <li>November–April: 17:30–20:10 from Sunday to Thursday, 17:30–20:40 on Friday and Saturday.</li>
  <li>By day, Simatai is open 09:00–17:00; entry closes at 16:10 from inside the water town and at 15:00 at the outside gate.</li>
  <li>Tickets: Simatai ¥40 by day; the Great Wall at night ¥200; Gubei Water Town ¥140.</li>
  <li>By public transport: bus 980 (express) from Dongzhimen to Miyun Xidaqiao, then bus Mi 51 towards Simatai.</li>
</ul>
<p>Jinshanling, across the border in Hebei, is popular with hikers. We could not confirm its current tickets and hours on an official site, so it is not covered here.</p>

<h2>How do I get there without a tour?</h2>
<p>The simplest is a car with a driver for the day, booked through your hotel or a ride-hailing app. For Badaling the train is easy. For Mutianyu and Simatai, public buses work but take a change and most of a morning. Save the Chinese name of the section to show your driver: Mutianyu <span lang="zh-Hans">慕田峪长城</span>, Badaling <span lang="zh-Hans">八达岭长城</span>, Juyongguan <span lang="zh-Hans">居庸关长城</span>, Simatai <span lang="zh-Hans">司马台长城</span>.</p>

<h2>How long should I allow?</h2>
<p>A full day, or a morning and early afternoon: about half the day on the road there and back, and two to three hours on the wall. Start early, especially in summer and at weekends. Bring water, and shoes with grip: the steps are steep and uneven. Do not plan the Forbidden City for the same day.</p>
''')

THREE_DAYS = Article(
    path='beijing/3-day-itinerary/',
    short='Beijing in 3 days',
    title='Beijing in 3 days: a first-time itinerary',
    description='A 3-day Beijing itinerary for a first visit: the Forbidden City and Jingshan, the Great Wall, the Temple of Heaven and the Summer Palace, with what to book ahead.',
    eyebrow='Itinerary',
    h1='Beijing in 3 days: a first-time itinerary',
    image='bld-foxiang-tower.webp',
    image_alt='Hand-drawn illustration of the Tower of Buddhist Incense at the Summer Palace',
    about=BEIJING,
    related=['beijing/great-wall-which-section/', 'beijing/visa-free-transit-2-day-plan/', 'forbidden-city/tickets-for-foreigners/', 'beijing/without-google/'],
    city='beijing',
    checked='2026-11-09',
    sources=[('Palace Museum: visiting information', 'https://www.dpm.org.cn/Visit.html'),
             ('Mutianyu Great Wall: visitor information', 'https://www.mutianyugreatwall.com/cnInformation'),
             ('Beijing Municipal Government: Temple of Heaven', 'https://english.beijing.gov.cn/specials/parktours/guidevisitors/templeofheaven/'),
             ('Beijing Municipal Government: Temple of Heaven tickets', 'https://english.beijing.gov.cn/specials/ticketing/parks/202407/t20240719_3753312.html'),
             ('Beijing Municipal Government: Summer Palace', 'https://english.beijing.gov.cn/specials/parktours/guidevisitors/summerpalace/')],
    body='''
<h2>Is 3 days enough for Beijing?</h2>
<p>Yes, for the essentials: the Forbidden City and Jingshan Park on day 1, the Great Wall on day 2, and the Temple of Heaven and the Summer Palace on day 3. It is a full plan with early starts. The one thing to fix first is the Forbidden City, which sells out: tickets go on sale at 20:00 Beijing time seven days ahead.</p>

<h2>What should I book before I go?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th>Sight</th><th>When booking opens</th><th>How</th></tr></thead>
  <tbody>
    <tr><td>Forbidden City</td><td>20:00, seven days ahead</td><td>Official ticket site, with your passport; <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book</a></td></tr>
    <tr><td>Great Wall at Mutianyu</td><td>Up to 30 days ahead</td><td>Official booking, with your passport; <a href="@ROOT@beijing/great-wall-which-section/">other sections</a></td></tr>
    <tr><td>Temple of Heaven</td><td>1–7 days ahead</td><td>The "Temple of Heaven" WeChat account, with your passport</td></tr>
    <tr><td>Summer Palace</td><td>Ahead of your visit</td><td>The "Summer Palace" WeChat account, with your passport</td></tr>
  </tbody>
</table>
</div>

<h2>Which days should I avoid?</h2>
<p>Mondays. The Forbidden City is closed on Mondays, and so are the halls inside the Temple of Heaven, except on public holidays. If your trip includes a Monday, make it your Great Wall day.</p>

<h2>Day 1: the Forbidden City and Jingshan Park</h2>
<ul>
  <li><strong>Morning</strong> Be at the Meridian Gate for the 08:30 opening. Walk the central axis north, with one side trip: <a href="@ROOT@forbidden-city/half-day-route/">the half-day route</a> takes 3–4 hours. Check <a href="@ROOT@forbidden-city/entrance-and-exit/">the entrance and exits</a> before you set off.</li>
  <li><strong>Lunch</strong> Out through the Gate of Divine Might, the north exit.</li>
  <li><strong>Afternoon</strong> Cross the road to <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a> and climb to Wanchun Pavilion for the view back over the palace roofs.</li>
  <li><strong>Late afternoon</strong> Walk north into the hutong lanes around Shichahai and the Drum and Bell Towers.</li>
</ul>

<h2>Day 2: the Great Wall</h2>
<ul>
  <li><strong>Early start</strong> Leave by 07:30. Mutianyu, about 70 km away, opens at 07:30 from mid-March to mid-November and at 08:00 in winter. See <a href="@ROOT@beijing/great-wall-which-section/">which section to choose</a>.</li>
  <li><strong>On the wall</strong> Allow two to three hours. Take the cable car up if you want to save the climb.</li>
  <li><strong>Back in town</strong> A quiet evening: you will be tired. Peking duck is a good reward.</li>
</ul>

<h2>Day 3: the Temple of Heaven and the Summer Palace</h2>
<ul>
  <li><strong>Early morning</strong> The <a href="@ROOT@beijing/temple-of-heaven/">Temple of Heaven</a> park opens at 06:00 (06:30 from November to March), and in the early morning it is full of locals doing tai chi, dancing and playing cards. The halls open at 08:00: the Hall of Prayer for Good Harvests, the Echo Wall and the Circular Mound Altar. Buy the combined ticket (¥34, or ¥28 from November to March) to see them. Metro: Line 5 to Tiantandongmen, Exit A.</li>
  <li><strong>Afternoon</strong> Cross the city to the <a href="@ROOT@summer-palace/one-day-route/">Summer Palace</a> in the northwest. Walk the Long Corridor along Kunming Lake to the Marble Boat, and climb to the Tower of Buddhist Incense if you have the energy.</li>
  <li><strong>Evening</strong> Back to the centre for dinner.</li>
</ul>

<h2>What if I have more time, or less?</h2>
<ul>
  <li><strong>2 days</strong> Drop the Temple of Heaven and pair the Great Wall with the Summer Palace on the way back; see <a href="@ROOT@beijing/visa-free-transit-2-day-plan/">Beijing in 2 days</a>.</li>
  <li><strong>4 days or more</strong> Give the Summer Palace a whole day, and spend a morning in the hutongs and an afternoon at the Lama Temple or Beihai Park.</li>
</ul>

<h2>How do I get around?</h2>
<p>The metro covers every stop on this plan except the Great Wall, and is signed in English. Taxis and DiDi are cheap for short hops; carry each place's name in Chinese. See <a href="@ROOT@beijing/without-google/">Beijing without Google</a> for payments and apps, and <a href="@ROOT@beijing/chinese-address-cards/">address cards</a> to show drivers.</p>
''')

AIRPORT = Article(
    path='beijing/airport-to-city/',
    short='Airport to the city',
    title='Beijing airport to the city: trains, taxis and buses',
    description='Getting from Beijing Capital (PEK) or Daxing (PKX) airport to the city: airport express fares and hours, taxi ranks and fares, and airport buses.',
    eyebrow='Arriving',
    h1='How do I get from Beijing airport to the city centre?',
    image=None,
    image_alt='',
    about=BEIJING,
    related=['beijing/without-google/', 'beijing/chinese-address-cards/', 'beijing/3-day-itinerary/'],
    city='beijing',
    checked='2026-11-09',
    sources=[('Beijing Capital International Airport: getting to and from the airport', 'https://www.bcia.com.cn/wljc.html'),
             ('Beijing Daxing International Airport: Daxing Airport Express', 'https://www.bdia.com.cn/#/airportExpress')],
    body='''
<h2>What is the easiest way into the city?</h2>
<p>The airport express train. From Capital Airport (PEK), the Capital Airport Express runs from Terminals 3 and 2 to Sanyuanqiao, Dongzhimen and Beixinqiao for a flat ¥25, about every 10 minutes. From Daxing Airport (PKX), the Daxing Airport Express runs to Caoqiao in the south of the city for ¥35. Both end at metro stations where you can change lines. With heavy bags, or after the last train, take a taxi from the official taxi rank.</p>

<h2>Which airport am I landing at?</h2>
<p>Check the airport code on your ticket. <strong>PEK</strong> is Beijing Capital International Airport, northeast of the centre, with Terminals 2 and 3. <strong>PKX</strong> is Beijing Daxing International Airport, far to the south. They are different airports with different trains, so make sure you plan for the right one.</p>

<h2>How do the two airport trains compare?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th></th><th>Capital Airport Express (PEK)</th><th>Daxing Airport Express (PKX)</th></tr></thead>
  <tbody>
    <tr><td>Fare</td><td>¥25, any distance</td><td>¥35 to Caoqiao; ¥25 to Daxing Xincheng; business carriage ¥50</td></tr>
    <tr><td>Where to board</td><td>T3: parking building, level 2. T2: parking building, level B2</td><td>Terminal, level B1</td></tr>
    <tr><td>Hours from the airport</td><td>T3 06:22–22:52; T2 06:36–23:10</td><td>06:00–23:00, Sundays to 23:30</td></tr>
    <tr><td>How often</td><td>About every 10 minutes</td><td>At most every 9 min 20 s until 22:30, then every 15 minutes</td></tr>
    <tr><td>Change to the metro at</td><td>Sanyuanqiao (Lines 10, 12), Dongzhimen (Lines 2, 13), Beixinqiao (Line 5)</td><td>Caoqiao (Lines 10, 19)</td></tr>
  </tbody>
</table>
</div>
<p>Fares and times are the airports' own figures when we checked. On the Daxing line, ticket sales stop five minutes before the last train, and the airport suggests being at the station ten minutes before it.</p>

<h2>Capital Airport (PEK): what else should I know?</h2>
<ul>
  <li><strong>Stations</strong> The line has five: Beixinqiao, Dongzhimen, Sanyuanqiao, Terminal 3 and Terminal 2. Going back to the airport, the first trains leave Beixinqiao at 05:56 and Dongzhimen at 06:00; the last leave at 22:26 and 22:30.</li>
  <li><strong>Taxis</strong> T3: the taxi area on level B1. T2: level 1, the middle lane outside doors 5 to 9. Use the official rank only.</li>
  <li><strong>Ride-hailing</strong> Pick-ups are in the parking buildings: for T3, parking building 3, level B2, zone H; for T2, parking building 2, level 1, south-east side.</li>
  <li><strong>Airport buses</strong> A 24-hour bus runs to Beijing West Railway Station, ¥25–30 depending on the stop, and another goes to Beijing South Railway Station, ¥20–30. Buses leave from outside door 1 on level 1 of T3 and door 11 on level 1 of T2.</li>
</ul>

<h2>How much is a taxi from Capital Airport?</h2>
<p>Taxis use the meter. The airport gives these main rules as a guide:</p>
<div class="table-scroll">
<table>
  <thead><tr><th>Item</th><th>Charge</th></tr></thead>
  <tbody>
    <tr><td>First 3 km</td><td>¥13</td></tr>
    <tr><td>Each further km</td><td>¥2.30, plus 50% for every km beyond 15 km</td></tr>
    <tr><td>Fuel surcharge</td><td>¥1 a trip</td></tr>
    <tr><td>23:00–05:00</td><td>Per-km rate plus 20%</td></tr>
    <tr><td>Road and bridge tolls</td><td>Paid by the passenger</td></tr>
  </tbody>
</table>
</div>
<p>Ask the driver for a receipt (<span lang="zh-Hans">发票</span>, fāpiào) and note the plate number in case you leave something behind. Have your hotel's address in Chinese ready to show; see <a href="@ROOT@beijing/chinese-address-cards/">address cards</a>.</p>

<h2>Daxing Airport (PKX): what else should I know?</h2>
<ul>
  <li><strong>Into town</strong> The express stops at Daxing Xincheng, then Caoqiao, where you change to metro Lines 10 or 19.</li>
  <li><strong>Children</strong> Children 1.3 m tall or under ride free with a paying adult.</li>
  <li><strong>Air–rail tickets</strong> China Southern, China Eastern, Air China and Xiamen Airlines offer discounted express tickets to some passengers flying from or to Daxing. The rules vary; check with your airline.</li>
  <li><strong>Flying out</strong> At Caoqiao you can check in, drop your bags and have them screened before you ride to the airport.</li>
</ul>

<h2>How do I get to the Forbidden City from the airport?</h2>
<p>Take the airport express to the metro, then the metro to Tiananmen East or Tiananmen West on Line 1, the stations the museum lists for the Meridian Gate, where visitors enter. Palace tickets go on sale online at 20:00 Beijing time seven days ahead and are never sold on the day, so book before you fly: see <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book with a passport</a> and <a href="@ROOT@forbidden-city/entrance-and-exit/">the entrance and exits</a>.</p>

<h2>What should I sort out before I land?</h2>
<p>A way to pay on your phone and a way to get online. Set up Alipay or WeChat Pay with your card before you fly; see <a href="@ROOT@beijing/without-google/">Beijing without Google</a>.</p>
''')

TEMPLE_OF_HEAVEN = Article(
    path='beijing/temple-of-heaven/',
    short='Temple of Heaven',
    title='Temple of Heaven, Beijing: tickets, hours and booking',
    description='Temple of Heaven tickets (¥15, or ¥34 combined), opening hours, Monday closures and how foreign visitors book with a passport, from official sources.',
    eyebrow='Temple of Heaven',
    h1='Temple of Heaven: tickets, hours and how to visit',
    image=None,
    image_alt='',
    about={'@type': 'TouristAttraction', 'name': 'Temple of Heaven', 'alternateName': '天坛', 'containedInPlace': {'@type': 'City', 'name': 'Beijing'}},
    related=['beijing/3-day-itinerary/', 'beijing/great-wall-which-section/', 'beijing/chinese-address-cards/'],
    city='beijing',
    cta=False,
    checked='2026-11-09',
    sources=[('Beijing Municipal Government: Temple of Heaven', 'https://english.beijing.gov.cn/specials/parktours/guidevisitors/templeofheaven/'),
             ('Beijing Municipal Government: Temple of Heaven tickets and booking', 'https://english.beijing.gov.cn/specials/ticketing/parks/202407/t20240719_3753312.html'),
             ('Visit Beijing (Beijing Municipal Bureau of Culture and Tourism): Temple of Heaven gates', 'https://www.visitbeijing.com.cn/article/47QrLHhZIb5')],
    body='''
<h2>Do I need to book the Temple of Heaven?</h2>
<p>Book ahead if you can. Tickets are sold by real-name booking 1–7 days in advance, and foreign visitors book on the "Temple of Heaven" WeChat account with their passport. Get the combined ticket, ¥34 from April to October or ¥28 from November to March, to go into the Hall of Prayer for Good Harvests, the Echo Wall and the Circular Mound Altar. These sights close on Mondays, except on public holidays, while the park itself is open every day.</p>

<h2>How much are the tickets?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th>Ticket</th><th>1 April – 31 October</th><th>1 November – 31 March</th></tr></thead>
  <tbody>
    <tr><td>Park admission</td><td>¥15</td><td>¥10</td></tr>
    <tr><td>Combined ticket</td><td>¥34</td><td>¥28</td></tr>
    <tr><td>Hall of Prayer for Good Harvests, Echo Wall and Circular Mound Altar</td><td colspan="2">¥20</td></tr>
    <tr><td>Divine Music Administration</td><td colspan="2">¥10</td></tr>
  </tbody>
</table>
</div>
<p>Each ticket also comes as a half-price discount ticket; check whether you qualify when you book. Prices are the official adult prices when we checked.</p>

<h2>What are the opening hours?</h2>
<div class="table-scroll">
<table>
  <thead><tr><th></th><th>1 April – 31 October</th><th>1 November – 31 March</th></tr></thead>
  <tbody>
    <tr><td>Park</td><td>06:00–22:00, last entry 21:00</td><td>06:30–22:00, last entry 21:00</td></tr>
    <tr><td>Ticketed sights</td><td>08:00–18:00, last entry 17:30</td><td>08:00–17:00, last entry 16:30</td></tr>
  </tbody>
</table>
</div>
<p>The ticketed sights are the Hall of Prayer for Good Harvests, the Echo Wall, the Circular Mound Altar, the Fasting Palace, the Divine Kitchen, the Animal Sacrifice Pavilion and the Divine Music Administration. All of them close on Mondays, except on public holidays.</p>

<h2>How do foreign visitors book?</h2>
<ul>
  <li>Book on the "Temple of Heaven" WeChat account with your passport, 1–7 days ahead, for a time slot. The e-ticket is valid only on the day you booked.</li>
  <li>At the gate, show the e-ticket QR code and the passport you booked with. Save a screenshot of the QR code before you go.</li>
  <li>If the main sights have not sold out, you can buy same-day tickets for them by scanning the QR code at the entrance, and the service counters in the park can also book for you.</li>
  <li>Unused tickets can be refunded free of charge within 7 days of the visit date, on the platform you booked through. Used tickets cannot be refunded.</li>
</ul>
<p>No WeChat yet? See <a href="@ROOT@beijing/without-google/">Beijing without Google</a> for setting it up before you travel.</p>

<h2>What is there to see?</h2>
<p>The Temple of Heaven is where the Ming and Qing emperors offered sacrifices to heaven and prayed for good harvests. The park covers 273 hectares inside a double wall. Its northern end is rounded and its southern end square, after the old belief that heaven is round and the earth square.</p>
<ul>
  <li><strong>Hall of Prayer for Good Harvests</strong> The temple's best-known building, built in 1420, 38.2 m high and 24.2 m across.</li>
  <li><strong>Imperial Vault of Heaven and the Echo Wall</strong> The hall and side halls that kept the tablets used at the sacrifices, in a courtyard ringed by a circular wall known as the Echo Wall.</li>
  <li><strong>Circular Mound Altar</strong> The open stone altar where the emperor made the sacrifice to heaven at the winter solstice. Its slabs, balustrades and steps come in nines or multiples of nine, the number of heaven.</li>
</ul>

<h2>Which way round should I walk?</h2>
<p>The park suggests a route for each season. In winter: in at the East Gate, along the Long Corridor to the Hall of Prayer for Good Harvests, then the Fasting Palace, the Divine Music Administration, the Imperial Vault of Heaven and the Echo Wall, and out at the South Gate. In spring and summer it starts from the West Gate instead. Allow two to three hours.</p>

<h2>How do I get there?</h2>
<ul>
  <li><strong>East Gate</strong> Metro Line 5 to Tiantandongmen, Exit A.</li>
  <li><strong>West Gate</strong> Metro Line 8 to Tianqiao, Exit C.</li>
  <li><strong>By taxi</strong> Show the driver <span lang="zh-Hans">天坛公园</span> (Tiāntán Gōngyuán) and the gate you want: <span lang="zh-Hans">东门</span> (east gate) or <span lang="zh-Hans">西门</span> (west gate).</li>
</ul>

<h2>When is the best time to go?</h2>
<p>Early. The park opens at 06:00 (06:30 from November to March), two hours before the halls, so you can walk the grounds while they are full of local people exercising, then be at the Hall of Prayer for Good Harvests when it opens at 08:00. Avoid Mondays unless you only want the park. It pairs well with an afternoon at the Summer Palace; see <a href="@ROOT@beijing/3-day-itinerary/">Beijing in 3 days</a>.</p>
''')

FC_MAP = Article(
    path='forbidden-city/map/',
    short='Forbidden City map',
    title='Forbidden City Map: Both Routes and 21 Spots (Hand-Drawn)',
    description='A hand-drawn map of the whole Forbidden City with two walking routes, the entrance and both exits, and 21 numbered spots, each with a line on what to look for.',
    eyebrow='Forbidden City · map',
    h1='Forbidden City map: two routes and 21 spots',
    image=None,
    image_alt='',
    about=FORBIDDEN_CITY,
    related=['forbidden-city/half-day-route/', 'forbidden-city/entrance-and-exit/', 'forbidden-city/tickets-for-foreigners/', 'jingshan-park/best-view-of-the-forbidden-city/'],
    checked='2026-11-10',
    og_image='fc-map.webp',
    sources=[('Palace Museum: opening hours, tickets and exits', 'https://www.dpm.org.cn/Visit.html'),
             ('Palace Museum: Hall of Military Prowess closed from 19 October 2026', 'https://www.dpm.org.cn/announce_detail/379651.html')],
    extra_ld=[{'@context': 'https://schema.org', '@type': 'ImageObject', 'name': 'Forbidden City map: two routes and 21 spots',
               'description': 'Hand-drawn map of the Forbidden City in Beijing with the Classic route (about 1 h 35 min, 1.8 km) and the Full route (about 4 h, 4.6 km), the Meridian Gate entrance, the Gate of Divine Might and East Glorious Gate exits, and 21 numbered spots.',
               'contentUrl': 'https://penyola.com/assets/img/fc-map-full.jpg', 'thumbnailUrl': 'https://penyola.com/assets/img/fc-map.webp',
               'width': 3000, 'height': 9000, 'encodingFormat': 'image/jpeg',
               'creditText': 'Map © Penyola; map data © OpenStreetMap contributors', 'copyrightNotice': '© Penyola',
               'creator': {'@type': 'Organization', 'name': 'Penyola', 'url': 'https://penyola.com/'},
               'acquireLicensePage': 'https://penyola.com/credits.html',
               'contentLocation': FORBIDDEN_CITY}],
    body='''
<p>This is the whole Forbidden City on one hand-drawn map. It shows two walking routes, the way in and the two ways out, and 21 numbered spots. Tap the map to open the full-size version, then zoom in on your phone.</p>
<figure class="big-map">
  <a href="@ROOT@assets/img/fc-map-full.jpg"><img src="@ROOT@assets/img/fc-map.webp" alt="Hand-drawn map of the Forbidden City with the Classic route in red, the Full route in dark green and 21 numbered spots" width="1200" height="3600"></a>
  <figcaption>Map © Penyola · map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a> · <a href="@ROOT@assets/img/fc-map-full.jpg">Full size (3000 × 9000 px, 3.2 MB)</a></figcaption>
</figure>

<h2>Which route should I take?</h2>
<p><strong>The Classic route</strong> (red) walks straight up the middle: about 1 hour 35 minutes and 1.8 km. It takes in spots 1 to 4 and 7 to 11, from the bronze lions to the Imperial Garden, and leaves by the Gate of Divine Might. Take this one if you have a morning, or if it is your first visit.</p>
<p><strong>The Full route</strong> (dark green) is about 4 hours and 4.6 km. It follows the same line through the big halls, then loops through the western palaces where later emperors lived and the eastern palaces with their courtyards, and heads for the Treasure Gallery in the northeast. The Clock and Watch Gallery and the Treasure Gallery each need their own small ticket on top of entry.</p>
<p>Both times are walking at an easy pace plus about 10 minutes at each stop. Queues, crowds and the extra galleries add more. For the stop-by-stop version of the shorter walk, see <a href="@ROOT@forbidden-city/half-day-route/">the Forbidden City in half a day</a>.</p>

<h2>Where do I go in and out?</h2>
<ul>
  <li><strong>In:</strong> everyone enters at the Meridian Gate, at the south end. See <a href="@ROOT@forbidden-city/entrance-and-exit/">how to get to it</a>.</li>
  <li><strong>Out:</strong> the Gate of Divine Might at the north end, across the road from <a href="@ROOT@jingshan-park/best-view-of-the-forbidden-city/">Jingshan Park</a>, or the East Glorious Gate on the east side, about 800 m from Wangfujing.</li>
  <li>The palace is closed on Mondays, except public holidays. Tickets are booked online in your own name, and your passport is your ticket. See <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book</a>.</li>
</ul>

<h2>What are the 21 spots?</h2>
<h3>Outer court</h3>
<ol class="spots" start="1">
  <li><strong>Bronze lions.</strong> One has a paw on a ball, the other a cub.</li>
  <li><strong>Hall of Supreme Harmony.</strong> Ten roof beasts, a sundial and bronze tortoises out front.</li>
  <li><strong>Hall of Central Harmony.</strong> Where the emperor got ready for big ceremonies.</li>
  <li><strong>Hall of Preserving Harmony.</strong> The largest carved stone ramp is round the back.</li>
  <li><strong>Hall of Military Prowess.</strong> Famous for the books printed here. Closed since 19 October 2026 for repairs.</li>
  <li><strong>Hall of Literary Glory.</strong> Scholars lectured the emperor here.</li>
</ol>
<h3>Inner court and garden</h3>
<ol class="spots" start="7">
  <li><strong>Gate of Heavenly Purity.</strong> Gilded lions mark the way into the inner palace.</li>
  <li><strong>Palace of Heavenly Purity.</strong> The heir's name was sealed behind the plaque.</li>
  <li><strong>Hall of Union.</strong> 25 imperial seals and two clocks.</li>
  <li><strong>Palace of Earthly Tranquility.</strong> Ming empresses lived here.</li>
  <li><strong>Imperial Garden.</strong> Pebble paths and two cypresses grown together.</li>
</ol>
<h3>West side</h3>
<ol class="spots" start="12">
  <li><strong>Hall of Mental Cultivation.</strong> Where later emperors lived and worked.</li>
  <li><strong>Palace of Gathered Elegance.</strong> Bronze dragons and deer in the courtyard.</li>
  <li><strong>Palace of Earthly Honor.</strong> Look for the little swing rings.</li>
  <li><strong>Palace of Compassion and Tranquility.</strong> Where empress dowagers lived.</li>
</ol>
<h3>East side</h3>
<ol class="spots" start="16">
  <li><strong>Palace of Celestial Favor.</strong> Pear blossom in spring.</li>
  <li><strong>Palace of Accumulated Purity.</strong> Magnolias in the courtyard.</li>
  <li><strong>Lingzhaoxuan.</strong> An unfinished building nicknamed the Crystal Palace.</li>
  <li><strong>Clock and Watch Gallery.</strong> Imperial clocks. Its own small ticket.</li>
  <li><strong>Nine-Dragon Screen.</strong> Nine dragons in glazed tile.</li>
  <li><strong>Treasure Gallery.</strong> Its own ticket. Old pines inside.</li>
</ol>

<h2>Can I print it or save it?</h2>
<p>Yes, for your own trip: save the full-size image to your phone before you go, since mobile data can be slow inside the palace. Please link to this page rather than re-posting the map elsewhere.</p>
''')

ARTICLES = [GREAT_WALL, THREE_DAYS, AIRPORT, TEMPLE_OF_HEAVEN, JINGSHAN_VIEW, HALF_DAY, FC_MAP, TICKETS, AUDIO, ENTRANCE, HALL, ROOF, WINTER, KIDS, CROWDS,
            SP_ROUTE, CORRIDOR, MARBLE, VISA_FREE, NO_GOOGLE, ADDRESS]


# "First time in <city>" hubs at /<city>/first-time/. Each lists its published guides in trip order (paths not yet
# written are skipped), and every guide with city=<key> links back here and to the city's detailed sight guides.
CITY_HUBS = {
    'beijing': dict(
        name='Beijing',
        title='First time in Beijing: a trip planning guide',
        description='Plan a first trip to Beijing: what to set up before you land, how to get around, how many days you need, which Great Wall section to pick and how to book the Forbidden City.',
        eyebrow='Beijing · trip planning',
        h1='First time in Beijing',
        about=BEIJING,
        intro='''<p>A first trip to Beijing goes smoothly if you sort out three things before you fly: payments on your phone, a way to get online, and your Forbidden City booking, which opens seven days ahead and sells out. The guides below follow the order of a trip, from before you land to planning each day.</p>
<h2>The short version</h2>
<ul>
  <li>Set up Alipay or WeChat Pay with your card and test it before you travel; see <a href="@ROOT@beijing/without-google/">Beijing without Google</a>.</li>
  <li>Book the Forbidden City at 20:00 Beijing time, seven days ahead, with your passport; see <a href="@ROOT@forbidden-city/tickets-for-foreigners/">how to book</a>.</li>
  <li>Carry the Chinese address of every place you are going; see <a href="@ROOT@beijing/chinese-address-cards/">address cards</a>.</li>
  <li>Keep your passport with you: it is your ticket at the big sights.</li>
</ul>''',
        sections=[
            ('Before you fly', ['beijing/before-you-land/', 'beijing/visa-free-entry/', 'beijing/without-google/']),
            ('Arriving and getting around', ['beijing/airport-to-city/', 'beijing/getting-around/', 'beijing/chinese-address-cards/']),
            ('Plan your days', ['beijing/visa-free-transit-2-day-plan/', 'beijing/3-day-itinerary/', 'beijing/4-day-itinerary/']),
            ('The big sights', ['forbidden-city/tickets-for-foreigners/', 'forbidden-city/half-day-route/', 'forbidden-city/map/', 'beijing/great-wall-which-section/',
                                'summer-palace/one-day-route/', 'beijing/temple-of-heaven/', 'jingshan-park/best-view-of-the-forbidden-city/', 'beijing/hutongs/']),
            ('Timing and pitfalls', ['beijing/best-time-to-visit/', 'forbidden-city/crowds-and-best-time/', 'beijing/common-mistakes/']),
        ],
        sights_heading="Beijing's imperial sights in detail",
        sights=['forbidden-city/half-day-route/', 'forbidden-city/tickets-for-foreigners/', 'summer-palace/one-day-route/', 'jingshan-park/best-view-of-the-forbidden-city/'],
    ),
}
