# 🧪 Archive-Lab

An archive of **early NumWorks MicroPython experiments, prototypes, debug tools, color utilities, and beginner graphics scripts** preserved from my calculator.

---

## 📂 Repository Structure

```
Archive-Lab/
├── prototypes_and_debug/
│   ├── sprite_rotator.py              # Inverse-mapping pixel sprite rotation test
│   ├── checkers_capture_analyzer.py   # Board capture analysis debugger for Checkers
│   ├── checkers_board_visualizer.py   # Visual debugger for Checkers move traces
│   ├── bitmap_char_renderer.py        # Binary/hex character bitmap rendering prototype
│   ├── qr_mask_patterns.py            # Visualizer for the 8 ISO QR-code data masks
│   └── maze_movement_test.py          # Minimalist 2-line movement loop test for Maze
├── colors/
│   ├── rgb_color_picker.py            # Interactive RGB color picker & RGB565 quantizer
│   ├── bilinear_color_gradient.py     # 4-corner bilinear color gradient
│   └── rgb565_pixel_inspector.py      # Quick get_pixel() RGB565 readback test
├── diagnostics_and_helpers/
│   ├── reflection_angle_wip.py        # Unfinished reflection-angle experiment
│   └── cps_benchmark.py               # Clicks-per-second (CPS) key-spam benchmark
└── early_graphics_and_toys/
    ├── turtle/
    │   ├── rosette_turtle.py          # Early Turtle rosette drawing
    │   ├── nested_squares_turtle.py   # 4 interlocked-square Turtle patterns
    │   └── fibonacci_spiral_turtle.py # Turtle Fibonacci spiral
    └── kandinsky/
        ├── rosette_kandinsky.py       # Kandinsky port of a classic rosette script
        ├── pixel_art_scene.py         # Hardcoded 16×11 pixel-art scene
        ├── bouncing_dvd_logo.py       # Classic bouncing DVD logo
        └── movable_rainbow_circle.py  # Movable rainbow circle toy
```

---

## 🧩 Prototypes & Debug Tools (`prototypes_and_debug/`)

Small experimental and debugging scripts built while developing larger projects:

### Sprite Rotator
[`prototypes_and_debug/sprite_rotator.py`](prototypes_and_debug/sprite_rotator.py) · *Created May 09, 2024*

Rotates a pixel-art projectile sprite around its center across any trigonometric angle. Uses **inverse (backward) mapping** over the rotated bounding box and **row-by-row horizontal run-length rendering** (`fill_rect`) to eliminate rotation gaps/holes and reduce draw calls.

### Checkers Capture Analyzer
[`prototypes_and_debug/checkers_capture_analyzer.py`](prototypes_and_debug/checkers_capture_analyzer.py) · *Created June 17, 2024*

