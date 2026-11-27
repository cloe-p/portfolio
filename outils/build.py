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
  <a class="nom" href="index.html">Mon Portfolio</a>
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
  <svg class="tampon" viewBox="0 0 150 150" aria-hidden="true"><defs><path id="cercle" d="M75,75 m-58,0 a58,58 0 1,1 116,0 a58,58 0 1,1 -116,0"/></defs><text><textPath href="#cercle" textLength="360" lengthAdjust="spacing">DISPO · POSTE EN COM · TOULOUSE · PYRÉNÉES ·</textPath></text></svg>
  <h2>On en parle ?</h2>
  <div class="btns"><a class="b plein" href="mailto:cloe.perot@icloud.com">cloe.perot@icloud.com</a><a class="b ligne" href="#" title="Bientôt disponible">Télécharger mon CV</a><a class="b ligne" href="https://www.linkedin.com/in/cloeperot/" target="_blank" rel="noopener">LinkedIn ↗</a></div>
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
tsr += ouverture(T + "couverture-groupe.webp", "Toulouse Social Run", "le running club qui court ensemble",
                 "Chargée de communication &amp; graphiste, bénévole, de 2024 à 2026.", "center 45%")
tsr = tsr.replace('<a class="retour" href="index.html#projets">', '<img class="sticker-ouv" src="assets/img/tsr/sticker_tsr.webp" alt="" aria-hidden="true">\n    <a class="retour" href="index.html#projets">', 1)
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
            + '<div class="encart formats"><h3>Nos formats</h3>' + pastilles(["Run &amp; brunch", "Run &amp; pilates", "Run &amp; cookies", "Run &amp; café", "Run pizza", "Run test", "et plein d'autres"]) + "</div>")

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
tsr += pied(("community-manager.html", "assets/img/cm/salon-deco.webp", "De Fil en Déco, O'ptimôme &amp; CFM Radio", "center 50%"))
open("toulouse-social-run.html", "w").write(tsr)

# ---------------------------------------------------------------- Community manager
C = "assets/img/cm/"
cm_css = """.ouv.mags { min-height: auto; padding-top: 140px; display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; align-items: end; }
.ouv.mags::after { display: none; }
.ouv.mags .couv { display: flex; gap: 18px; justify-content: center; align-items: flex-end; }
.ouv.mags .couv img { position: static; width: 46%; height: auto; filter: drop-shadow(0 18px 30px rgba(0,0,0,0.5)); }
.ouv.mags .couv img:first-child { transform: rotate(-4deg); } .ouv.mags .couv img:last-child { transform: rotate(3deg) translateY(-20px); }
@media (max-width: 900px) { .ouv.mags { grid-template-columns: 1fr; } }"""
cm = head("De Fil en Déco, O'ptimôme & CFM Radio", "Première alternance de Cloé Pérot : community manager pour De Fil en Déco et O'ptimôme à Toulouse, et CFM Radio à Montauban.", cm_css, classe="cm")
cm += f"""  <div class="ouv mags">
    <div>
      <a class="retour" href="index.html#projets">← Tous les projets</a>
      <h1>De Fil en Déco, O'ptimôme &amp; CFM Radio</h1>
      <p class="ex">ma première alternance et mes premiers pas dans la communication</p>
      <p class="role">Community manager en alternance, de septembre 2023 à septembre 2024.</p>
    </div>
    <div class="couv">
      <img src="{C}df_n84.webp" alt="Couverture du magazine De Fil en Déco n°84">
      <img src="{C}op_n64.webp" alt="Couverture du magazine O'ptimôme n°64">
    </div>
  </div>
"""
cm += intro("Trois médias locaux : De Fil en Déco (magazine déco) et O'ptimôme (guide des sorties en famille) à Toulouse, et CFM Radio à Montauban. Ma première vraie expérience en com, sur trois comptes à la fois&nbsp;!",
            ["Community management", "Social media", "Création de contenus", "Planning éditorial", "Print", "Meta Business Suite"], [])
cm += sommaire([("defilendeco", "De Fil en Déco"), ("optimome", "O'ptimôme"), ("cfm", "CFM Radio")])
cm += bloc("defilendeco", "De Fil en Déco",
           ["Le magazine déco de Toulouse. J'y gérais toute la com digitale : les réseaux, le site, la fiche Google et l'emailing, avec un modèle de feed précis, des contenus pros et inspirants, et des formats qui changent.", "Sur le terrain aussi : photos, vidéos et interviews d'artisans, et la com pendant les événements du magazine."],
           f"""<div class="g df-haut">
        {fig(C + "df_feed.webp", "Feed Instagram De Fil en Déco", "Feed Instagram", "photos, conseils déco, citations, interviews")}
        <div class="reels itv"><figure><div class="vid"><video class="reel" src="assets/video/itv_julie.mp4" poster="assets/img/cm/poster_itv_julie.webp" autoplay muted loop playsinline preload="metadata" aria-label="Interview vidéo de Julie Delvaux pour De Fil en Déco"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Interview</b>Julie Delvaux</figcaption></figure>
        <figure><div class="vid"><video class="reel" src="assets/video/itv_maxime.mp4" poster="assets/img/cm/poster_itv_maxime.webp" autoplay muted loop playsinline preload="metadata" aria-label="Interview vidéo de Maxime Jordan pour De Fil en Déco"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Interview</b>Maxime Jordan</figcaption></figure></div>
        {fig(C + "df_n84.webp", "Couverture du magazine De Fil en Déco n°84", "Le magazine", "n°84, février 2024", "transp")}
      </div>
      <div class="g g2 pubs" style="align-items:center">{z(C + "df_pub_double.webp", "Pub De Fil en Déco en double page", "transp")}{z(C + "df_pub_page.webp", "Pub De Fil en Déco en pleine page", "transp")}</div>
      {note("Pubs print : des pages dans le magazine pour renvoyer les lecteurs vers les réseaux et le site")}""",
           ["<b>Réseaux sociaux</b> : calendrier éditorial, création et rédaction des posts sur Instagram, Facebook et LinkedIn", "<b>Vidéo</b> : tournage et montage des interviews sur Premiere Pro et CapCut", "<b>Photo</b> : prises de vue et retouche", "<b>Site internet</b> : mise en ligne des articles", "<b>Fiche Google</b> : posts et articles", "<b>Emailing</b> : campagnes sur Brevo", "<b>Événements</b> : la com en direct", "<b>Visuels</b> : posts, pubs print pour faire connaître les réseaux"])
cm += bloc("optimome", "O'ptimôme",
           ["Le guide des familles : des sorties, des spectacles, des idées d'activités… des contenus utiles et pensés pour toute la famille.", "J'ai lancé son compte Instagram, animé la communauté avec des jeux concours réguliers et tenu le site à jour avec les articles et l'agenda des sorties."],
           f"""<div class="op-fb">{fig(C + "op_facebook.webp", "Page Facebook O'ptimôme", "Page Facebook", "le canal principal du guide")}</div>
      <div class="g g3" style="align-items:center">
        {fig(C + "op_instagram.webp", "Compte Instagram O'ptimôme", "Instagram", "", "ratio-916")}
        {fig(C + "op_n64.webp", "Couverture du magazine O'ptimôme n°64", "Le magazine", "n°64, printemps 2024", "transp")}
        {fig(C + "op_pub_hiver.webp", "Pub O'ptimôme hiver", "Pub print", "hiver", "transp")}
      </div>
      <div class="pub-double">{fig(C + "op_pub_printemps.webp", "Pub O'ptimôme printemps en double page", "Pub print", "printemps, en double page : une pub par saison pour renvoyer vers le site et Facebook", "transp")}</div>""",
           ["<b>Instagram</b> : création du compte", "<b>Réseaux sociaux</b> : création des posts sur Facebook et Instagram", "<b>Jeux concours</b> : sur Instagram, Facebook et le site", "<b>Site internet</b> : mise en ligne des articles et des événements", "<b>Bots</b> : gestion des réponses automatiques", "<b>Événements</b> : la com en direct", "<b>Visuels</b> : posts, pubs print par saison"])
cm += bloc("cfm", "CFM Radio",
           ["La radio locale de Montauban. J'animais ses réseaux sociaux au quotidien : des jeux concours, des directs depuis les événements de la région, des annonces… et une série vidéo pour le Festival Albi Jazz."],
           f"""<h3 style="margin:0">Le Festival Albi Jazz, en 3 épisodes</h3>
      <div class="g g3 reels">
        <figure><div class="vid"><video class="reel" src="assets/video/cfm_jazz1.mp4" poster="assets/img/cm/poster_cfm_jazz1.webp" autoplay muted loop playsinline preload="metadata" aria-label="Festival Albi Jazz, jour 1"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Jour 1</b>retour aux sources de la musique</figcaption></figure>
        <figure><div class="vid"><video class="reel" src="assets/video/cfm_jazz2.mp4" poster="assets/img/cm/poster_cfm_jazz2.webp" autoplay muted loop playsinline preload="metadata" aria-label="Festival Albi Jazz, jour 2"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Jour 2</b>retour sur la journée</figcaption></figure>
        <figure><div class="vid"><video class="reel" src="assets/video/cfm_jazz3.mp4" poster="assets/img/cm/poster_cfm_jazz3.webp" autoplay muted loop playsinline preload="metadata" aria-label="Festival Albi Jazz, jour 3"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Jour 3</b>les performances</figcaption></figure>
      </div>
      <h3 style="margin:14px 0 0">Les posts Instagram et Facebook</h3>
      <div class="g g3">
        {fig(C + "cfm_cine.webp", "Jeu concours : gagnez vos places pour un ciné-débat au choix", "Jeu concours", "des places de ciné-débat, avec France Nature Environnement")}
        {fig(C + "cfm_direct.webp", "En direct de Montbeton, salon Bienvenue à la campagne", "Direct", "la radio en direct du salon Bienvenue à la campagne")}
        {fig(C + "cfm_stage.webp", "Annonce : CFM Montauban cherche un stagiaire en journalisme", "Recrutement", "l'annonce du stage en journalisme")}
      </div>""",
           ["<b>Réseaux sociaux</b> : gestion et création des posts sur Instagram et Facebook", "<b>Jeux concours</b> : lancement et animation", "<b>Festivals</b> : médiatisation sur place, à l'Albi Jazz Festival, à Pause Guitare…", "<b>Vidéo</b> : montage sur Premiere Pro et CapCut", "<b>Visuels</b> : création de visuels et d'affiches"])
