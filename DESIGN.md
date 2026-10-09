---
name: Obsidian Vector
colors:
  surface: '#0f131d'
  surface-dim: '#0f131d'
  surface-bright: '#353944'
  surface-container-lowest: '#0a0e18'
  surface-container-low: '#171b26'
  surface-container: '#1c1f2a'
  surface-container-high: '#262a35'
  surface-container-highest: '#313540'
  on-surface: '#dfe2f1'
  on-surface-variant: '#bcc9cd'
  inverse-surface: '#dfe2f1'
  inverse-on-surface: '#2c303b'
  outline: '#869397'
  outline-variant: '#3d494c'
  surface-tint: '#4cd7f6'
  primary: '#4cd7f6'
  on-primary: '#003640'
  primary-container: '#06b6d4'
  on-primary-container: '#00424f'
  inverse-primary: '#00687a'
  secondary: '#d0bcff'
  on-secondary: '#3c0091'
  secondary-container: '#571bc1'
  on-secondary-container: '#c4abff'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#1bbd85'
  on-tertiary-container: '#00452e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#acedff'
  primary-fixed-dim: '#4cd7f6'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5c'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0f131d'
  on-background: '#dfe2f1'
  surface-variant: '#313540'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
    letterSpacing: -0.005em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0.005em
  label-mono-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0em
  label-mono-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-desktop: 1.5rem
  margin: 1rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

The design system is crafted for high-performance machine learning research, topological data analysis, and multidimensional projection platforms (e.g., t-SNE, UMAP, PCA). It prioritizes analytical rigor, technical depth, and focused immersion.

The visual direction combines **Technical Precision** with **Atmospheric Minimalist Glow**. It features an ultra-dark canvas structured by low-contrast slate scaffolding, allowing multidimensional data points, vector projections, and status nodes to command immediate attention. Visual clutter is stripped away in favor of high-density tabular matrices, crisp micro-borders, and targeted neon luminescence that signifies computational state, variance convergence, and active latent clusters.

## Colors

The palette establishes an obsidian hierarchy designed to reduce optical fatigue during continuous model analysis while maintaining clear contrast ratios.

- **Canvas & Backgrounds:** The master background anchors at deep obsidian (`#0B0F19`), shifting up to `#111827` for elevated structural containers. Surface cards and interactive panels sit between `#161E2E` (flat panels) and `#1E293B` (hovered or elevated modules).
- **Structural Framing:** Borders and grid dividers employ dark slate at `#334155` (1px, 40%–100% opacity) to provide architectural rigidity without competing with graphic plots.
- **Accents & Telemetry:**
  - **Electric Cyan / Teal (`#06B6D4` / `#14B8A6`):** Primary action nodes, active hyperparameter states, crosshairs, and dominant manifold trajectories.
  - **Vibrant Violet (`#8B5CF6`):** Secondary projections, latent dimensions, secondary clustering groupings, and algorithm run states.
  - **Subtle Emerald (`#10B981`):** Convergence metrics, loss reductions, explained variance indicators, and valid pipeline statuses.
  - **Text Layers:** High-emphasis data uses `#F8FAFC`, secondary documentation uses `#94A3B8`, and disabled states or structural labels rely on `#64748B`.

## Typography

Typography balances structural clarity with engineering precision through a deliberate three-tier typeface hierarchy:

1. **Display & Structural Heads (`Space Grotesk`):** Provides a sharp, modern geometric voice for view headers, model names, and major metric summaries without sacrificing horizontal density.
2. **Interface & Prose (`Inter`):** Delivers clean readability across analytical documentation, configuration forms, settings, and complex control drawers.
3. **Data Values & Telemetry (`JetBrains Mono`):** Applied to all loss metrics, coordinates ($x, y, z$), dimensionality counts, eigenvalues, hyperparameter inputs, and tabular outputs to guarantee vertical optical alignment and legibility across uniform character widths.

## Layout & Spacing

The layout is built around a flexible, high-density dashboard grid engineered for multi-view visualization and parameter calibration.

