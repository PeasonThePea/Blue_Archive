import imageio.v3 as iio
filenames = ['hina1.png', 'hina2.png', 'hina3.png']
images = [ ]
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('hina_special.gif', images, duration = 1000, loop = 0)
