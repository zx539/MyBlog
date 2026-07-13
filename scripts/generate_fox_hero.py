from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageFilter


SCALE = 2
WIDTH = 1200
HEIGHT = 1600
W = WIDTH * SCALE
H = HEIGHT * SCALE


def box(values):
    return tuple(int(value * SCALE) for value in values)


def points(values):
    return [(int(x * SCALE), int(y * SCALE)) for x, y in values]


def color(hex_value):
    value = hex_value.lstrip("#")
    return tuple(int(value[index:index + 2], 16) for index in (0, 2, 4))


canvas = Image.new("RGB", (W, H), color("#fff0f7"))
pixels = canvas.load()
stops = [
    (0.0, color("#765f9e")),
    (0.38, color("#d47fb0")),
    (0.68, color("#f4a4c5")),
    (1.0, color("#ffd9d5")),
]

for y in range(H):
    position = y / max(H - 1, 1)
    for index in range(len(stops) - 1):
        start_pos, start_color = stops[index]
        end_pos, end_color = stops[index + 1]
        if start_pos <= position <= end_pos:
            amount = (position - start_pos) / (end_pos - start_pos)
            row_color = tuple(
                int(start_color[channel] * (1 - amount) + end_color[channel] * amount)
                for channel in range(3)
            )
            break
    for x in range(W):
        pixels[x, y] = row_color

random.seed(539)
sky = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sky_draw = ImageDraw.Draw(sky)

# Fine stars and cross-shaped glints.
for _ in range(95):
    x = random.randint(35, WIDTH - 35)
    y = random.randint(45, 650)
    radius = random.choice([1, 1, 2, 2, 3])
    alpha = random.randint(90, 220)
    sky_draw.ellipse(box((x - radius, y - radius, x + radius, y + radius)), fill=(255, 244, 250, alpha))

for x, y, size in [(140, 240, 17), (1010, 180, 12), (880, 500, 16), (275, 610, 10)]:
    sky_draw.line(points(((x - size, y), (x + size, y))), fill=(255, 244, 249, 210), width=2 * SCALE)
    sky_draw.line(points(((x, y - size), (x, y + size))), fill=(255, 244, 249, 210), width=2 * SCALE)

# Soft cloud banks.
clouds = Image.new("RGBA", (W, H), (0, 0, 0, 0))
cloud_draw = ImageDraw.Draw(clouds)
for cx, cy, rx, ry, alpha in [
    (170, 410, 260, 105, 120),
    (920, 350, 330, 125, 105),
    (360, 700, 410, 120, 95),
    (1050, 730, 310, 115, 100),
]:
    for offset in range(-2, 3):
        cloud_draw.ellipse(
            box((cx - rx + offset * 55, cy - ry - abs(offset) * 18, cx + rx + offset * 55, cy + ry)),
            fill=(255, 225, 241, alpha),
        )
clouds = clouds.filter(ImageFilter.GaussianBlur(25 * SCALE))
canvas = Image.alpha_composite(canvas.convert("RGBA"), clouds)
canvas = Image.alpha_composite(canvas, sky)

scene = ImageDraw.Draw(canvas)

# Sunlit horizon and distant city.
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)
for radius in range(230, 20, -14):
    alpha = int(2 + (230 - radius) * 0.18)
    glow_draw.ellipse(box((165 - radius, 970 - radius, 165 + radius, 970 + radius)), fill=(255, 231, 174, alpha))
glow = glow.filter(ImageFilter.GaussianBlur(18 * SCALE))
canvas = Image.alpha_composite(canvas, glow)
scene = ImageDraw.Draw(canvas)

scene.rectangle(box((0, 1120, WIDTH, HEIGHT)), fill="#55415f")
random.seed(42)
x = 0
while x < WIDTH:
    building_width = random.randint(45, 100)
    building_height = random.randint(80, 300)
    top = 1120 - building_height
    shade = random.choice(["#493850", "#5e4766", "#684d6a", "#3f344d"])
    scene.rectangle(box((x, top, x + building_width, 1240)), fill=shade)
    for wy in range(top + 22, 1110, 34):
        for wx in range(x + 12, x + building_width - 9, 24):
            if random.random() > 0.48:
                scene.rectangle(box((wx, wy, wx + 7, wy + 12)), fill=random.choice(["#ffd878", "#f9a6bb", "#9edbe1"]))
    x += building_width + random.randint(5, 14)

# Rooftop railing and cables.
scene.rectangle(box((0, 1230, WIDTH, 1260)), fill="#302a3d")
scene.line(points(((0, 1080), (1200, 880))), fill="#413548", width=4 * SCALE)
scene.line(points(((0, 1125), (1200, 930))), fill="#413548", width=2 * SCALE)
for x in (180, 760, 1050):
    scene.ellipse(box((x - 8, 1028, x + 8, 1044)), outline="#413548", width=3 * SCALE)

# Fox tail behind the character.
tail = Image.new("RGBA", (W, H), (0, 0, 0, 0))
tail_draw = ImageDraw.Draw(tail)
tail_draw.ellipse(box((675, 930, 1250, 1510)), fill="#c75584", outline="#51334e", width=10 * SCALE)
tail_draw.ellipse(box((810, 1030, 1170, 1425)), fill="#f08db2")
tail_draw.polygon(points(((1020, 1350), (1195, 1500), (1000, 1475), (890, 1390))), fill="#fff0f6")
tail = tail.filter(ImageFilter.GaussianBlur(1.2 * SCALE))
canvas = Image.alpha_composite(canvas, tail)
draw = ImageDraw.Draw(canvas)

