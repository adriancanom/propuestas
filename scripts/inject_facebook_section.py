c = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8').read()

# CSS para Facebook (solo si no existe ya)
fb_css = """
/* Facebook Page section */
.kpi-card.fb-card{background:linear-gradient(135deg,#1e1a2e,#0f1627);border:1px solid rgba(124,58,237,.2);}
.kpi-card.fb-card::after{background:linear-gradient(135deg,rgba(124,58,237,.07) 0%,transparent 60%);}
.kpi-card.fb-card .kpi-lbl{color:#C4B5FD;}
.fb-badge{background:rgba(124,58,237,.15);border:1px solid rgba(124,58,237,.3);color:#C4B5FD;font-size:10px;font-weight:600;padding:2px 8px;border-radius:12px;letter-spacing:.5px;text-transform:uppercase;}
.analysis-block.fb-block{border-left-color:#7C3AED;background:linear-gradient(135deg,#f5f3ff,white 60%);}
.note-warning{background:#FFF7ED;border:1px solid #FED7AA;border-radius:8px;padding:14px 18px;font-size:13px;color:#92400E;margin:0 0 20px;display:flex;gap:10px;align-items:flex-start;}
"""
if 'fb-card' not in c:
    c = c.replace('/* comparativa */', fb_css + '\n/* comparativa */')

# Sección FB completa
fb_html = """<!-- SECCIÓN 02: FACEBOOK PAGE ORGÁNICO -->
<section class="section">
  <div class="container">
    <div class="section-header">
      <div class="section-accent" style="background:#7C3AED"></div>
      <div class="section-title-block">
        <span class="section-num">02</span>
        <span class="section-title">Facebook Page Orgánico — Arichy Real Estate</span>
        <span class="fb-badge">● Facebook Page API</span>
      </div>
    </div>
    <div class="note-warning">
      <span style="font-size:16px;flex-shrink:0">⚠️</span>
      <div><strong>Acción requerida para activar datos reales:</strong> La Fan Page debe vincularse al System User del Business Manager con permiso <code>pages_read_engagement</code>. Una vez hecho, este bloque mostrará alcance, impresiones, fans nuevos y engagement de forma automática cada mes.</div>
    </div>
    <p class="desc">Sección configurada y lista para recibir datos de <strong>Facebook Page API</strong>. Las métricas que se mostrarán automáticamente al activar son:</p>
    <div class="kpi-grid kpi-grid-4">
      <div class="kpi-card fb-card"><div class="kpi-val" style="font-size:22px;opacity:.3">—</div><div class="kpi-lbl">Alcance orgánico página</div><div class="kpi-vs">Pendiente Page Token</div></div>
      <div class="kpi-card fb-card"><div class="kpi-val" style="font-size:22px;opacity:.3">—</div><div class="kpi-lbl">Impresiones totales</div><div class="kpi-vs">Pendiente Page Token</div></div>
      <div class="kpi-card fb-card"><div class="kpi-val" style="font-size:22px;opacity:.3">—</div><div class="kpi-lbl">Fans nuevos en el mes</div><div class="kpi-vs">Pendiente Page Token</div></div>
      <div class="kpi-card fb-card"><div class="kpi-val" style="font-size:22px;opacity:.3">—</div><div class="kpi-lbl">Engagement total</div><div class="kpi-vs">Pendiente Page Token</div></div>
    </div>
    <div class="analysis-grid">
      <div class="analysis-block fb-block">
        <div class="analysis-title">📊 Qué se jalará: Alcance & Impresiones</div>
        <div class="analysis-text">Alcance orgánico de la página, impresiones totales, visitas al perfil y reproducciones de video orgánicas del mes completo vía <code>page_impressions</code>, <code>page_reach</code>.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">👥 Qué se jalará: Crecimiento de audiencia</div>
        <div class="analysis-text">Fans nuevos (<code>page_fan_adds</code>), fans perdidos (<code>page_fan_removes</code>) y total de seguidores de la página en el período.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">❤️ Qué se jalará: Posts de Facebook</div>
        <div class="analysis-text">Tabla de publicaciones del mes con alcance, impresiones y usuarios comprometidos por post, incluyendo imagen de portada y enlace directo.</div>
      </div>
      <div class="analysis-block fb-block">
        <div class="analysis-title">🔧 Cómo activarlo</div>
        <div class="analysis-text">Business Manager → Configuración → Usuarios del sistema → asignar Fan Page al System User con permiso <strong>pages_read_engagement</strong>. El siguiente informe lo activa automáticamente.</div>
      </div>
    </div>
  </div>
</section>

"""

# Renumerar las secciones existentes antes de insertar
c = c.replace(
    '<span class="section-num">02</span><span class="section-title">Meta Ads',
    '<span class="section-num">03</span><span class="section-title">Meta Ads'
)
c = c.replace(
    '<span class="section-num">03</span><span class="section-title">Mail Marketing',
    '<span class="section-num">04</span><span class="section-title">Mail Marketing'
)
c = c.replace(
    '<span class="section-num">04</span><span class="section-title">Próximos Pasos',
    '<span class="section-num">05</span><span class="section-title">Próximos Pasos'
)

# Insertar FB section justo antes de la sección Meta Ads (ahora numerada 03)
# Buscar el <section> que contiene section-num 03 / Meta Ads
anchor = '<!-- SECCIÓN 02: META ADS API -->'
# El ancla en el HTML real es diferente — buscamos el <section> de Meta Ads por su contenido único
import re
# Buscar el inicio del bloque section que tiene Meta Ads
meta_pattern = r'(<section class="section"[^>]*>\s*<div class="container">\s*<div class="section-header">[^<]*<div class="section-accent" style="background:#3B82F6")'
m = re.search(meta_pattern, c)
if m:
    insert_pos = m.start()
    c = c[:insert_pos] + fb_html + c[insert_pos:]
    print('OK - FB section insertada antes de Meta Ads')
else:
    # Fallback: buscar por section-num 03 Meta Ads
    idx = c.find('<span class="section-num">03</span><span class="section-title">Meta Ads')
    if idx > 0:
        sec_start = c.rfind('<section class="section"', 0, idx)
        c = c[:sec_start] + fb_html + c[sec_start:]
        print('OK - FB section insertada por fallback section-num')
    else:
        print('ERROR - no se encontró ancla')

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('total chars:', len(c))
