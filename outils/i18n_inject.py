# Ajoute le script de traduction juste avant le premier script de fin de page
import re, sys, pathlib
TAG = '<script src="assets/i18n.js"></script>\n'
for f in sys.argv[1:]:
    p = pathlib.Path(f); s = p.read_text()
    if 'assets/i18n.js' in s: continue
    m = re.search(r'<script src="assets/projet\.js"></script>', s) or re.search(r'\n<script>\n', s[s.index('</main>') if '</main>' in s else 0:])
    if '<script src="assets/projet.js"></script>' in s:
        s = s.replace('<script src="assets/projet.js"></script>', TAG + '<script src="assets/projet.js"></script>', 1)
    else:
        i = s.index('<script>', s.rindex('</footer>') if '</footer>' in s else 0)
        s = s[:i] + TAG + s[i:]
    p.write_text(s)
