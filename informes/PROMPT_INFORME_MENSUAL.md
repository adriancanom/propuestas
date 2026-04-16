# PROMPT ESTÁNDAR — INFORME MENSUAL MARKETING VIP®
> Guardar este archivo. Usarlo cada mes para generar informes de cualquier cliente.

---

## CÓMO USARLO

Copia y pega este prompt en Claude al inicio de cada mes:

---

## EL PROMPT

```
Genera el informe mensual de gestión para el cliente [NOMBRE DEL CLIENTE].

**Datos del cliente:**
- Nombre: [NOMBRE]
- Mes a reportar: [MES] [AÑO]
- ClickUp List ID: [ID_LISTA]
- Instagram Business Account ID: [IG_ID]
- Facebook Page ID: [PAGE_ID]
- Meta Ads Account ID: [act_XXXXXXXXXX]
- Brevo API Key: [xkeysib-...]  ← opcional
- URL del informe anterior (para comparativa): [URL]  ← opcional

**Instrucciones:**
Sigue el formato estándar de Marketing VIP® exactamente como está en:
https://marketingvipco.github.io/propuestas/informes/arichy-real-estate-marzo-2026.html

Genera el informe completo con:
1. Hero portada con nombre del cliente
2. Resumen ejecutivo con KPIs (estilo Reportei: valor + variación vs mes anterior)
3. Sección Instagram orgánico vía IG API (tabla de posts + thumbnails + métricas)
4. Sección Facebook Page orgánico vía Page API (alcance, impresiones, fans, engagement)
5. Sección Meta Ads vía API (campañas, acciones, comparativa orgánico vs pagado)
6. Sección Mail Marketing — Brevo (si hay API key disponible)
7. Sección ClickUp — tareas gestionadas en el mes
8. Comparativa mes anterior vs mes actual (si hay URL anterior)
9. Próximos pasos por área

Publica en:
https://marketingvipco.github.io/propuestas/informes/[slug-cliente]-[mes]-[año].html

REGLAS DE DISEÑO — NUNCA CAMBIAR:
- Misma estructura HTML/CSS del informe de referencia (Arichy marzo 2026)
- Fuente: Geist (Google Fonts)
- Colores: --navy #1A1A2E · --green #51DD7D
- Hero oscuro full-height con grid decorativo
- Secciones alternas: blanco / var(--gray1) #F1F5F9
- KPI cards: navy con kpi-val + kpi-lbl + kpi-vs (valor anterior + % cambio)
- Badges formato: Reel morado · Carrusel azul · Historia ámbar · Post verde · Banner rosa
- Pills estado: Publicado verde · Aprobado azul · Stand By amarillo · En Cambios rojo
- Tablas: thead navy, filas alternadas blanco/gris, border var(--gray2)
- analysis-block: borde izquierdo verde (orgánico) · azul (Meta Ads) · rosa (IG) · morado (FB)
- Thumbnails IG: 48x48px redondeados, click abre post en Instagram
- NO usar tablas como divisores — usar border-bottom en párrafos
- Footer: "© [AÑO] Marketing VIP® · Datos: Meta Graph API v19.0 · Instagram Graph API · Facebook Page API · ClickUp API"
```

---

## FUENTES DE DATOS — APIs disponibles

### Instagram Graph API
```
GET /v19.0/{IG_ID}/media
  ?fields=id,media_type,timestamp,like_count,comments_count,
          thumbnail_url,media_url,permalink,
          insights.metric(reach,saved,shares)
  &since={DESDE}&until={HASTA}

GET /v19.0/{IG_ID}
  ?fields=followers_count,media_count,biography,website
```
**Métricas disponibles:** alcance por post, likes, comentarios, shares, guardados,
thumbnail real, permalink, seguidores totales, total de posts en perfil.

---

### Facebook Page API  ← **INCLUIR SIEMPRE**
```
GET /v19.0/{PAGE_ID}/insights
  ?metric=page_impressions,page_reach,page_engaged_users,
          page_fans,page_fan_adds,page_fan_removes,
          page_views_total,page_post_engagements,
          page_video_views,page_actions_post_reactions_total
  &since={DESDE}&until={HASTA}&period=month

GET /v19.0/{PAGE_ID}/posts
  ?fields=message,created_time,
          insights.metric(post_impressions,post_reach,
          post_engaged_users,post_reactions_by_type_total)
  &since={DESDE}&until={HASTA}
```
**Métricas disponibles:** alcance orgánico de página, impresiones totales,
fans nuevos, fans perdidos (unlikes), visitas a la página, engagement de posts,
reproducciones de video, reacciones por tipo.

> ⚠️ **Nota:** Para acceder a Page Insights se necesita un **Page Access Token**,
> no un User Token. Se obtiene así:
> ```
> GET /v19.0/me/accounts?access_token={USER_TOKEN}
> ```
> Esto devuelve las páginas con su `access_token` individual.
> Guardarlo en el script para usarlo en las llamadas de insights.

