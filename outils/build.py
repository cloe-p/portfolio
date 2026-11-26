"""Génère les pages Toulouse Social Run, Community manager, Labo et À propos.
Lancer depuis la racine du dépôt : python3 outils/build.py"""
import html

E = html.escape


def head(titre, desc, extra_css="", classe=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(titre)} · Cloé Pérot</title>
<meta name="description" content="{E(desc)}">
<link rel="stylesheet" href="assets/base.css">
<link rel="stylesheet" href="assets/projet.css">
{('<style>' + extra_css + '</style>') if extra_css else ''}
</head>
<body class="{classe}">

<header class="menu" id="menu">
  <a class="nom" href="index.html">Cloé Pérot</a>
  <nav aria-label="Navigation principale">
    <a href="index.html#projets">Projets pro</a>
    <a href="labo.html" class="opt">Labo</a>
    <a href="a-propos.html" class="opt">À propos</a>
    <a class="cv" href="#" title="Bientôt disponible">Mon CV</a>
  </nav>
</header>

<main>
"""


def pied(suivant=None):
    s = ""
    if suivant:
        href, img, titre, pos = suivant
        s = f"""
  <section>
    <a class="suivant" href="{href}">
      <img src="{img}" alt="" loading="lazy" style="object-position:{pos}">
      <div><span>Projet suivant</span><h2>{titre}</h2></div>
    </a>
  </section>
"""
    return s + """</main>

<footer id="contact">
  <h2>On en parle ?</h2>
  <div class="btns"><a class="b plein" href="mailto:cloe.perot@icloud.com">cloe.perot@icloud.com</a><a class="b ligne" href="#" title="Bientôt disponible">Télécharger mon CV</a></div>
  <small>Cloé Pérot · Toulouse</small>
</footer>

<dialog class="vue" id="vue" aria-label="Image agrandie">
  <button type="button" aria-label="Fermer">×</button>
  <img src="" alt="">
  <p></p>
</dialog>

<script src="assets/projet.js"></script>
</body>
</html>
"""


def z(src, alt, cls="", style=""):
    st = f' style="{style}"' if style else ""
    return f'<a class="zoom {cls}" href="{src}"><img src="{src}" alt="{E(alt)}" loading="lazy"{st}></a>'


def fig(src, alt, titre="", texte="", cls="", style=""):
    cap = ""
    if titre or texte:
        cap = "<figcaption>" + (f"<b>{titre}</b>" if titre else "") + texte + "</figcaption>"
    return f"<figure>{z(src, alt, cls, style)}{cap}</figure>"


def note(t):
    return f'<p style="margin:-6px 0 0;color:var(--doux);font-size:14px">{t}</p>'


def ouverture(img, titre, ex, role, pos="center"):
    return f"""  <div class="ouv">
    <img src="{img}" alt="" style="object-position:{pos}">
    <a class="retour" href="index.html#projets">← Tous les projets</a>
    <h1>{titre}</h1>
    <p class="ex">{ex}</p>
    <p class="role">{role}</p>
  </div>
"""


def intro(texte, domaines, chiffres):
    d = "".join(f"<li>{x}</li>" for x in domaines)
    c = "".join(f"<div><strong>{a}</strong><span>{b}</span></div>" for a, b in chiffres)
    ch = f'<div class="chiffres">{c}</div>' if chiffres else ""
    return f"""
  <section class="intro">
    <div>
      <p class="grand">{texte}</p>
      <ul class="domaines">{d}</ul>
    </div>
    {ch}
  </section>
"""


def sommaire(items):
    li = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return f"""
  <nav class="sommaire" aria-label="Sections du projet">
    <ul>{li}</ul>
  </nav>
"""


def bloc(id_, titre, textes, media, liste=None):
    p = "".join(f"<p>{t}</p>" for t in textes)
    ul = ("<ul>" + "".join(f"<li>{x}</li>" for x in liste) + "</ul>") if liste else ""
    return f"""
  <section class="bloc" id="{id_}">
    <div class="txt">
      <h2>{titre}</h2>
      {p}{ul}
    </div>
    <div class="media">
      {media}
    </div>
  </section>
