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

// visionneuse
const vue = document.getElementById('vue'), vImg = vue.querySelector('img'), vTxt = vue.querySelector('p');
document.querySelectorAll('a.zoom').forEach(a => a.addEventListener('click', ev => {
  ev.preventDefault();
  const i = a.querySelector('img');
  vImg.src = a.href; vImg.alt = i.alt; vTxt.textContent = i.alt;
  vue.showModal();
}));
vue.addEventListener('click', ev => { if (ev.target !== vImg) vue.close(); });
