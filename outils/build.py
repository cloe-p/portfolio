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
  <div class="fondtexte" aria-hidden="true">Com · Contenu · Communauté · Com · Contenu · Communauté ·&nbsp;</div>
  <svg class="tampon" viewBox="0 0 150 150" aria-hidden="true"><defs><path id="cercle" d="M75,75 m-58,0 a58,58 0 1,1 116,0 a58,58 0 1,1 -116,0"/></defs><text><textPath href="#cercle" textLength="360" lengthAdjust="spacing">DISPO POUR UN CDI · TOULOUSE · PYRÉNÉES ·</textPath></text></svg>
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
<script src="assets/pied.js"></script>
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
LABO = [
    ("Nicolas Dupré", "Logo pour un ingénieur en mécanique", "Le E de engineer, serré dans un écrou : un clin d'œil à son métier, avec son nom en couronne autour.", "logo-nicolas-dupre"),
    ("Digiconcept", "Logo pour une société de services numériques", "La balise de code au cœur d'un motif pixelisé, dans le bleu choisi par la société.", "logo-digiconcept"),
    ("Bat Inn", "Logo pour un installateur VELUX", "Le nom tient dans une maison : le « t » sert de cheminée, et le toit rouge rappelle son métier.", "logo-bat-inn"),
    ("Cabinet S·D", "Logo pour une infirmière libérale", "Le bâton d'Esculape, symbole du soin, s'enroule autour de ses initiales.", "logo-sd-infirmiere"),
]
labo_css = """.logos-grille { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; }
.logos-grille figure { margin: 0; }
.logos-grille .zoom { position: relative; background: #fff; border-radius: 22px; aspect-ratio: 4 / 3; }
.logos-grille .zoom img { position: absolute; inset: 14%; width: 72%; height: 72%; object-fit: contain; }
.logos-grille .zoom:hover img { transform: scale(1.04); }
.logos-grille figcaption { margin-top: 14px; }
.logos-grille figcaption b { font-size: 22px; letter-spacing: -0.02em; }
.logos-grille figcaption small { display: block; color: var(--lilas); font-size: 14px; margin: 2px 0 6px; }
.chap { display: flex; justify-content: space-between; align-items: end; gap: 20px; flex-wrap: wrap; margin-bottom: 30px; }
.chap h2 { font-size: clamp(36px, 4.4vw, 60px); }
.chap p { color: var(--doux); margin: 0; max-width: 46ch; }
.bientot { margin-top: 70px; border: 1px dashed rgba(255,255,255,0.3); border-radius: 22px; padding: 30px; color: var(--doux); text-align: center; }
@media (max-width: 640px) { .logos-grille { grid-template-columns: 1fr; } }"""
labo_css += """
.filtres { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 50px; }
.filtres button { font: 500 15px "Bricolage", sans-serif; color: var(--doux); background: none; border: 1px solid var(--ligne); border-radius: 999px; padding: 10px 18px; cursor: pointer; min-height: 44px; }
.filtres button[aria-pressed="true"] { background: var(--texte); color: var(--nuit); border-color: var(--texte); }
.projet-labo { scroll-margin-top: 110px; padding-bottom: 80px; margin-bottom: 80px; border-bottom: 1px solid var(--ligne); }
.projet-labo[hidden] { display: none; }
.etiquettes { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 14px; }
.etiquettes span { font-size: 13px; font-weight: 700; border-radius: 999px; padding: 5px 12px; background: var(--lilas); color: var(--nuit); }
.etiquettes span + span { background: none; color: var(--doux); border: 1px solid var(--ligne); }
.ikea-avant { display: grid; grid-template-columns: 1fr auto 2fr; gap: 16px; align-items: center; margin-bottom: 16px; }
.ikea-avant .fl { font-size: 32px; color: var(--lilas); }
.g-pages { display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-top: 14px; }
.g-pages .zoom img, .ikea-avant .zoom img { aspect-ratio: 16 / 9; object-fit: cover; }
.charte-ikea { display: flex; flex-wrap: wrap; gap: 26px; align-items: center; margin: 26px 0; color: var(--doux); font-size: 15px; }
.charte-ikea i { display: inline-block; width: 28px; height: 28px; border-radius: 50%; vertical-align: middle; margin-right: 8px; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.2); }
.podcast { display: grid; grid-template-columns: minmax(0, 340px) 1fr; gap: clamp(24px, 4vw, 56px); align-items: center; }
.podcast > img { width: 100%; aspect-ratio: 1; object-fit: cover; border-radius: 22px; }
.lecteur { display: flex; align-items: center; gap: 18px; margin-top: 26px; max-width: 520px; }
.lecteur button { flex: none; width: 64px; height: 64px; border-radius: 50%; border: 0; background: var(--lilas); color: var(--nuit); font-size: 22px; cursor: pointer; display: grid; place-items: center; transition: scale 0.2s; }
.lecteur button:hover { scale: 1.06; }
.lecteur .barre { flex: 1; height: 6px; border-radius: 6px; background: rgba(255,255,255,0.14); cursor: pointer; position: relative; }
.lecteur .barre i { position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 6px; background: var(--lilas); }
.lecteur time { color: var(--doux); font-size: 14px; font-variant-numeric: tabular-nums; white-space: nowrap; }
.accroche-bfc { line-height: 1.15; margin: 0 0 40px; font-size: clamp(24px, 2.6vw, 36px); font-weight: 700; letter-spacing: -0.03em; color: var(--lilas); max-width: 30ch; }
.etapes-bfc { list-style: none; margin: 0 0 40px; padding: 0; display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px; counter-reset: e; }
.etapes-bfc li { counter-increment: e; border-top: 2px solid var(--lilas); padding-top: 14px; }
.etapes-bfc li::before { content: counter(e); display: block; color: var(--lilas); font-weight: 700; font-size: 14px; margin-bottom: 6px; }
.etapes-bfc b { display: block; font-size: 19px; margin-bottom: 6px; }
.etapes-bfc span { color: var(--doux); font-size: 14px; line-height: 1.45; display: block; }
.chiffres-bfc { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--ligne); border: 1px solid var(--ligne); border-radius: 22px; overflow: hidden; margin-bottom: 40px; }
.chiffres-bfc div { background: var(--nuit); padding: 24px; }
.chiffres-bfc strong { display: block; font-size: clamp(36px, 3.6vw, 52px); font-weight: 800; letter-spacing: -0.05em; line-height: 1; }
.chiffres-bfc span { display: block; color: var(--doux); font-size: 14px; margin-top: 10px; }
.canaux-bfc h3 { font-size: clamp(24px, 2.4vw, 32px); margin-bottom: 14px; }
.canaux-bfc ul { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--ligne); }
.canaux-bfc li { display: grid; grid-template-columns: 200px 1fr; gap: 20px; padding: 14px 0; border-bottom: 1px solid var(--ligne); color: var(--doux); }
.canaux-bfc li b { color: var(--texte); }
@media (max-width: 900px) { .etapes-bfc { grid-template-columns: 1fr 1fr; } .chiffres-bfc { grid-template-columns: 1fr 1fr; } }
@media (max-width: 560px) { .etapes-bfc, .chiffres-bfc { grid-template-columns: 1fr; } .canaux-bfc li { grid-template-columns: 1fr; gap: 2px; } }
.equipe { color: var(--doux); font-size: 14px; margin: -14px 0 24px; }
.equipe::before { content: ""; display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: var(--lilas); margin-right: 8px; vertical-align: 1px; }
.duo-labo { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
.duo-labo .zoom { background: var(--fond-img, #f8f6f2); }
.duo-labo .zoom img { aspect-ratio: 16 / 9; object-fit: contain; }
.g-libre { columns: 2; column-gap: 14px; margin-top: 14px; }
.vitrine + .g-libre, .chap + .g-libre { margin-top: 14px; }
.g-libre .zoom { break-inside: avoid; margin-bottom: 14px; }
@media (max-width: 640px) { .g-libre { columns: 1; } }
.bref { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
.bref .zoom img, .citation-rb { aspect-ratio: 16 / 10; object-fit: cover; }
.bref h3 { font-size: 24px; letter-spacing: -0.03em; margin: 4px 0 8px; }
.bref p { color: var(--doux); font-size: 15px; margin: 0 0 14px; }
.bref .etiquettes { margin: 16px 0 6px; }
.bref .equipe { margin: 0; }
.citation-rb { border-radius: 14px; background: #1d2a7a; color: #f9c80e; display: grid; place-items: center; padding: 24px; text-align: center; font-weight: 800; font-size: clamp(20px, 2vw, 26px); letter-spacing: -0.03em; line-height: 1.15; }
.gam { display: grid; grid-template-columns: 1fr; gap: 30px; align-items: center; margin: 50px 0 16px; padding-top: 40px; border-top: 1px solid var(--ligne); }
.gam h3 { font-size: clamp(26px, 2.6vw, 36px); margin-bottom: 12px; }
.gam > div > p { color: var(--doux); margin: 0 0 22px; }
.gam .zoom { background: #f6f5f2; max-width: 260px; justify-self: center; }
.stats-gam { display: flex; gap: 30px; flex-wrap: wrap; margin-bottom: 22px; }
.stats-gam strong { display: block; font-size: clamp(30px, 3vw, 42px); font-weight: 800; letter-spacing: -0.05em; color: var(--lilas); line-height: 1; }
.stats-gam span { color: var(--doux); font-size: 14px; }
@media (max-width: 900px) { .bref { grid-template-columns: 1fr; } .gam { grid-template-columns: 1fr; } }
@media (max-width: 640px) { .duo-labo { grid-template-columns: 1fr; } }
.chap > div { max-width: 52ch; }
.brief { color: #d3d1cc; margin: 0 0 14px; }
.brief b { color: var(--texte); }
.competences { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }
.competences li { border: 1px solid var(--ligne); border-radius: 999px; padding: 5px 12px; font-size: 13px; color: var(--doux); }
.vitrine { background: var(--v); border-radius: 22px; padding: clamp(28px, 6vw, 80px); display: flex; justify-content: center; align-items: center; gap: clamp(20px, 5vw, 70px); margin-top: 26px; }
.vitrine .zoom { background: transparent; max-width: 520px; }
.vitrine .zoom img { max-height: 340px; width: auto; max-width: 100%; margin: auto; }
.evo { display: grid; grid-template-columns: 1fr auto 1.6fr; gap: clamp(12px, 3vw, 32px); align-items: end; margin-top: 26px; }
.evo figure { margin: 0; }
.evo .vitrine { margin-top: 0; padding: clamp(22px, 4vw, 48px); }
.evo .vitrine .zoom img { max-height: 200px; }
.evo-avant .zoom img { aspect-ratio: 16 / 10.4; object-fit: cover; border-radius: 22px; }
.evo figcaption, .rang figcaption, .carrousel figcaption { margin-top: 10px; color: var(--doux); font-size: 14px; }
.evo .fl { font-size: 34px; color: var(--lilas); align-self: center; }
.evo figcaption { font-weight: 600; }
.rang { display: grid; grid-template-columns: var(--a); gap: 14px; margin-top: 14px; align-items: start; }
.rang figure, .carrousel { margin: 0; }
.carrousel { margin-top: 14px; }
.piste-c { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
@media (max-width: 760px) { .evo { grid-template-columns: 1fr; } .evo .fl { transform: rotate(90deg); justify-self: center; } .rang { grid-template-columns: 1fr; } .piste-c { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; } .piste-c .zoom { flex: 0 0 72%; scroll-snap-align: start; } }
.duo-photos { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 26px; }
.duo-photos .zoom img { aspect-ratio: 16 / 10; object-fit: cover; }
.ecrans { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; align-items: start; }
.ecrans .zoom { background: #0f0f1a; }
@media (max-width: 760px) { .ecrans { grid-template-columns: 1fr 1fr; } .duo-photos { grid-template-columns: 1fr; } .vitrine { flex-direction: column; } }
@media (max-width: 760px) { .podcast { grid-template-columns: 1fr; } .podcast > img { max-width: 320px; } .ikea-avant { grid-template-columns: 1fr; } .ikea-avant .fl { display: none; } .g-pages { grid-template-columns: 1fr; } }"""
labo = head("Labo", "Projets d'école et projets perso de Cloé Pérot : identités visuelles, stratégies, social ads, site web, podcast.", labo_css)
cartes = "".join(f"""
      <figure>{z("assets/img/labo/" + f + ".webp", "Logo " + n)}<figcaption><b>{n}</b><small>{t}</small>{d}</figcaption></figure>""" for n, t, d, f in LABO)
