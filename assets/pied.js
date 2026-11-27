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
