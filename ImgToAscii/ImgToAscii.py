import sys
from PIL import Image

if len(sys.argv) < 2:
    print("Please provide a image file")
else:
    try:
        filename = sys.argv[1]
        im = Image.open(filename)
        pixels = im.load()
        finalimage = ""
        grayscalevalues = list("@B%&#*okbdpqwmZOLCJUYXzcvuxrjft/|(1[?-+<>i!lI:,\"`. ")

        width, height = im.size
        with open("Test.txt", "w") as outfile:
            for i in range(height):
                for j in range(width):
                    pixel = pixels[j,i]
                    grayscale = (int) (0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2])//5
                    finalimage += grayscalevalues[grayscale-1]
                finalimage += "\n"
                outfile.write(finalimage)
                finalimage = ""

    except IOError:
        print("The file given was not a valid image file")