from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os

#API
    var ourBrands = [
            {
                "name": "Acuvue",
                "cruelty": "yes",
                "contact": "1-888-364-3577"
            },
            {
                "name": "HydroFlask",
                "cruelty": "no",
                "contact": "https://www.hydroflask.com/"
            },
            {
                "name": "Revlon",
                "cruelty": "yes",
                "contact": "1-800-992-5629"
            },
            {
                "name": "AquaFresh",
                "cruelty": "yes",
                "contact": "1-800-897-7535"
            },
            {
                "name": "Arm & Hammer",
                "cruelty": "yes",
                "contact": "1-800-524-1328"
            },
            {
                "name": "BENGAY",
                "cruelty": "yes",
                "contact": "1-800-223-0182"
            },
            {
                "name": "Benefit Cosmetics",
                "cruelty": "yes",
                "contact": "1-800-781-2336"
            },
            {
                "name": "Revlon",
                "cruelty": "yes",
                "contact": "1-800-992-5629"
            },
            {
                "name": "Band Aid",
                "cruelty": "yes",
                "contact": "1-866-565-2873"
            },
            {
                "name": "Calvin Klein Cosmetics",
                "cruelty": "yes",
                "contact": "No #"
            },
            {
                "name": "Clinique",
                "cruelty": "yes",
                "contact": "212-572-3800"
            },
            {
                "name": "Clorox",
                "cruelty": "yes",
                "contact": "1-800-227-1860"
            },
            {
                "name": "Coppertone",
                "cruelty": "yes",
                "contact": "1-800-842-4090"
            },
            {
                "name": "Downy",
                "cruelty": "yes",
                "contact": "1-800-543-1745"
            },
            {
                "name": "Febreze",
                "cruelty": "yes",
                "contact": "1-800-543-1745"
            },
            {
                "name": "Gillette",
                "cruelty": "yes",
                "contact": "1-800-543-1745"
            },
            {
                "name": "24K Cosmetics",
                "cruelty": "no",
                "contact": "http://www.24kcosmetics.com/"
            },
            {
                "name": "Anastasia Beverly Hills",
                "cruelty": "no",
                "contact": "310-474-4300"
            },
            {
                "name": "Avalon Organics",
                "cruelty": "no",
                "contact": "1-800-227-5120"
            },
            {
                "name": "Fenty Beauty",
                "cruelty": "yes",
                "contact": "https://fentybeauty.com/"
            },
            {
                "name": "Covergirl",
                "cruelty": "no",
                "contact": "https://www.covergirl.com/"
            },
            {
                "name": "ELF Cosmetics",
                "cruelty": "no",
                "contact": "https://www.elfcosmetics.com/"
            },
            {
                "name": "Milani",
                "cruelty": "no",
                "contact": "https://www.milanicosmetics.com/"
            },
            {
                "name": "Urban Decay",
                "cruelty": "no",
                "contact": "https://www.urbandecay.com/"
            },
            {
                "name": "Rare Beauty",
                "cruelty": "no",
                "contact": "https://www.rarebeauty.com/"
            },
            {
                "name": "NARS Cosmetics",
                "cruelty": "no",
                "contact": "https://www.narscosmetics.com/"
            },
            {
                "name": "Charlotte Tilbury",
                "cruelty": "no",
                "contact": "https://www.charlottetilbury.com/us"
            },
            {
                "name": "Florence by Mills",
                "cruelty": "yes",
                "contact": "https://florencebymills.com/"
            },
            {
                "name": "NYX Cosmetics",
                "cruelty": "no",
                "contact": "https://www.nyxcosmetics.com/"
            },
            {
                "name": "Jeffree Star Cosmetics",
                "cruelty": "no",
                "contact": "https://jeffreestarcosmetics.com/"
            },
            {
                "name": "Burt's Bees",
                "cruelty": "no",
                "contact": "https://www.burtsbees.com/"
            }

];


# Load the model
model = load_model('keras_model.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
# Replace this with the path to your image
for pic in os.listdir("./test_images"):
    path = os.path.join("test_images", pic)
    image = Image.open(path)
#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    labels=["Disney", "Clinique"]
    prediction = model.predict(data)
    print(prediction)
    print("image:", path)
    print("model's guess:", labels[np.argmax(prediction)])
