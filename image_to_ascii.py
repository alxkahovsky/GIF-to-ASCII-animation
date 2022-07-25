import os
from PIL import Image, ImageOps, ImageEnhance


with os.scandir('Gandalf_laugh_frames') as dir:
    a = len([name for name in os.listdir('Gandalf_laugh_frames')]) + 1
    for c, f in enumerate(dir, a):
        chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        img = Image.open('Gandalf_laugh_frames/' + f.name)
        r_img = img.resize((400, 100))
        brspns_image = ImageEnhance.Brightness(r_img).enhance(1.6)
        r_img = brspns_image
        brspns_image = ImageEnhance.Sharpness(r_img).enhance(1.6)
        r_img = brspns_image
        gr_img = r_img.convert('L')
        pixels = gr_img.getdata()
        characters = ''.join([chars[pixel // 25] for pixel in pixels])
        pix_c = len(characters)
        ascii_img = '\n'.join(
            [characters[index:(index + r_img.size[0])] for index in range(0, pix_c, r_img.size[0])])
        n = f.name[0]
        with open('Gandalf_laugh_ascii/'+n+'.txt', "w") as file:
            file.write(ascii_img)





