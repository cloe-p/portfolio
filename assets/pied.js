{
  const pied = document.querySelector('footer');
  const titre = pied && pied.querySelector('h2');
  if (titre) {
    titre.setAttribute('aria-label', titre.textContent);
    titre.innerHTML = [...titre.textContent].map((c, i) => c === ' ' ? ' ' : `<span class="l" aria-hidden="true" style="--i:${i}">${c}</span>`).join('');
    new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) pied.classList.add('joue'); }), { threshold: 0.35 }).observe(pied);
  }
}

// pas de clic droit ni de glisser-déposer sur les images et les vidéos
document.addEventListener('contextmenu', e => { if (e.target.closest('img, video, picture, .zoom, .caro, .vid')) e.preventDefault(); });
document.addEventListener('dragstart', e => { if (e.target.closest('img, video, a')) e.preventDefault(); });

// menu téléphone
{
  const m = document.getElementById('menu'), nav = m && m.querySelector('nav');
  if (nav) {
    const b = document.createElement('button');
    b.type = 'button'; b.className = 'burger'; b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-controls', 'nav-principale');
    b.innerHTML = '<span>Menu</span><i aria-hidden="true"></i>';
    nav.id = 'nav-principale'; m.appendChild(b);
    const bascule = on => { m.classList.toggle('ouvert', on); document.body.classList.toggle('menu-ouvert', on); b.setAttribute('aria-expanded', on); b.firstChild.textContent = on ? 'Fermer' : 'Menu'; };
    b.addEventListener('click', () => bascule(!m.classList.contains('ouvert')));
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => bascule(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape') bascule(false); });
  }
}