# Character body and sailor-inspired outfit.
draw.ellipse(box((350, 1030, 990, 1710)), fill="#252238", outline="#3a2941", width=9 * SCALE)
draw.polygon(points(((515, 1070), (805, 1070), (940, 1510), (350, 1510))), fill="#fff8fc", outline="#3a2941")
draw.polygon(points(((485, 1090), (650, 1260), (820, 1090), (750, 1030), (555, 1030))), fill="#d84f83", outline="#3a2941", width=7 * SCALE)
draw.polygon(points(((650, 1215), (735, 1310), (650, 1390), (565, 1310))), fill="#f2b9cf", outline="#3a2941", width=6 * SCALE)
draw.line(points(((650, 1390), (650, 1570))), fill="#d84f83", width=18 * SCALE)

# Hair mass, fox ears, neck, and face.
draw.ellipse(box((330, 280, 980, 1235)), fill="#542f52", outline="#35263d", width=10 * SCALE)
draw.polygon(points(((395, 390), (425, 95), (575, 360))), fill="#542f52", outline="#35263d", width=10 * SCALE)
draw.polygon(points(((745, 340), (900, 92), (930, 430))), fill="#542f52", outline="#35263d", width=10 * SCALE)
draw.polygon(points(((435, 326), (454, 165), (535, 347))), fill="#f08db2")
draw.polygon(points(((786, 330), (875, 160), (891, 383))), fill="#f08db2")
draw.rectangle(box((570, 910, 740, 1120)), fill="#f2c2bd", outline="#543642", width=7 * SCALE)
draw.ellipse(box((430, 365, 855, 1010)), fill="#f8d2ca", outline="#513342", width=8 * SCALE)

# Hair framing and layered bangs.
draw.pieslice(box((330, 255, 950, 870)), start=178, end=358, fill="#542f52")
draw.polygon(points(((390, 440), (470, 300), (515, 660), (455, 750))), fill="#542f52")
draw.polygon(points(((480, 340), (575, 255), (610, 630), (535, 690))), fill="#66375f")
draw.polygon(points(((565, 300), (675, 245), (690, 620), (615, 650))), fill="#542f52")
draw.polygon(points(((655, 275), (785, 320), (760, 645), (688, 610))), fill="#66375f")
draw.polygon(points(((755, 340), (870, 445), (835, 760), (770, 680))), fill="#542f52")

# Eyes, lashes, brows, blush, nose, and mouth.
for eye_x in (555, 730):
    draw.arc(box((eye_x - 58, 600, eye_x + 58, 690)), start=195, end=345, fill="#3b2a43", width=9 * SCALE)
    draw.ellipse(box((eye_x - 34, 626, eye_x + 34, 713)), fill="#9f4f91", outline="#3b2a43", width=5 * SCALE)
    draw.ellipse(box((eye_x - 20, 648, eye_x + 20, 710)), fill="#402b56")
    draw.ellipse(box((eye_x - 13, 640, eye_x + 2, 660)), fill="#ffffff")
draw.arc(box((500, 555, 600, 610)), start=195, end=330, fill="#6c4059", width=5 * SCALE)
draw.arc(box((680, 555, 780, 610)), start=210, end=345, fill="#6c4059", width=5 * SCALE)
draw.ellipse(box((470, 735, 565, 785)), fill="#ef9da9")
draw.ellipse(box((735, 735, 830, 785)), fill="#ef9da9")
draw.line(points(((647, 705), (635, 765), (655, 770))), fill="#c4777d", width=4 * SCALE)
draw.arc(box((595, 770, 700, 845)), start=15, end=165, fill="#9f4e68", width=5 * SCALE)

# Hair highlights and floating petals.
draw.arc(box((390, 300, 880, 980)), start=190, end=286, fill="#9e5b86", width=13 * SCALE)
draw.arc(box((430, 320, 850, 930)), start=198, end=265, fill="#d779a4", width=6 * SCALE)
for px, py, rotation in [(130, 870, 0), (1030, 620, 1), (210, 1020, 2), (965, 310, 3), (90, 535, 1)]:
    petal = Image.new("RGBA", (90 * SCALE, 90 * SCALE), (0, 0, 0, 0))
    petal_draw = ImageDraw.Draw(petal)
    petal_draw.ellipse(box((20, 8, 58, 68)), fill=(255, 203, 224, 225))
    petal = petal.rotate(rotation * 28 + 18, resample=Image.Resampling.BICUBIC, expand=True)
    canvas.alpha_composite(petal, (int((px - 45) * SCALE), int((py - 45) * SCALE)))

# Subtle foreground light.
overlay = Image.new("RGBA", (W, H), (255, 217, 234, 16))
canvas = Image.alpha_composite(canvas, overlay)
canvas = canvas.convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

output = Path(__file__).resolve().parents[1] / "static" / "images" / "fox-girl-hero.png"
output.parent.mkdir(parents=True, exist_ok=True)
canvas.save(output, "PNG", optimize=True)
print(output)