"""


def pastilles(xs):
    return '<ul class="pastilles">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"


# ---------------------------------------------------------------- Toulouse Social Run
T = "assets/img/tsr/"
tsr = head("Toulouse Social Run", "Identité visuelle, réseaux sociaux et partenariats pour le Toulouse Social Run, running club associatif à Toulouse.", classe="tsr")
tsr += ouverture(T + "ph_group2.webp", "Toulouse Social Run", "le running club qui court ensemble",
                 "Chargée de communication &amp; graphiste, bénévole, de 2024 à 2026.", "center 42%")
tsr += intro("Au départ, c'était un projet d'école… devenu une vraie association&nbsp;! Un club de course gratuit et ouvert à tous, où chaque run finit par un moment ensemble. Moi, j'y gère la com et l'identité visuelle.",
             ["Identité visuelle", "Direction artistique", "Social media", "Partenariats", "Événementiel", "Merch", "Community management"],
             [("~50", "coureurs par run, et 110+ sur les gros événements"), ("×4,4", "abonnés Instagram en un an, 2&nbsp;825 en mai 2026"),
              ("2&nbsp;016", "membres du club sur Strava"), ("3", "versions de l'identité en deux ans")])
tsr += sommaire([("esprit", "L'esprit du club"), ("identite", "L'identité"), ("da", "Nouvelle DA"), ("evenements", "Événements"), ("communaute", "Communauté")])

tsr += bloc("esprit", "Courir ensemble",
            ["Ce qu'on raconte, ce n'est pas juste une course : c'est la ville, les rencontres et ce qu'on partage après.",
             "Un brunch, un cours de pilates, des cookies… le moment social change à chaque fois&nbsp;!"],
            '<div class="mosaique">'
            + z(T + "ph_bridge.webp", "Coureurs Toulouse Social Run sur le pont Saint-Pierre", "h2", "object-position:center 85%")
            + z(T + "ph_social.webp", "Coureurs qui discutent devant le Café Cerise", "", "object-position:center 40%")
            + z(T + "ph_park.webp", "Coureurs dans un parc de Toulouse", "h2", "object-position:center 60%")
            + z(T + "ph_latte.webp", "Latte au Café Cerise après la course", "h2", "object-position:center 40%")
            + z(T + "ph_river.webp", "Les coureurs le long de la Garonne", "", "object-position:center 65%")
            + z(T + "ph_counter.webp", "Le comptoir du Café Cerise vu d'en haut")
            + z(T + "ph_legs.webp", "Coureurs en mouvement", "w2", "object-position:center 70%")
            + z(T + "ph_talk.webp", "Coureurs qui discutent après le run")
            + "</div>"
            + '<div class="encart"><h3>Nos formats</h3>' + pastilles(["Run &amp; brunch", "Run &amp; pilates", "Run &amp; cookies", "Run &amp; café", "Run pizza", "Run test", "et plein d'autres"]) + "</div>")

tsr += bloc("identite", "L'identité",
            ["Des cerises dessinées au logo actuel, j'ai fait grandir l'identité en même temps que le club, jusqu'à une vraie charte complète."],
            f"""<div class="logos">
        <div class="frise">
          <div><img src="{T}lg_cerise.webp" alt="Premier logo Toulouse Social Run avec deux cerises" loading="lazy"><b>Sept. 2024</b><span>le premier logo</span></div>
          <div><img src="{T}lg_rond.webp" alt="Deuxième logo Toulouse Social Run, plus sobre" loading="lazy"><b>Févr. 2025</b><span>un logo plus sobre</span></div>
          <div><img src="{T}lg_tsr.webp" alt="Logo TSR actuel" loading="lazy"><b>Déc. 2025</b><span>la nouvelle DA</span></div>
        </div>
        <div class="charte">
          <div>
            <p style="margin:0 0 14px;font-weight:700">La charte de décembre 2025</p>
            <div class="couleurs">
              <div><i style="background:#000"></i><small>noir</small></div><div><i style="background:#de1d1a"></i><small>rouge</small></div>
              <div><i style="background:#f07f1a"></i><small>orange</small></div><div><i style="background:#f5c71a"></i><small>jaune</small></div>
              <div><i style="background:#c0bfbf"></i><small>gris</small></div><div><i style="background:#fff"></i><small>blanc</small></div>
            </div>
          </div>
          <div>
            <div class="typo"><strong style="font-family:'League Spartan',sans-serif;font-weight:800">Aa</strong><div><b>League Spartan</b><span>titres</span></div></div>
            <div class="typo"><strong style="font-family:Montserrat,sans-serif;font-weight:500">Aa</strong><div><b>Montserrat</b><span>sous-titres et textes</span></div></div>
          </div>
        </div>
        <div class="g g3" style="margin-top:26px;align-items:center">
          <img src="{T}lg_tsr.webp" alt="Logotype TSR" loading="lazy" style="max-height:90px;margin:auto">
          <img src="{T}lg_principal.webp" alt="Logo principal Toulouse Social Run" loading="lazy" style="max-height:90px;margin:auto">
          <img src="{T}lg_secondaire.webp" alt="Logo secondaire Toulouse Social Run" loading="lazy" style="max-height:40px;margin:auto">
        </div>
        <p style="margin:12px 0 0;font-size:14px;color:#5a5a5a;text-align:center">Logotype, logo principal et logo secondaire</p>
      </div>""",
            ["3 logos : logotype, principal, secondaire", "La charte : 6 couleurs, 2 typos", "Les stickers et le t-shirt technique"])

pano = "".join(z(T + f"car{i}.webp", f"Carrousel d'annonce de la nouvelle DA, slide {i}") for i in range(1, 7))
tsr += bloc("da", "Nouvelle DA",
            ["Pour annoncer la nouvelle identité, j'ai fait un carrousel panoramique qui se swipe d'une slide à l'autre… puis la DA a pris vie sur le terrain."],
            f"""<div class="panorama">{pano}</div>
      {note("Le carrousel d'annonce, décembre 2025 : 6 slides qui se suivent jusqu'au « Rejoins-nous ! »")}
      <div class="g g2" style="align-items:stretch">
        <div class="stickers" style="background:#1c1c1c">
          <img src="{T}st_tsr_rouge.webp" alt="Sticker TSR rouge" loading="lazy">
          <img src="{T}st_principal_orange.webp" alt="Sticker Toulouse Social Run orange" loading="lazy">
          <img class="long" src="{T}st_second_jaune.webp" alt="Sticker Toulouse Social Run, version longue" loading="lazy">
        </div>
        <a class="zoom" href="{T}tshirt.webp" style="background:#f2f1ee"><img src="{T}tshirt.webp" alt="T-shirt technique Toulouse Social Run, dos et face" loading="lazy" style="padding:6%"></a>
      </div>
      <div class="g g2"><p style="margin:0;color:var(--doux);font-size:14px">Les stickers, en trois couleurs</p><p style="margin:0;color:var(--doux);font-size:14px">Le t-shirt technique : TSR® côté cœur, logo principal au dos</p></div>""",
            ["Carrousel d'annonce en 6 slides", "Stickers en 3 couleurs", "T-shirt technique pour les coureurs"])

tsr += bloc("evenements", "Événements &amp; runs partenaires",
            ["Brunch, pilates, cookies, pizza, run test… chaque run partenaire a son affiche, et avec la nouvelle DA, un gabarit reconnaissable."],
            f"""<div class="avant">
        <div class="g g2">{fig(T + "old_coffee.webp", "Affiche run and coffee, ancienne DA", "", "Run and coffee")}{fig(T + "old_brunch.webp", "Affiche run and brunch, ancienne DA", "", "Run and brunch")}</div>
        <span class="fl" aria-hidden="true">→</span>
        <div class="g g2">{fig(T + "pt_toto.webp", "Annonce run avec Totobello, nouvelle DA", "", "Totobello")}{fig(T + "pt_diago.webp", "Annonce run avec Diago, nouvelle DA", "", "Diago")}{fig(T + "pt_cooks.webp", "Annonce run avec Oh My Cooks, nouvelle DA", "", "Oh My Cooks")}{fig(T + "pt_cooks_offre.webp", "Post offre exclusive Oh My Cooks pour les coureurs", "", "Offre coureurs")}</div>
      </div>
      {note("Avant (2025) et après la nouvelle DA (2026)")}
      <div class="g duo">
        <figure class="feed">{z(T + "pt_hoka.webp", "Story run test Hoka Speedgoat 7 avec Alltricks", "ratio-916")}<figcaption><b>Story run test</b>Hoka x Alltricks : les coureurs testent les Speedgoat 7</figcaption></figure>
        <div class="encart"><h3>Ils ont couru avec nous</h3>{pastilles(["Alltricks", "Hoka", "Chullanka", "Nnormal", "Näak", "Totobello", "Oh My Cooks", "Diago", "Cafés Di Costanzo", "Abuelo", "Waycy", "Kilomètres Dehors", "+ plein d'autres"])}</div>
      </div>""")

cartes = [("Instagram", "2&nbsp;825", "abonnés", "637", "×4,4"), ("Strava", "2&nbsp;016", "membres du club", "435", "×4,6"),
          ("WhatsApp", "661", "membres du groupe", "152", "×4,3"), ("TikTok", "641", "abonnés", "447", "+43 %")]
cc = "".join(f"<div><small>{k}</small><em>{g}</em><strong>{n}</strong><p>{u} en mai 2026, contre {d} en juin 2025</p></div>" for k, n, u, d, g in cartes)
tsr += bloc("communaute", "Communauté",
            ["Instagram, Strava, TikTok, le groupe WhatsApp… j'ai fait vivre chaque canal avec la même énergie, et la communauté a suivi&nbsp;!"],
            f"""<div class="cartes">{cc}</div>
      <div class="g g2" style="align-items:center">
        <div class="encart"><h3>Coureurs par run</h3><div class="stats"><div><strong>3 → ~50</strong><span>des 3 premiers coureurs à environ 50 en moyenne</span></div><div><strong>110+</strong><span>sur les gros événements</span></div></div></div>
        {z(T + "ph_bridge.webp", "Coureurs sur le pont Saint-Pierre", "", "aspect-ratio:4/3;object-fit:cover;object-position:50% 75%")}
      </div>
      <div class="encart"><h3>Stratégie des moyens</h3>
        <div class="colonnes">
          <div><h3>Owned</h3><ul><li>Instagram, TikTok</li><li>Strava, Threads</li><li>WhatsApp, biosite</li><li>Google Business</li></ul></div>
          <div><h3>Earned</h3><ul><li>Partenaires</li><li>Bouche à oreille</li><li>Relais des coureurs</li><li>UGC, presse</li></ul></div>
          <div><h3>Paid</h3><ul><li>Site internet</li><li>Merch</li></ul></div>
        </div>
      </div>""")
tsr += pied(("community-manager.html", "assets/img/cm/df_reel.webp", "Community manager", "center 35%"))
open("toulouse-social-run.html", "w").write(tsr)

# ---------------------------------------------------------------- Community manager
C = "assets/img/cm/"
cm_css = """.ouv.mags { min-height: auto; padding-top: 140px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; align-items: end; }
.ouv.mags::after { display: none; }
.ouv.mags .couv { display: flex; gap: 18px; justify-content: center; align-items: flex-end; }
.ouv.mags .couv img { position: static; width: 46%; height: auto; filter: drop-shadow(0 18px 30px rgba(0,0,0,0.5)); }
.ouv.mags .couv img:first-child { transform: rotate(-4deg); } .ouv.mags .couv img:last-child { transform: rotate(3deg) translateY(-20px); }
@media (max-width: 900px) { .ouv.mags { grid-template-columns: 1fr; } }"""
cm = head("Community manager", "Première alternance de Cloé Pérot : community manager pour De Fil en Déco, O'ptimôme et CFM Radio à Toulouse.", cm_css, classe="cm")
cm += f"""  <div class="ouv mags">
    <div>
      <a class="retour" href="index.html#projets">← Tous les projets</a>
      <h1>Community manager</h1>
      <p class="ex">ma première alternance</p>
      <p class="role">Community manager en alternance, de septembre 2023 à septembre 2024.</p>
    </div>
    <div class="couv">
      <img src="{C}df_n84.webp" alt="Couverture du magazine De Fil en Déco n°84">
      <img src="{C}op_n64.webp" alt="Couverture du magazine O'ptimôme n°64">
    </div>
  </div>
