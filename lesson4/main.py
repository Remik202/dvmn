from PIL import Image

image = Image.open("example.jpg")
image.convert ("RGB")
red, green, blue = image.split()

red_croped = red.crop((50, 0, red.width, red.height))
red_croped2 = red.crop((25, 0, red.width - 25, red.height))
red_image = Image.blend(red_croped, red_croped2, 0.5)

blue_croped = blue.crop((0, 0, blue.width - 50, blue.height))
blue_croped2 = blue.crop((25, 0, blue.width - 25, blue.height))
blue_image = Image.blend(blue_croped, blue_croped2, 0.5)

green_image = green.crop((25, 0, green.width - 25, green.height))

icon = Image.merge("RGB", (red_image, green_image, blue_image))

icon.save("icon.jpg")
