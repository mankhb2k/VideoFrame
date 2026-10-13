# khi

Nhân vật video OOP vs POP (2026-10-13). Nền trong suốt, 1024x1024, phong cách hoạt hình vector bóng.

## khi.png

- model: `gpt-image-2.5-flare`, quality `medium`, size `1024x1024`, `background: transparent`

- cách tạo: từ chữ (`/v1/images/generations`)


Prompt:

```
Glossy cartoon vector illustration: smooth cel-shading with 2-3 tonal steps, soft white specular highlights on rounded surfaces, thin outline in a darker shade of each shape's own color (no black outline), large glossy expressive eyes with white catchlights, chubby rounded proportions, clean smooth edges, no textures. A cute baby monkey, full body, three-quarter view, standing in a playful slightly tilted pose, one arm hanging down with the open palm facing forward and empty, the other arm relaxed, curious slightly puzzled expression with round orange-brown eyes and a small open mouth. Warm brown fur, tan-pink face, ears and belly, curly tail. Single subject centered, full body visible with a small margin, no text, no ground, no cast shadow, no extra props, completely transparent background.
```

## khi-cam-chuoi.png

- model: `gpt-image-2.5-flare`, quality `medium`, size `1024x1024`, `background: transparent`

- cách tạo: chỉnh sửa ảnh `khi.png` (`/v1/images/edits`)


Prompt:

```
Edit the reference image: keep the exact same monkey, identical proportions, colors, face and art style. Only change: one raised fist now firmly grips a ripe yellow banana held upright above its head, banana peel intact, fingers wrapped around the middle of the banana. Keep the other hand and everything else the same. Completely transparent background, no ground, no cast shadow.
```
