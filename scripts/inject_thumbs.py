f = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8')
c = f.read()
f.close()

# Agregar CSS para thumbnails — mínimo, dentro del estilo existente
thumb_css = """
/* thumbnails tabla */
.thumb-cell{width:56px;text-align:center!important;}
.thumb-wrap{display:block;width:48px;height:48px;border-radius:6px;overflow:hidden;margin:0 auto;position:relative;border:1px solid var(--gray2);}
.thumb-wrap img{width:100%;height:100%;object-fit:cover;display:block;}
.thumb-wrap .play-icon{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,.3);}
.thumb-wrap .play-icon::after{content:'▶';font-size:12px;color:white;line-height:1;}
"""

c = c.replace('</style>', thumb_css + '</style>', 1)

# Datos de posts con thumbnails reales (ordenados por alcance)
posts = [
  {"date":"8 MAR",  "type":"IMAGE",          "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/644612678_122103950007265691_7080597214042140976_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=Asgphyu5T24Q7kNvwH9B3iA&_nc_oc=Adoy5eG8FHdNydgdBatKxINJSrjE1maRatZFSJceUa-va3rdvnh-ZANzJYamaRY1BJ0&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af0mTqfZIHWj5r66KASlNXohNEBVZcawQ_uvlX6lb3dkoQ&oe=69E6E183", "url":"https://www.instagram.com/p/DVoBje8Ekio/", "content":"Día Internacional de la Mujer — Equipo Arichy", "prop":"General", "prop_cls":"prop-gen", "reach":693, "likes":66, "comments":1, "shares":7, "saved":2, "rank":"top", "fmt":"fmt-img"},
  {"date":"22 MAR", "type":"VIDEO",           "thumb":"https://scontent.cdninstagram.com/v/t51.82787-15/656279327_18012583208832482_3404356448503105540_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=SFThZbbBKAgQ7kNvwGBu68H&_nc_oc=AdqMXQtXC2T9B8WlOqaAevUCrHngNIZunFMcWMVgQNwi_ier4qNl11xiv9vdG3vYfPE&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&_nc_tpa=Q5bMBQF3kiFm2kPY2pJE50gPO7ZvIr93plRuk9pvdBQzQTZbqEslsIegYhvfY0X6RqHlQDhuOHZ54QuvVA&oh=00_Af0EGO2hcnlehCk8_8Guy16Z8-SXPcnR-NCiJhWXU0xgwQ&oe=69E6EBD6", "url":"https://www.instagram.com/reel/DWNJYFTgVkg/", "content":"One Circle — Trusted by Leaders", "prop":"Cap Cana", "prop_cls":"prop-gua", "reach":384, "likes":19, "comments":1, "shares":8, "saved":0, "rank":"alto", "fmt":"fmt-reel"},
  {"date":"28 MAR", "type":"VIDEO",           "thumb":"https://scontent.cdninstagram.com/v/t51.82787-15/657370266_18013300814832482_7404703796889365901_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=53C1WcD1EdoQ7kNvwFogJT4&_nc_oc=AdpAnJKGJGg7l3XSE3ig53q8LBgRHpTxIkBbC83KFJ3h_iOHg71t1e5W2ckz8hBbSWU&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&_nc_tpa=Q5bMBQEyE6W8EDHtYFKPzAAbSRoZlQzZZ9rifaMi6noFcjuew2Ae5LEKLk-niBidOG-tySLKreDHZwMfhg&oh=00_Af3daXNX76QO0h9qgNy9gf5gkYcjwxrQtLY376qCCtP-7g&oe=69E6DBDB", "url":"https://www.instagram.com/reel/DWb44wxjGGM/", "content":"Testimonio — Elena Rusinova (confianza)", "prop":"Testimonio", "prop_cls":"prop-gen", "reach":313, "likes":8, "comments":0, "shares":5, "saved":0, "rank":"alto", "fmt":"fmt-reel"},
  {"date":"16 MAR", "type":"VIDEO",           "thumb":"https://scontent.cdninstagram.com/v/t51.82787-15/653969041_18011726705832482_7742152191021193333_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=107&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=kQzznnlQ578Q7kNvwH8Q3F0&_nc_oc=Adqv5pBH3RZfMYeG_5PBWvYCToL35sVTpUlKAjW1SVAUXqg726UmR3xV9H1FRM-dbTU&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&_nc_tpa=Q5bMBQEUBYwj3k32CGCMMm9TiqrkJ-xi94ZgiO-2Sc1i3tGaPDZp7zbPLK_2LeM1QVu0y7P_Jb7S15yQBQ&oh=00_Af0yZ6ZyY7Wd9fvOgqrnUuj80cwSQBHUE8w0sijCPCIG_g&oe=69E6DC8E", "url":"https://www.instagram.com/reel/DV8xFiYlb0U/", "content":"Vista Alta A401 — Strategic Allocation", "prop":"Vista Alta", "prop_cls":"prop-vista", "reach":283, "likes":9, "comments":0, "shares":9, "saved":1, "rank":"bueno", "fmt":"fmt-reel"},
  {"date":"16 MAR", "type":"VIDEO",           "thumb":"https://scontent.cdninstagram.com/v/t51.82787-15/652723497_18011780585832482_5468949667955565969_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=103&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=jAWNtXRJ4OcQ7kNvwEWVF-_&_nc_oc=Adq1QUgBeKRG51f12qx9elosg9Ufev7f8sDZrwTj8sHan7khiKIEWw0jHsUZAby8pE0&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&_nc_tpa=Q5bMBQFODjChB4LjpKH6OYU22xyAP1K39hjnINXA7j5NlRIfzUQV7_a_qPgvJU4KBQI8MckVFCvhfG3Mfw&oh=00_Af2eDYoUSheo44HezRs6HwFJbzVprtEJpxI9nxqv_t3rjw&oe=69E706E3", "url":"https://www.instagram.com/reel/DV9oanxCv0Y/", "content":"Dezenove, Cap Cana — Final stage", "prop":"Dezenove", "prop_cls":"prop-dez", "reach":238, "likes":4, "comments":0, "shares":10, "saved":0, "rank":"bueno", "fmt":"fmt-reel"},
  {"date":"19 MAR", "type":"VIDEO",           "thumb":"https://scontent.cdninstagram.com/v/t51.82787-15/654606996_18012168983832482_6654545127296531899_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0xJUFMuYmVzdF9pbWFnZV91cmxnZW4uQzMifQ%3D%3D&_nc_ohc=ZKeFxKRe_hYQ7kNvwFqF0el&_nc_oc=AdqpVx2fB0LjwnOsSP50SYDNh6WnFMiPn5Y1Z2729T5mR_wgfa11nCA4k9tbenZ5v9Q&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&_nc_tpa=Q5bMBQEJ6CDxj0RHF_Htiw_viXbxDBJR0Oyzbp-s8_ksrzPvfLC4QRVhDRiA1s-y2_XcxkBv5lwaIi1TPg&oh=00_Af0CslMSskXNqtJrZuhWU9-pPpkiTQ6oDkdDdijYxO9c6g&oe=69E6E464", "url":"https://www.instagram.com/reel/DWFKHaljFah/", "content":"Aquamarina 1224 — Living at the Marina", "prop":"Aquamarina", "prop_cls":"prop-aq", "reach":235, "likes":6, "comments":0, "shares":9, "saved":2, "rank":"bueno", "fmt":"fmt-reel"},
  {"date":"28 MAR", "type":"IMAGE",           "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/661153475_122107592943265691_5396622749598373041_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=105&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=9qVDcmrjtOAQ7kNvwEu3v5U&_nc_oc=AdrcIEYoDfcPsrgtahnbMfutNcihlFAYNQ1T8S-IliSE0C7q5q4nSuOEtb4g1BvElvE&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af37ycmlezS5z7yrZPkwk58ebkBv5SHXJvs4T6jNZhkgRw&oe=69E70E8F", "url":"https://www.instagram.com/p/DWcbHv1E3IQ/", "content":"Blog — Cap Cana vs Punta Cana inversión", "prop":"Blog", "prop_cls":"prop-blog", "reach":147, "likes":5, "comments":0, "shares":0, "saved":0, "rank":"normal", "fmt":"fmt-img"},
  {"date":"6 MAR",  "type":"CAROUSEL_ALBUM",  "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/643433220_122103277179265691_3606340222791259012_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=106&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=jsyFdKeBtrYQ7kNvwG_7S5N&_nc_oc=Adrb4G_B0sCtVilCSD0FbE1LYHK2i9N-P1vTyb9AABf0VIdjA-NMY4lWFFTgB2meMbI&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af34OBKfNOfa_9avNY3si6ZsakAHIFXhwgHeNhmiZjDQiw&oe=69E6E505", "url":"https://www.instagram.com/p/DVj3fEmDXak/", "content":"CONFOTUR — Tax Benefits para inversores", "prop":"Educativo", "prop_cls":"prop-gen", "reach":142, "likes":5, "comments":0, "shares":5, "saved":0, "rank":"normal", "fmt":"fmt-carru"},
  {"date":"10 MAR", "type":"CAROUSEL_ALBUM",  "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/646808652_122104421937265691_5213250855014669665_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=108&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=C_yg16QuNh0Q7kNvwFhtj7j&_nc_oc=AdoupMiBpvrihUrAW4ooCiSq287tyoak2nu2fT0IZYrgdsVsEezIwukOBlICez5abxk&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af2Tjsk3YUlsPd6ZBatYAkcvdBBHgItYJSGe8H-w9gcsRw&oe=69E70402", "url":"https://www.instagram.com/p/DVuEvYtgVvW/", "content":"Early Entry Cap Cana — equity curve", "prop":"Educativo", "prop_cls":"prop-gen", "reach":136, "likes":10, "comments":0, "shares":4, "saved":0, "rank":"normal", "fmt":"fmt-carru"},
  {"date":"20 MAR", "type":"IMAGE",           "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/648737200_122104563735265691_3194064679154793085_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=100&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=SjVM-EhzGUAQ7kNvwGrIZ8q&_nc_oc=AdojEk8YNCI4hH8Au9m2UnAI8eNJyQHeb-MrQzfR7L3EY4vMJQd8X8lZL3iSHbaJpzo&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af2vvAGVeebppJY0o4cJwUMGgtZFxw81OCFlBTctlH6k3w&oe=69E6F545", "url":"https://www.instagram.com/p/DWHItJnFeex/", "content":"Spring 2026 — Click to Key roadmap", "prop":"Educativo", "prop_cls":"prop-gen", "reach":133, "likes":7, "comments":0, "shares":4, "saved":0, "rank":"normal", "fmt":"fmt-img"},
  {"date":"18 MAR", "type":"CAROUSEL_ALBUM",  "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/654253441_122106054789265691_5396493419457122917_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiQ0FST1VTRUxfSVRFTS5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=S9xTWJvgAUAQ7kNvwFpooma&_nc_oc=Adpr-o4-PFE6Akh19Z0PRks-WGlL6xmwYdV3UWIwmUfVdo-y9fnVA1bB3_VqP5jm7H0&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af132pij9X-mjRssaLFl_hm1DgIlML387bl0dOsXluKIHA&oe=69E6E05C", "url":"https://www.instagram.com/p/DWB8RCdAfnQ/", "content":"Roadmap 4 pasos — Click to Key", "prop":"Educativo", "prop_cls":"prop-gen", "reach":110, "likes":7, "comments":0, "shares":4, "saved":0, "rank":"normal", "fmt":"fmt-carru"},
  {"date":"17 MAR", "type":"IMAGE",           "thumb":"https://scontent.cdninstagram.com/v/t39.30808-6/648622966_122104564311265691_3354054771136852472_n.jpg?stp=dst-jpg_e35_tt6&_nc_cat=110&ccb=7-5&_nc_sid=18de74&efg=eyJlZmdfdGFnIjoiRkVFRC5iZXN0X2ltYWdlX3VybGdlbi5DMyJ9&_nc_ohc=7uIcyoaTfOYQ7kNvwH8kyxd&_nc_oc=Ado7v_j6xqLNzIoDs66Xurt_N8eEKNqazaMmG2FqeNkRI8KyGHPIg0ThKXl9IWx-tGw&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&_nc_gid=LXk8X2GeS2wHacP0k4We5Q&oh=00_Af2pmQuA3tKpuW-lzGLGWVyaucRDXuyWda1IMPfq77STrg&oe=69E6EDE6", "url":"https://www.instagram.com/p/DWAGRxdAfvf/", "content":"Capital Efficiency — Wealth strategy", "prop":"Educativo", "prop_cls":"prop-gen", "reach":119, "likes":5, "comments":0, "shares":6, "saved":1, "rank":"normal", "fmt":"fmt-img"},
]

