f = open(r'C:\Users\adria\propuestas-mvip\informes\euro-money-marzo-2026.html', encoding='utf-8')
c = f.read()
f.close()
c = c.replace(
    'family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap',
    'family=Geist:wght@300;400;500;600;700;800;900&display=swap'
)
c = c.replace("'Syne'", "'Geist'")
c = c.replace("'DM Sans'", "'Geist'")
open(r'C:\Users\adria\propuestas-mvip\informes\euro-money-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('ok')
