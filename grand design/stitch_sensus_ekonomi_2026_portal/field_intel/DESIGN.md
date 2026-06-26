---
name: Field Intel
colors:
  surface: '#0c1324'
  surface-dim: '#0c1324'
  surface-bright: '#33394c'
  surface-container-lowest: '#070d1f'
  surface-container-low: '#151b2d'
  surface-container: '#191f31'
  surface-container-high: '#23293c'
  surface-container-highest: '#2e3447'
  on-surface: '#dce1fb'
  on-surface-variant: '#dfc0b2'
  inverse-surface: '#dce1fb'
  inverse-on-surface: '#2a3043'
  outline: '#a78b7e'
  outline-variant: '#584237'
  surface-tint: '#ffb691'
  primary: '#ffb691'
  on-primary: '#552000'
  primary-container: '#f27221'
  on-primary-container: '#542000'
  inverse-primary: '#9e4300'
  secondary: '#ffe391'
  on-secondary: '#3c2f00'
  secondary-container: '#f1c500'
  on-secondary-container: '#665200'
  tertiary: '#8ccdff'
  on-tertiary: '#00344e'
  tertiary-container: '#00a0e7'
  on-tertiary-container: '#00334d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcb'
  primary-fixed-dim: '#ffb691'
  on-primary-fixed: '#341100'
  on-primary-fixed-variant: '#793100'
  secondary-fixed: '#ffe081'
  secondary-fixed-dim: '#eec200'
  on-secondary-fixed: '#231b00'
  on-secondary-fixed-variant: '#564500'
  tertiary-fixed: '#cae6ff'
  tertiary-fixed-dim: '#8ccdff'
  on-tertiary-fixed: '#001e30'
  on-tertiary-fixed-variant: '#004b70'
  background: '#0c1324'
  on-background: '#dce1fb'
  surface-variant: '#2e3447'
  slate-950: '#020617'
  slate-900: '#0f172a'
  slate-800: '#1e293b'
  slate-400: '#94a3b8'
  slate-100: '#f1f7feb'
  highlight-yellow: '#FACD15'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  button-text:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max-width: 448px
  edge-margin: 1.25rem
  gutter: 1rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 1.5rem
  touch-target-min: 48px
---

## Brand & Style

This design system is engineered for **PR-SE2026**, a high-performance field survey application. The brand persona is technical, authoritative, and reliable—built for students navigating challenging environments. 

The aesthetic follows a **Premium Dark Mode** approach, prioritizing high-contrast legibility for outdoor use in bright sunlight while maintaining a sophisticated, utilitarian feel. The style merges **Modern Minimalist** structures with **Tactile** interactive elements. Every component is optimized for one-handed operation, acknowledging the physical reality of field work where users are often on the move. Micro-interactions, such as a subtle scale-down on press, provide haptic-like visual feedback to confirm actions in low-signal or high-distraction scenarios.

## Colors

The palette is anchored in a deep **Slate-950** background to minimize glare and maximize contrast. 

- **Primary (BPS Orange):** Used exclusively for high-priority actions, active states, and essential wayfinding. It is the "energy" of the interface.
- **Secondary/Highlight (Yellow-400):** Reserved for critical data points, status alerts, or specific field-entry highlights that require immediate visual attention.
- **Surface Strategy:** Cards utilize a semi-transparent **Slate-900/80** with a solid **Slate-800** border. This "glass-on-dark" effect creates depth without relying on heavy shadows that wash out in sunlight.
- **Text Tiers:** **Slate-100** provides maximum readability for titles, while **Slate-400** is used for secondary metadata to establish a clear information hierarchy.

## Typography

This design system utilizes **Inter** for its exceptional legibility and neutral, technical character. 

The type scale is generous to account for outdoor viewing conditions. Headlines are bold and tightly spaced to command attention, while body text maintains ample line height to prevent eye fatigue during long data entry sessions. **Yellow-400** should be applied to `label-md` or specific spans within `body-base` when identifying critical survey variables.

## Layout & Spacing

The layout is strictly **Mobile-First**, constrained to a maximum width of 448px (`max-w-md`) to ensure a consistent experience across all handsets.

- **One-Handed Zones:** Interactive elements are concentrated in the bottom two-thirds of the screen (the "thumb zone"). 
- **Grid:** A flexible 4-column system is used within the container, with a **1.25rem (20px)** outer margin to prevent content from hitting the screen edges.
- **Rhythm:** Vertical spacing follows an 8px (0.5rem) baseline grid. Elements are grouped using `stack-sm` for related fields and `stack-lg` to separate distinct sections or cards.

## Elevation & Depth

In a high-contrast dark environment, elevation is communicated through **Tonal Layering** and **Borders** rather than traditional shadows.

1.  **Level 0 (Background):** Slate-950.
2.  **Level 1 (Cards/Surfaces):** Slate-900 at 80% opacity with a 1px border of Slate-800. This creates a "cut-out" feel.
3.  **Level 2 (Active/Floating):** Primary Orange elements or active input fields. These appear "closest" to the user due to their high chroma.

When an element is touched, it utilizes a `scale-98` transform—a tactile "dip" that mimics the physical displacement of a button.

## Shapes

The shape language is defined by **Rounded-XL (1rem/16px)** corners. This softness balances the "hard" technical nature of the Slate color palette and makes the application feel approachable for student users.

- **Cards & Containers:** Always 16px (rounded-xl).
- **Buttons:** 16px to match the card language, creating a cohesive nested appearance.
- **Inputs:** 12px (rounded-lg) to provide a slight visual distinction from the outer container.

## Components

### Buttons
- **Primary:** Solid BPS Orange (#F27221) with Slate-950 text. Minimum height 56px for thumb-friendly interaction.
- **Secondary:** Slate-800 background with Slate-100 text.
- **Feedback:** On touch, all buttons must trigger a `scale(0.98)` transition (150ms ease-out).

### Cards
- **Structure:** Slate-900/80 background, 1px Slate-800 border, 16px padding.
- **Usage:** Used to group survey questions or display data summary modules.

### Input Fields
- **Default State:** Slate-900 background, 1px Slate-800 border.
- **Active/Focus State:** 2px BPS Orange border. Text remains Slate-100.
- **Labels:** Always visible above the field in Slate-400 to ensure context is never lost.

### Chips & Badges
- **Status Chips:** Small, 8px rounded corners.
- **Selection:** Use Primary Orange for selected states and Slate-800 for unselected.

### Lists
- Separate list items with a 1px Slate-800 divider. Each row should have a minimum height of 64px to ensure tap accuracy in the field.