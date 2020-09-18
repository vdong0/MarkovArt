from PIL import Image
from ImageParser import ImageParser
from MarkovModel import MarkovModel
from MarkovProcess import MarkovProcess

ip = ImageParser()
mm = MarkovModel()
mp = MarkovProcess()

# All images are png and 300x300
try:
    img1 = Image.open('Blossoming-Almond-Tree.png')
    img2 = Image.open('Café-Terrace-on-the-Place-du-Forum,-Arles,-at-Night,-The.png')
    img3 = Image.open('Irises.png')
    img4 = Image.open('Wheat-Field-with-Cypresses.png')
    img5 = Image.open('Starry-Night.png')
except IOError:
    pass

width, height = img1.size

training_data = [img1, img2, img3, img4, img5]

combined_rgb_lists = []

for img in training_data:
    rgb_list = ip.image_to_list(img)
    combined_rgb_lists.append(rgb_list)

order = 2
markov_dict = mm.train_model(combined_rgb_lists, order)

created_rgb_list = mp.create_rgb_list(markov_dict, width*height, order)

created_image = ip.list_to_image(created_rgb_list, width, height)

created_image.save("CreatedImage.png")