Console diagnostic script created to inspect and benchmark how my [Checkers](https://github.com/maelangallais/Checkers) capture-detection algorithm behaved on specific board states.

### Checkers Board Visualizer
[`prototypes_and_debug/checkers_board_visualizer.py`](prototypes_and_debug/checkers_board_visualizer.py) · *Created June 17, 2024*

Companion `kandinsky` visualizer that renders the move/capture paths output by `checkers_capture_analyzer.py` directly onto a `10 × 10` board.

### Bitmap Character Renderer
[`prototypes_and_debug/bitmap_char_renderer.py`](prototypes_and_debug/bitmap_char_renderer.py) · *Created June 13, 2024*

Early prototype testing how to decode and draw binary- and hexadecimal-encoded character bitmaps on screen — the direct precursor to [Custom-Font-Drawer](https://github.com/maelangallais/Custom-Font-Drawer).

### QR Mask Patterns
[`prototypes_and_debug/qr_mask_patterns.py`](prototypes_and_debug/qr_mask_patterns.py) · *Created August 03, 2023*

Visualizes the **8 standard QR-code data-masking patterns** on screen to experiment with checkerboard/masking formulas prior to QR-code generation.

### Minimalist Maze Movement Test
[`prototypes_and_debug/maze_movement_test.py`](prototypes_and_debug/maze_movement_test.py) · *Created March 31, 2023*

An early movement-input experiment built for [Maze](https://github.com/maelangallais/Maze). Never used in the final game, but preserved for the simplicity of its **2-line `while True:` movement loop** (`x, y = x + kd(3) - kd(0), y + kd(2) - kd(1)`).

---

## 🎨 Colors (`colors/`)

### Interactive RGB Color Picker & Quantizer
[`colors/rgb_color_picker.py`](colors/rgb_color_picker.py) · *Created October 04, 2023*

The most genuinely useful utility in this archive. Displays a live full-width color preview alongside three interactive `R`, `G`, `B` gradient bars at the bottom of the screen:
- **Real-time RGB adjustment**: Use calculator keys (`Toolbox` / `Backspace` for Red, `,` / `x^y` for Green, `√` / `x²` for Blue) to step each channel from `0` to `255` with wrap-around.
- **Hardware RGB565 Quantization**: Includes `get_pixel_quantifier(color)`, which computes and displays the exact quantized RGB tuple (`5-bit` Red/Blue via `31/255`, `6-bit` Green via `63/255`) actually rendered by the NumWorks LCD.

### Bilinear Color Gradient
[`colors/bilinear_color_gradient.py`](colors/bilinear_color_gradient.py) · *Created October 13, 2025*

Draws a smooth 2D gradient across the `320 × 222` screen by bilinearly interpolating between 4 corner colors (`red`, `green`, `blue`, `magenta`). More generally, it serves as a clean 12-line reference for computing any weighted value between 4 corner points.

### RGB565 Pixel Inspector
[`colors/rgb565_pixel_inspector.py`](colors/rgb565_pixel_inspector.py) · *Created August 03, 2023*

Minimal 7-line test filling the screen with a target color and printing `get_pixel(160, 111)` to observe the difference between the requested RGB888 tuple and what the calculator reads back.

---

## 🔧 Diagnostics & Helpers (`diagnostics_and_helpers/`)

### Reflection Angle (Unfinished)
[`diagnostics_and_helpers/reflection_angle_wip.py`](diagnostics_and_helpers/reflection_angle_wip.py) · *Created April 02, 2024*

An early standalone attempt at computing a bounce reflection angle from an incident ray angle and an arbitrary surface angle (built while experimenting toward [Physics-Bounce](https://github.com/maelangallais/Physics-Bounce)). *Note: Despite several test attempts, this version never worked properly and was left as-is.*

### Clicks-Per-Second (CPS) Benchmark
[`diagnostics_and_helpers/cps_benchmark.py`](diagnostics_and_helpers/cps_benchmark.py) · *Created November 15, 2023*

Measures how many times you can press `EXE` (configurable on line 10) within 1 second (configurable on line 11) using `ion.keydown` and `time.monotonic`.

---

## 🐢 Early Graphics & Screen Toys (`early_graphics_and_toys/`)

### Turtle (`early_graphics_and_toys/turtle/`)

#### Turtle Rosette
[`early_graphics_and_toys/turtle/rosette_turtle.py`](early_graphics_and_toys/turtle/rosette_turtle.py) · *Created February 05, 2023*

A very early beginner `turtle` script drawing a colorful rosette.

#### Nested Squares (Turtle)
[`early_graphics_and_toys/turtle/nested_squares_turtle.py`](early_graphics_and_toys/turtle/nested_squares_turtle.py) · *Created March 09, 2023*

Draws interlocked squares using `turtle`. Mostly based on NumWorks' default example script, expanded with **4 different geometric pattern modes**.

#### Fibonacci Spiral
[`early_graphics_and_toys/turtle/fibonacci_spiral_turtle.py`](early_graphics_and_toys/turtle/fibonacci_spiral_turtle.py) · *Created May 01, 2023*

Simple `turtle` script that draws a Fibonacci-proportioned spiral for a user-chosen number of iterations.

### Kandinsky (`early_graphics_and_toys/kandinsky/`)

#### Kandinsky Rosette (Port)
[`early_graphics_and_toys/kandinsky/rosette_kandinsky.py`](early_graphics_and_toys/kandinsky/rosette_kandinsky.py) · *Created February 05, 2023*

Originally a third-party `turtle` rosette script that I adapted to run on **`kandinsky`** instead, adding custom color selection and interactive instructions while keeping its clean circle-drawing helper functions.

#### Pixel-Art Scene
[`early_graphics_and_toys/kandinsky/pixel_art_scene.py`](early_graphics_and_toys/kandinsky/pixel_art_scene.py) · *Created May 21, 2023*

Displays a hardcoded `16 × 11` pre-recorded pixel-art drawing on screen.

#### Bouncing DVD Logo
[`early_graphics_and_toys/kandinsky/bouncing_dvd_logo.py`](early_graphics_and_toys/kandinsky/bouncing_dvd_logo.py) · *Created May 11, 2023*

Simulates a pixel-art DVD logo bouncing off the NumWorks screen boundaries and changing color on impact.

#### Movable Rainbow Circle
[`early_graphics_and_toys/kandinsky/movable_rainbow_circle.py`](early_graphics_and_toys/kandinsky/movable_rainbow_circle.py) · *Created September 15, 2023*

Draws a multicolored circle that you can move around the screen with the directional keys.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `turtle`, `ion`, `math`, `random`, `time`).
