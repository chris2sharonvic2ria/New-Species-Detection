from PIL import Image
import os

# set the path to the directory containing the images
path = "lizard_turtle/turtle"

# loop through all the files in the directory
for filename in os.listdir(path):
    # check if the file is a .jpg image
    if filename.endswith(".jpg"):
        # open the image file
        img = Image.open(os.path.join(path, filename))

        # create the new file name with .jpeg extension
        new_filename = os.path.splitext(filename)[0] + ".jpeg"

        # save the image with the new file name and jpeg format
        img.save(os.path.join(path, new_filename), "JPEG")

        # close the image file
        img.close()
print("done")
