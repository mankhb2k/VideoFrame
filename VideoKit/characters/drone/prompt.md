# drone

Nhân vật video OOP vs POP (2026-10-13). Nền trong suốt, 1024x1024, phong cách hoạt hình vector bóng.

## drone.png

- model: `gpt-image-2.5-flare`, quality `medium`, size `1024x1024`, `background: transparent`

- cách tạo: lấy `khi.png` làm tham chiếu phong cách (`/v1/images/edits`)


Prompt:

```
Use the reference image ONLY as a style guide (rendering style, shading, outline, eye style, proportions' roundness). Do not copy the reference character. Draw a new subject: Glossy cartoon vector illustration: smooth cel-shading with 2-3 tonal steps, soft white specular highlights on rounded surfaces, thin outline in a darker shade of each shape's own color (no black outline), large glossy expressive eyes with white catchlights, chubby rounded proportions, clean smooth edges, no textures. a cute toy-like quadcopter drone, three-quarter view from slightly above, rounded glossy body in white and light gray with slate-blue accents, four arms each with a clearly drawn static propeller (no motion blur), a small camera gimbal underneath that looks like a big friendly eye, short landing legs, one small blue indicator light. No red or green colors anywhere. Single subject centered, full body visible with a small margin, no text, no ground, no cast shadow, no extra props, completely transparent background.
```
