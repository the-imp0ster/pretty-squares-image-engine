# ‧͙⁺˚*･༓☾　Imp0ster's Colorful Squares Image Engine.　☽༓･*˚⁺‧͙

# ‧͙⁺˚*･༓☾  Imports.
import os
import random
from PIL import Image

# ‧͙⁺˚*･༓☾  Rouse the image engine from its slumber.
def image_engine(trait_directory, num_images):

# ‧͙⁺˚*･༓☾ Create/find a directory called Finished in the project folder to save the generated images to.
    finished_directory = "finished"
    if not os.path.exists(finished_directory):
        os.makedirs(finished_directory)

# ‧͙⁺˚*･༓☾ Get the layers in each trait folder.
    top_left_layers = os.listdir(os.path.join(trait_directory, "TopLeft"))
    top_right_layers = os.listdir(os.path.join(trait_directory, "TopRight"))
    bottom_right_layers = os.listdir(os.path.join(trait_directory, "BottomRight"))
    bottom_left_layers = os.listdir(os.path.join(trait_directory, "BottomLeft"))

# ‧͙⁺˚*･༓☾ Make a list of previously used combinations (so it doesn't make duplicates).
    used_combos = []

    for i in range(1, num_images + 1):
        while True:
# ‧͙⁺˚*･༓☾  Select a random layer from each subdirectory
            top_left_layer = random.choice(top_left_layers)
            top_right_layer = random.choice(top_right_layers)
            bottom_right_layer = random.choice(bottom_right_layers)
            bottom_left_layer = random.choice(bottom_left_layers)

# ‧͙⁺˚*･༓☾  Combine the four selected layers into one image by stacking them.
            top_left_image = Image.open(os.path.join(trait_directory, "TopLeft", top_left_layer))
            top_right_image = Image.open(os.path.join(trait_directory, "TopRight", top_right_layer))
            bottom_right_image = Image.open(os.path.join(trait_directory, "BottomRight", bottom_right_layer))
            bottom_left_image = Image.open(os.path.join(trait_directory, "BottomLeft", bottom_left_layer))

# ‧͙⁺˚*･༓☾  Resize each layer to 200x200 pixels (if needed).
            layer_size = (200, 200)
            top_left_image = top_left_image.resize(layer_size, Image.LANCZOS)
            top_right_image = top_right_image.resize(layer_size, Image.LANCZOS)
            bottom_right_image = bottom_right_image.resize(layer_size, Image.LANCZOS)
            bottom_left_image = bottom_left_image.resize(layer_size, Image.LANCZOS)

# ‧͙⁺˚*･༓☾  Create a new transparent image and stack the layers to make the finished image.
            combined_image = Image.new('RGBA', (200, 200), (0, 0, 0, 0))
            combined_image = Image.alpha_composite(combined_image, top_left_image)
            combined_image = Image.alpha_composite(combined_image, top_right_image)
            combined_image = Image.alpha_composite(combined_image, bottom_right_image)
            combined_image = Image.alpha_composite(combined_image, bottom_left_image)

# ‧͙⁺˚*･༓☾  Before saving the image, check if this combination has already been used.
            combination = (top_left_layer, top_right_layer, bottom_right_layer, bottom_left_layer)
            if combination not in used_combos:
                image_filename = os.path.join(finished_directory, f"{i}.png")
                combined_image.save(image_filename)
                
# ‧͙⁺˚*･༓☾  Add the combination to the used combinations list
                used_combos.append(combination)
                break

# ‧͙⁺˚*･༓☾ Provide the trait directory and number of images desired here, then call the image_engine function.
if __name__ == "__main__":
    trait_directory = "traits"
    num_images = 10
    image_engine(trait_directory, num_images)