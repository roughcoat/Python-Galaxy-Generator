#
# This script generates a 3D galaxy from a number of parameters and stores
# it in an array. You can modify this script to store the data in a database
# or whatever your purpose is. THIS script uses the data only to generate a
# PNG with a 2D view from top of the galaxy.
#
# The algorithm used to generate the galaxy is borrowed from Ben Motz
# <motzb@hotmail.com>. The original C source code for DOS (including a 3D
# viewer) can be downloaded here:
#
# http://bits.bristol.ac.uk/motz/tep/galaxy.html
#
# Unfortunately, the original python code has been lost to time and a lack of wanting-to- search-through-several-hundred-webpages-for-one-webarchive-page. Sorry, original python guy.
#
# A fair portion of the revisions and code is from /u/_Foxtrot_ on reddit. They are much better with the python-fu than I!
#

from PIL import Image
from PIL import ImageDraw
import random
import math
import sys

# Generation parameters:

# raw_input the user's desired values
# Background color of the created PNG
PNGBGCOLOR = (0, 0, 0)

# Foreground color of the created PNG
PNGCOLOR = (255, 255, 255)

# Quick Filename
RAND = random.randrange(0, 108000000000)

# ---------------------------------------------------------------------------
NAME = raw_input('Galaxy Name <You must input a name>:')

STRAMT = int(raw_input('Number of Stars <Example:2000>:') or "2000")

HUBX   = float(raw_input('Length of Galaxy <Example:600>:') or "600")

HUBY   = float(raw_input('Height of Galaxy <Example:300>:') or "300")

HUBZ   = float(raw_input('Depth of Galaxy <Example:100>:') or "100")

PNGSIZE = float(raw_input('X and Y Size of PNG <Default:1200>:') or "1200")

PNGFRAME = float(raw_input('PNG Frame Size <Default:50>:') or "50")

stars = []


def generateStars():
    # Now generate the Hub. This places a point on or under the curve
    # maxHubZ - s d^2 where s is a scale factor calculated so that z = 0 is
    # at maxHubR (s = maxHubZ / maxHubR^2) AND so that minimum hub Z is at
    # maximum disk Z. (Avoids edge of hub being below edge of disk)

    scale = HUBZ / (HUBX * HUBY)
    i = 0
    while i < STRAMT:
        # Choose a random distance from center
        distX = random.random() * HUBX
        distY = random.random() * HUBY

        # Any rotation (points are not on arms)
        theta = random.random() * 360

        # Convert to cartesian
        x = math.cos(theta * math.pi / 180.0) * distX
        y = math.sin(theta * math.pi / 180.0) * distY
        z = (random.random() * 2 - 1) * (HUBZ - scale * distX * distY)

        # Add star to the stars array
        stars.append((x, y, z))

        # Process next star
        i = i + 1


def drawToPNG(filename):
    image = Image.new("RGB", (int(PNGSIZE), int(PNGSIZE)), PNGBGCOLOR)
    draw = ImageDraw.Draw(image)

    # Find maximal star distance
    max = 0
    for (x, y, z) in stars:
        if abs(x) > max: max = x
        if abs(y) > max: max = y
        if abs(z) > max: max = z

    # Calculate zoom factor to fit the galaxy to the PNG size
    factor = float(PNGSIZE - PNGFRAME * 2) / (max * 2)
    for (x, y, z) in stars:
        sx = factor * x + PNGSIZE / 2
        sy = factor * y + PNGSIZE / 2
        draw.point((sx, sy), fill=PNGCOLOR)

    # Save the PNG
    image.save(filename)


# Generate the galaxy          
generateStars()

# Save the galaxy as PNG to galaxy.png
drawToPNG("ellipticalgalaxy" + str(RAND) + "-" + str(NAME) + ".png")

# Create the galaxy's data galaxy.txt
with open("ellipticalgalaxy" + str(RAND) + "-" + str(NAME) + ".txt", "w") as text_file:
    text_file.write("Galaxy Number: {}".format(RAND))
    text_file.write("Galaxy Name: {}".format(NAME))
    text_file.write("Hub Stars: {}".format(STRAMT))
    text_file.write("Hub Length: {}".format(HUBX))
    text_file.write("Hub Width: {}".format(HUBY))
    text_file.write("Hub Depth: {}".format(HUBZ))
    text_file.write("Image Size: {}".format(PNGSIZE))
    text_file.write("Frame Size: {}".format(PNGFRAME))