"""
cm += intro("Trois médias toulousains : De Fil en Déco (magazine déco), O'ptimôme (guide des sorties en famille) et CFM Radio (radio locale). Ma première vraie expérience en com, sur trois comptes à la fois&nbsp;!",
            ["Community management", "Social media", "Création de contenus", "Planning éditorial", "Print", "Meta Business Suite"], [])
cm += sommaire([("defilendeco", "De Fil en Déco"), ("optimome", "O'ptimôme")])
cm += bloc("defilendeco", "De Fil en Déco",
           ["Le magazine déco de Toulouse. Sur Instagram, Facebook et LinkedIn, je suivais un modèle de feed précis : des contenus pros et inspirants, avec des formats qui changent."],
           f"""<div class="g g3">
        {fig(C + "df_feed.webp", "Feed Instagram De Fil en Déco", "Feed Instagram", "photos, conseils déco, citations, interviews")}
        {fig(C + "df_reel.webp", "Reel interview d'un peintre sculpteur", "Reel interview", "des portraits d'artisans et de pros", "ratio-916")}
        {fig(C + "df_n84.webp", "Couverture du magazine De Fil en Déco n°84", "Le magazine", "n°84, février 2024", "transp")}
      </div>
      <div class="g g2" style="align-items:center">{z(C + "df_pub_double.webp", "Pub De Fil en Déco en double page", "transp")}{z(C + "df_pub_page.webp", "Pub De Fil en Déco en pleine page", "transp")}</div>
      {note("Pubs print : des pages dans le magazine pour renvoyer les lecteurs vers les réseaux et le site")}""",
           ["Réseaux sociaux via Meta Business Suite", "Formats variés : interviews, conseils, citations", "Pubs print pour faire connaître les réseaux"])
cm += bloc("optimome", "O'ptimôme",
           ["Le guide des familles : des sorties, des spectacles, des idées d'activités… des contenus utiles et pensés pour toute la famille, avec des jeux concours réguliers&nbsp;!"],
           f"""{fig(C + "op_facebook.webp", "Page Facebook O'ptimôme", "Page Facebook", "le canal principal du guide")}
      <div class="g g3" style="align-items:center">
        {fig(C + "op_instagram.webp", "Compte Instagram O'ptimôme", "Instagram", "", "ratio-916")}
        {fig(C + "op_n64.webp", "Couverture du magazine O'ptimôme n°64", "Le magazine", "n°64, printemps 2024", "transp")}
        {fig(C + "op_pub_hiver.webp", "Pub O'ptimôme hiver", "Pub print", "hiver", "transp")}
      </div>
      {fig(C + "op_pub_printemps.webp", "Pub O'ptimôme printemps en double page", "Pub print", "printemps, en double page : une pub par saison pour renvoyer vers le site et Facebook", "transp")}""",
           ["Page Facebook et compte Instagram", "Jeux concours pour animer la communauté", "Pubs print pour faire connaître le site"])
cm += pied(("vancore.html", "assets/img/vancore/cover_van.webp", "Vancore", "center 60%"))
cm = cm.replace('.ouv.mags .couv img { position: static;', '.ouv.mags .couv img { position: static;')
open("community-manager.html", "w").write(cm)

# ---------------------------------------------------------------- Labo
labo_css = """.vide { border: 1px dashed rgba(255,255,255,0.3); border-radius: 22px; padding: clamp(40px, 7vw, 90px) clamp(24px, 4vw, 50px); text-align: center; }
.vide p { color: var(--doux); max-width: 46ch; margin: 14px auto 28px; }
.filtres { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 30px; }
.filtres button { font: 500 15px "Bricolage", sans-serif; color: var(--doux); background: none; border: 1px solid var(--ligne); border-radius: 999px; padding: 8px 16px; cursor: pointer; }
.filtres button[aria-pressed="true"] { background: var(--texte); color: var(--nuit); border-color: var(--texte); }"""
labo = head("Labo", "Projets d'école et projets personnels de Cloé Pérot.", labo_css)
labo += """  <div class="ouv" style="min-height:62svh">
    <img src="assets/img/moi/lac-nuages.webp" alt="" style="object-position:center 45%">
    <a class="retour" href="index.html">← Accueil</a>
    <h1>Labo</h1>
    <p class="role">Mes projets d'école et mes projets perso : là où je teste, je dessine et je m'amuse.</p>
  </div>

  <section>
    <div class="filtres" role="group" aria-label="Filtrer par domaine">
      <button type="button" aria-pressed="true">Tout</button><button type="button" aria-pressed="false">École</button><button type="button" aria-pressed="false">Perso</button>
      <button type="button" aria-pressed="false">Identité visuelle</button><button type="button" aria-pressed="false">Photo &amp; vidéo</button><button type="button" aria-pressed="false">Print</button>
    </div>
    <div class="vide">
      <h2 style="font-size:clamp(32px,4vw,52px)">Le Labo se remplit</h2>
      <p>Mes projets d'école et mes projets perso arrivent ici très bientôt. En attendant, mes projets pro sont à voir.</p>
      <a class="b plein" href="index.html#projets">Voir les projets pro</a>
    </div>
  </section>
