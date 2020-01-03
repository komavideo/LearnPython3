# 切出图像透明区
from PIL import Image, ImageDraw, ImageFilter

# 图像文件打开
im_rgb = Image.open('res/mylogo.png')

###############################################
# 半透明50%(128/255)
# im_rgba = im_rgb.copy()
# im_rgba.putalpha(128)
# im_rgba.save('out/img_putalpha.png')

###############################################
# 切出形状透明
im_a = Image.new("L", im_rgb.size, 255) # white
draw = ImageDraw.Draw(im_a)
draw.rectangle((200, 100, 300, 200), fill=0, outline=0) # black
# draw.ellipse((200, 100, 300, 200), fill=0)
im_a.save("out/img_a.png")

im_rgba = im_rgb.copy()
im_rgba.putalpha(im_a)
# 高斯羽化 Start
# im_a_blur = im_a.filter(ImageFilter.GaussianBlur(1))
# im_rgba.putalpha(im_a_blur)
# 高斯羽化 End

im_rgba.save('out/img_putalpha.png')
