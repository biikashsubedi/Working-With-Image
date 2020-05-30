from PIL import Image, ImageFilter

img = Image.open('./image/bulbasaur.jpg')
img_filter = img.filter(ImageFilter.BLUR)
img_filter2 = img.convert('L')
img_filter3 = img.rotate(90)
img_filter4 = img.resize((100,100))
box = (100,100, 400,400)
img_filter5 = img.crop(box)

img_filter2.save("bulbasaur_BW.png", 'png')
img_filter.save("bulbasaur_blur.png", 'png')
img_filter3.save("bulbasaur_rotate90.png", 'png')
img_filter4.save("bulbasaur_resize.png", 'png')
img_filter5.save("bulbasaur_crop.png", 'png')

print(img)

# img_filter.show()
# img_filter2.show()






#THUMBNAIL~ best way to resize photo

img1 = Image.open('./image/home.jpg')
img1.thumbnail((400,400))
img1.save('thumbnail.png', 'png')


















