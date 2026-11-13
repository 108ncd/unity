import pathlib, shutil
HERE = pathlib.Path(__file__).resolve().parent
S = HERE/'src'; GH = HERE.parent; AR = HERE/'artifact'
GH.mkdir(exist_ok=True); AR.mkdir(exist_ok=True)
pages = [('index','Spiritual Unity Movement','Home','How the world\'s traditions relate: many paths, one ocean of love.'),
         ('bhakti','Bhakti · Spiritual Unity Movement','Bhakti','Words of love for God from prophets and saints across traditions.'),
         ('themes','Themes · Spiritual Unity Movement','Themes','Six themes on bhakti, karma, awareness, pitfalls, psychology and the holy name.'),
         ('what-is-bhakti','What Is Bhakti? · Spiritual Unity Movement','What is bhakti?','Bhakti as sanatana-dharma, the eternal function of the soul: loving service.'),
         ('what-is-karma','What Is Karma? · Spiritual Unity Movement','What is karma?','Karma as the process by which the world teaches us to love without motive and without interruption.'),
         ('karma-stories','Stories from Practice · Spiritual Unity Movement','Stories from practice','Twenty-five accounts from Sergey Lazarev\'s Diagnostics of Karma: destiny, finances, relationships, kindness and health.'),
         ('four-levels','Four Levels of Awareness · Spiritual Unity Movement','Four levels','From body and mind to Brahman, Paramatma and Bhagavan: four levels of self-realisation.'),
         ('pitfalls','Pitfalls on the Path · Spiritual Unity Movement','Pitfalls','What weakens and what nourishes love for God, and how we fall and rise.'),
         ('bhakti-psychology','Bhakti and Psychology · Spiritual Unity Movement','Psychology','How bhakti heals vasanas, trauma and anarthas at the root, in dialogue with modern psychology.'),
         ('kirtan','Kirtan and the Holy Name · Spiritual Unity Movement','Kīrtan','Kirtan and the holy name: calling on God across traditions, and the path given for this age.'),
         ('darshanas','Six Darśanas · Spiritual Unity Movement','Six darśanas','The six Vedic schools of philosophy and their modern echoes.'),
         ('varnashrama','Varṇāśrama · Spiritual Unity Movement','Varṇāśrama','Varṇāśrama as a natural social order that holds modern political systems.')]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Marcellus&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=Tiro+Devanagari+Sanskrit&display=swap">'
NAV = [('index','Home'),('bhakti','Bhakti'),('themes','Themes'),('darshanas','Six darśanas'),('varnashrama','Varṇāśrama')]
THEMES = {'what-is-bhakti','what-is-karma','karma-stories','four-levels','pitfalls','bhakti-psychology','kirtan'}
def nav(cur):
    cur = 'themes' if cur in THEMES else cur
    return ''.join(f'<a href="{p}.html"{" aria-current=\"page\"" if p==cur else ""}>{n}</a>' for p,n in NAV)
for p,title,_,desc in pages:
    body = (S/f'{p}.body.html').read_text()
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="description" content="{desc}">\n{FONTS}\n<link rel="stylesheet" href="style.css">'
    inner = f'''<header class="site-head"><div class="wrap"><a class="brand" href="index.html">Spiritual <span>Unity</span> Movement</a><nav class="site-nav" aria-label="Main">{nav(p)}</nav></div></header>
{body}
<footer class="site-foot"><div class="wrap"><p>The Spiritual Unity Movement offers this site as its own perspective, with respect for every tradition it quotes.</p><p>Quotes are cited to their sources and translators. Spotted an error? Please tell us so we can correct it.</p></div></footer>'''
    full = f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head>\n<body>\n{inner}\n</body>\n</html>\n'
    (GH/f'{p}.html').write_text(full)
    (AR/f'{p}.html').write_text(full if p!='index' else head+'\n'+inner+'\n')
for d in (GH, AR): shutil.copy(S/'style.css', d/'style.css')
(GH/'.nojekyll').write_text('')