def rank_html(r):
    if r == "top":    return '<span class="star">★ Top</span>'
    if r == "alto":   return '<span class="star">★ Alto</span>'
    if r == "bueno":  return 'Bueno'
    return 'Normal'

def fmt_label(t):
    if t == "VIDEO":          return 'Reel'
    if t == "CAROUSEL_ALBUM": return 'Carrusel'
    return 'Imagen'

def fmt_cls(t):
    if t == "VIDEO":          return 'fmt-reel'
    if t == "CAROUSEL_ALBUM": return 'fmt-carru'
    return 'fmt-img'

def thumb_html(p):
    is_video = p["type"] == "VIDEO"
    play = '<div class="play-icon"></div>' if is_video else ''
    return f'<a href="{p["url"]}" target="_blank" class="thumb-wrap"><img src="{p["thumb"]}" alt="" loading="lazy">{play}</a>'

def row_class(p):
    return ' class="td-top"' if p["rank"] == "top" else ''

rows = []
for p in posts:
    rc = row_class(p)
    rows.append(f"""          <tr{rc}>
            <td class="thumb-cell">{thumb_html(p)}</td>
            <td class="td-date">{p["date"]}</td>
            <td><span class="fmt {fmt_cls(p["type"])}">{fmt_label(p["type"])}</span></td>
            <td class="td-left">{p["content"]} <span class="prop {p['prop_cls']}">{p["prop"].upper()}</span></td>
            <td class="{('td-pink td-bold' if p['reach'] > 400 else 'td-bold') if p['reach'] > 200 else ''}">{p["reach"]}</td>
            <td{'class="td-bold"' if p['likes'] > 20 else ''}>{p["likes"]}</td>
            <td>{p["comments"]}</td>
            <td{'class="td-bold"' if p['shares'] > 7 else ''}>{p["shares"]}</td>
            <td>{p["saved"]}</td>
            <td>{rank_html(p["rank"])}</td>
          </tr>""")

