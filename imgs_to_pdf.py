import os
from PIL import Image

os.mkdir('PDFs')
os.chdir('output')
prs = os.listdir()
for index, pr in enumerate(prs):
    os.chdir(pr)
    slides = os.listdir()
    slides_r = []
    slide_1 = None
    for ind, slide in enumerate(slides):
        sl = Image.open(slide)
        sl_r = sl.convert('RGB')
        if ind == 0:
            slide_1 = sl_r
        else:
            slides_r.append(sl_r)
    os.chdir('..')
    slide_1.save(f'../PDFs/presentation{index+1}.pdf', save_all=True, append_images=slides_r)