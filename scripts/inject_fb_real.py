c = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8').read()

# CSS fb-card si no existe
fb_css = """
/* Facebook Page section */
.kpi-card.fb-card{background:linear-gradient(135deg,#1e1a2e,#0f1627);border:1px solid rgba(124,58,237,.2);}
.kpi-card.fb-card::after{background:linear-gradient(135deg,rgba(124,58,237,.07) 0%,transparent 60%);}
.kpi-card.fb-card .kpi-lbl{color:#C4B5FD;}
.fb-badge{background:rgba(124,58,237,.15);border:1px solid rgba(124,58,237,.3);color:#C4B5FD;font-size:10px;font-weight:600;padding:2px 8px;border-radius:12px;letter-spacing:.5px;text-transform:uppercase;}
.analysis-block.fb-block{border-left-color:#7C3AED;background:linear-gradient(135deg,#f5f3ff,white 60%);}
.info-box{background:#EFF6FF;border:1px solid #BFDBFE;border-radius:8px;padding:14px 18px;font-size:13px;color:#1D4ED8;margin-bottom:20px;display:flex;gap:10px;align-items:flex-start;}
"""
if 'fb-card' not in c:
    c = c.replace('/* comparativa */', fb_css + '\n/* comparativa */')

# Sección FB con datos REALES (14 fans, sin posts en marzo)
fb_section = """<!-- SECCIÓN 02: FACEBOOK PAGE ORGÁNICO -->
<section class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-accent" style="background:#7C3AED"></div>
      <div class="section-title-block">
        <span class="section-num">02</span>
        <span class="section-title">Facebook Page — Arichy Real Estate</span>
        <span class="fb-badge">● Facebook Page API</span>
      </div>
    </div>
    <p class="desc">Datos obtenidos directamente de la <strong>Facebook Page API</strong> para la página <strong>Arichy Real Estate</strong> (ID: 976877848844666). La página está activa pero tiene actividad orgánica mínima en este período.</p>

    <div class="kpi-grid kpi-grid-4">
      <div class="kpi-card fb-card">
        <div class="kpi-val">14</div>
        <div class="kpi-lbl">Fans totales</div>
        <div class="kpi-vs">Audiencia de la Fan Page</div>
      </div>
      <div class="kpi-card fb-card">
        <div class="kpi-val" style="font-size:22px">0</div>
        <div class="kpi-lbl">Posts en marzo</div>
        <div class="kpi-vs">Sin publicaciones en el período</div>
      </div>
      <div class="kpi-card fb-card">
        <div class="kpi-val" style="font-size:22px">0</div>
        <div class="kpi-lbl">Alcance orgánico</div>
        <div class="kpi-vs">Sin actividad registrada</div>
      </div>
      <div class="kpi-card fb-card">
        <div class="kpi-val" style="font-size:22px">0</div>
        <div class="kpi-lbl">Engagement total</div>
        <div class="kpi-vs">Sin interacciones en el período</div>
      </div>
    </div>

    <div class="info-box">
      <span style="font-size:16px;flex-shrink:0">💡</span>
      <div><strong>Oportunidad estratégica:</strong> La Fan Page tiene solo 14 seguidores y no registró publicaciones en marzo 2026. La estrategia de contenido orgánico de Arichy está concentrada en Instagram (@arichyrealestate · 1,889 seguidores). Se recomienda evaluar si activar Facebook como canal secundario o mantener el foco en Instagram + Meta Ads como vía pagada.</div>
    </div>

    <div class="analysis-grid">
      <div class="analysis-block fb-block">
        <div class="analysis-title">📊 Estado actual de la Fan Page</div>
        <div class="analysis-text">La página existe y está activa en Meta Business Suite, pero no tiene estrategia de contenido orgánico activa en Facebook. Los 14 fans son la audiencia acumulada desde su creación.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">🎯 Recomendación</div>
        <div class="analysis-text">Si se decide activar Facebook orgánico, el contenido más eficiente sería <strong>compartir los mismos Reels de Instagram</strong> en la página de Facebook — duplica el alcance sin producción adicional, y Meta los favorece en distribución.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">📣 Meta Ads sí está activo</div>
        <div class="analysis-text">La cuenta de Meta Ads (vinculada a esta Fan Page) sí tiene actividad pagada en marzo: <strong>$112.13 USD gastados</strong>, 70,904 personas alcanzadas, CPC $0.042. El canal pagado funciona correctamente.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">📈 Próximo paso</div>
        <div class="analysis-text">Empezar a publicar en Facebook al menos <strong>2–3 veces por semana</strong> usando el contenido ya producido para Instagram. La API ya está conectada y las métricas se jalarán automáticamente en el próximo informe.</div>
      </div>
    </div>
  </div>
</section>

"""

# Renumerar secciones si no están ya renumeradas
if '<span class="section-num">02</span><span class="section-title">Meta Ads' in c:
    c = c.replace(
        '<span class="section-num">02</span><span class="section-title">Meta Ads',
        '<span class="section-num">03</span><span class="section-title">Meta Ads'
    )
if '<span class="section-num">03</span><span class="section-title">Mail Marketing' in c:
    c = c.replace(
        '<span class="section-num">03</span><span class="section-title">Mail Marketing',
        '<span class="section-num">04</span><span class="section-title">Mail Marketing'
    )
if '<span class="section-num">04</span><span class="section-title">Próximos Pasos' in c:
    c = c.replace(
        '<span class="section-num">04</span><span class="section-title">Próximos Pasos',
        '<span class="section-num">05</span><span class="section-title">Próximos Pasos'
    )

# Eliminar sección FB anterior si ya existe (la que tenía el warning de pendiente)
import re
# Quitar bloque anterior si ya fue insertado
old_fb = re.search(r'<!-- SECCIÓN 02: FACEBOOK PAGE ORGÁNICO -->.*?</section>\n\n', c, re.DOTALL)
if old_fb:
    c = c[:old_fb.start()] + c[old_fb.end():]
    print('Sección FB anterior eliminada')

# Insertar antes de la sección Meta Ads
m = re.search(r'<section class="section"[^>]*>\s*<div class="container">\s*<div class="section-header">[^<]*<div class="section-accent" style="background:#3B82F6"', c)
if m:
    c = c[:m.start()] + fb_section + c[m.start():]
    print('OK - FB section insertada con datos reales')
else:
    idx = c.find('<span class="section-num">03</span><span class="section-title">Meta Ads')
    if idx > 0:
        sec = c.rfind('<section class="section"', 0, idx)
        c = c[:sec] + fb_section + c[sec:]
        print('OK - fallback')
    else:
        print('ERROR')

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('ok', len(c))
