"""Générateur de la maquette Restaurant Carlino by L'ÉpiKurien. Usage : python build.py <dossier-du-projet>
Contenus relevés sur l-epikurien-01.eatbu.com, Instagram @lepikurien.01 et la page Facebook (13/11/2026).
Rien d'inventé : textes, visuels, carte d'automne, prix, horaires, coordonnées."""
import os
import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "."
A = 'assets/'
PH = A + 'ph/'
V = 1  # cache : incrémenter à chaque changement de CSS ou JS
TEL, TELH = '09 83 94 89 00', 'tel:0983948900'
MAIL = 'lepikurien.contact@gmail.com'
ADR = ('27 rue Jean Marie Delorme', '01400 Châtillon-sur-Chalaronne')
CMD = 'https://commande-en-ligne.laddition.com/commande-en-ligne/restaurant-carlino/carte'
IG = 'https://www.instagram.com/lepikurien.01/'
FB = 'https://www.facebook.com/profile.php?id=61563339757208'
HOR = [('Lundi, mardi, mercredi', '12 h – 14 h'), ('Jeudi, vendredi, samedi', '12 h – 14 h et 18 h 30 – 22 h'), ('Dimanche', 'fermé')]
NAV = [('restaurant.html', 'Le restaurant'), ('carte.html', 'La carte')]


def pill(t, href, cls='', arrow='↗', ext=False):
    x = ' target="_blank" rel="noopener"' if ext else ''
    return f'<a class="pill {cls}" href="{href}"{x}><span class="r"><span>{t}</span><span>{t}</span></span><b>{arrow}</b></a>'


def tile(src, cls='', style='', alt='', par=None, lazy=True):
    p = f' data-par="{par}" style="height:118%;width:100%"' if par else ''
    return f'<figure class="tile {cls}" style="{style}"><img src="{src}" alt="{alt}"{p}{" loading=lazy" if lazy else ""}></figure>'


def logo(cls=''):
    return f'<span class="lgo {cls}" aria-hidden="true"><img src="{A}logo.png" alt=""><span><span class="wm">Restaurant <i>Carlino</i></span><small>by L’ÉpiKurien</small></span></span>'


def head(title, desc, cur):
    def a(h, t, cls=''):
        return f'<a href="{h}"{" class="+cls if cls else ""}{" aria-current=page" if h == cur else ""}>{t}</a>'
    items = a('index.html', 'Accueil') + ''.join(a(h, t) for h, t in NAV) + a('reserver.html', 'Réserver', 'hl')
    return f'''<!doctype html>
<html lang="fr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website">
<meta name="theme-color" content="#1f2419">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="{A}logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=Quattrocento+Sans:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}style.css?v={V}">
</head><body>
<div id="bar"></div>
<header class="top">
<a class="logo" href="index.html" aria-label="Restaurant Carlino by L’ÉpiKurien, accueil">{logo()}</a>
<nav class="nav" aria-label="Navigation principale"><button class="stop" type="button" aria-label="Fermer le menu"><span>MENU</span></button>{items}</nav>
<span class="side"><a class="tel" href="{TELH}" aria-label="Appeler le {TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z" fill="currentColor"/></svg><span>{TEL}</span></a></span>
<button class="burger" aria-label="Menu" aria-expanded="false"><i></i><i></i></button>
</header>
<main>'''


def foot():
    return f'''</main>
<footer><div class="wrap"><div class="fg">
<div>{logo('big')}<p>Une ambiance chaleureuse et conviviale, une cuisine généreuse, préparée avec passion. Sur place, à emporter ou en livraison.</p></div>
<div><h4 class="micro">Le restaurant</h4><ul><li><a href="restaurant.html">Notre maison</a></li><li><a href="carte.html">La carte d’automne</a></li><li><a href="reserver.html">Réserver une table</a></li><li><a href="{CMD}" target="_blank" rel="noopener">Commander en ligne</a></li></ul></div>
<div><h4 class="micro">Contact</h4><ul><li><a href="{TELH}">{TEL}</a></li><li><a href="mailto:{MAIL}">{MAIL}</a></li><li><a href="{IG}" target="_blank" rel="noopener">Instagram</a></li><li><a href="{FB}" target="_blank" rel="noopener">Facebook</a></li></ul></div>
<div><h4 class="micro">Nous trouver</h4><ul><li>{ADR[0]}</li><li>{ADR[1]}</li><li>Fermé le dimanche</li></ul></div>
</div></div>
<div class="fw" aria-hidden="true">ÉPIKURIEN</div>
<div class="fb micro"><span class="pad">© Restaurant Carlino by L’ÉpiKurien</span><span class="pad">Maquette de site · Le Génie Numérique</span></div></footer>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="{A}main.js?v={V}"></script></body></html>'''


