f = open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', encoding='utf-8')
c = f.read()
f.close()

# Nuevas clases CSS — mínimas, se insertan al final del bloque de estilos
new_css = """
/* comparativa */
.delta-up{color:#22C55E;font-weight:700;}
.delta-down{color:#EF4444;font-weight:700;}
.delta-flat{color:#94A3B8;font-weight:600;}
.cmp-bar{height:6px;border-radius:3px;background:#E2E8F0;overflow:hidden;margin-top:4px;}
.cmp-bar-fill{height:100%;border-radius:3px;background:var(--green);}
.cmp-bar-fill.feb{background:#94A3B8;}
.td-delta{font-size:13px;font-weight:700;}
"""

# Insertar CSS antes del cierre </style>
c = c.replace('</style>', new_css + '</style>', 1)

# Bloque HTML de la sección comparativa — va antes del cierre del .report
comparativa = """
<!-- SECCIÓN 5: COMPARATIVA FEB vs MAR — mismo diseño -->
<section class="section" style="background:white;padding-top:56px">
  <div class="container">
    <div class="section-header">
      <div class="section-accent"></div>
      <div class="section-title-block">
        <span class="section-num">05</span>
        <span class="section-title">Comparativa Instagram — Febrero vs Marzo 2026</span>
        <span class="ig-badge">● IG API · Datos reales</span>
      </div>
    </div>
    <p class="desc">Evolución mes a mes obtenida directamente de la <strong>Instagram Graph API</strong>. Todos los datos son reales — sin estimaciones manuales.</p>

    <!-- KPIs comparativos -->
    <div class="kpi-grid kpi-grid-6">
      <div class="kpi-card ig-card">
        <div class="kpi-val">12</div>
        <div class="kpi-lbl">Posts en marzo</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 7 en feb <span class="delta-up">▲ +71%</span></div>
      </div>
      <div class="kpi-card ig-card">
        <div class="kpi-val">2,933</div>
        <div class="kpi-lbl">Alcance orgánico</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 1,499 en feb <span class="delta-up">▲ +96%</span></div>
      </div>
      <div class="kpi-card ig-card">
        <div class="kpi-val">244</div>
        <div class="kpi-lbl">Alcance / post</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 214 en feb <span class="delta-up">▲ +14%</span></div>
      </div>
      <div class="kpi-card ig-card">
        <div class="kpi-val">151</div>
        <div class="kpi-lbl">Likes totales</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 103 en feb <span class="delta-up">▲ +47%</span></div>
      </div>
      <div class="kpi-card ig-card">
        <div class="kpi-val">71</div>
        <div class="kpi-lbl">Shares totales</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 51 en feb <span class="delta-up">▲ +39%</span></div>
      </div>
      <div class="kpi-card ig-card">
        <div class="kpi-val">6</div>
        <div class="kpi-lbl">Guardados</div>
        <div style="font-size:11px;color:#F9A8D4;margin-top:6px;">vs 8 en feb <span class="delta-down">▼ -25%</span></div>
      </div>
    </div>

    <!-- Tabla detallada -->
    <div class="section-sub">Tabla comparativa detallada</div>
    <div class="table-wrap">
      <table>
        <thead class="ig-head">
          <tr>
            <th class="tl">Métrica</th>
            <th>Febrero 2026</th>
            <th>Marzo 2026</th>
            <th>Variación</th>
            <th>% Cambio</th>
            <th>Tendencia</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="td-left td-bold">Publicaciones</td>
            <td class="td-gray">7</td>
            <td class="td-bold">12</td>
            <td class="td-delta delta-up">+5</td>
            <td class="td-delta delta-up">+71.4%</td>
            <td>
              <div style="font-size:11px;color:var(--gray3);margin-bottom:3px">Mar</div>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div style="font-size:11px;color:var(--gray3);margin-top:4px">Feb</div>
              <div class="cmp-bar"><div class="cmp-bar-fill feb" style="width:58%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Alcance orgánico total</td>
            <td class="td-gray">1,499</td>
            <td class="td-bold">2,933</td>
            <td class="td-delta delta-up">+1,434</td>
            <td class="td-delta delta-up">+95.7%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:51%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Alcance promedio / post</td>
            <td class="td-gray">214</td>
            <td class="td-bold">244</td>
            <td class="td-delta delta-up">+30</td>
            <td class="td-delta delta-up">+14.0%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:88%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Likes totales</td>
            <td class="td-gray">103</td>
            <td class="td-bold">151</td>
            <td class="td-delta delta-up">+48</td>
            <td class="td-delta delta-up">+46.6%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:68%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Shares totales</td>
            <td class="td-gray">51</td>
            <td class="td-bold">71</td>
            <td class="td-delta delta-up">+20</td>
            <td class="td-delta delta-up">+39.2%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:72%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Comentarios</td>
            <td class="td-gray">2</td>
            <td class="td-bold">2</td>
            <td class="td-delta delta-flat">0</td>
            <td class="td-delta delta-flat">0%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:100%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:100%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Guardados</td>
            <td class="td-gray">8</td>
            <td class="td-bold">6</td>
            <td class="td-delta delta-down">-2</td>
            <td class="td-delta delta-down">-25.0%</td>
            <td>
              <div class="cmp-bar"><div class="cmp-bar-fill" style="width:75%"></div></div>
              <div class="cmp-bar" style="margin-top:4px"><div class="cmp-bar-fill feb" style="width:100%"></div></div>
            </td>
          </tr>
          <tr>
            <td class="td-left td-bold">Alcance pagado (Meta Ads)</td>
            <td class="td-gray">0</td>
            <td class="td-bold td-blue">70,904</td>
            <td class="td-delta delta-up">+70,904</td>
            <td class="td-delta delta-up">Nuevo</td>
            <td class="td-gray" style="font-size:12px;text-align:left">Camp. activa desde 17 Mar</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Análisis comparativo en el mismo formato de analysis-block -->
    <div class="section-sub">Puntos clave de la evolución</div>
    <div class="analysis-grid">
      <div class="analysis-block ig-block">
        <div class="analysis-title">📈 Alcance casi duplicado</div>
        <div class="analysis-text">El alcance orgánico pasó de <strong>1,499 a 2,933 cuentas</strong> (+95.7%). Publicar 5 piezas más en marzo y el viral del Día de la Mujer (693 alcance) son los factores principales.</div>
      </div>
      <div class="analysis-block ig-block">
        <div class="analysis-title">🎬 Más posts, más eficiencia</div>
        <div class="analysis-text">El alcance promedio por post subió de <strong>214 a 244</strong> (+14%). No solo publicamos más — cada pieza llegó a más gente. La calidad del contenido mejoró junto con la cantidad.</div>
      </div>
      <div class="analysis-block ig-block">
        <div class="analysis-title">📤 Shares: +39% — indicador clave</div>
        <div class="analysis-text">71 shares vs 51 en febrero. Para Real Estate de lujo los shares son el indicador de intención más valioso — alguien que comparte una propiedad es un <strong>lead potencial activo</strong>.</div>
      </div>
      <div class="analysis-block ig-block">
        <div class="analysis-title">💾 Guardados bajaron — oportunidad</div>
        <div class="analysis-text">De 8 a 6 guardados (–25%). Señal clara: incluir más <strong>contenido tipo guía</strong> — Legal Guide, CONFOTUR, Roadmap de inversión — que la gente guarda para consultar después.</div>
      </div>
      <div class="analysis-block meta-block">
        <div class="analysis-title">🚀 Meta Ads: multiplicador x49</div>
        <div class="analysis-text">La pauta activada el 17 marzo sumó <strong>70,904 personas alcanzadas</strong> con $112 USD — 49x más que el orgánico del mes. El alcance total combinado llegó a <strong>73,837 cuentas</strong>.</div>
      </div>
      <div class="analysis-block meta-block">
        <div class="analysis-title">🎯 Objetivo abril: 3,500+ orgánico</div>
        <div class="analysis-text">Manteniendo la cadencia de 12+ posts, con más Reels y contenido testimonial, el target de alcance orgánico para abril es <strong>3,500 cuentas</strong>. Con Meta Ads escalado: <strong>140,000+ alcance combinado</strong>.</div>
      </div>
    </div>
    <p class="note">Datos obtenidos vía Instagram Graph API v19.0 y Meta Ads API. Febrero: 01/02–28/02/2026 · Marzo: 01/03–31/03/2026.</p>
  </div>
</section>
"""

# Insertar antes del cierre del .report
c = c.replace('\n</div>\n<footer', comparativa + '\n</div>\n<footer', 1)

open(r'C:\Users\adria\propuestas-mvip\informes\arichy-real-estate-marzo-2026.html', 'w', encoding='utf-8').write(c)
print('ok', len(c))
