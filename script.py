import os
from PIL import Image, ImageOps, ImageEnhance
from jinja2 import Environment, FileSystemLoader


path = 'r'+input('Input path to your GIF-FILE: ')
num_key_frames = 12

filename = path.split('.')[0].split('\\')[-1]
img_frames_root = 'media/img_frames/'
ascii_frames_root = 'media/ascii_frames/'
if os.path.exists(img_frames_root+filename):
    pass
else:
    os.mkdir(img_frames_root+filename)
with Image.open(path[1:].replace('\\', '/')) as im:
    for i in range(num_key_frames):
        im.seek(im.n_frames // num_key_frames * i)
        im.save(img_frames_root + filename + '/' + '{}.png'.format(i))
if os.path.exists(ascii_frames_root+filename):
    pass
else:
    os.mkdir(ascii_frames_root+filename)
ascii_list = []
with os.scandir(img_frames_root + filename) as dir:
    for c, f in enumerate(dir):
        chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        img = Image.open(img_frames_root + filename + '/' + f.name).convert('RGB')
        r_img = img.resize((350, 100))
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
        with open(ascii_frames_root + filename + '/' + '{}.txt'.format(c), "w") as file:
            file.write(ascii_img)
        ascii_list.append(ascii_img)
print('TXT ASCII FRAMES SAVED IN ' + ascii_frames_root + filename)
print('JPG IMAGE FRAMES SAVED IN ' + img_frames_root + filename)
abs_path = os.path.abspath(os.curdir)
env = Environment(
    loader=FileSystemLoader(abs_path),
    trim_blocks=True,
    lstrip_blocks=True)
template = env.get_template('web_page/static/base.html')

data = {
    'title': filename,
    'ascii_list': ascii_list,
}
with open('web_page/' + filename + '.html', "w", encoding='utf-8') as file:
    print(template.render(data), file=file)
