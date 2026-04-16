import re

f = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8')
c = f.read()
f.close()

# Fix todos los <tdclass= -> <td class= en una sola pasada
fixed = re.sub(r'<tdclass=', '<td class=', c)

# Fix también <td class=""> vacías (alcance sin clase) -> <td>
fixed = re.sub(r'<td class="">', '<td>', fixed)

# Contar cuántos se arreglaron
n = c.count('<tdclass=')
print(f'Tags rotos encontrados y arreglados: {n}')

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(fixed)
print('ok', len(fixed))
