const menu = document.getElementById('menu');
const ouv = document.querySelector('.ouv');
const seuil = () => ouv ? Math.max(40, ouv.offsetTop + ouv.offsetHeight - 90) : 40;
const etatMenu = () => menu.classList.toggle('fond', scrollY > seuil());
addEventListener('scroll', etatMenu, { passive: true }); etatMenu();

// sous-menu : section en cours
const liens = [...document.querySelectorAll('.sommaire a')];
const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  liens.forEach(a => {
    const on = a.getAttribute('href') === '#' + e.target.id;
    a.classList.toggle('actif', on);
    if (on) a.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' });
  });
}), { rootMargin: '-45% 0px -50% 0px' });
document.querySelectorAll('.bloc').forEach(s => io.observe(s));

// visionneuse : une image, ou une petite galerie (data-suite="url::légende|url::légende")
const vue = document.getElementById('vue'), vImg = vue.querySelector('img'), vTxt = vue.querySelector('p');
vue.querySelectorAll('button').forEach((b, k) => k ? b.remove() : b.classList.add('fermer'));
const prec = Object.assign(document.createElement('button'), { type: 'button', className: 'nav prec', textContent: '←' });
const suiv = Object.assign(document.createElement('button'), { type: 'button', className: 'nav suiv', textContent: '→' });
const cpt = Object.assign(document.createElement('span'), { className: 'cpt' });
prec.setAttribute('aria-label', 'Image précédente'); suiv.setAttribute('aria-label', 'Image suivante');
vue.append(prec, suiv, cpt);
let liste = [], pos = 0;
const affiche = () => {
  const [src, alt] = liste[pos];
  vImg.src = src; vImg.alt = alt; vTxt.textContent = alt;
  const plusieurs = liste.length > 1;
  prec.hidden = suiv.hidden = cpt.hidden = !plusieurs;
  cpt.textContent = (pos + 1) + ' / ' + liste.length;
};
const bouge = d => { if (liste.length > 1) { pos = (pos + d + liste.length) % liste.length; affiche(); } };
document.querySelectorAll('a.zoom').forEach(a => {
  const suite = (a.dataset.suite || '').split('|').filter(Boolean).map(x => x.split('::'));
  if (suite.length) { a.classList.add('serie'); a.dataset.n = '1 / ' + (suite.length + 1); }
  a.addEventListener('click', ev => {
    ev.preventDefault();
    const i = a.querySelector('img');
    liste = [[a.href, i.alt], ...suite.map(([u, t]) => [u, t || i.alt])]; pos = 0;
    affiche(); vue.showModal();
  });
});
prec.addEventListener('click', () => bouge(-1));
suiv.addEventListener('click', () => bouge(1));
vue.addEventListener('keydown', e => { if (e.key === 'ArrowLeft') bouge(-1); if (e.key === 'ArrowRight') bouge(1); });
let x0 = null;
vue.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
vue.addEventListener('touchend', e => { if (x0 === null) return; const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) bouge(dx < 0 ? 1 : -1); x0 = null; });
vue.addEventListener('click', ev => { if (ev.target === vue || ev.target.classList.contains('fermer')) vue.close(); });

// réels : le son sur chacun, et celui qu'on survole passe devant
document.querySelectorAll('.reels').forEach(zone => {
  const figs = [...zone.querySelectorAll('figure')];
  const coupe = (sauf) => figs.forEach(f => { if (f !== sauf) { const v = f.querySelector('video'); v.muted = true; f.classList.remove('son'); } });
  const son = (f, on) => {
    const v = f.querySelector('video');
    if (on) { coupe(f); v.muted = false; v.play().catch(() => { v.muted = true; f.classList.remove('son'); v.play(); }); }
    else v.muted = true;
    f.classList.toggle('son', on && !v.muted);
  };
  figs.forEach(f => {
    const b = f.querySelector('.son-bt');
    b.addEventListener('click', e => { e.stopPropagation(); son(f, f.querySelector('video').muted); });
    if (matchMedia('(hover: hover)').matches) {
      f.addEventListener('mouseenter', () => son(f, true));
      f.addEventListener('mouseleave', () => son(f, false));
    }
  });
});
