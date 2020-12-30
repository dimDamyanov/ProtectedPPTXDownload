from PIL import Image

img1 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p1.png')
img2 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p2.png')
img3 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p3.png')
img4 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p4.png')
img5 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p5.png')
img6 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p6.png')
img7 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p7.png')
img8 = Image.open(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\p8.png')

img1 = img1.convert('RGB')
img2 = img2.convert('RGB')
img3 = img3.convert('RGB')
img4 = img4.convert('RGB')
img5 = img5.convert('RGB')
img6 = img6.convert('RGB')
img7 = img7.convert('RGB')
img8 = img8.convert('RGB')

image_list = [img2, img3, img4, img5, img6, img7, img8]

img1.save(r'C:\Users\Dimitar Damyanov\Desktop\presentation1\presentation.pdf', save_all=True, append_images=image_list)