# RedStarTrust Design System

Version 1.0 · 3 September 2026  
CSS source of truth: `Noting/design/design-system.css`

This file defines the decisions that every RedStarTrust screen must follow. Page-level exceptions belong in `pages/<page>.md`; an exception must state why it exists and must not redefine the global palette.

## Brand principles

RedStarTrust is an independent financial-rating authority. The interface should feel evidence-led, calm and institutional—not promotional, playful or fintech-neon.

- Use red to identify the institution and decisive actions.
- Use white and neutral gray for surfaces. Pink is not a surface color.
- Gold is restricted to verified award contexts and must never imply a paid ranking.
- Prefer clear hierarchy and evidence density over decorative effects.
- One component has one visual treatment across routes.

## Foundations

### Color

| Role | Token | Value |
|---|---|---:|
| Primary brand | `--ds-color-brand` | `#CF2027` |
| Brand hover | `--ds-color-brand-hover` | `#B42318` |
| Deep brand | `--ds-color-brand-deep` | `#790F14` |
| Canvas / surface | `--ds-color-canvas`, `--ds-color-surface` | `#FFFFFF` |
| Muted surface | `--ds-color-surface-muted` | `#F2F4F7` |
| Primary text | `--ds-color-text` | `#101828` |
| Secondary text | `--ds-color-text-secondary` | `#475467` |
| Border | `--ds-color-border` | `#EAECF0` |
| Strong border | `--ds-color-border-strong` | `#D0D5DD` |
| Focus | `--ds-color-focus` | `#CF2027` |

Forbidden: pink panels, decorative gradients, low-contrast red body copy and raw hex colors inside new components.

Award-only tokens are `--ds-award-*`. They may appear only on certificate, trophy and verified-award elements.

### Typography

| Role | Token | Typeface |
|---|---|---|
| Brand wordmark | `--ds-font-brand` | Cormorant Garamond 600 |
| Interface headings | `--ds-font-display` | DM Sans / IBM Plex Sans Thai |
| Body and controls | `--ds-font-body` | Inter / IBM Plex Sans Thai |
| Editorial Thai accent | `--ds-font-editorial-th` | Noto Serif Thai |
| Data and identifiers | `--ds-font-mono` | IBM Plex Sans |

Body copy is at least 14px in dense data UI and 16px in reading contexts. Default body line-height is 1.65. Do not use the wordmark face for ordinary headings.

### Spacing and layout

- Spacing follows the 4px scale `--ds-space-1` through `--ds-space-24`.
- Desktop presentation frame: `--ds-container: 1440px`.
- Primary readable content: `--ds-content: 1200px`.
- Full-width framed sections use `--ds-gutter: 56px` as their safe inset.
- Mobile safe inset is 20px.
- Interactive controls are at least `--ds-control-height: 44px`.

### Shape and depth

- Controls: `--ds-radius-md` (12px).
- Standard cards: `--ds-radius-lg` (16px).
- Feature panels: `--ds-radius-xl` or `--ds-radius-2xl` (20–28px).
- Use `--ds-shadow-sm` by default; reserve `--ds-shadow-lg` for overlays.
- Hover may move an interactive card by at most 2px. Static cards never lift.

## Components

Canonical primitives are available in the shared stylesheet:

- `.ds-container`, `.ds-content`, `.ds-safe`
- `.ds-button`, `.ds-button--primary`, `.ds-button--secondary`
- `.ds-input`
- `.ds-card`, `.ds-card--interactive`
- `.ds-badge`

Existing classes such as `.btn-solid`, `.art-card`, `.pk-card` and `.rk-pick` remain supported during migration. New work must use the canonical token values even when retaining a legacy class for JavaScript compatibility.

### Required states

Every interactive component needs default, hover, focus-visible, disabled and loading/empty behavior where applicable. Focus must remain visible without relying on color alone. Icon-only controls require an accessible name.

## Content and data rules

- Stars communicate an audit level; scores communicate comparison. Never merge the two meanings.
- Sample data must be labelled as sample data.
- Dates, evidence IDs and audit status use tabular/data typography.
- Broker logos are identification aids, not endorsements.
- Do not use urgency, scarcity or exaggerated conversion language.

## Accessibility and motion

- Normal text contrast: minimum 4.5:1.
- Large text contrast: minimum 3:1.
- Keyboard focus must be visible on every action.
- Do not communicate status by color alone.
- Honor `prefers-reduced-motion`; the shared stylesheet disables non-essential motion.
- Verify at 375, 768, 1024 and 1440px before handoff.

## Contribution workflow

1. Check this Master file and the route override in `pages/`.
2. Use an existing semantic token; do not add a raw visual value to a component.
3. If no token fits, add and document a semantic token in the shared stylesheet first.
4. Validate keyboard states, contrast and overflow.
5. Update the deployed copy at `public/design-system.css` together with the source.

## Legacy migration map

| Legacy family | Canonical destination | Status |
|---|---|---|
| `--rs-*` | `--ds-*` | Home aliases connected |
| `--aw-*` | `--ds-*` + `--ds-award-*` | Retained for compatibility; migrate per component |
| `--rst-*` | `--ds-*` | Archived homepage experiment; do not use |
| `--lux-*` | `--ds-*` | Archived homepage experiment; do not use |

The four legacy families are not separate design systems. This document and `design-system.css` are the only source of truth from version 1.0 onward.
