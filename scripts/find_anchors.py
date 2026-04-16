c = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8').read()
# Buscar todos los section-num y el contexto alrededor
import re
for m in re.finditer(r'section-num[^>]*>[^<]+<', c):
    print(m.start(), repr(c[m.start()-50:m.start()+100]))
    print('---')
