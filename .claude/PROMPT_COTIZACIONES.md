# PROMPT PARA CREAR COTIZACIONES MARKETING VIP

Eres experto creando cotizaciones en HTML para Marketing VIP®. Las cotizaciones están en `C:\Users\adria\propuestas-mvip` y se despliegan en GitHub Pages.

## REGLAS FUNDAMENTALES

### Estructura de archivos
- Cada cotización va en su carpeta: `cotizacion{NÚMERO}/index.html`
- El CSS está en `../styles.css` (NUNCA modificar, NUNCA incluir CSS inline)
- El HTML solo llama al estilo: `<link rel="stylesheet" href="../styles.css">`
- Para saber el siguiente número de cotización, revisar qué carpetas existen

### Deploy
- Ejecutar en CMD (no PowerShell): `cd /d C:\Users\adria\propuestas-mvip && git add -A && git commit -m "update" && git push`
- URL final: `https://marketingvipco.github.io/propuestas/cotizacion{NÚMERO}/`

### Sección "Quiénes somos" (FIJA - NO MODIFICAR POR PROYECTO)
Esta sección es IDÉNTICA en todas las cotizaciones. NUNCA adaptarla al proyecto específico:

**Subtítulo fijo:**
"Somos una agencia tech con más de 12 años impulsando negocios a través de la tecnología y el marketing digital."

**Glass card principal fija:**
Título: "Especialistas en desarrollo web, marketing digital y branding"
Texto: "Desde 2012, hemos entregado más de 1,000 proyectos de diseño, desarrollo web, marketing digital y branding. Dominamos WordPress, Divi, Elementor, Shopify, Webflow, React, Next.js, Astro y más. Complementamos con estrategias de Meta Ads, Google Ads, TikTok Ads, SEO, email marketing y gestión de redes sociales. Además, creamos identidades de marca completas: naming, logotipos, brandboards y branding integral."

**Stats fijos:** +1000 Proyectos | 12+ Años | 99% Satisfacción | 24/7 Soporte

**Herramientas (3 glass cards fijas):**

💻 Web:
Figma, WordPress, Elementor, Divi, PHP, HTML, CSS, JavaScript, Next.js, React, Node, Tailwind, Astro, Express, MySQL, PostgreSQL, Shopify, Webflow, Liquid

📣 Social Media y Marketing:
Meta Ads, Google Ads, TikTok Ads, Google Analytics, Google Tag Manager, LinkedIn, Pinterest, Email Marketing, Social Media, Postproducción de video, Diseño gráfico

✨ Branding y logotipos:
Naming, Logotipos, Brandboard, Branding

**Proyectos recientes (links clickeables con clase tech-tag):**
- cybershop.mx → https://www.cybershop.mx/
- toonicetravel.com → https://toonicetravel.com/
- holycosmetics.com.co → https://holycosmetics.com.co/
- aka.com.uy → https://aka.com.uy/
- balibody.uy → https://balibody.uy/
- cloudclinic.health → https://cloudclinic.health/

**¿Por qué elegirnos? (fijo):**
- Equipo completo: desarrolladores, diseñadores UX/UI y especialistas en marketing
- Código limpio, escalable y documentado para facilitar futuras mejoras
- Comunicación constante con reportes de avance semanales
- Garantía post-entrega con soporte técnico incluido
- Más de 1,000 proyectos entregados con 99% de satisfacción

### Forma de pago (FIJA)
"El pago se deposita al 100% en Workana al iniciar. Se liberará el 50% como anticipo al comenzar el proyecto y el 50% restante al finalizar y aprobar la entrega final."

### CTA final (FIJO)
- Texto: "Contrátame ahora" (sin mayúsculas)
- Link Workana: https://www.workana.com/freelancer/3c7342412de95a79a3ac63d14ea69a0a
- Plataforma siempre: Workana

### Validez (FIJA)
"Esta cotización es válida por 15 días a partir de la fecha de envío."

## ESTRUCTURA TÍPICA DE PÁGINAS
1. **Cover** — Título del proyecto + subtítulo + mes/año + Workana + # propuesta
2. **Quiénes somos** — TODA la sección fija descrita arriba
3. **Entendimiento** — Análisis del proyecto específico, retos identificados
4. **Metodología/Opciones** — Fases de trabajo o comparativa de opciones
5. **Alcance** — Entregables detallados del proyecto
6. **Inversión** — Precios, opciones si aplica
7. **CTA Final** — Timeline, forma de pago, botón Workana

## CLASES CSS DISPONIBLES (usar tal cual, no inventar)
- `cover`, `inner-section`, `glass-card`, `module-grid`, `module-item`
- `stat-row`, `stat-item`, `pricing-card`, `tech-row`, `tech-tag`
- `timeline`, `timeline-item`, `timeline-dot`, `timeline-content`, `duration`
- `cta-box`, `cta-final`, `cta-workana-btn`, `cta-label`
- `page-header`, `page-footer`, `section-title`, `section-desc`
- `brand-name`, `brand-text`, `section-label`, `divider-line`
- `meta-info`, `meta-item`, `dot`, `bottom-bar`
- `mod-num` (para numeración dentro de module-item)
- `highlight`, `text-sm`, `mb-10`, `mb-20`, `mb-30`

## IMPORTANTE
- Leer siempre la cotización base más reciente antes de crear una nueva (por si algo cambió)
- NUNCA poner precios sin que el usuario los indique
- Si el usuario no indica precio, preguntar antes de crear
- Para deploy usar shell CMD, no PowerShell (PowerShell no soporta &&)
