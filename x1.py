import os

# set the directory path where the images are stored
dir_path = "lizard_turtle/turtle"

# initialize a counter variable
counter = 50

# iterate over all the files in the directory
for filename in os.listdir(dir_path):

    # check if the file is an image file
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):

        # create a new filename with the counter variable
        new_filename = "image_" + str(counter) + os.path.splitext(filename)[1]

        # rename the file with the new filename
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))

        # increment the counter variable
        counter += 1
print("done")