"""
labo += pied()
labo = labo.replace('<script src="assets/projet.js"></script>', """<script src="assets/projet.js"></script>
<script>
document.querySelectorAll('.filtres button').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('.filtres button').forEach(x => x.setAttribute('aria-pressed', x === b));
}));
</script>""")
open("labo.html", "w").write(labo)

# ---------------------------------------------------------------- À propos
ap_css = """.bio { display: grid; grid-template-columns: 1.2fr 1fr; gap: clamp(30px, 6vw, 90px); align-items: center; }
.bio p { font-size: clamp(20px, 2vw, 26px); line-height: 1.45; color: #dad8d3; margin: 0 0 22px; }
.bio img { border-radius: 22px; aspect-ratio: 1; object-fit: cover; width: 100%; }
@media (max-width: 900px) { .bio { grid-template-columns: 1fr; } }
.parcours { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(30px, 5vw, 70px); }
.parcours h3 { font-size: 15px; letter-spacing: 0; color: var(--lilas); font-weight: 700; margin-bottom: 8px; }
.parcours ol { list-style: none; margin: 0; padding: 0; }
.parcours li { padding: 18px 0; border-top: 1px solid var(--ligne); }
.parcours li b { display: block; font-size: 19px; line-height: 1.3; }
.parcours li span { color: var(--doux); font-size: 15px; }
.parcours li time { display: block; color: var(--doux); font-size: 14px; margin-bottom: 4px; }
@media (max-width: 900px) { .parcours { grid-template-columns: 1fr; } }
.terrains { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
.terrains div { border: 1px solid var(--ligne); border-radius: 22px; padding: 24px; }
.terrains h3 { font-size: 24px; letter-spacing: -0.03em; margin-bottom: 10px; }
.terrains p { margin: 0; color: var(--doux); }
@media (max-width: 900px) { .terrains { grid-template-columns: 1fr 1fr; } } @media (max-width: 560px) { .terrains { grid-template-columns: 1fr; } }
.univers { display: grid; grid-template-columns: 1fr 1.6fr 1fr; grid-template-rows: 260px 260px; gap: 14px; }
.univers a:nth-child(1) { grid-row: span 2; } .univers a:nth-child(3) { grid-row: span 2; grid-column: 3; } .univers a:nth-child(2) { grid-column: 2; } .univers a:nth-child(4) { grid-column: 2; }
.univers a { height: 100%; } .univers img { height: 100%; object-fit: cover; }
@media (max-width: 700px) { .univers { grid-template-columns: 1fr 1fr; grid-template-rows: 240px 160px 160px; } .univers a:nth-child(n) { grid-row: auto; grid-column: auto; } .univers a:nth-child(1), .univers a:nth-child(3) { grid-row: 1; } .univers a:nth-child(2), .univers a:nth-child(4) { grid-column: span 2; } }
.outils { display: flex; flex-wrap: wrap; gap: 10px; list-style: none; padding: 0; margin: 0; }
.outils li { border: 1px solid var(--ligne); border-radius: 999px; padding: 11px 20px; font-size: 17px; }"""
ap = head("À propos", "Le parcours, les compétences et les outils de Cloé Pérot, chargée de communication à Toulouse.", ap_css)
ap += """  <div class="ouv" style="min-height:62svh">
    <img src="assets/img/moi/lac-braies.webp" alt="" style="object-position:center 60%">
    <a class="retour" href="index.html">← Accueil</a>
    <h1>À propos</h1>
  </div>

  <section class="bio">
    <div>
      <p>Moi, c'est Cloé. Je suis chargée de communication à Toulouse, et je cherche un CDI ici ou dans les Pyrénées.</p>
      <p>Montagne, van et running : j'aime les marques qui ont une vraie communauté, et les faire grandir. Que ce soit sur les réseaux, en print ou sur le terrain.</p>
      <p>Et quand je ne suis pas derrière mon écran, je suis sûrement en rando avec Atlas, mon berger australien.</p>
      <div class="btns"><a class="b plein" href="mailto:cloe.perot@icloud.com">Me contacter</a><a class="b ligne" href="#" title="Bientôt disponible">Mon CV</a></div>
    </div>
    <img src="assets/img/moi/cloe-atlas.webp" alt="Cloé et Atlas, son berger australien, en randonnée dans les Dolomites" style="object-position:62% 40%">
  </section>

  <section>
    <h2>Mon univers</h2>
    <div class="univers">
      <a class="zoom" href="assets/img/moi/atlas-sommets.webp"><img src="assets/img/moi/atlas-sommets.webp" alt="Atlas assis devant les sommets des Dolomites" loading="lazy"></a>
      <a class="zoom" href="assets/img/moi/lac-foret.webp"><img src="assets/img/moi/lac-foret.webp" alt="Lac turquoise entouré de forêt dans les Dolomites" loading="lazy"></a>
      <a class="zoom" href="assets/img/moi/atlas-lac.webp"><img src="assets/img/moi/atlas-lac.webp" alt="Atlas qui fait le beau au bord d'un lac de montagne" loading="lazy"></a>
      <a class="zoom" href="assets/img/moi/lac-nuages.webp"><img src="assets/img/moi/lac-nuages.webp" alt="Lac de montagne sous les nuages" loading="lazy"></a>
    </div>
  </section>

  <section>
    <h2>Mon parcours</h2>
    <div class="parcours">
      <div>
        <h3>Expériences</h3>
        <ol>
          <li><time>2024–2026 · alternance</time><b>Chargée de communication &amp; marketing</b><span>Vancore, ex Mon Fourgon Shop</span></li>
          <li><time>2024–2026 · bénévole</time><b>Chargée de communication &amp; graphiste</b><span>Toulouse Social Run</span></li>
          <li><time>2023–2024 · alternance</time><b>Community manager</b><span>CFM Radio, De Fil en Déco, O'ptimôme</span></li>
        </ol>
      </div>
      <div>
        <h3>Formation</h3>
        <ol>
          <li><time>2024–2026</time><b>Mastère Content Marketing &amp; Brand Entertainment</b></li>
          <li><time>2023–2024</time><b>Bachelor 3 Marketing &amp; Communication Création Digitale</b></li>
          <li><time>2019–2023</time><b>Licence d'Études Anglophones (LLCER)</b></li>
          <li><time>2019</time><b>Baccalauréat Économique &amp; Social</b><span>spécialité Économie approfondie</span></li>
        </ol>
      </div>
    </div>
  </section>

  <section>
    <h2>Mes terrains de jeu</h2>
    <div class="terrains">
      <div><h3>Social media</h3><p>Stratégie, contenus, communauté</p></div>
      <div><h3>Création graphique</h3><p>Identité visuelle, print, digital</p></div>
      <div><h3>Influence &amp; affiliation</h3><p>Partenariats, contrats, suivi</p></div>
      <div><h3>Photo &amp; vidéo</h3><p>Shooting, retouche, montage</p></div>
      <div><h3>Rédaction web &amp; SEO</h3><p>Articles, pages web, emailing</p></div>
      <div><h3>Com interne &amp; événementiel</h3><p>Supports, team building, salons</p></div>
    </div>
  </section>

  <section>
    <h2>Mes outils</h2>
    <ul class="outils"><li>Adobe Creative Cloud</li><li>Canva</li><li>Figma</li><li>WordPress</li><li>CapCut</li><li>Asana</li><li>Google Analytics</li><li>Meta Business Suite</li><li>Klaviyo</li></ul>
  </section>
"""
ap += pied()
open("a-propos.html", "w").write(ap)
print("ok")
