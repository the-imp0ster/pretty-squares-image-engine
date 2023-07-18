# pretty-squares-image-engine

![image_engine](image_engine_preview.png)

Welcome to my first image engine!
This Python program generates unique and vibrant square images by combining various layers from different trait directories (16 layers in total), and saves them to the user's local machine.

## How It Works

The image engine works by selecting random layers from four different subdirectories: TopLeft, TopRight, BottomRight, and BottomLeft.
It then stacks these layers together to create a visually appealing square image.
To ensure non-fungibility, the engine keeps track of previously used combinations, preventing duplicates.

## Requirements

- Python 3.11
- PIL (Python Imaging Library)

## Installation

1. Make sure you have Python installed on your system.
2. Install the required PIL library by running the following command:

```bash
pip install pillow
```

Clone this repo to your machine, replacing your_username in the url below with... your username.

```bash
git clone https://github.com/your_username/image-engine.git
```

##Usage

I have provided the original layers and their directory to play with.
Or, you can prepare yourown trait images by organizing them into four subdirectories: TopLeft, TopRight, BottomRight, and BottomLeft, within a directory called traits, or changing these names if you like within the program, to reflect your directory structure.

Run the image engine by providing the trait_directory and the number of images you want to generate (num_images) in the __main__ block:

```bash
if __name__ == "__main__":
    trait_directory = "traits"
    num_images = 10
    image_engine(trait_directory, num_images)
```
The generated images will be saved in a directory called "finished" within the project folder, numbered sequentially starting at 1.

##Customization

Feel free to customize the size of the layers and output images by modifying the layer_size and combined_image dimensions in the script.
Additionally, you can create your own trait images to add more variety to the generated artwork.

##License
This project is licensed under the MIT License.

###Have fun!