I = "assets/img/labo/ikea/"
pages = lambda xs: "".join(z(I + x + ".webp", a) for x, a in xs)
labo += f"""  <div class="ouv" style="min-height:62svh">
    <img src="assets/img/moi/lac-nuages.webp" alt="" style="object-position:center 45%">
    <a class="retour" href="index.html">← Accueil</a>
    <h1>Labo</h1>
    <p class="role">Mes projets d'école et mes projets perso : là où je teste, je dessine et je m'amuse.</p>
  </div>

  <section>
    <div class="filtres" role="group" aria-label="Filtrer les projets">
      <button type="button" aria-pressed="true" data-f="tout">Tout</button>
      <button type="button" aria-pressed="false" data-f="identite">Identité visuelle</button>
      <button type="button" aria-pressed="false" data-f="strategie">Stratégie &amp; social ads</button>
      <button type="button" aria-pressed="false" data-f="web">Web &amp; podcast</button>
      <button type="button" aria-pressed="false" data-f="perso">Projets perso</button>
    </div>

    <article class="projet-labo" data-cat="identite" id="ikea">
      <div class="etiquettes"><span>École</span><span>Identité visuelle</span></div>
      <div class="chap"><h2>IKEA, version psychédélique</h2><div><p class="brief"><b>Le brief :</b> retravailler l'identité visuelle d'une marque et sa communication selon un courant artistique. J'ai choisi le rétro-psychédélique des années 70, mêlé au bubble street art.</p><ul class="competences"><li>Identité visuelle</li><li>Logo</li><li>Direction artistique</li><li>Print</li><li>Social media</li></ul></div></div>
      <div class="evo"><figure class="evo-avant">{z("assets/img/labo/ikea/avant.webp", "Le logo IKEA d'origine, lettres bleues dans un ovale jaune")}<figcaption>Le logo d'origine</figcaption></figure><span class="fl" aria-hidden="true">→</span><figure class="evo-apres"><div class="vitrine" style="--v:#ffd900">{z("assets/img/labo/ikea/logo-png.webp", "Le nouveau logo IKEA, lettres fluides bleues dans un contour noir")}{z("assets/img/labo/ikea/fleur-png.webp", "Le logotype fleur")}</div><figcaption>Notre évolution</figcaption></figure></div>
      <div class="rang" style="--a:1.304fr 0.563fr">{fig("assets/img/labo/ikea/abribus-chaise.webp", "Affiche d'abribus : Votre future obsession ? Fauteuil SOLSTÄLE", "Affichage abribus")}{fig("assets/img/labo/ikea/story-salon.webp", "Story Instagram : un salon rétro, produits entourés de jaune et de bleu", "Story Instagram")}</div>
      <figure class="carrousel"><div class="piste-c">{z("assets/img/labo/ikea/carrousel-1.webp", "Slide CHATMÖ : un chat sur un coussin vert")}{z("assets/img/labo/ikea/carrousel-2.webp", "Slide DOGVIK : un bouledogue à côté d'un fauteuil orange")}{z("assets/img/labo/ikea/carrousel-3.webp", "Slide DOGVIK : un bouledogue français sur un fauteuil vert")}{z("assets/img/labo/ikea/carrousel-4.webp", "Slide CHATMÖ : un chat roux sur un fauteuil bleu nuit")}{z("assets/img/labo/ikea/carrousel-5.webp", "Slide DOGVIK : un berger dans un salon lumineux")}</div><figcaption><b>Carrousel Instagram</b></figcaption></figure>
      <div class="rang" style="--a:0.706fr 1.778fr">{fig("assets/img/labo/ikea/pub-catalogue.webp", "Publicité catalogue : FLOCRA et ENIDTH dans une entrée vert sauge", "Publicité")}{fig("assets/img/labo/ikea/carton-notice.webp", "Carton IKEA et notice de montage, annotés de formes jaunes", "Carton et notice")}</div>
    </article>

    <article class="projet-labo" data-cat="identite" id="matp">
      <div class="etiquettes"><span>École</span><span>Identité visuelle</span></div>
      <div class="chap"><h2>Musée des Arts et Traditions Populaires</h2><div><p class="brief"><b>Le brief :</b> créer l'identité d'un musée parisien et la communication de son inauguration. Le « A » central rappelle l'Arc de Triomphe et la tour Eiffel, entre patrimoine et design contemporain.</p><ul class="competences"><li>Logo</li><li>Charte graphique</li><li>Affiche</li><li>Social media</li><li>Goodies</li></ul></div></div>
      <div class="vitrine" style="--v:#fff">{z("assets/img/labo/matp/logo-png.webp", "Le logo MATP")}</div><div class="g-libre">{z("assets/img/labo/matp/story.webp", "Story Instagram de l'inauguration du 8 novembre")}{z("assets/img/labo/matp/banniere.webp", "Bannière Facebook de l'inauguration")}{z("assets/img/labo/matp/casquette.webp", "Casquette aux couleurs du musée")}</div>
    </article>

    <article class="projet-labo" data-cat="identite strategie" id="hyros" style="--fond-img:#000">
      <div class="etiquettes"><span>École</span><span>Lancement de produit</span></div>
      <div class="chap"><h2>Hyros, la Tesla à hydrogène</h2><div><p class="brief"><b>Le brief :</b> lancer le premier véhicule à hydrogène de Tesla : trouver le nom, créer le logotype, imaginer le modèle et construire toute la campagne de lancement.</p><ul class="competences"><li>Naming</li><li>Logotype</li><li>Visuels IA</li><li>Newsletter</li><li>Magazine</li><li>Carrousel</li></ul></div></div>
      <div class="vitrine" style="--v:#000">{z("assets/img/labo/hyros/nom.webp", "Le nom HYROS")}</div><div class="g-libre">{z("assets/img/labo/hyros/voiture.webp", "Le modèle Hyros, généré par IA")}{z("assets/img/labo/hyros/magazine-couv.webp", "Couverture de magazine pour le lancement")}{z("assets/img/labo/hyros/carrousel-1.webp", "Visuel du carrousel Instagram")}{z("assets/img/labo/hyros/newsletter-hd.webp", "La newsletter de lancement Model Hyros")}</div>
    </article>

    <article class="projet-labo" data-cat="identite strategie" id="kinetic">
      <div class="etiquettes"><span>École</span><span>Branding</span></div>
      <div class="chap"><h2>Kinetic, ex Sparks</h2><div><p class="brief"><b>Le brief :</b> un vrai client, une startup de bien-être et de performance en entreprise, à qui il fallait un nouveau projet de marque : nom, identité, stratégie digitale et pitch.</p><ul class="competences"><li>Naming</li><li>Brandbook</li><li>Stratégie digitale</li><li>Maquettes app & site</li></ul></div></div>
      <div class="vitrine" style="--v:#fff">{z("assets/img/labo/kinetic/logo.webp", "Le logo Kinetic")}</div><div class="g-libre">{z("assets/img/labo/kinetic/mockups.webp", "Kinetic sur une montre, une casquette, des tote bags et une gourde")}{z("assets/img/labo/kinetic/site.webp", "Le site web Kinetic")}{z("assets/img/labo/kinetic/app.webp", "Les écrans de l'application")}</div>
    </article>

    <article class="projet-labo" data-cat="strategie" id="pgw">
      <div class="etiquettes"><span>École</span><span>Social ads</span></div>
      <div class="chap"><h2>Paris Games Week 2027</h2><div><p class="brief"><b>Le brief :</b> passer de 42 % à 60 % de billets vendus un mois avant le salon, avec une stratégie publicitaire sur TikTok, Meta et Twitch.</p><ul class="competences"><li>Social ads</li><li>Funnel</li><li>Hooks</li><li>Brief créatif</li><li>Création d'assets</li></ul></div></div>
      <div class="g-libre">{z("assets/img/labo/pgw/stories.webp", "Story interactive et visuel « Le mode solo est mort »")}{z("assets/img/labo/pgw/miniatures.webp", "Miniature YouTube et overlay Twitch")}{z("assets/img/labo/pgw/lead-ads.webp", "Lead ads et formulaire de préinscription")}</div>
    </article>

    <article class="projet-labo" data-cat="web" id="pawtes">
      <div class="etiquettes"><span>École</span><span>Site web</span></div>
      <div class="chap"><h2>Entre Pawtes</h2><div><p class="brief"><b>Le brief :</b> créer et animer le site d'une crèche pour chiens à Toulouse, du design aux textes.</p><ul class="competences"><li>Webdesign</li><li>Rédaction web</li><li>Animation</li><li>WordPress</li></ul></div></div>
      <div class="g-libre">{z("assets/img/labo/pawtes/accueil.webp", "Accueil du site Entre Pawtes : Crèche de toutous à Toulouse")}{z("assets/img/labo/pawtes/apropos.webp", "Section À propos avec une mosaïque de chiens")}{z("assets/img/labo/pawtes/faq.webp", "Questions de pawtes : la FAQ en accordéon")}</div>
    </article>

    <article class="projet-labo" data-cat="strategie" id="bfc">
      <div class="etiquettes"><span>École</span><span>Stratégie & gamification</span></div>
      <div class="chap"><h2>Book, Food &amp; Créa</h2><div><p class="brief"><b>Le brief :</b> lancer à Toulouse une expérience de 3 heures pour les femmes de 18 à 35 ans : un livre, un moment gourmand et un atelier créatif, pour créer du lien. On a étudié le marché, construit la stratégie et le plan de com, puis imaginé une appli pour donner envie de revenir.</p><ul class="competences"><li>Étude de marché</li><li>Stratégie marketing</li><li>Plan de communication</li><li>Fidélisation</li><li>Gamification</li></ul></div></div>
      <div class="duo-photos">{z("assets/img/labo/bfc/photo-aquarelle.webp", "Atelier aquarelle, des fleurs peintes à la main")}{z("assets/img/labo/bfc/photo-atelier.webp", "Pinceaux et pots de peinture dans un atelier")}</div><div class="gam"><div><h3>Le Jardin Créatif, l'appli du projet</h3><p>Chaque participante fait pousser un jardin grâce à des petits défis du quotidien : lire 5 pages, prendre son petit-déj en photo, dessiner en 60 secondes. Une plante par pilier, Book, Food et Créa, et la récolte ne se débloque qu'en revenant à un atelier.</p></div></div><div class="ecrans">{z("assets/img/labo/bfc/app-jardin.webp", "Le jardin et les défis du jour")}{z("assets/img/labo/bfc/app-boutique.webp", "La boutique XP")}{z("assets/img/labo/bfc/app-evenements.webp", "La réservation des ateliers")}{z("assets/img/labo/bfc/app-scan.webp", "L'espace organisatrice pour valider les récoltes")}</div>
    </article>

    <article class="projet-labo" data-cat="strategie" id="dab">
      <div class="etiquettes"><span>École</span><span>Concept de marque</span></div>
      <div class="chap"><h2>Le DAB</h2><div><p class="brief"><b>Le brief :</b> imaginer une marque : une épicerie le jour, un distributeur la nuit, rempli de produits créés par les créateurs de contenu food.</p><ul class="competences"><li>Concept</li><li>Plateforme de marque</li><li>Ton</li><li>Stratégie de canaux</li></ul></div></div>
      <div class="g-libre">{z("assets/img/labo/dab/marque.webp", "Le DAB, distributeur à bouffe")}{z("assets/img/labo/dab/produits.webp", "Les produits de créateurs")}</div>
    </article>

    <article class="projet-labo" data-cat="web" id="podcast">
      <div class="etiquettes"><span>École</span><span>Podcast</span></div>
      <div class="podcast">
        <img src="assets/img/labo/podcast-cover.webp" alt="Pochette du podcast Les clés du voisin by Airbnb : un chalet en A dans la forêt">
        <div>
          <h2 style="font-size:clamp(36px,4.4vw,60px)">Les clés du voisin</h2>
          <p style="color:var(--doux);max-width:46ch;margin:16px 0 0">Un podcast imaginé pour Airbnb : la pochette, l'écriture et le montage. Mets le son !</p>
          <div class="lecteur">
            <button type="button" id="lire" aria-label="Écouter le podcast">▶</button>
            <div class="barre" id="barre" role="progressbar" aria-label="Progression"><i></i></div>
            <time id="temps">0:00 / 0:43</time>
          </div>
          <audio id="audio" src="assets/audio/les-cles-du-voisin.mp3" preload="metadata"></audio>
        </div>
      </div>
    </article>

    <article class="projet-labo" data-cat="strategie" id="bref">
      <div class="chap"><h2>Et aussi, en bref</h2><p>Des projets plus courts, menés en cours.</p></div>
      <div class="bref">
        <div>
          {z("assets/img/labo/autres/3soeurs-photo.webp", "Brunch au Trois Sœurs Café")}
          <div class="etiquettes"><span>Fidélisation</span></div>
          <h3>Trois Sœurs Café</h3>
          <p>Un programme de fidélité pour un café toulousain : 1 € = 1 point, des récompenses du café offert au brunch, des points gagnés sur Instagram et Google, et les données à collecter.</p>
        </div>
        <div>
          {z("assets/img/labo/autres/mariage-coffret.webp", "Le coffret Théâtre des Sens et sa carte signée")}
          <div class="etiquettes"><span>Brand content</span></div>
          <h3>Mariage Frères × Pierre Niney</h3>
          <p>Un coffret de 4 thés en édition limitée, « Théâtre des Sens », co-signé par l'acteur, avec une carte et une playlist en QR code. Plus l'événement de lancement et la pub TV.</p>
        </div>
        <div>
          {z("assets/img/labo/autres/redbull-kiosque-limitless.webp", "Affiche LIMITLESS Red Bull en situation sur un kiosque")}
          <div class="etiquettes"><span>Storytelling</span></div>
          <h3>Red Bull, #NouvellesAiles</h3>
          <p>Une campagne « LIMITLESS » qui raconte le parcours d'un pilote, du karting à Monaco jusqu'à Red Bull Racing : affiches, court-métrage, campagne digitale et événement immersif.</p>
        </div>
      </div>
    </article>

    <article class="projet-labo" data-cat="perso identite" id="logos" style="border:0">
      <div class="etiquettes"><span>Perso</span><span>Logos</span></div>
      <div class="chap">
        <h2>Des logos pour des proches</h2>
        <p>Des identités créées pour les petites entreprises de mon entourage. À chaque fois, je pars du métier pour trouver le symbole.</p>
      </div>
      <div class="logos-grille">{cartes}
      </div>
    </article>

  </section>
"""
labo += pied()
labo = labo.replace('<script src="assets/pied.js"></script>', """<script src="assets/pied.js"></script>
<script>
{
  const bts = document.querySelectorAll('.filtres button');
  bts.forEach(b => b.addEventListener('click', () => {
    bts.forEach(x => x.setAttribute('aria-pressed', x === b));
    document.querySelectorAll('.projet-labo').forEach(p => p.hidden = !(b.dataset.f === 'tout' || p.dataset.cat.split(' ').includes(b.dataset.f)));
  }));
  const au = document.getElementById('audio'), bt = document.getElementById('lire'), barre = document.getElementById('barre'), t = document.getElementById('temps');
  const mmss = s => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  bt.addEventListener('click', () => au.paused ? au.play() : au.pause());
  au.addEventListener('play', () => { bt.textContent = '❚❚'; bt.setAttribute('aria-label', 'Mettre en pause'); });
  au.addEventListener('pause', () => { bt.textContent = '▶'; bt.setAttribute('aria-label', 'Écouter le podcast'); });
  au.addEventListener('timeupdate', () => { const d = au.duration || 43; barre.firstElementChild.style.width = (au.currentTime / d * 100) + '%'; t.textContent = mmss(au.currentTime) + ' / ' + mmss(d); });
  barre.addEventListener('click', e => { const r = barre.getBoundingClientRect(); if (au.duration) au.currentTime = (e.clientX - r.left) / r.width * au.duration; });
}
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
    <h2>Une com qui donne envie de sortir.</h2>
    <p style="color:var(--doux);margin:-18px 0 30px;max-width:52ch">Le van, la montagne, le running : mes projets parlent tous de grand air. Et ça tombe bien, c'est là que je me sens chez moi.</p>
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
    <h2>Mes spécialités</h2>
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
