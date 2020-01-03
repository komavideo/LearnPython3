from PIL import Image, ImageDraw, ImageFont
 
image = Image.open("mylogo.jpg")

image_draw = ImageDraw.Draw(image)

# 画线
image_draw.line((0, image.height, image.width, 0), fill=(255, 0, 0), width=8)
# 矩形
image_draw.rectangle((100, 100, 200, 200), fill=(0, 255, 0))
# # 圆形
image_draw.ellipse((250, 300, 450, 400), fill=(255, 0, 0))
# # 写字
image_font = ImageFont.truetype("C:\Windows\Fonts\msyh.ttc", size=48)
image_draw.multiline_text((0, 0), 'Pillow is good!', fill=(255, 255, 0), font = image_font)

image.save("img_edited.png")
