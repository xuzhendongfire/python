from PIL import Image

path = 'D:/迅雷下载/images_003/images/00003923_017.png'
path2 = 'C:/Users/xuzhendong/Pictures/Camera Roll/14-1509250Z615109.jpg'
path3 = 'D:/xzd/bisai/IBMPowerAI/sample2.jpg'
im = Image.open(path3)
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        print(r,g,b)