---

### Meta Ads API
```
GET /v19.0/{AD_ACCOUNT}/campaigns
  ?fields=name,status,insights{spend,impressions,reach,clicks,
          cpc,cpm,cpp,frequency,actions,cost_per_action_type,
          video_play_actions}
  &time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}
```
**Métricas disponibles:** gasto, impresiones, alcance, clicks, CPC, CPM,
frecuencia, acciones por tipo (link_click, video_view, page_engagement,
like, post_reaction, onsite_conversion.post_save).

---

### Brevo API  ← pendiente de activar
```
GET https://api.brevo.com/v3/emailCampaigns
  ?status=sent&startDate=YYYY-MM-DD&endDate=YYYY-MM-DD
  Header: api-key: {BREVO_KEY}
```
**Métricas disponibles:** tasa de apertura, tasa de clics, entregas,
rebotes (hard/soft), desuscripciones, spam reports, fecha de envío.

---

## DATOS DE CLIENTES CONFIGURADOS

### Arichy Real Estate
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324565657` |
| Instagram ID | `17841454974456376` |
| Facebook Page ID | `976877848844666` |
| Meta Ads Account | `act_255327741430906​10` |
| Meta Token | *(renovar en Business Manager → Usuarios del sistema)* |
| Brevo API Key | *(pendiente)* |
| Slug | `arichy-real-estate` |
| Informe anterior | `arichy-real-estate-marzo-2026.html` |

### Euro Money Exchange
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324303147` |
| Instagram ID | *(pendiente)* |
| Facebook Page ID | *(pendiente)* |
| Meta Ads Account | *(pendiente — CSV disponible)* |
| Slug | `euro-money` |

### Miami Money Exchange
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901324303203` |
| Instagram ID | *(pendiente)* |
| Facebook Page ID | *(pendiente)* |
| Meta Ads Account | *(pendiente — CSV disponible)* |
| Slug | `miami-money` |

### AC Depot
| Campo | Valor |
|-------|-------|
| ClickUp List ID | `901322350882` |
| Instagram ID | *(pendiente)* |
| Facebook Page ID | *(pendiente)* |
| Meta Ads Account | *(pendiente)* |
| Slug | `ac-depot` |

---

## SCRIPTS DISPONIBLES (en /scripts/)

| Script | Qué hace |
|--------|----------|
| `meta-fetch.js` | Campañas + métricas Meta Ads API |
| `organic-fetch.js` | Posts IG + métricas + perfil + Page Insights FB |
| `compare-fetch.js` | Datos de 2 meses para comparativa mes a mes |
| `media-thumbs.js` | Thumbnails reales de posts IG |

**Uso:**
```bash
node scripts/meta-fetch.js 2026-04-01 2026-04-30
node scripts/organic-fetch.js 2026-04-01 2026-04-30
node scripts/compare-fetch.js
```

---

## ESTRUCTURA DE LA SECCIÓN FACEBOOK PAGE EN EL INFORME

La sección de Fan Page va **después de Instagram orgánico** y **antes de Meta Ads**,
con el mismo diseño de sección, usando:
- `section-accent` color morado `#7C3AED` para diferenciarla visualmente de IG (rosa) y Meta (azul)
- KPI cards con clase `.fb-card` (fondo navy con acento morado)
- Tabla de posts de Facebook con las mismas clases de tabla existentes
- analysis-block con `border-left-color: #7C3AED`

---

## CHECKLIST MENSUAL

Antes de generar el informe verificar:
- [ ] Token Meta Ads vigente (Page Access Token incluido)
- [ ] ClickUp List ID correcto del cliente
- [ ] Instagram Business Account ID
- [ ] Facebook Page ID
- [ ] Meta Ads Account ID (`act_XXXXXXXXXX`)
- [ ] URL del informe del mes anterior para comparativa
- [ ] Brevo API Key (cuando esté disponible)

---

## ESTRUCTURA DE URLs

```
https://marketingvipco.github.io/propuestas/informes/[slug]-[mes]-[año].html
```

Ejemplos:
- `arichy-real-estate-abril-2026.html`
- `euro-money-abril-2026.html`
- `miami-money-abril-2026.html`
- `ac-depot-abril-2026.html`

---

## TOKEN META — IMPORTANTE

El token actual es de usuario. Para producción usar **System User Token** permanente:
1. Business Manager → Configuración → Usuarios del sistema
2. Crear usuario → Administrador
3. Asignar cuentas publicitarias + páginas
4. Generar token con permisos:
   `ads_read`, `business_management`, `read_insights`, `pages_read_engagement`
5. Este token no expira y da acceso a Page Insights

---

*Documento creado por Marketing VIP® · Última actualización: Abril 2026*