cm += pied(("vancore.html", "assets/img/vancore/cover_van_paysage.webp", "Vancore", "center 62%"))
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
labo_css = """.logos-grille { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
@media (max-width: 1000px) { .logos-grille { grid-template-columns: repeat(2, 1fr); } }
.logos-grille figure { margin: 0; }
.logos-grille .zoom { position: relative; background: #fff; border-radius: 22px; aspect-ratio: 4 / 3; }
.logos-grille .zoom img { position: absolute; inset: 14%; width: 72%; height: 72%; object-fit: contain; }
.logos-grille .zoom:hover img { transform: scale(1.04); }
.logos-grille figcaption { margin-top: 14px; }
.logos-grille figcaption b { font-size: 19px; letter-spacing: -0.02em; }
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
.carte-bref { all: unset; box-sizing: border-box; display: block; cursor: pointer; border-radius: 22px; transition: translate 0.4s cubic-bezier(.2,.8,.2,1); }
.carte-bref img { width: 100%; aspect-ratio: 16 / 10; object-fit: cover; border-radius: 18px; transition: scale 0.6s cubic-bezier(.2,.7,.2,1); }
.carte-bref:hover img { scale: 1.03; }
.carte-bref:focus-visible { outline: 2px solid var(--lilas); outline-offset: 6px; }
.carte-bref .etiquettes { display: flex; }
.carte-bref .plus { display: inline-block; margin-top: 2px; color: var(--lilas); font-weight: 700; font-size: 15px; border-bottom: 1px solid currentColor; }
.carte-bref:hover .plus::after { content: " →"; }
dialog.fiche { width: min(1040px, 94vw); max-height: 90vh; border: 0; border-radius: 26px; padding: clamp(22px, 3vw, 38px); background: var(--carte); color: var(--texte); display: none; grid-template-columns: 1.15fr 1fr; gap: clamp(20px, 3vw, 40px); overflow: auto; }
dialog.fiche[open] { display: grid; animation: fiche 0.35s cubic-bezier(.2,.8,.2,1); }
@keyframes fiche { from { opacity: 0; translate: 0 18px; } }
dialog.fiche::backdrop { background: rgba(5,5,7,0.78); backdrop-filter: blur(4px); }
.fiche .fermer { position: absolute; top: 14px; right: 14px; width: 42px; height: 42px; border-radius: 50%; border: 0; background: rgba(255,255,255,0.1); color: var(--texte); font: 400 26px/1 "Bricolage", sans-serif; cursor: pointer; }
.fiche .fermer:hover { background: var(--lilas); color: var(--nuit); }
.fiche-media { display: grid; gap: 12px; align-content: start; }
.fiche-media.trois { grid-template-columns: 1fr 1fr; }
.fiche-media.trois .zoom:last-child { grid-column: span 2; }
.fiche-media.trois .zoom:last-child { background: #000; border-radius: 14px; }
.fiche-media.trois .zoom:last-child img { width: auto; max-width: 100%; max-height: 40vh; margin: 0 auto; object-fit: contain; }
.fiche-media .zoom img { border-radius: 14px; width: 100%; max-height: 36vh; object-fit: cover; }
.bref { align-items: start; }
.fiche-texte h3 { font-size: clamp(26px, 2.6vw, 34px); letter-spacing: -0.04em; line-height: 1.05; margin: 12px 0 14px; padding-right: 40px; }
.fiche-texte p { color: var(--doux); font-size: 15.5px; margin: 0 0 12px; }
.fiche-texte p b { color: var(--texte); }
.paliers { border-collapse: collapse; width: 100%; margin: 4px 0 14px; font-size: 15px; }
.paliers th, .paliers td { text-align: left; padding: 8px 0; border-top: 1px solid var(--ligne); }
.paliers th { color: var(--lilas); width: 90px; font-weight: 700; }
@media (max-width: 760px) { dialog.fiche[open] { grid-template-columns: 1fr; } }

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
.competences { list-style: none; margin: 22px 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: 6px; }
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
.rang figcaption b + * , .rang figcaption { font-weight: 400; }
.rang figcaption b { font-weight: 700; color: var(--texte); }
.carrousel { margin-top: 14px; }
.piste-c { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
@media (max-width: 760px) { .evo { grid-template-columns: 1fr 1.4fr; gap: 10px; } .evo .fl { display: none; } .evo .vitrine { padding: 14px; gap: 10px; } .evo-avant .zoom img { aspect-ratio: 1; } .evo .vitrine { aspect-ratio: auto; flex-direction: row; } .evo .vitrine .zoom img { max-height: 70px; } .evo-avant .zoom img { aspect-ratio: 1.3; } .rang { gap: 8px; } .piste-c { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; } .piste-c .zoom { flex: 0 0 40%; scroll-snap-align: start; } }
.ouv-relief { margin-top: 26px; }
.ouv-relief .zoom img { border-radius: 22px; }

/* tailles maîtrisées : on voit un projet d'un coup d'œil */
.projet-labo { --h: clamp(220px, 36vh, 340px); }
.rang { max-width: calc(var(--h) * var(--s) + 14px); }
.carrousel { max-width: calc(var(--h) * 0.8 * 5 * 0.62 + 32px); }
.evo { max-width: calc(var(--h) * 2.6); }
.evo .vitrine .zoom img { max-height: calc(var(--h) * 0.5); }
.vitrine { max-width: 1100px; padding: clamp(24px, 4vw, 54px); }
.vitrine .zoom img { max-height: calc(var(--h) * 0.7); }
.ouv-relief { max-width: calc(var(--h) * 1.78 * 1.15); }
.g-libre { max-width: 1100px; }
@media (min-width: 1000px) {
  .projet-labo.duo { display: grid; grid-template-columns: minmax(260px, 340px) 1fr; gap: clamp(32px, 4vw, 70px); align-items: start; }
  .duo .cote { position: sticky; top: 110px; }
  .duo .chap { display: block; margin: 0; }
  .duo .chap h2 { font-size: clamp(32px, 3vw, 44px); margin: 14px 0 18px; }
  .duo .medias > :first-child { margin-top: 0; }
  .duo .medias .rang, .duo .medias .evo, .duo .medias .carrousel { margin-inline: 0; }
}
.duo-photos, .ecrans, .gam { max-width: 1100px; }
.pile { display: flex; flex-direction: column; gap: 14px; }
.pile2 { --h: clamp(300px, 56vh, 460px); }
.pile2 .zoom img { width: 100%; }
.duo .vitrine { padding: 22px 32px; max-width: 710px; }
.duo .ecrans { max-width: 640px; }
.duo .gam { max-width: 710px; }
.duo .vitrine .zoom img { max-height: calc(var(--h) * 0.42); }
.duo .duo-photos { max-width: calc(var(--h) * 3.556 * 0.75); }
.g2x2 { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; max-width: 760px; }
.g2x2 .zoom img { aspect-ratio: 16 / 10; object-fit: cover; object-position: top; }
.photos { display: flex; flex-wrap: wrap; gap: 8px; --ph: clamp(120px, 19vh, 175px); }
.photos .zoom { flex: calc(var(--r) * 100) 1 calc(var(--r) * var(--ph)); height: var(--ph); }
.photos img { width: 100%; height: 100%; object-fit: cover; border-radius: 10px; }
.photos a[href$="mustang.webp"] img { object-position: 50% 38%; }
@media (max-width: 760px) { .photos { --ph: 110px; gap: 6px; } }
.li-chiffres { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 14px 0; }
.li-chiffres div { background: rgba(183,204,156,0.1); border-radius: 16px; padding: 14px 16px; }
.li-chiffres strong { display: block; font-size: clamp(26px, 2.6vw, 36px); letter-spacing: -0.04em; line-height: 1; color: var(--lilas); }
.li-chiffres span { font-size: 13.5px; color: var(--doux); }
.li-posts { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, var(--lc))); gap: 14px; align-items: start; }
#linkedin { --lc: calc(min(52vh, 480px) * 0.8 + 2px); }
.li-chiffres { max-width: calc(var(--lc) * 2 + 14px); }
#linkedin .medias > .zoom { max-width: calc(var(--lc) * 2 + 14px); }
.li-posts .accroche { font-size: 16px; }
.li-posts details.post { margin: -4px 0 14px; }
.li-posts details.post summary { cursor: pointer; color: var(--lilas); font-weight: 700; font-size: 14.5px; list-style: none; display: inline-flex; gap: 6px; align-items: center; }
.li-posts details.post summary::-webkit-details-marker { display: none; }
.li-posts details.post summary::after { content: "+"; font-size: 18px; line-height: 1; transition: rotate .25s; }
.li-posts details.post[open] summary::after { rotate: 45deg; }
.li-posts details.post p { white-space: pre-line; font-size: 14px; line-height: 1.5; color: var(--doux); margin: 10px 0 0; padding: 12px 14px; background: rgba(255,255,255,0.04); border-radius: 12px; }
.li-posts .lire { all: unset; cursor: pointer; color: var(--lilas); font-weight: 700; font-size: 14.5px; margin: -4px 0 14px; border-bottom: 1px solid currentColor; align-self: flex-start; }
.li-posts .lire:hover { color: var(--texte); }
.li-posts .lire:focus-visible { outline: 2px solid var(--lilas); outline-offset: 4px; }
.li-modal .caro-n { right: auto; left: 10px; }
dialog.li-modal { padding-top: 68px; width: min(1080px, 94vw); grid-template-columns: 1.1fr minmax(0, calc(min(72vh, 620px) * 0.8)); align-items: start; }
.li-modal .li-post { max-height: calc(90vh - 76px); overflow: auto; padding-right: 8px; }
.li-tete { display: flex; gap: 12px; align-items: center; margin-bottom: 18px; padding-right: 40px; }
.li-tete img { width: 52px; height: 52px; border-radius: 50%; }
.li-tete b { display: block; font-size: 17px; }
.li-tete span { display: block; font-size: 13px; color: var(--doux); line-height: 1.35; }
.li-texte { white-space: pre-line; font-size: 16px; line-height: 1.6; margin: 0 0 20px; }
.li-modal dl { display: grid; grid-template-columns: repeat(4, auto); gap: 4px 16px; margin: 0; padding-top: 14px; border-top: 1px solid var(--ligne); justify-content: start; }
.li-modal dl div { display: flex; flex-direction: column-reverse; }
.li-modal dd { margin: 0; font-weight: 700; font-size: 20px; color: var(--lilas); } .li-modal dt { font-size: 12.5px; color: var(--doux); }
.li-modal .caro { margin: 0; border-radius: 16px; }
@media (max-width: 760px) { .li-modal .caro-n { right: auto; left: 10px; } dialog.li-modal[open] { grid-template-columns: 1fr; } .li-modal .caro { order: -1; max-width: 340px; } .li-modal .li-post { max-height: none; overflow: visible; } }
.li-posts dl { gap: 4px 8px; grid-template-columns: repeat(4, minmax(0, auto)); } .li-posts dt { white-space: nowrap; font-size: 11px; }
.li-posts li { border: 1px solid var(--ligne); border-radius: 18px; padding: 18px 18px 14px; display: flex; flex-direction: column; }
.li-posts .sujet { flex: none !important; }
.li-posts .accroche { font-weight: 700; font-size: 17px; line-height: 1.3; letter-spacing: -0.01em; margin: 0 0 8px; }
.li-posts .sujet { color: var(--doux); font-size: 14.5px; margin: 0 0 14px; flex: 1; }
.caro { position: relative; margin: -18px -18px 16px; border-radius: 17px 17px 0 0; overflow: hidden; background: #f4f1ec; }
.caro-piste { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scrollbar-width: none; scroll-behavior: smooth; }
.caro-piste::-webkit-scrollbar { display: none; }
.caro-piste img { flex: 0 0 100%; width: 100%; aspect-ratio: 4 / 5; object-fit: cover; scroll-snap-align: start; }
.caro-bt { position: absolute; top: 50%; translate: 0 -50%; width: 38px; height: 38px; border-radius: 50%; border: 0; background: rgba(13,14,17,0.72); color: #fff; font: 700 24px/1 "Bricolage", sans-serif; cursor: pointer; display: grid; place-items: center; padding-bottom: 3px; transition: opacity .25s, background .2s; }
.caro-bt:hover { background: var(--lilas); color: var(--nuit); }
.caro-bt.g { left: 10px; } .caro-bt.d { right: 10px; }
.caro-bt:disabled { opacity: 0; pointer-events: none; }
.caro-n { position: absolute; top: 10px; right: 10px; background: rgba(13,14,17,0.72); color: #fff; font-size: 12.5px; font-weight: 700; padding: 4px 10px; border-radius: 99px; }
.li-posts dl { display: grid; grid-template-columns: repeat(4, auto); gap: 4px 12px; margin: 0; border-top: 1px solid var(--ligne); padding-top: 10px; }
.li-posts dd { margin: 0; font-weight: 700; font-size: 16px; } .li-posts dt { font-size: 11.5px; color: var(--doux); order: 2; }
.li-posts dl div { display: flex; flex-direction: column-reverse; }
.li-posts li:first-child dd { color: var(--lilas); }
#linkedin .medias > .zoom img { border-radius: 18px; }
@media (max-width: 760px) { .li-posts { grid-template-columns: 1fr; justify-content: center; } .li-chiffres { grid-template-columns: 1fr 1fr 1fr; gap: 6px; } .li-chiffres div { padding: 10px; } }
.mv-titre { font-size: 17px; margin: 0 0 12px; }
.mv-titre + .reels { margin-bottom: 26px; }
.mv-courts { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.mv-longs { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.mv-courts figcaption, .mv-longs figcaption { font-size: 13.5px; color: var(--doux); }
.mv-courts figcaption { margin-top: 6px; }
video.reel.paysage { aspect-ratio: 16 / 9; }
@media (hover: hover) { .mv-longs figure:hover { scale: 1.06; } }
@media (max-width: 760px) { .mv-courts { grid-template-columns: repeat(2, 1fr); } .mv-longs { grid-template-columns: 1fr; } }
.projet-labo[hidden], .chapitre[hidden], .zone-perso[hidden] { display: none !important; }
.barre-labo { position: sticky; top: 62px; z-index: 8; display: flex; flex-wrap: wrap; gap: 14px 24px; align-items: center; padding: 14px 0; margin-bottom: 40px; background: color-mix(in srgb, var(--nuit) 88%, transparent); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid var(--ligne); }
.barre-labo .filtres { margin: 0; }
.onglets { display: inline-flex; padding: 4px; border-radius: 999px; background: var(--carte); border: 1px solid var(--ligne); }
.onglets button { font: 700 15px "Bricolage", sans-serif; color: var(--doux); background: none; border: 0; border-radius: 999px; padding: 9px 18px; cursor: pointer; }
.onglets button small { font-weight: 500; opacity: 0.7; margin-left: 4px; }
.onglets button[aria-pressed="true"] { background: var(--lilas); color: var(--nuit); }
.barre-labo .filtres button { padding: 7px 14px; font-size: 14px; }
.aucun { color: var(--doux); padding: 40px 0; }
.chapitre { margin: 10px 0 60px; }
.chapitre span { display: inline-block; font-size: 14px; color: var(--doux); border: 1px solid var(--ligne); border-radius: 999px; padding: 4px 12px; }
.chapitre h2 { font-size: clamp(46px, 7vw, 96px); letter-spacing: -0.05em; line-height: 0.95; margin: 14px 0 12px; }
.chapitre p { color: var(--doux); max-width: 52ch; margin: 0; font-size: 17px; }
.projet-labo:has(+ .zone-perso) { border-bottom: 0; }
.zone-perso { margin: 0 calc(-1 * var(--m)); padding: clamp(60px, 8vw, 110px) var(--m) clamp(50px, 6vw, 80px); background: #f2efe7; color: #14151a; border-radius: 34px; margin-bottom: 60px !important; --texte: #14151a; --doux: #55555a; --ligne: rgba(20,21,26,0.14); --carte: #e7e3d9; }
.zone-perso .chapitre span { border-color: rgba(20,21,26,0.25); }
.zone-perso dialog { --texte: #f2f1ee; --doux: #b8b6b1; --ligne: rgba(255,255,255,0.14); --carte: #17181c; color: var(--texte); }
.zone-perso .projet-labo:last-child { border-bottom: 0; margin-bottom: 0; padding-bottom: 0; }
.zone-perso .etiquettes span:first-child { background: #14151a; color: #f2efe7; }
.zone-perso .brief { color: #3c3c40; }
.zone-perso .li-posts li, .zone-perso .li-chiffres div { background: #fff; }
.zone-perso .li-chiffres strong { color: #4d6a2c; }
.zone-perso .li-posts li:first-child { background: #14151a; color: #f2efe7; border-color: #14151a; position: relative; }
.zone-perso .li-posts li:first-child .accroche { color: #f2efe7; }
.zone-perso .li-posts li:first-child .sujet, .zone-perso .li-posts li:first-child dt { color: #b8b6b1; }
.zone-perso .li-posts li:first-child dd { color: #b7cc9c; font-size: 18px; }
.zone-perso .li-posts li:first-child dl { border-color: rgba(255,255,255,0.15); }
.zone-perso .li-posts li:first-child .lire { color: #b7cc9c !important; }
.li-posts .top-post { display: inline-block; align-self: flex-start; background: #b7cc9c; color: #14151a; font-size: 12.5px; font-weight: 700; padding: 4px 11px; border-radius: 99px; margin-bottom: 10px; }
.zone-perso .lire { color: #5e7a3c !important; }
.zone-perso .b.plein { background: #14151a; color: #f2efe7; }
.zone-perso .mv-courts figcaption, .zone-perso .mv-longs figcaption { color: #55555a; }
@media (max-width: 760px) { .barre-labo { position: static; } .onglets { width: 100%; } .onglets button { flex: 1; } }
.ikea-caro { max-width: calc(min(52vh, 480px) * 0.8 + 38px); border: 1px solid var(--ligne); border-radius: 18px; padding: 18px; margin-top: 14px; }
.ikea-caro .accroche { font-weight: 700; margin: 0 0 4px; } .ikea-caro .sujet { color: var(--doux); font-size: 14.5px; margin: 0; }
.pod-fiche { list-style: none; padding: 0; margin: 18px 0 0; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; max-width: 640px; }
.pod-fiche li { border: 1px solid var(--ligne); border-radius: 14px; padding: 12px 14px; font-size: 14px; line-height: 1.4; color: var(--doux); }
.pod-fiche b { display: block; color: var(--lilas); font-size: 15px; margin-bottom: 4px; }
.pod-format { font-size: 14px; color: var(--doux); margin: 14px 0 0; }
@media (max-width: 760px) { .pod-fiche { grid-template-columns: 1fr; } }
.duo-photos { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 26px; }
.duo-photos .zoom img { aspect-ratio: 16 / 10; object-fit: cover; }
.ecrans { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; align-items: start; }
.ecrans .zoom { background: #0f0f1a; }
@media (max-width: 760px) { .ecrans { grid-template-columns: 1fr 1fr; } .duo-photos { grid-template-columns: 1fr; } .vitrine { flex-direction: column; } }
@media (max-width: 760px) { .podcast { grid-template-columns: 1fr; } .podcast > img { max-width: 320px; } .ikea-avant { grid-template-columns: 1fr; } .ikea-avant .fl { display: none; } .g-pages { grid-template-columns: 1fr; } }"""
labo = head("Labo", "Projets d'école et projets perso de Cloé Pérot : identités visuelles, stratégies, site web, podcast.", labo_css)
cartes = "".join(f"""
      <figure>{z("assets/img/labo/" + f + ".webp", "Logo " + n)}<figcaption><b>{n}</b><small>{t}</small>{d}</figcaption></figure>""" for n, t, d, f in LABO)