def cta(t='Une table <em>vous attend</em>'):
    return f'''<section class="sec cta"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.6rem">Le plaisir de partager</span><h2 class="sp">{t}</h2>
<div class="row rv">{pill('Réserver une table', 'reserver.html', 'blue')}{pill(TEL, TELH, 'ghost')}</div></div></section>'''


def pagehead(crumb, h1, lead, img, img2=None, extra=''):
    t2 = tile(img2, 'small', lazy=False) if img2 else ''
    return f'''<section class="ph"><div class="wrap"><div class="crumb micro"><a href="index.html">Accueil</a> / {crumb}</div><h1 class="sp">{h1}</h1><p class="lead rv">{lead}</p>{extra}</div>{tile(img, lazy=False)}{t2}</section>'''


def gal(items):
    return '<div class="gal">' + ''.join(f'<figure class="rv" data-c="{c}" style="--d:{(i % 3) * .07}s"><img src="{PH}{k}.webp" alt="{t}" loading="lazy"><figcaption><span class="micro">{c}</span>{t}</figcaption></figure>' for i, (k, c, t) in enumerate(items)) + '</div>'


def hours():
    return ''.join(f'<span><b>{j}</b> · {h}</span>' for j, h in HOR)


# carte d'automne 2026 (publiée sur Instagram le 01/10/2026)
CARTE = [
    ('Entrées', [('Friture de Joël', 'Aïoli maison et fleur de sel de Guérande', '10,90 €'),
                 ('Os à moelle', 'Gratons et salade verte', '12,90 €'),
                 ('Velouté de lentilles', 'Toast de pain de campagne grillé à la raclette', '11,90 €'),
                 ('Poitrine fumée croustillante', 'Noisettes torréfiées, crème de champignons et croûtons', '13,90 €')]),
    ('Plats', [('Ballottine de cabillaud', 'Mousseline de céleri-rave, épinards et poireaux fondants, bisque de crustacés', '24,00 €'),
               ('Filet de canette rôti', 'Jus réduit au thym, pommes grenailles et légumes d’automne glacés', '24,00 €'),
               ('Linguines aux fruits de mer', 'Jus de coquillages', '19,00 €')]),
    ('Burgers', [('Épikurien', 'Pain multi-céréales, steak haché frais, oignons rouges, poivrons confits, salade, tomate, bacon, sauce cheddar', '16,50 €'),
                 ('Chicken', 'Pain multi-céréales, poulet croustillant, oignons rouges, salade, tomate, sauce au bacon fumé', '15,50 €'),
                 ('Raclette', 'Pain multi-céréales, steak haché frais, cornichons, oignons rouges, salade, bacon, raclette, sauce tartare', '16,50 €'),
                 ('Texan', 'Pain multi-céréales, steak haché frais, poivrons confits, oignons frits, salade, tomate, bacon, sauce barbecue', '16,50 €'),
                 ('Chèvre-miel', 'Pain multi-céréales, poulet croustillant, salade, tomate, oignons rouges, chèvre, miel, sauce aux herbes', '15,50 €'),
                 ('Savoyard', 'Pain multi-céréales, galette de pommes de terre, steak haché frais, bacon, oignons rouges, tomate, salade, reblochon', '17,50 €')]),
    ('Bowls', [('Bowl à composer', 'Riz au curcuma ou quinoa · une protéine : falafels, saumon frais, poulet mariné, crevettes tempura ou poulet croustillant · cinq accompagnements au choix', '16,50 €')]),
    ('Fromages et desserts', [('Assortiment de fromages secs', '', '8,50 €'),
                              ('Fromage blanc', '', '4,00 €'),
                              ('Desserts et glaces du jour', 'Selon nos envies', '8,50 €')]),
]
MENUS = [('Le midi', 'Du jour', 'Du lundi au samedi', ['Menu du jour, produits de saison', 'Suggestion du jour, selon l’inspiration du chef', 'Bowls et burgers préparés à la commande']),
         ('Menu d’automne', '28 €', 'Jeudi, vendredi et samedi soir', ['Velouté de lentilles, os à moelle ou poitrine fumée croustillante', 'Burger au choix, linguines, ballottine de cabillaud ou filet de canette', 'Fromage ou dessert']),
         ('Menu grenouilles', '31 €', 'Ouverture exceptionnelle du 13 septembre', ['Grenouilles en persillade, en deux services', 'Gratin dauphinois · cervelle de canut', 'Dessert au choix, café compris'])]


