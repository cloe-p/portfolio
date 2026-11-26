{
  const pied = document.querySelector('footer');
  const titre = pied && pied.querySelector('h2');
  if (titre) {
    titre.setAttribute('aria-label', titre.textContent);
    titre.innerHTML = [...titre.textContent].map((c, i) => c === ' ' ? ' ' : `<span class="l" aria-hidden="true" style="--i:${i}">${c}</span>`).join('');
    new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) pied.classList.add('joue'); }), { threshold: 0.35 }).observe(pied);
  }
}