I = "assets/img/labo/ikea/"
pages = lambda xs: "".join(z(I + x + ".webp", a) for x, a in xs)
labo += f"""  <div class="ouv" style="min-height:62svh">
    <img src="assets/img/labo/couverture-foret.webp" alt="" style="object-position:center 40%">
    <a class="retour" href="index.html">← Accueil</a>
    <h1>Labo</h1>
    <p class="role">Mes projets d'école et mes projets perso : là où je teste, je dessine et je m'amuse.</p>
  </div>

  <section>
    <div class="barre-labo">
      <div class="onglets" role="group" aria-label="Projets d'école ou projets perso">
        <button type="button" aria-pressed="true" data-o="tout">Tout <small>13</small></button>
        <button type="button" aria-pressed="false" data-o="ecole">École <small>10</small></button>
        <button type="button" aria-pressed="false" data-o="perso">Perso <small>3</small></button>
      </div>
      <div class="filtres" role="group" aria-label="Type de projet">
        <button type="button" aria-pressed="true" data-f="tout">Tous les types</button>
        <button type="button" aria-pressed="false" data-f="identite">Identité visuelle</button>
        <button type="button" aria-pressed="false" data-f="strategie">Stratégie</button>
        <button type="button" aria-pressed="false" data-f="web">Web &amp; podcast</button>
        <button type="button" aria-pressed="false" data-f="video">Vidéo</button>
        <button type="button" aria-pressed="false" data-f="photo">Photo</button>
      </div>
    </div>
    <p class="aucun" hidden>Pas de projet de ce type ici. Essaie un autre filtre&nbsp;!</p>

    <header class="chapitre" data-o="ecole"><span>10 projets</span><h2>Projets d'école</h2><p>Des briefs de marques, réelles ou imaginées, en Bachelor puis en Mastère à YNOV Toulouse.</p></header>


    <article class="projet-labo duo" data-cat="identite" id="ikea">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Identité visuelle</span></div>
      <div class="chap"><h2>IKEA, version psychédélique</h2><div><p class="brief"><b>Le brief :</b> retravailler l'identité visuelle d'une marque et sa communication selon un courant artistique. J'ai choisi le rétro-psychédélique des années 70, mêlé au bubble street art.</p><ul class="competences"><li>Identité visuelle</li><li>Logo</li><li>Direction artistique</li><li>Print</li><li>Social media</li></ul></div></div></div>
      <div class="medias">
      <div class="evo"><figure class="evo-avant">{z("assets/img/labo/ikea/avant.webp", "Le logo IKEA d'origine, lettres bleues dans un ovale jaune")}<figcaption>Le logo d'origine</figcaption></figure><span class="fl" aria-hidden="true">→</span><figure class="evo-apres"><div class="vitrine" style="--v:#ffd900">{z("assets/img/labo/ikea/logo-png.webp", "Le nouveau logo IKEA, lettres fluides bleues dans un contour noir")}{z("assets/img/labo/ikea/fleur-png.webp", "Le logotype fleur")}</div><figcaption>L'évolution</figcaption></figure></div>
      <div class="rang" style="--a:1.304fr 0.563fr;--s:1.867">{fig("assets/img/labo/ikea/abribus-chaise.webp", "Affiche d'abribus : Votre future obsession ? Fauteuil SOLSTÄLE", "Affichage abribus")}{fig("assets/img/labo/ikea/story-salon.webp", "Story Instagram : un salon rétro, produits entourés de jaune et de bleu", "Story Instagram")}</div>
      <div class="ikea-caro"><div class="caro" aria-roledescription="carrousel" aria-label="Carrousel Instagram IKEA"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/ikea/carrousel-1.webp" alt="Slide CHATMÖ : un chat sur un coussin vert" loading="lazy"><img src="assets/img/labo/ikea/carrousel-2.webp" alt="Slide DOGVIK : un bouledogue à côté d'un fauteuil orange" loading="lazy"><img src="assets/img/labo/ikea/carrousel-3.webp" alt="Slide DOGVIK : un bouledogue français sur un fauteuil vert" loading="lazy"><img src="assets/img/labo/ikea/carrousel-4.webp" alt="Slide CHATMÖ : un chat roux sur un fauteuil bleu nuit" loading="lazy"><img src="assets/img/labo/ikea/carrousel-5.webp" alt="Slide DOGVIK : un berger dans un salon lumineux" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Slide précédente">‹</button><button type="button" class="caro-bt d" aria-label="Slide suivante">›</button><span class="caro-n">1 / 5</span></div>
        <p class="accroche">Carrousel Instagram</p><p class="sujet">CHATMÖ et DOGVIK, en 5 slides.</p></div>
      <div class="rang" style="--a:0.706fr 1.778fr;--s:2.484">{fig("assets/img/labo/ikea/pub-catalogue.webp", "Publicité catalogue : FLOCRA et ENIDTH dans une entrée vert sauge", "Publicité")}{fig("assets/img/labo/ikea/carton-notice.webp", "Carton IKEA et notice de montage, annotés de formes jaunes", "Carton et notice")}</div></div>
    </article>

    <article class="projet-labo duo" data-cat="identite" id="matp">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Identité visuelle</span></div>
      <div class="chap"><h2>Musée des Arts et Traditions Populaires</h2><div><p class="brief"><b>Le brief :</b> créer l'identité d'un musée parisien et la communication de son inauguration. Le « A » central rappelle l'Arc de Triomphe et la tour Eiffel, entre patrimoine et design contemporain.</p><ul class="competences"><li>Logo</li><li>Charte graphique</li><li>Affiche</li><li>Social media</li><li>Goodies</li></ul></div></div></div>
      <div class="medias">
      <div class="vitrine" style="--v:#fff">{z("assets/img/labo/matp/logo-png.webp", "Le logo MATP")}</div><div class="rang pile2" style="--a:0.562fr 0.952fr;--s:1.514">{z("assets/img/labo/matp/story.webp", "Story Instagram de l'inauguration du 8 novembre")}<div class="pile">{z("assets/img/labo/matp/casquette.webp", "Casquette aux couleurs du musée")}{z("assets/img/labo/matp/banniere.webp", "Bannière Facebook de l'inauguration")}</div></div></div>
    </article>

    <article class="projet-labo duo" data-cat="identite strategie" id="hyros" style="--fond-img:#000">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Lancement de produit</span></div>
      <div class="chap"><h2>Hyros, la Tesla à hydrogène</h2><div><p class="brief"><b>Le brief :</b> lancer le premier véhicule à hydrogène de Tesla : trouver le nom, créer le logotype, imaginer le modèle et construire toute la campagne de lancement.</p><ul class="competences"><li>Naming</li><li>Logotype</li><li>Visuels IA</li><li>Newsletter</li><li>Magazine</li><li>Carrousel</li></ul></div></div></div>
      <div class="medias">
      <div class="rang" style="--a:1.778fr 0.6fr;--s:2.378">{fig("assets/img/labo/hyros/logo-relief.webp", "Le logo HYROS en lettres métalliques sur un mur de béton", "Le logotype")}{fig("assets/img/labo/hyros/newsletter-hd.webp", "La newsletter de lancement Model Hyros", "Newsletter", "<br>Clique pour la lire en entier", "", "aspect-ratio:0.6;object-fit:cover;object-position:top")}</div><div class="rang" style="--a:1fr 0.707fr 0.8fr;--s:2.507">{fig("assets/img/labo/hyros/voiture.webp", "Le modèle Hyros, généré par IA", "Visuel IA")}{fig("assets/img/labo/hyros/magazine-couv.webp", "Couverture de magazine pour le lancement", "Couverture magazine")}{fig("assets/img/labo/hyros/carrousel-1.webp", "Visuel IA de la Hyros, phare avant", "Visuel IA")}</div>
    </article>

    <article class="projet-labo duo" data-cat="identite strategie" id="kinetic">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Branding</span></div>
      <div class="chap"><h2>Kinetic, ex Sparks</h2><div><p class="brief"><b>Le brief :</b> un vrai client, une startup de bien-être et de performance en entreprise, à qui il fallait un nouveau projet de marque : nom, identité, stratégie digitale et pitch.</p><ul class="competences"><li>Naming</li><li>Brandbook</li><li>Stratégie digitale</li><li>Maquettes app & site</li></ul></div></div></div>
      <div class="medias">
      <div class="rang" style="--a:1.504fr 1.778fr;--s:3.282">{fig("assets/img/labo/kinetic/couverture.webp", "Le logo Kinetic en blanc sur une photo de deux sprinteurs", "Le logo")}{fig("assets/img/labo/kinetic/affiche.webp", "Affiche Beyond movement, towards harmony sur la façade d'un immeuble", "Affichage urbain")}</div><div class="rang" style="--a:1fr;max-width:none">{fig("assets/img/labo/kinetic/objets.webp", "Une montre, une casquette, deux tote bags, une gourde et une seconde montre aux couleurs de Kinetic", "Les goodies")}</div><div class="rang" style="--a:1.49fr 1.473fr;--s:2.963">{fig("assets/img/labo/kinetic/site.webp", "Le site web Kinetic sur un ordinateur et un téléphone", "Le site")}{fig("assets/img/labo/kinetic/app.webp", "Les écrans de l'application Kinetic", "L'appli")}</div>
    </article>


    <article class="projet-labo duo" data-cat="web" id="pawtes">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Site web</span></div>
      <div class="chap"><h2>Entre Pawtes</h2><div><p class="brief"><b>Le brief :</b> créer et animer le site d'une crèche pour chiens à Toulouse, du design aux textes.</p><ul class="competences"><li>Webdesign</li><li>Rédaction web</li><li>Animation</li><li>WordPress</li></ul></div></div></div>
      <div class="medias">
      <div class="g2x2">{z("assets/img/labo/pawtes/accueil.webp", "Accueil du site Entre Pawtes : Crèche de toutous à Toulouse")}{z("assets/img/labo/pawtes/apropos.webp", "Section À propos avec une mosaïque de chiens")}{z("assets/img/labo/pawtes/avis.webp", "La parole aux truffes : les avis des clients")}{z("assets/img/labo/pawtes/faq.webp", "Questions de pawtes : la FAQ en accordéon")}</div></div>
    </article>

    <article class="projet-labo duo" data-cat="strategie" id="bfc">
      <div class="cote"><div class="etiquettes"><span>École</span><span>Stratégie & gamification</span></div>
      <div class="chap"><h2>Book, Food &amp; Créa</h2><div><p class="brief"><b>Le brief :</b> lancer à Toulouse une expérience de 3 heures pour les femmes de 18 à 35 ans : un livre, un moment gourmand et un atelier créatif, pour créer du lien. On a étudié le marché, construit la stratégie et le plan de com, puis imaginé une appli pour donner envie de revenir.</p><ul class="competences"><li>Étude de marché</li><li>Stratégie marketing</li><li>Plan de communication</li><li>Fidélisation</li><li>Gamification</li></ul></div></div></div>
      <div class="medias">
      <div class="duo-photos">{z("assets/img/labo/bfc/photo-aquarelle.webp", "Atelier aquarelle, des fleurs peintes à la main")}{z("assets/img/labo/bfc/photo-atelier.webp", "Pinceaux et pots de peinture dans un atelier")}</div><div class="gam"><div><h3>Le Jardin Créatif, l'appli du projet</h3><p>Chaque participante fait pousser un jardin grâce à des petits défis du quotidien : lire 5 pages, prendre son petit-déj en photo, dessiner en 60 secondes. Une plante par pilier, Book, Food et Créa, et la récolte ne se débloque qu'en revenant à un atelier.</p></div></div><div class="ecrans">{z("assets/img/labo/bfc/app-jardin.webp", "Le jardin et les défis du jour")}{z("assets/img/labo/bfc/app-boutique.webp", "La boutique XP")}{z("assets/img/labo/bfc/app-evenements.webp", "La réservation des ateliers")}{z("assets/img/labo/bfc/app-scan.webp", "L'espace organisatrice pour valider les récoltes")}</div></div>
    </article>


    <article class="projet-labo" data-cat="web" id="podcast">
      <div class="etiquettes"><span>École</span><span>Podcast</span></div>
      <div class="podcast">
        <img src="assets/img/labo/podcast-cover.webp" alt="Pochette du podcast Les clés du voisin by Airbnb : un chalet en A dans la forêt">
        <div>
          <h2 style="font-size:clamp(36px,4.4vw,60px)">Les clés du voisin</h2>
          <p class="brief" style="max-width:52ch;margin:16px 0 0"><b>Le brief :</b> imaginer le podcast d'une marque qui n'en a pas encore, et le présenter.</p>
          <p style="color:var(--doux);max-width:52ch;margin:12px 0 0"><b style="color:var(--texte)">L'idée pour Airbnb :</b> un podcast où voyageurs et hôtes se confient, anonymement, sur leurs histoires les plus drôles, les plus folles ou les plus touchantes. Du genre « Mon colocataire Airbnb avait un chat psychopathe ».</p>
          <ul class="pod-fiche"><li><b>Image</b>rappeler que l'ADN d'Airbnb, c'est l'hospitalité humaine</li><li><b>Fidélisation</b>un rendez-vous chaque semaine pour la communauté</li><li><b>Acquisition</b>faire découvrir des logements atypiques</li></ul>
          <p class="pod-format">Hebdomadaire · 20 min · pour les 25-35 ans, 22 % des auditeurs de podcasts</p>
          <ul class="competences"><li>Concept éditorial</li><li>Stratégie de marque</li><li>Écriture</li><li>Montage audio</li><li>Pochette</li></ul>
          <p style="color:var(--doux);margin:22px 0 0">L'extrait, mets le son :</p>
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
        <button type="button" class="carte-bref" data-fiche="f-3s">
          <img src="assets/img/labo/autres/3soeurs-photo.webp" alt="" loading="lazy">
          <span class="etiquettes"><span>Fidélisation</span></span>
          <h3>Trois Sœurs Café</h3>
          <p>Un programme de fidélité pour un café toulousain : 1 € = 1 point, des récompenses du café offert au brunch.</p>
          <span class="plus">En savoir plus</span>
        </button>
        <button type="button" class="carte-bref" data-fiche="f-mf">
          <img src="assets/img/labo/autres/mariage-coffret.webp" alt="" loading="lazy">
          <span class="etiquettes"><span>Brand content</span></span>
          <h3>Mariage Frères × Pierre Niney</h3>
          <p>Un coffret de 4 thés en édition limitée, « Théâtre des Sens », co-signé par l'acteur.</p>
          <span class="plus">En savoir plus</span>
        </button>
        <button type="button" class="carte-bref" data-fiche="f-rb">
          <img src="assets/img/labo/autres/redbull-kiosque-limitless.webp" alt="" loading="lazy" style="object-position:50% 72%">
          <span class="etiquettes"><span>Storytelling</span></span>
          <h3>Red Bull, #NouvellesAiles</h3>
          <p>Une campagne « LIMITLESS » qui raconte le parcours d'un pilote, du karting à Red Bull Racing.</p>
          <span class="plus">En savoir plus</span>
        </button>
      </div>

      <dialog class="fiche" id="f-3s" aria-labelledby="t-3s">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="fiche-media">{z("assets/img/labo/autres/3soeurs-photo.webp", "Brunch au Trois Sœurs Café")}{z("assets/img/labo/autres/3soeurs-workflow.webp", "Le parcours client du programme de fidélité, du QR code à la récompense")}</div>
        <div class="fiche-texte">
          <span class="etiquettes"><span>École</span><span>Fidélisation</span></span>
          <h3 id="t-3s">Trois Sœurs Café</h3>
          <p class="brief"><b>Le brief :</b> imaginer le programme de fidélité d'un café-brunch toulousain, sans casser son côté chaleureux et familial.</p>
          <p><b>Les Sœurs Fidèles :</b> on scanne le QR code à table, on s'inscrit en quelques secondes (10 points offerts) et chaque passage rapporte des points automatiquement.</p>
          <table class="paliers"><tbody><tr><th>100 pts</th><td>5 € de réduction</td></tr><tr><th>150 pts</th><td>Une boisson offerte</td></tr><tr><th>200 pts</th><td>Pâtisserie et café offerts</td></tr><tr><th>300 pts</th><td>Un brunch pour une personne</td></tr></tbody></table>
          <p>Des points bonus en laissant un avis Google ou en partageant une story Instagram, et la liste des données à collecter pour mieux connaître les clients.</p>
          <ul class="competences"><li>Programme de fidélité</li><li>Parcours client</li><li>Data &amp; CRM</li></ul>
        </div>
      </dialog>

      <dialog class="fiche" id="f-mf" aria-labelledby="t-mf">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="fiche-media">{z("assets/img/labo/autres/mariage-coffret.webp", "Le coffret Théâtre des Sens, ouvert et fermé")}{z("assets/img/labo/autres/mariage-collab.webp", "Visuel de la collaboration : la boîte de thé Mariage Frères face à Pierre Niney")}</div>
        <div class="fiche-texte">
          <span class="etiquettes"><span>École</span><span>Brand content</span></span>
          <h3 id="t-mf">Mariage Frères × Pierre Niney</h3>
          <p class="brief"><b>Le brief :</b> créer une collaboration entre une maison de thé et une personnalité, qui fasse sens pour les deux.</p>
          <p><b>Théâtre des Sens :</b> un coffret noir et or de 4 thés en édition limitée. Dedans, une carte avec un texte signé qui fait du thé « une scène invisible », et un QR code vers une playlist à écouter pendant la dégustation.</p>
          <p>Autour du coffret : un événement de lancement et un spot TV.</p>
          <ul class="competences"><li>Co-branding</li><li>Packaging</li><li>Rédaction</li><li>Événementiel</li></ul>
        </div>
      </dialog>

      <dialog class="fiche" id="f-rb" aria-labelledby="t-rb">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="fiche-media trois">{z("assets/img/labo/autres/redbull-nouvelles-ailes.webp", "Affiche #NouvellesAiles : une Formule 1 dans un tunnel")}{z("assets/img/labo/autres/redbull-limitless-pilote.webp", "Affiche LIMITLESS avec le pilote sur le podium")}{z("assets/img/labo/autres/redbull-kiosque-limitless.webp", "L'affiche LIMITLESS sur un kiosque")}</div>
        <div class="fiche-texte">
          <span class="etiquettes"><span>École</span><span>Storytelling</span></span>
          <h3 id="t-rb">Red Bull, #NouvellesAiles</h3>
          <p class="brief"><b>Le brief :</b> analyser la communication de Red Bull puis proposer une campagne qui raconte une histoire.</p>
          <p><b>Le concept :</b> le parcours d'un pilote, du karting à son arrivée chez Red Bull Racing, pour montrer comment la marque « donne des ailes ».</p>
          <p><b>Trois temps forts :</b> un court-métrage, une campagne digitale autour du hashtag #NouvellesAiles où chacun partage son propre défi, et un événement immersif avec simulation de course en réalité virtuelle.</p>
          <ul class="competences"><li>Storytelling</li><li>Concept de campagne</li><li>Affiches</li><li>Plan de communication</li></ul>
        </div>
      </dialog>
    </article>

    <div class="zone-perso">
    <header class="chapitre" data-o="perso"><span>3 projets</span><h2>Projets perso</h2><p>Ce que je fais pour moi, par curiosité : écrire, monter, photographier.</p></header>
    <article class="projet-labo duo" data-cat="perso strategie" id="linkedin">
      <div class="cote"><div class="etiquettes"><span>Perso</span><span>LinkedIn</span></div>
      <div class="chap"><h2>Alternante, mais pas que&nbsp;!</h2><p class="brief">Pendant mon alternance, j'ai testé LinkedIn pour moi. Une collègue rédactrice web m'a appris les codes, puis j'ai écrit et designé mes posts pour parler aux étudiants et aux jeunes actifs, avec humour et sincérité.</p>
      <ul class="competences"><li>Personal branding</li><li>Copywriting</li><li>Carrousels</li><li>Ligne éditoriale</li></ul>
      <p style="margin-top:20px"><a class="b plein" href="https://www.linkedin.com/in/cloeperot/" target="_blank" rel="noopener">Voir mon profil ↗</a></p></div></div>
      <div class="medias">
        {z("assets/img/labo/linkedin/banniere.webp", "Mon profil LinkedIn : bannière Alternante mais pas que, 2 623 abonnés")}
        <div class="li-chiffres"><div><strong>2&nbsp;623</strong><span>abonnés</span></div><div><strong>248k</strong><span>impressions sur ces 4 posts</span></div><div><strong>+218</strong><span>abonnés gagnés grâce à eux</span></div></div>
        <ol class="li-posts">
          <li><div class="caro" aria-roledescription="carrousel" aria-label="Guide du langage corporate"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/corporate-1.webp" alt="Guide du langage corporate, page 1 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-2.webp" alt="Guide du langage corporate, page 2 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-3.webp" alt="Guide du langage corporate, page 3 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-4.webp" alt="Guide du langage corporate, page 4 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-5.webp" alt="Guide du langage corporate, page 5 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-6.webp" alt="Guide du langage corporate, page 6 sur 6" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 6</span></div>
            <span class="top-post">Mon post le plus vu</span><p class="accroche">« J'ai mis 6 mois à décrypter le langage corporate. »</p><p class="sujet">Un guide du langage « politiquement correct » de l'entreprise.</p>
            <button type="button" class="lire" data-post="post-1">Lire le post</button>
            <dl><div><dt>impressions</dt><dd>99 911</dd></div><div><dt>réactions</dt><dd>724</dd></div><div><dt>commentaires</dt><dd>77</dd></div><div><dt>abonnés</dt><dd>+87</dd></div></dl></li>
          <li><div class="caro" aria-roledescription="carrousel" aria-label="Ma semaine d'école"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/semaine-1.webp" alt="Ma semaine d'école, page 1 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-2.webp" alt="Ma semaine d'école, page 2 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-3.webp" alt="Ma semaine d'école, page 3 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-4.webp" alt="Ma semaine d'école, page 4 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-5.webp" alt="Ma semaine d'école, page 5 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-6.webp" alt="Ma semaine d'école, page 6 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-7.webp" alt="Ma semaine d'école, page 7 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-8.webp" alt="Ma semaine d'école, page 8 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-9.webp" alt="Ma semaine d'école, page 9 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-10.webp" alt="Ma semaine d'école, page 10 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-11.webp" alt="Ma semaine d'école, page 11 sur 11" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 11</span></div>
            <p class="accroche">« Tout le monde me dit, mais Sabrina comment tu fais pour tenir ta ferme… »</p><p class="sujet">Ma semaine d'école racontée en photos.</p>
            <button type="button" class="lire" data-post="post-2">Lire le post</button>
            <dl><div><dt>impressions</dt><dd>74 976</dd></div><div><dt>réactions</dt><dd>688</dd></div><div><dt>commentaires</dt><dd>38</dd></div><div><dt>abonnés</dt><dd>+71</dd></div></dl></li>
          <li><div class="caro" aria-roledescription="carrousel" aria-label="Refonte du profil du big boss"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/refonte-1.webp" alt="Refonte du profil du big boss, page 1 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-2.webp" alt="Refonte du profil du big boss, page 2 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-3.webp" alt="Refonte du profil du big boss, page 3 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-4.webp" alt="Refonte du profil du big boss, page 4 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-5.webp" alt="Refonte du profil du big boss, page 5 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-6.webp" alt="Refonte du profil du big boss, page 6 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-7.webp" alt="Refonte du profil du big boss, page 7 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-8.webp" alt="Refonte du profil du big boss, page 8 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-9.webp" alt="Refonte du profil du big boss, page 9 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-10.webp" alt="Refonte du profil du big boss, page 10 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-11.webp" alt="Refonte du profil du big boss, page 11 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-12.webp" alt="Refonte du profil du big boss, page 12 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-13.webp" alt="Refonte du profil du big boss, page 13 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-14.webp" alt="Refonte du profil du big boss, page 14 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-15.webp" alt="Refonte du profil du big boss, page 15 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-16.webp" alt="Refonte du profil du big boss, page 16 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-17.webp" alt="Refonte du profil du big boss, page 17 sur 17" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 17</span></div>
            <p class="accroche">« Si je te dis un secret, tu ne le répètes à personne ? »</p><p class="sujet">L'avant/après de la refonte du profil LinkedIn de mon boss (visages et noms floutés).</p>
            <button type="button" class="lire" data-post="post-3">Lire le post</button>
            <dl><div><dt>impressions</dt><dd>45 042</dd></div><div><dt>réactions</dt><dd>515</dd></div><div><dt>commentaires</dt><dd>38</dd></div><div><dt>abonnés</dt><dd>+31</dd></div></dl></li>
          <li><div class="caro" aria-roledescription="carrousel" aria-label="La petite Cloé vs la big"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/jouets-1.webp" alt="La petite Cloé vs la big, page 1 sur 2" loading="lazy"><img src="assets/img/labo/linkedin/jouets-2.webp" alt="La petite Cloé vs la big, page 2 sur 2" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 2</span></div>
            <p class="accroche">« J'vous parle d'un temps que les moins de 20 ans ne peuvent pas connaître. »</p><p class="sujet">Mes jouets d'enfance face à mes applis préférées.</p>
            <button type="button" class="lire" data-post="post-4">Lire le post</button>
            <dl><div><dt>impressions</dt><dd>28 190</dd></div><div><dt>réactions</dt><dd>286</dd></div><div><dt>commentaires</dt><dd>33</dd></div><div><dt>abonnés</dt><dd>+29</dd></div></dl></li>
        </ol>
      <dialog class="fiche li-modal" id="post-1" aria-label="Post LinkedIn : Guide du langage corporate">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="li-post">
          <div class="li-tete"><img src="assets/img/labo/linkedin/avatar.webp" alt=""><div><b>Cloé Pérot</b><span>Chargée de communication en alternance | Je te partage les secrets de l'alternance</span></div></div>
          <p class="li-texte">J&#x27;ai mis 6 mois à décrypter le langage corporate.
Je t&#x27;ai créé un guide pour éviter de te prendre les pieds dans le tapis.

Après un an et demi dans différentes entreprises.
Après des mois à analyser et faire des recherches.
Après des semaines à hocher la tête sans rien comprendre.

Je sors enfin mon guide.
(Et ne va pas t&#x27;imaginer que je vais te demander 50€ derrière).

Avec lui, tu vas enfin avoir une longueur d&#x27;avance et une répartie de fou
(pas 3h après -oui, oui ça me connait)

Et toi, c&#x27;est quoi ta formulation “politiquement correcte” pref&#x27; ?

———
Hello, moi c&#x27;est Cloé !
☀️ Un concentré du sud en bouteille
🍵 Multi-tâche, multi-lingue et surtout multi-ref
Psst, abonne-toi pour spill the tea !</p>
          <dl><div><dt>impressions</dt><dd>99 911</dd></div><div><dt>réactions</dt><dd>724</dd></div><div><dt>commentaires</dt><dd>77</dd></div><div><dt>abonnés</dt><dd>+87</dd></div></dl>
        </div>
        <div class="caro" aria-roledescription="carrousel" aria-label="Guide du langage corporate"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/corporate-1.webp" alt="Guide du langage corporate, page 1 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-2.webp" alt="Guide du langage corporate, page 2 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-3.webp" alt="Guide du langage corporate, page 3 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-4.webp" alt="Guide du langage corporate, page 4 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-5.webp" alt="Guide du langage corporate, page 5 sur 6" loading="lazy"><img src="assets/img/labo/linkedin/corporate-6.webp" alt="Guide du langage corporate, page 6 sur 6" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 6</span></div>
      </dialog>
      <dialog class="fiche li-modal" id="post-2" aria-label="Post LinkedIn : Ma semaine d'école">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="li-post">
          <div class="li-tete"><img src="assets/img/labo/linkedin/avatar.webp" alt=""><div><b>Cloé Pérot</b><span>Chargée de communication en alternance | Je te partage les secrets de l'alternance</span></div></div>
          <p class="li-texte">Tout le monde me dit, mais Sabrina comment tu fais pour tenir ta ferme,
alors déjà j&#x27;ai pas de ferme et je m&#x27;appelle pas Sabrina.

Moi c&#x27;est Cloé, je suis toujours alternante,
et la semaine dernière, j&#x27;étais à l&#x27;école.

Alors, j&#x27;ai décidé de t&#x27;embarquer dans cette autre facette de l&#x27;alternance.
Toujours dans mon sud natal,
Prend ton meilleur matcha et suis-moi.

Quel est ton moment marquant de ta semaine ?

———
Hello, moi c&#x27;est Cloé !
☀️ Un concentré du sud en bouteille
🍵 Multi-tâche, multi-lingue et surtout multi-ref
Psst, abonne-toi pour spill the tea !</p>
          <dl><div><dt>impressions</dt><dd>74 976</dd></div><div><dt>réactions</dt><dd>688</dd></div><div><dt>commentaires</dt><dd>38</dd></div><div><dt>abonnés</dt><dd>+71</dd></div></dl>
        </div>
        <div class="caro" aria-roledescription="carrousel" aria-label="Ma semaine d'école"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/semaine-1.webp" alt="Ma semaine d'école, page 1 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-2.webp" alt="Ma semaine d'école, page 2 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-3.webp" alt="Ma semaine d'école, page 3 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-4.webp" alt="Ma semaine d'école, page 4 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-5.webp" alt="Ma semaine d'école, page 5 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-6.webp" alt="Ma semaine d'école, page 6 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-7.webp" alt="Ma semaine d'école, page 7 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-8.webp" alt="Ma semaine d'école, page 8 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-9.webp" alt="Ma semaine d'école, page 9 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-10.webp" alt="Ma semaine d'école, page 10 sur 11" loading="lazy"><img src="assets/img/labo/linkedin/semaine-11.webp" alt="Ma semaine d'école, page 11 sur 11" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 11</span></div>
      </dialog>
      <dialog class="fiche li-modal" id="post-3" aria-label="Post LinkedIn : Refonte du profil du big boss">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="li-post">
          <div class="li-tete"><img src="assets/img/labo/linkedin/avatar.webp" alt=""><div><b>Cloé Pérot</b><span>Chargée de communication en alternance | Je te partage les secrets de l'alternance</span></div></div>
          <p class="li-texte">Si je te dis un secret,
tu ne le répètes à personne ?

J. -c&#x27;est mon boss, chez Mon Fourgon Shop,
et ces dernières semaines, il a eu une petite idée.
(Enfin, on lui a peut-être soufflé avec A.).

Il revient en force après 6 longues années d&#x27;absence.

Parce qu&#x27;entre toi et moi, les 2 posts pour trouver des salariés,
ça ne compte pas vraiment.

Mais pour revenir dans le game,
il lui fallait un coup de pinceau à son profil.

C&#x27;est là que j&#x27;entre en scène.
(Oui, oui la reine des bannières, c&#x27;est moi -et laisse mes chevilles tranquilles)

Alors t&#x27;en penses quoi de cette refonte de bannière ?

———
Hello, moi c&#x27;est Cloé !
☀️ Un concentré du sud en bouteille
🍵 Multi-tâche, multi-lingue et surtout multi-ref
Psst, abonne-toi pour spill the tea !</p>
          <dl><div><dt>impressions</dt><dd>45 042</dd></div><div><dt>réactions</dt><dd>515</dd></div><div><dt>commentaires</dt><dd>38</dd></div><div><dt>abonnés</dt><dd>+31</dd></div></dl>
        </div>
        <div class="caro" aria-roledescription="carrousel" aria-label="Refonte du profil du big boss"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/refonte-1.webp" alt="Refonte du profil du big boss, page 1 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-2.webp" alt="Refonte du profil du big boss, page 2 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-3.webp" alt="Refonte du profil du big boss, page 3 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-4.webp" alt="Refonte du profil du big boss, page 4 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-5.webp" alt="Refonte du profil du big boss, page 5 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-6.webp" alt="Refonte du profil du big boss, page 6 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-7.webp" alt="Refonte du profil du big boss, page 7 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-8.webp" alt="Refonte du profil du big boss, page 8 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-9.webp" alt="Refonte du profil du big boss, page 9 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-10.webp" alt="Refonte du profil du big boss, page 10 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-11.webp" alt="Refonte du profil du big boss, page 11 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-12.webp" alt="Refonte du profil du big boss, page 12 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-13.webp" alt="Refonte du profil du big boss, page 13 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-14.webp" alt="Refonte du profil du big boss, page 14 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-15.webp" alt="Refonte du profil du big boss, page 15 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-16.webp" alt="Refonte du profil du big boss, page 16 sur 17" loading="lazy"><img src="assets/img/labo/linkedin/refonte-17.webp" alt="Refonte du profil du big boss, page 17 sur 17" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 17</span></div>
      </dialog>
      <dialog class="fiche li-modal" id="post-4" aria-label="Post LinkedIn : La petite Cloé vs la big">
        <button type="button" class="fermer" aria-label="Fermer">×</button>
        <div class="li-post">
          <div class="li-tete"><img src="assets/img/labo/linkedin/avatar.webp" alt=""><div><b>Cloé Pérot</b><span>Chargée de communication en alternance | Je te partage les secrets de l'alternance</span></div></div>
          <p class="li-texte">J&#x27;vous parle d&#x27;un temps que les moins de 20 ans ne peuvent pas connaitre.
J&#x27;ai 23 ans, j&#x27;me prends pour qui ?

J&#x27;ai vu une trend.
S. l&#x27;a reprise.
J&#x27;ai adoré.

Alors, moi aussi, je veux la faire à ma façon.

Rien de plus simple.
Mes jouets d&#x27;enfance vs mes applications préférées aujourd&#x27;hui.

Est-ce que tu y vois un lien ?
Parce que clairement, avec tous mes jouets,
j&#x27;avais déjà un bel indice sur mes études.

Elles seraient créatives.

Je veux savoir, c&#x27;était quoi tes jouets prefs&#x27; ?

———
Hello, moi c&#x27;est Cloé !
☀️ Un concentré du sud en bouteille
🍵 Multi-tâche, multi-lingue et surtout multi-ref
Psst, abonne-toi pour spill the tea !</p>
          <dl><div><dt>impressions</dt><dd>28 190</dd></div><div><dt>réactions</dt><dd>286</dd></div><div><dt>commentaires</dt><dd>33</dd></div><div><dt>abonnés</dt><dd>+29</dd></div></dl>
        </div>
        <div class="caro" aria-roledescription="carrousel" aria-label="La petite Cloé vs la big"><div class="caro-piste" tabindex="0"><img src="assets/img/labo/linkedin/jouets-1.webp" alt="La petite Cloé vs la big, page 1 sur 2" loading="lazy"><img src="assets/img/labo/linkedin/jouets-2.webp" alt="La petite Cloé vs la big, page 2 sur 2" loading="lazy"></div><button type="button" class="caro-bt g" aria-label="Page précédente">‹</button><button type="button" class="caro-bt d" aria-label="Page suivante">›</button><span class="caro-n">1 / 2</span></div>
      </dialog>
      </div>
    </article>

    <article class="projet-labo duo" data-cat="perso video" id="montage">
      <div class="cote"><div class="etiquettes"><span>Perso</span><span>Vidéo</span></div>
      <div class="chap"><h2>Vidéo</h2><p class="brief">Des formats courts pour TikTok et les réels Instagram, tournés et montés sur mon temps perso. Et deux vidéos plus longues, un aftermovie du Garorock et Bali, où j'ai récolté des rushs et des sons de plusieurs vidéos pour les remonter à ma façon.</p>
      <ul class="competences"><li>Montage</li><li>Rythme &amp; transitions</li><li>Choix du son</li><li>Formats verticaux</li></ul></div></div>
      <div class="medias">
        <h3 class="mv-titre">Les formats courts</h3>
        <div class="reels mv-courts"><figure><div class="vid"><video class="reel" src="assets/video/mv_saintsernin.mp4" poster="assets/img/labo/video/mv_saintsernin.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo à Saint-Sernin"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Saint-Sernin</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_concert.mp4" poster="assets/img/labo/video/mv_concert.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo d'un concert"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Concert</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_ariege.mp4" poster="assets/img/labo/video/mv_ariege.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo en Ariège"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Ariège</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_photo.mp4" poster="assets/img/labo/video/mv_photo.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo autour d'un appareil photo"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Appareil photo</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_moodboard.mp4" poster="assets/img/labo/video/mv_moodboard.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo façon moodboard"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Moodboard</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_chiens.mp4" poster="assets/img/labo/video/mv_chiens.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo de chiens"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Les chiens</figcaption></figure><figure><div class="vid"><video class="reel" src="assets/video/mv_carthel.mp4" poster="assets/img/labo/video/mv_carthel.webp" autoplay muted loop playsinline preload="metadata" aria-label="Montage vidéo au bar Carthel"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption>Le Carthel</figcaption></figure></div>
        <h3 class="mv-titre">Les montages longs</h3>
        <div class="reels mv-longs"><figure><div class="vid"><video class="reel paysage" src="assets/video/mv_garorock.mp4" poster="assets/img/labo/video/mv_garorock.webp" muted loop playsinline preload="none" aria-label="Aftermovie du festival Garorock, remonté à partir de rushs"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Aftermovie Garorock</b>rushs et sons récoltés, remontés par moi</figcaption></figure><figure><div class="vid"><video class="reel paysage" src="assets/video/mv_bali.mp4" poster="assets/img/labo/video/mv_bali.webp" muted loop playsinline preload="none" aria-label="Montage vidéo de Bali, à partir de rushs"></video><button type="button" class="son-bt" aria-label="Activer ou couper le son"></button></div><figcaption><b>Bali</b>rushs et sons récoltés, remontés par moi</figcaption></figure></div>
      </div>
    </article>

    <article class="projet-labo duo" data-cat="perso photo" id="photo" style="border:0">
      <div class="cote"><div class="etiquettes"><span>Perso</span><span>Photographie</span></div>
      <div class="chap"><h2>Photographie</h2><p class="brief">Ce que je regarde quand je n'ai pas de brief : des façades, des couleurs, des lacs de montagne et un chien qui pose très bien.</p>
      <ul class="competences"><li>Cadrage</li><li>Lumière</li><li>Œil couleur</li></ul></div></div>
      <div class="medias"><div class="photos"><a class="zoom" href="assets/img/labo/photo/camden.webp" style="--r:0.75"><img src="assets/img/labo/photo/camden.webp" alt="Façade peinte avec une tête d'éléphant à Camden, Londres" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/sacre-coeur.webp" style="--r:0.75"><img src="assets/img/labo/photo/sacre-coeur.webp" alt="Les dômes du Sacré-Cœur au soleil couchant" loading="lazy"></a><a class="zoom" href="assets/img/moi/lac-braies.webp" style="--r:1.778"><img src="assets/img/moi/lac-braies.webp" alt="Un lac de montagne entouré de sapins, dans les Dolomites" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/mustang.webp" style="--r:0.75"><img src="assets/img/labo/photo/mustang.webp" alt="La calandre d'une Mustang jaune et noire" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/chapelle-crete.webp" style="--r:0.75"><img src="assets/img/labo/photo/chapelle-crete.webp" alt="Une chapelle blanche et bleue au bord de la mer en Crète" loading="lazy"></a><a class="zoom" href="assets/img/moi/atlas-sommets.webp" style="--r:0.5625"><img src="assets/img/moi/atlas-sommets.webp" alt="Mon chien devant des sommets rocheux" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/peintre-montmartre.webp" style="--r:0.75"><img src="assets/img/labo/photo/peintre-montmartre.webp" alt="Les toiles d'un peintre de rue à Montmartre" loading="lazy"></a><a class="zoom" href="assets/img/mont-jour.webp" style="--r:1.778"><img src="assets/img/mont-jour.webp" alt="Des sommets calcaires au-dessus d'une forêt de mélèzes" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/big-ben.webp" style="--r:0.75"><img src="assets/img/labo/photo/big-ben.webp" alt="Le cadran de Big Ben" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/passerelle.webp" style="--r:0.75"><img src="assets/img/labo/photo/passerelle.webp" alt="Une passerelle en bois au-dessus d'une rivière transparente" loading="lazy"></a><a class="zoom" href="assets/img/moi/lac-foret.webp" style="--r:1.778"><img src="assets/img/moi/lac-foret.webp" alt="Un lac turquoise au pied de la forêt" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/notting-hill.webp" style="--r:0.75"><img src="assets/img/labo/photo/notting-hill.webp" alt="Façades bleue et blanches à Notting Hill" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/bonifacio.webp" style="--r:0.75"><img src="assets/img/labo/photo/bonifacio.webp" alt="La citadelle de Bonifacio sous un ciel bleu" loading="lazy"></a><a class="zoom" href="assets/img/moi/atlas-lac.webp" style="--r:0.5625"><img src="assets/img/moi/atlas-lac.webp" alt="Mon chien assis au bord d'un lac" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/crete-baie.webp" style="--r:0.75"><img src="assets/img/labo/photo/crete-baie.webp" alt="Une baie turquoise en Crète" loading="lazy"></a><a class="zoom" href="assets/img/moi/lac-nuages.webp" style="--r:1.778"><img src="assets/img/moi/lac-nuages.webp" alt="Un lac sous les nuages, montagnes en reflet" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/immeuble-paris.webp" style="--r:0.75"><img src="assets/img/labo/photo/immeuble-paris.webp" alt="Un immeuble haussmannien et son dôme d'ardoise" loading="lazy"></a><a class="zoom" href="assets/img/labo/photo/mont-soir.webp" style="--r:1.788"><img src="assets/img/labo/photo/mont-soir.webp" alt="Une crête de montagne au coucher du soleil" loading="lazy"></a></div></div>
    </article>
    </div>

  </section>
"""
labo += pied()
labo = labo.replace('<script src="assets/pied.js"></script>', """<script src="assets/pied.js"></script>
<script>
{
  let o = 'tout', f = 'tout';
  const projets = [...document.querySelectorAll('.projet-labo')], zone = document.querySelector('.zone-perso');
  const filtre = () => {
    let vus = 0;
    projets.forEach(p => { const c = p.dataset.cat.split(' '), perso = c.includes('perso'); const ok = (o === 'tout' || (o === 'perso') === perso) && (f === 'tout' || c.includes(f)); p.hidden = !ok; if (ok) vus++; });
    document.querySelectorAll('.chapitre').forEach(h => { h.hidden = !projets.some(p => !p.hidden && (p.dataset.cat.includes('perso') ? 'perso' : 'ecole') === h.dataset.o); });
    zone.hidden = !projets.some(p => !p.hidden && p.dataset.cat.includes('perso'));
    document.querySelector('.aucun').hidden = vus > 0;
    const barre = document.querySelector('.barre-labo'); if (barre.getBoundingClientRect().top < 70) scrollTo({ top: barre.parentElement.offsetTop + 20 - 70, behavior: 'smooth' });
  };
  document.querySelectorAll('.onglets button').forEach(b => b.addEventListener('click', () => { o = b.dataset.o; document.querySelectorAll('.onglets button').forEach(x => x.setAttribute('aria-pressed', x === b)); filtre(); }));
  document.querySelectorAll('.filtres button').forEach(b => b.addEventListener('click', () => { f = b.dataset.f; document.querySelectorAll('.filtres button').forEach(x => x.setAttribute('aria-pressed', x === b)); filtre(); }));
  const au = document.getElementById('audio'), bt = document.getElementById('lire'), barre = document.getElementById('barre'), t = document.getElementById('temps');
  const mmss = s => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');
  bt.addEventListener('click', () => au.paused ? au.play() : au.pause());
  au.addEventListener('play', () => { bt.textContent = '❚❚'; bt.setAttribute('aria-label', (window.t || (x => x))('Mettre en pause')); });
  au.addEventListener('pause', () => { bt.textContent = '▶'; bt.setAttribute('aria-label', (window.t || (x => x))('Écouter le podcast')); });
  au.addEventListener('timeupdate', () => { const d = au.duration || 43; barre.firstElementChild.style.width = (au.currentTime / d * 100) + '%'; t.textContent = mmss(au.currentTime) + ' / ' + mmss(d); });

  document.querySelectorAll('.carte-bref').forEach(c => c.addEventListener('click', () => document.getElementById(c.dataset.fiche).showModal()));
  document.querySelectorAll('.lire').forEach(c => c.addEventListener('click', () => { const d = document.getElementById(c.dataset.post); d.showModal(); d.querySelector('.caro-piste').dispatchEvent(new Event('scroll')); }));
  document.querySelectorAll('dialog.fiche').forEach(d => {
    d.querySelector('.fermer').addEventListener('click', () => d.close());
    d.addEventListener('click', e => { if (e.target === d) d.close(); });
  });
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
.outils li { border: 1px solid var(--ligne); border-radius: 999px; padding: 9px 17px; font-size: 16px; }
.outils-groupes { display: grid; grid-template-columns: 1fr 1fr; gap: 34px 40px; }
.outils-groupes h3 { font-size: 15px; color: var(--lilas); margin: 0 0 14px; font-weight: 700; }
@media (max-width: 800px) { .outils-groupes { grid-template-columns: 1fr; } }"""
ap = head("À propos", "Le parcours, les compétences et les outils de Cloé Pérot, chargée de communication à Toulouse.", ap_css)
ap += """  <div class="ouv" style="min-height:62svh">
    <img src="assets/img/moi/lac-braies.webp" alt="" style="object-position:center 60%">
    <a class="retour" href="index.html">← Accueil</a>
    <h1>Et moi, dans tout ça ?</h1>
  </div>

  <section class="bio">
    <div>
      <p class="accroche-bio">Besoin d'un peu de soleil dans ta journée&nbsp;?</p>
      <p>Moi, c'est Cloé : chargée de com à Toulouse, amoureuse de la vie, avec un penchant pour l'aventure, le digital, la création… et les rires contagieux.</p>
      <p>Je cherche mon prochain poste en com, à Toulouse ou dans les Pyrénées : chargée de communication, responsable communication, chef de projet digital ou social media manager. (Le titre exact, on en discute. Ce qui est sûr : j'ai envie d'aller plus loin que le community management.)</p>
      <p>Et quand je ne suis pas derrière mon écran, je suis sûrement en rando avec Atlas, mon berger australien.</p>
      <div class="btns"><a class="b plein" href="mailto:cloe.perot@icloud.com">Me contacter</a><a class="b ligne" href="#" title="Bientôt disponible">Mon CV</a></div>
    </div>
    <img src="assets/img/moi/cloe-atlas.webp" alt="Cloé et Atlas, son berger australien, en randonnée dans les Dolomites" style="object-position:62% 40%">
  </section>

  <section>
    <h2>Pourquoi moi&nbsp;?</h2>
    <p class="sous-titre">Parce que je fais une com qui donne envie de sortir. En trois preuves&nbsp;:</p>
    <div class="preuves"><a class="preuve" href="vancore.html"><strong>×2</strong><h3>Je fais grandir les communautés</h3><p>Chez Vancore, l'Instagram est passé de 3&nbsp;000 à 6&nbsp;002 abonnés. Au Toulouse Social Run, on est passés de 3 coureurs à une cinquantaine par run.</p><span>Voir Vancore ↗</span></a><a class="preuve" href="toulouse-social-run.html"><strong>110+</strong><h3>Je vais sur le terrain</h3><p>Des runs à plus de 110 coureurs, des salons, des festivals, des team buildings : la com, je la vis aussi en vrai, pas seulement derrière un écran.</p><span>Voir le Toulouse Social Run ↗</span></a><a class="preuve" href="vancore.html#influence"><strong>5 pattes</strong><h3>J'apprends vite (très vite)</h3><p>Caissière, secrétaire médicale, préparatrice de commandes… et maintenant la com. Un vrai mouton à 5 pattes&nbsp;: quand l'équipe Vancore s'est réorganisée, j'ai repris l'influence de A à Z.</p><span>Voir l'influence ↗</span></a></div>
  </section>

  <section>
    <h2>Ce que mon CV ne dit pas</h2>
    <div class="funs"><div class="fun"><b>50 livres</b><p>en 2026. Et la pile à côté du lit ne baisse pas.</p></div><div class="fun"><b>Licence d'anglais</b><p>Avant la com, il y avait les mots… en anglais.</p></div><div class="fun"><b>2 km</b><p>Mon record perso. Oui, je fais la com d'un running club.</p></div><div class="fun"><b>Atlas</b><p>Mon berger australien, copilote de rando et star de mes photos.</p></div><div class="fun"><b>Un concentré du sud</b><p>Multi-tâche, multi-lingue et surtout multi-ref.</p></div><a class="fun" href="labo.html#photo"><b>Un œil photo</b><p>Je photographie tout ce qui a une couleur.</p></a></div>
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
          <li><time>2024–2026</time><b>Mastère Content Marketing &amp; Brand Entertainment</b><span>Titre RNCP niveau 7 · Manager de la communication et du marketing digital · INSEEC × Ynov Toulouse</span><span class="memoire">Mémoire&nbsp;: « L'authenticité comme clé de confiance : le brand content face à la saturation informationnelle dans les communautés de niche »</span></li>
          <li><time>2023–2024</time><b>Bachelor 3 Marketing &amp; Communication Création Digitale</b><span>Titre RNCP niveau 6 · Chef de projets digitaux, option E-business · EEMI × Ynov Toulouse</span></li>
          <li><time>2019–2023</time><b>Licence d'Études Anglophones (LLCER)</b><span>Université Toulouse Jean Jaurès</span></li>
          <li><time>2019</time><b>Baccalauréat Économique &amp; Social</b><span>spécialité Économie approfondie · Lycée Clémence Royer, Fonsorbes</span></li>
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
    <div class="outils-groupes"><div><h3>Création & vidéo</h3><ul class="outils"><li>Illustrator</li><li>InDesign</li><li>Photoshop</li><li>Premiere Pro</li><li>Affinity</li><li>Canva</li><li>Figma</li><li>CapCut</li></ul></div><div><h3>IA</h3><ul class="outils"><li>Claude</li><li>ChatGPT</li><li>Gemini</li><li>Nano Banana</li><li>Midjourney</li><li>Lovable</li></ul></div><div><h3>Web, réseaux & emailing</h3><ul class="outils"><li>WordPress</li><li>GitHub</li><li>Meta Business Suite</li><li>Google Analytics</li><li>Klaviyo</li><li>Brevo</li></ul></div><div><h3>Organisation & relation client</h3><ul class="outils"><li>Notion</li><li>Asana</li><li>Trello</li><li>Freshdesk</li><li>Ekan / Evo</li></ul></div></div>
  </section>
"""
ap += pied()
open("a-propos.html", "w").write(ap)
print("ok")

import subprocess, sys
subprocess.run([sys.executable, "outils/i18n_inject.py", "toulouse-social-run.html", "community-manager.html", "labo.html", "a-propos.html"], check=True)
