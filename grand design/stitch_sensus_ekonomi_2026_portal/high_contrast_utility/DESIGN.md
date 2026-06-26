---
name: High-Contrast Utility
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#584237'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#8c7265'
  outline-variant: '#dfc0b2'
  surface-tint: '#9e4300'
  primary: '#9e4300'
  on-primary: '#ffffff'
  primary-container: '#f27221'
  on-primary-container: '#542000'
  inverse-primary: '#ffb691'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#006493'
  on-tertiary: '#ffffff'
  tertiary-container: '#00a0e7'
  on-tertiary-container: '#00334d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcb'
  primary-fixed-dim: '#ffb691'
  on-primary-fixed: '#341100'
  on-primary-fixed-variant: '#793100'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#cae6ff'
  tertiary-fixed-dim: '#8ccdff'
  on-tertiary-fixed: '#001e30'
  on-tertiary-fixed-variant: '#004b70'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
  surface-pure: '#FFFFFF'
  text-solid: '#0F172A'
  institutional-blue: '#003366'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 34px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  title-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  touch-target: 48px
  margin-mobile: 20px
  margin-desktop: 40px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for maximum legibility and operational efficiency in high-stakes, outdoor environments. It serves as a bridge between institutional reliability and modern utility, prioritizing rapid information retrieval and physical ease of use.

The aesthetic follows a **High-Contrast / Modern** philosophy. It utilizes a stark, "ink-on-paper" contrast ratio for core content, paired with high-chroma interactive cues. The interface is tactile and physical, using generous touch targets and clear structural containment to facilitate one-handed operations for users in the field. Every element is designed to remain distinct even under direct sunlight or while the user is in motion.

## Colors

The palette is optimized for extreme visibility. **Pure White (#FFFFFF)** serves as the primary canvas to maximize screen luminance. **Solid Black (#0F172A)** is reserved for structural elements and primary typography to ensure a crisp, high-contrast reading experience.

**BPS Orange (#F27221)** acts as the singular interactive signal, used exclusively for buttons, active states, and critical notifications. This ensures that the primary "action path" is always unmistakable. The **Light Gray (#F8FAFC)** is used for secondary surfaces and background grouping to prevent visual fatigue without sacrificing contrast.

## Typography

Typography is the backbone of this design system. We utilize **Inter** across all levels for its exceptional legibility and modern, neutral character. 

- **Titles & Headlines:** Rendered in Solid Black with bold weights (700-800). These function as landmarks for the eye.
- **Body Text:** Uses a slightly softer Slate-900 (derived from the structural black) to improve long-form reading comfort while maintaining a high contrast ratio.
- **Labels:** Always uppercase with increased letter spacing to differentiate metadata from actionable content.
- **Mobile Scaling:** Headlines transition to slightly smaller sizes on mobile to prevent awkward line breaks while maintaining heavy weights for impact.

## Layout & Spacing

The layout employs a **Fluid Grid** system designed for field use. On mobile, we use a 4-column grid; on desktop, a 12-column grid. 

A strict "Thumb-Zone" philosophy governs the layout: all primary actions (buttons, toggles, navigation) are placed within the bottom 40% of the mobile screen. 

- **Spacing Rhythm:** Based on an 8px baseline.
- **Touch Safety:** Every interactive element must adhere to a minimum 48px height/width to accommodate one-handed operation and gloved use if necessary.
- **Margins:** Generous side margins (20px on mobile) prevent accidental edge-taps and frame the content clearly.

## Elevation & Depth

This design system uses **Tonal Layering** combined with **Tactile Outlines** rather than heavy shadows to maintain outdoor readability. Shadows often wash out in bright sunlight, so we rely on physical containment:

- **Level 0 (Background):** Pure White or Secondary Surface (#F8FAFC).
- **Level 1 (Cards/Containers):** Pure White surface with a 1px border (#0F172A at 10% opacity) to provide definition without clutter.
- **Level 2 (Interactive/Floating):** Use a subtle, high-diffusion shadow (Color: #0F172A, Alpha: 0.08, Blur: 12px) only to indicate elements that are "above" the main flow, such as bottom sheets or floating action buttons.
- **Active State:** When pressed, elements should visually "depress" through a subtle scale-down (98%) and a darken overlay to provide immediate tactile feedback.

## Shapes

The shape language is defined by **Rounded-XL** corners, providing a friendly yet professional appearance that feels comfortable in the hand.

- **Primary Containers:** 1.5rem (24px) corner radius for cards and main modules.
- **Buttons & Inputs:** 1rem (16px) corner radius.
- **Small Components:** 0.5rem (8px) for chips and tags.

The use of large radii helps visually separate the UI components from the rigid rectangular hardware of mobile devices, making the software feel more organic and approachable.

## Components

### Buttons
Primary buttons are solid BPS Orange with Bold White text. They must span the full width of their container on mobile to maximize the touch target. Secondary buttons use a thick 2px Solid Black outline with black text.

### Cards
Cards are the primary organizational unit. They use a Pure White background, the standard Rounded-XL radius, and a subtle 1px border. Content within cards should have a minimum of 20px internal padding to maintain a premium, spacious feel.

### Input Fields
Fields use the Light Gray (#F8FAFC) background with a bottom-only 2px border in Solid Black. This "underline" style maintains high visibility while keeping the form looking modern. On focus, the border shifts to BPS Orange.

### Chips & Tags
Used for status indicators. High-saturation backgrounds with white text for critical states, or Light Gray backgrounds with black text for neutral metadata.

### Navigation
A persistent Bottom Navigation Bar is required for one-handed operation. Icons should be stroke-based (2px weight) to match the crispness of the typography. The active tab is indicated by the BPS Orange accent.