def pages():
    P = {}
    hero_tiles = [('t1', 'devanture-s'), ('t2', 'salle'), ('t3', 'bieres'), ('t4', 'salle2'), ('t5', 'burgers'), ('t6', 'menu31'), ('t7', 'ouverture')]
    ht = ''.join(f'<figure class="tile {c}"><div class="fl"><div class="in"><img src="{PH}{f}.webp" alt=""></div></div></figure>' for c, f in hero_tiles)
    stack = ''.join(tile(f'{PH}{f}.webp') for f in ['carte-entrees', 'carte-plats', 'burgers', 'bowls', 'menu28', 'menu31', 'bieres', 'nouvelle-carte'])
    wall_imgs = ['devanture-s', 'carte-plats', 'salle', 'bieres', 'burgers', 'salle2', 'nouvelle-carte', 'menu31', 'bowls', 'ouverture', 'guru', 'menu28', 'tgtg', 'carte-entrees']
    wall = ''.join(tile(f'{PH}{wall_imgs[i % len(wall_imgs)]}.webp') for i in range(54))
    items = [('restaurant.html', '01', 'Le restaurant', 'Une ambiance chaleureuse, une cuisine généreuse, préparée avec passion.', 'devanture-s', 'Depuis le 20 juillet'),
             ('carte.html', '02', 'La carte', 'Entrées, plats, burgers, bowls. Menu d’automne à 28 €.', 'carte-plats', 'Automne 2026'),
             ('reserver.html', '03', 'Réserver', 'Votre table en ligne, en 30 secondes.', 'salle', 'Midi · soir'),
             (CMD, '04', 'Commander', 'Click & Collect, ou livraison via Uber Eats.', 'ubereats', 'À emporter')]
    pl = ''.join(f'<a href="{h}"{" target=_blank rel=noopener" if h.startswith("http") else ""}><span class="micro mute">{n}</span><span class="nm">{t}</span><span class="d">{d}<b>{b}</b></span></a>' for h, n, t, d, _, b in items)
    prev = ''.join(tile(f'{PH}{it[4]}.webp', 'on' if i == 0 else '') for i, it in enumerate(items))
    track = ''.join(f'<figure class="tile"><img src="{PH}{f}.webp" alt="{l}" loading="lazy"><span class="tag">{l}</span></figure>' for f, l in [
        ('carte-entrees', 'Entrées'), ('carte-plats', 'Plats'), ('burgers', 'Burgers'), ('bowls', 'Bowls'), ('menu28', 'Menu à 28 €'), ('bieres', 'Au bar')])
    steps = [('Vous réservez', f'En ligne, ou au {TEL}.'),
             ('Vous arrivez', f'{ADR[0]}, à Châtillon.'),
             ('Vous choisissez', 'Menu du jour, carte, burger ou bowl.'),
             ('Vous savourez', 'Sur place, à emporter ou livré chez vous.')]
    st = ''.join(f'<div class="stp"><div class="n">{i + 1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    mq = ''.join(f'<span>{x}</span>' for x in ['Cuisine traditionnelle', 'Burgers', 'Bowls', 'Sur place', 'À emporter', 'Livraison', 'Produits de saison'] * 2)

    P['index.html'] = head('Restaurant Carlino by L’ÉpiKurien — Châtillon-sur-Chalaronne', 'Restaurant Carlino by L’ÉpiKurien à Châtillon-sur-Chalaronne : cuisine traditionnelle, burgers et bowls. Sur place, à emporter ou en livraison. 09 83 94 89 00.', 'index.html') + f'''
<section class="hero">
<div class="cap micro c1"><b>Le plaisir</b>de partager</div>
<div class="cap micro c2"><b>Cuisine traditionnelle</b>burgers · bowls</div>
<div class="cap micro c3"><b>Sur place</b>à emporter · livraison</div>
<div class="go">{pill('Réserver une table', 'reserver.html')}</div>
{ht}
<p class="para">Une cuisine généreuse, préparée avec passion.</p>
<h1 class="word">ÉPIKURIEN</h1>
<div class="scrollhint micro"><i></i>Défiler</div>
</section>

<div class="mq" aria-hidden="true"><div>{mq}</div></div>

<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Bienvenue</span><h2 class="sp">Chaleureux <em>et convivial</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Un déjeuner rapide, un dîner en famille, un repas entre amis ou une occasion particulière : toute l’équipe est heureuse de vous accueillir.</p>
<ul class="checks rv" style="margin-bottom:2rem"><li><span><b>Le midi</b>, menu du jour et suggestion du chef.</span></li><li><span><b>Le soir</b>, du jeudi au samedi, une carte plus élaborée.</span></li><li><span><b>Titres-restaurant</b> acceptés, carte et papier.</span></li></ul>{pill('Découvrir le restaurant', 'restaurant.html', 'blue')}</div>{tile(PH + 'devanture.webp', '', par=8, alt='La devanture du Restaurant Carlino')}</div></section>

<section class="story"><span class="micro mute m3">Notre cuisine</span>
<h2><span class="w">Une</span> <span class="w">cuisine</span> <span class="w">généreuse,</span> <span class="w">préparée</span> <span class="w">avec</span> <span class="w"><em>passion</em></span></h2>
<div class="stack">{stack}</div>
<p class="micro mute m1">Traditionnelle, généreuse et raffinée.</p><span class="micro mute m2">Produits de saison</span></section>

<section class="wall"><div class="grid">{wall}</div><div class="mid"><span class="micro mute">Automne 2026</span><h2>La carte <em>d’automne</em></h2>{pill('Voir la carte', 'carte.html', 'blue')}</div></section>

<section class="sec" id="services"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Sur place ou chez vous</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,4rem)">Que souhaitez-vous <em>faire ?</em></h2>
<div class="plist">{pl}</div></div><div class="prev">{prev}</div></section>

<section class="hz"><div class="pin"><div class="wrap top2"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">À table</span><h2>L’automne <em>s’invite dans vos assiettes</em></h2></div>{pill('La carte', 'carte.html')}</div>
<div class="track">{track}</div></div></section>

<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Ce qu’en disent nos clients</span><h2 class="sp">Une adresse <em>recommandée</em></h2>
<div class="cnt rv"><div><b data-to="211">0</b><span>avis sur Google, note de 4,5 sur 5</span></div><div><b data-to="100">0</b><span>% de recommandations sur Facebook</span></div><div><b data-to="2026">0</b><span>recommandé sur Restaurant Guru</span></div></div>
<p class="note" style="margin-top:1.4rem">Chiffres relevés le 12/11/2026, à confirmer avec le restaurant.</p></div></section>

<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.4rem">Anti-gaspi</span><h2 class="sp">De bons plats <em>méritent une seconde vie</em></h2>
<p class="lead rv" style="margin:1.4rem 0 2rem">Le restaurant a rejoint Too Good To Go : paniers surprise menu du jour, plat du jour ou desserts, selon les disponibilités.</p>{pill('Commander en ligne', CMD, 'blue', ext=True)}</div>{tile(PH + 'tgtg.webp', '', par=8, alt='Le restaurant rejoint Too Good To Go')}</div></section>

<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.4rem">Votre venue</span><h2 class="sp">Simple <em>comme bonjour</em></h2><div class="steps">{st}</div></div></section>
{cta()}''' + foot()

    P['restaurant.html'] = head('Le restaurant — Restaurant Carlino by L’ÉpiKurien', 'Restaurant Carlino by L’ÉpiKurien : une ambiance chaleureuse et conviviale, une cuisine généreuse, le midi du lundi au samedi et le soir du jeudi au samedi.', 'restaurant.html') + pagehead('Le restaurant', 'Le plaisir <em>de partager</em>', 'Bienvenue au Restaurant Carlino by L’ÉpiKurien : une ambiance chaleureuse et conviviale, une cuisine généreuse, préparée avec passion.', PH + 'salle2.webp', PH + 'bieres.webp') + f'''
<section class="sec"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Le midi</span><h2 class="sp">Gourmand, <em>rapide</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Pour vos pauses déjeuner, une offre gourmande et rapide, sans compromis sur la qualité : le menu du jour élaboré avec des produits de saison, la suggestion du jour selon l’inspiration du chef, nos bowls frais et équilibrés, nos burgers préparés à la commande.</p></div>{tile(PH + 'burgers.webp', '', par=8, alt='La carte des burgers')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap fin"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Le soir</span><h2 class="sp">Prendre <em>le temps</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Les jeudi, vendredi et samedi soir, une carte plus élaborée, imaginée pour prendre le temps de savourer. Une cuisine traditionnelle, généreuse et raffinée, avec des produits de qualité.</p></div>{tile(PH + 'carte-plats.webp', '', par=8, alt='La carte d’automne, les plats')}</div></section>
<section class="sec" style="padding-top:0"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">À la maison</span><h2 class="sp">Chez vous <em>aussi</em></h2></div>
<ul class="checks rv"><li><span><b>Click & Collect</b> : commandez en ligne, passez récupérer.</span></li><li><span><b>Livraison</b> via Uber Eats.</span></li><li><span><b>Too Good To Go</b> : des paniers anti-gaspi.</span></li><li><span><b>Titres-restaurant</b> acceptés sur place.</span></li><li><span><b>Terrasse</b>, coin enfants, animaux acceptés.</span></li></ul></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos nouvelles</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">La vie <em>du restaurant</em></h2>
<div class="flt" data-t=".gal figure"><button class="on" data-f="*">Tout</button><button data-f="Carte">La carte</button><button data-f="Nouvelles">Les nouvelles</button></div>
{gal([('salle', 'Nouvelles', 'La salle'), ('devanture-s', 'Nouvelles', 'La devanture'), ('carte-entrees', 'Carte', 'Les entrées d’automne'), ('merci', 'Nouvelles', 'Merci pour votre confiance'), ('carte-plats', 'Carte', 'Les plats d’automne'), ('titres', 'Nouvelles', 'Les titres-restaurant acceptés'), ('burgers', 'Carte', 'Les burgers'), ('guru', 'Nouvelles', 'Recommandé sur Restaurant Guru 2026'), ('bowls', 'Carte', 'Les bowls'), ('ubereats', 'Nouvelles', 'Uber Eats est de retour'), ('menu28', 'Carte', 'Le menu à 28 €'), ('tgtg', 'Nouvelles', 'Le restaurant rejoint Too Good To Go'), ('menu31', 'Carte', 'Le menu grenouilles'), ('salle2', 'Nouvelles', 'La salle, côté rue'), ('bieres', 'Nouvelles', 'Au bar')])}</div></section>''' + cta() + foot()

    tabs = ''.join(f'<button{" class=on" if i == 0 else ""} data-f="{c}">{c}</button>' for i, (c, _) in enumerate(CARTE))
    rows = ''.join(f'<div class="dish rv{"" if c == CARTE[0][0] else " hide"}" data-c="{c}"><div><h3>{n}</h3>{f"<p>{d}</p>" if d else ""}</div><b>{p}</b></div>' for c, its in CARTE for n, d, p in its)
    mn = ''.join(f'<div class="menu rv"><span class="micro mute">{s}</span><h3>{n}</h3><b>{p}</b><ul>{"".join(f"<li>{x}</li>" for x in its)}</ul></div>' for n, p, s, its in MENUS)
    P['carte.html'] = head('La carte d’automne — Restaurant Carlino by L’ÉpiKurien', 'Carte d’automne 2026 : friture de Joël, os à moelle, ballottine de cabillaud, filet de canette, burgers dès 15,50 €, bowls à 16,50 €, menu à 28 €.', 'carte.html') + pagehead('La carte', 'La carte <em>d’automne</em>', 'De nouvelles assiettes, de nouvelles saveurs et toujours la même envie : vous faire passer un bon moment.', PH + 'carte-plats.webp', PH + 'carte-entrees.webp') + f'''
<section class="sec"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">Nos formules</span><h2 class="sp" style="margin-bottom:clamp(2rem,5vw,3.4rem)">Midi et soir, <em>toutes les envies</em></h2><div class="menus m3">{mn}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><span class="micro mute" style="display:block;margin-bottom:1.2rem">À la carte</span><h2 class="sp" style="margin-bottom:2rem">Choisissez <em>votre plat</em></h2>
<div class="flt" data-t=".dish">{tabs}</div><div class="dishes">{rows}</div>
<p class="note" style="margin-top:2rem">Burgers en double : de 2 € à 3,50 € de plus. Bowls : cinq accompagnements au choix parmi cacahuètes, oignons frits, champignons, haricots mungo, carottes râpées, tomates confites, maïs, radis, fèves, avocat, brocolis, chou rouge. Prix relevés sur Instagram, à confirmer avec le restaurant.</p></div></section>''' + cta() + foot()

    cov = ''.join(f'<button type="button"{" class=on" if i == 2 else ""}>{i}</button>' for i in range(1, 9))
    P['reserver.html'] = head('Réserver une table — Restaurant Carlino by L’ÉpiKurien', f'Réservez votre table au Restaurant Carlino by L’ÉpiKurien, Châtillon-sur-Chalaronne. Midi du lundi au samedi, soir du jeudi au samedi. {TEL}.', 'reserver.html') + pagehead('Réserver', 'Votre table <em>vous attend</em>', 'La réservation en ligne est arrivée. Choisissez le jour, le service et le nombre de couverts.', PH + 'salle.webp') + f'''
<section class="sec" id="reserver"><div class="wrap split"><div><span class="micro mute" style="display:block;margin-bottom:1.2rem">Réservation en ligne</span><h2 class="sp">En <em>30 secondes</em></h2>
<p class="lead rv" style="margin-top:1.4rem">Vous recevez une confirmation par e-mail. Pour un groupe ou un événement privé, appelez-nous au <a href="{TELH}">{TEL}</a>.</p>
<div class="hor rv">{hours()}<span>{ADR[0]}, {ADR[1]}</span><span class="micro">Horaires à confirmer avec le restaurant</span></div></div>
<form class="f calc rv" id="resa"><div class="seg"><button type="button" class="on" data-m="table">Déjeuner</button><button type="button" data-m="table" data-s="soir">Dîner</button></div>
<div class="r2"><div class="fld"><label for="rd">Date</label><input id="rd" type="date" required></div><div class="fld"><label for="rh">Heure</label><select id="rh"><option>12 h 00</option><option>12 h 30</option><option>13 h 00</option><option>13 h 30</option></select></div></div>
<div class="fld"><label>Couverts</label><div class="cov">{cov}</div></div>
<div class="r2"><div class="fld"><label for="rn">Nom</label><input id="rn" required></div><div class="fld"><label for="rt">Téléphone</label><input id="rt" type="tel" required></div></div>
<div class="fld"><label for="re">E-mail</label><input id="re" type="email"></div>
<div class="fld"><label for="rm">Une occasion particulière ?</label><input id="rm" placeholder="Anniversaire, allergie, chaise bébé…"></div>
<button class="pill blue" type="submit" style="justify-self:start"><span class="r"><span>Réserver</span><span>Réserver</span></span><b>↗</b></button><div class="ok">Merci ! (Maquette : aucune réservation n’est envoyée.)</div></form></div></section>''' + foot()
    return P


for k, v in pages().items():
    open(os.path.join(OUT, k), 'w', encoding='utf-8').write(v)
print('ok')