new_table = """    <div class="table-wrap"><table>
      <thead class="ig-head"><tr>
        <th class="thumb-cell">Preview</th>
        <th>Fecha</th><th>Tipo</th><th class="tl">Contenido / Propiedad</th>
        <th>Alcance</th><th>Likes</th><th>Coment.</th><th>Shares</th><th>Guardados</th><th>Rendimiento</th>
      </tr></thead>
      <tbody>
""" + "\n".join(rows) + """
      </tbody>
    </table></div>
    <p class="note">★ Top = publicación de mayor rendimiento del mes · Click en la miniatura para ver el post en Instagram · Datos vía Instagram Graph API v19.0 en tiempo real</p>"""

# Reemplazar la tabla original (sin thumbnail) por la nueva (con thumbnail)
old_header = """    <div class="table-wrap"><table>
      <thead class="ig-head"><tr>
        <th>Fecha</th><th>Tipo</th><th class="tl">Contenido / Propiedad</th><th>Alcance</th><th>Likes</th><th>Coment.</th><th>Shares</th><th>Guardados</th><th>Rendimiento</th>
      </tr></thead>"""

if old_header in c:
    # Encontrar el cierre de esa tabla
    idx_start = c.index(old_header)
    idx_end = c.index('</table></div>\n    <p class="note">★ Top', idx_start) + len('</table></div>\n    <p class="note">★ Top = publicación de mayor rendimiento del mes · Datos obtenidos vía Instagram Graph API v19.0 en tiempo real</p>')
    c = c[:idx_start] + new_table + c[idx_end:]
    print('tabla reemplazada ok')
else:
    print('ERROR: no se encontró la tabla original')
    print(repr(c[c.find('ig-head'):c.find('ig-head')+200]))

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('ok', len(c))