- **Desktop (1280px+):** A 12-column fluid grid system with `gutter-desktop` (24px) and `margin-desktop` (32px). Canvas split views accommodate a persistent 280px parameter rail, a main WebGL viewport, and dynamic 360px secondary decomposition panels.
- **Tablet (768px – 1279px):** An 8-column layout with 16px gutters and 24px margins. Dimensionality scatter plots lock to full width; hyperparameter panels collapse into floating slide-out trays.
- **Mobile (<768px):** A 4-column layout with 16px margins. Complex multi-scatter graphs shift to sequential tabbed projections; tabular matrices toggle horizontal lock-and-scroll.
- **Internal Density:** Internal component padding stays compact (`space-xs` to `space-md`) to maximize information display area.

## Elevation & Depth

Visual hierarchy relies on crisp borders and tonal layering rather than heavy drop shadows:

- **Surface Tiers:**
  - **Base Canvas:** `#0B0F19` with a subtle 32px CSS dot-grid pattern (`rgba(51, 65, 85, 0.25)`).
  - **Flat Container:** `#111827`, bordered by 1px solid `rgba(51, 65, 85, 0.5)`.
  - **Interactive Surface:** `#161E2E`, framed by 1px solid `#334155`.
  - **Overlay Modals & Trays:** `#1E293B`, framed by 1px solid `rgba(6, 182, 212, 0.3)`.
- **Glow & Atmospheric Lighting:**
  - Elevated status items use restrained, colored ambient glows instead of neutral shadows. Active cluster selectors and running iteration loops feature `box-shadow: 0 0 16px -2px rgba(6, 182, 212, 0.2)`.
  - Tooltips and contextual overlays incorporate a subtle backdrop blur (`backdrop-filter: blur(8px)`) over a semi-translucent `#111827` base.

## Shapes

The design system adopts a **Soft / Precision (Level 1)** geometric standard. 

Base components (buttons, text inputs, segment toggles, metric chips) use `0.25rem` (4px) corner radii. Structural cards, modal viewports, and scatter canvas frames use `0.5rem` (8px), maintaining technical sharpness that matches Cartesian plotting environments. Badges and status pills use fully rounded pills for immediate contrast against rectangular data modules.

## Components

- **Buttons:**
  - *Primary:* `#06B6D4` background, `#0B0F19` bold text, with a faint glow on hover (`0 0 12px rgba(6, 182, 212, 0.4)`).
  - *Secondary / Outline:* Transparent fill, 1px solid `#334155`, `#F8FAFC` text; borders transition to `#06B6D4` on hover.
  - *Ghost / Monospace:* 1px transparent border, `#94A3B8` text, transitioning to `#1E293B` background on interaction.
- **Chips & Badges:**
  - Compact badges using `label-mono-sm`. Status pills use translucent color washes: Emerald (`rgba(16, 185, 129, 0.12)` fill, `#10B981` text, 1px border `rgba(16, 185, 129, 0.3)`), Violet for categorical manifolds, and Cyan for primary vector tags.
- **Input Fields & Sliders:**
  - Numeric inputs and hyperparameter fields (e.g., Perplexity, Min Distance, Metric) use `#111827` fills, `#334155` borders, and `JetBrains Mono` values. Active fields shift border color to `#06B6D4` with an inner glow.
  - Range sliders feature a 2px `#334155` track with a `#06B6D4` filled state and a 12px squared-circle cyan handle.
- **Data Tables:**
  - Matrix tables feature sticky headers set in `label-mono-md`, borders in `rgba(51, 65, 85, 0.4)`, and alternate row shading via `#0E1422`. Numerical values align to the right in `JetBrains Mono`.
- **Cards & Data Panels:**
  - Surface panels feature a 1px `#334155` border, a 40px linear gradient header strip (`rgba(22, 30, 46, 0.7)` to `#111827`), integrated minimize/maximize controls, and corner crosshair accents.
- **Tooltips:**
  - Dark floating panels (`#0F172A`) with 1px border (`#334155`), backdrop-blur (12px), monospaced $(x, y, z)$ coordinates, and an inline colored swatch identifying the hover cluster ID.