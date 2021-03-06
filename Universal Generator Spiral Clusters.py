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

# Quick Filename
RAND = random.randrange(0, 240000000000)

# ---------------------------------------------------------------------------
NAME = raw_input('Galaxy Name:')

NUMC = int(raw_input('Number of Globular Clusters <Default:1>:') or "1")

NUMHUB = int(raw_input('Number of Core Stars <Default:2000>:') or "2000")

NUMDISK = int(raw_input('Number of Disk Stars <Default:4000>:') or "4000")

NUMCLUS = int(raw_input('Number of Stars in each Cluster <Default:100>:') or "100")

HUBRAD = float(raw_input('Radius of Core <Default:90.0>:') or "90.0")

DISKRAD = float(raw_input('Radius of Disk <Default:45.0>:') or "45.0")

CLUSRAD = int (raw_input('Radius of each cluster <Default:10>:') or "10")

NUMARMS = int(raw_input('Number of Galactic Arms <Default:3>:') or "3")

ARMROTS = float(raw_input('Tightness of Arm Winding <Default:0.5>:') or "0.5")

ARMWIDTH = float(raw_input('Arm Width in Degrees <Default:65>:') or "65")

MAXHUBZ = float(raw_input('Maximum Depth of Core <Default:16.0>:') or "16.0")

MAXDISKZ = float(raw_input('Maximum Depth of Arms <Default:2.0>:') or "2.0")

FUZZ = float(raw_input('Maximum Outlier Distance from Arms <Default:25.0>:') or "25.0")

PNGSIZE = float(raw_input('X and Y Size of PNG <Default:1200>:') or "1200")

PNGFRAME = float(raw_input('PNG Frame Size <Default:50>:') or "50")

#star_colors = [(255, 185, 201)()()()()()()()()()()()()()()()()()()()()()()()]

clusters = []


def generateClusters():
    c = 0
    while c < GLOC:
        dist = random.random() * DISKRAD
        theta = random.random() * 360
        
        # Convert to Cartesian
        x = math.cos(theta * math.pi / 180.0) * dist
        y = math.sin(theta * math.pi / 180.0) * dist
        z = (random.random() * 2 - 1) * ((HUBRAD + DISKRAD) - scale * dist * dist)
        
        clusters.append((x, y, z, GLOS))
        
        c = c+1

stars = []

def generateStars():
    # omega is the separation (in degrees) between each arm
    # Prevent div by zero error:
    if NUMARMS:
        omega = 360.0 / NUMARMS
    else:
        omega = 0.0
    i = 0
    while i < NUMDISK:
        
        # Choose a random distance from center
        dist = HUBRAD + random.random() * DISKRAD

        # This is the 'clever' bit, that puts a star at a given distance
        # into an arm: First, it wraps the star round by the number of
        # rotations specified.  By multiplying the distance by the number of
        # rotations the rotation is proportional to the distance from the
        # center, to give curvature
        theta = ((360.0 * ARMROTS * (dist / DISKRAD))

                 # Then move the point further around by a random factor up to
                 # ARMWIDTH
                 + random.random() * ARMWIDTH

                 # Then multiply the angle by a factor of omega, putting the
                 # point into one of the arms
                 # + (omega * random.random() * NUMARMS )
                 + omega * random.randrange(0, NUMARMS)

                 # Then add a further random factor, 'fuzzin' the edge of the arms
                 + random.random() * FUZZ * 2.0 - FUZZ
                 # + random.randrange( -FUZZ, FUZZ )
                 )

        # Convert to cartesian
        #def cartesian_convert
        x = math.cos(theta * math.pi / 180.0) * dist
        y = math.sin(theta * math.pi / 180.0) * dist
        z = random.random() * MAXDISKZ * 2.0 - MAXDISKZ
        
        SRAN = random.randrange(0, 23)
        if SRAN == 0:
            scol = (255, 185, 201)
        elif SRAN == 1: 
            scol = (255, 204, 198)
        elif SRAN == 2:  
            scol = (255, 218, 198)
        elif SRAN == 3: 
            scol = (255, 219, 178)
        elif SRAN == 4: 
            scol = (255, 233, 178)
        elif SRAN == 5:
            scol = (255, 233, 178)
        elif SRAN == 6:
            scol = (255, 233, 178)
        elif SRAN == 7:
            scol = (255, 233, 178)
        elif SRAN == 8:
            scol = (255, 233, 178)
        elif SRAN == 9: 
            scol = (255, 246, 178)
        elif SRAN == 10: 
            scol = (255, 246, 178)
        elif SRAN == 11: 
            scol = (255, 253, 178)
        elif SRAN == 13:
            scol = (255, 253, 178)
        elif SRAN == 14: 
            scol = (255, 254, 212)
        elif SRAN == 15:
            scol = (255, 254, 212)
        elif SRAN == 16: 
            scol = (254, 255, 248)
        elif SRAN == 17: 
            scol = (255, 255, 255)
        elif SRAN == 18:
            scol = (236, 255, 255)
        elif SRAN == 19:
            scol = (236, 255, 255)
        elif SRAN == 20:
            scol = (207, 251, 255)
        elif SRAN == 21:
            scol = (207, 251, 255)
        elif SRAN == 22:
            scol = (207, 238, 255)
        elif SRAN == 23:
            scol = (165, 196, 255)

        # Add star to the stars array
        stars.append((x, y, z, scol))

        # Process next star
        i = i + 1
        sran = 0

    # Now generate the Hub. This places a point on or under the curve
    # maxHubZ - s d^2 where s is a scale factor calculated so that z = 0 is
    # at maxHubR (s = maxHubZ / maxHubR^2) AND so that minimum hub Z is at
    # maximum disk Z. (Avoids edge of hub being below edge of disk)

    scale = MAXHUBZ / (HUBRAD * HUBRAD)
    i = 0
    while i < NUMHUB:
        
        # Choose a random distance from center
        dist = random.random() * HUBRAD

        # Any rotation (points are not on arms)
        theta = random.random() * 360

        # Convert to cartesian
        x = math.cos(theta * math.pi / 180.0) * dist
        y = math.sin(theta * math.pi / 180.0) * dist
        z = (random.random() * 2 - 1) * (MAXHUBZ - scale * dist * dist)

        
        SRAN = random.randrange(0, 23)
        if SRAN == 0:
            scol = (255, 185, 201)
        elif SRAN == 1: 
            scol = (255, 204, 198)
        elif SRAN == 2:
            scol = (255, 204, 198)
        elif SRAN == 3:  
            scol = (255, 218, 198)
        elif SRAN == 4:
            scol = (255, 218, 198)
        elif SRAN == 5: 
            scol = (255, 219, 178)
        elif SRAN == 6: 
            scol = (255, 233, 178)
        elif SRAN == 7:
            scol = (255, 233, 178)
        elif SRAN == 8:
            scol = (255, 233, 178)
        elif SRAN == 9:
            scol = (255, 233, 178)
        elif SRAN == 10: 
            scol = (255, 246, 178)
        elif SRAN == 11: 
            scol = (255, 253, 178)
        elif SRAN == 12:
            scol = (255, 253, 178)
        elif SRAN == 13: 
            scol = (255, 254, 212)
        elif SRAN == 14:
            scol = (255, 254, 212)
        elif SRAN == 15: 
            scol = (254, 255, 248)
        elif SRAN == 16: 
            scol = (255, 255, 255)
        elif SRAN == 17:
            scol = (236, 255, 255)
        elif SRAN == 18:
            scol = (236, 255, 255)
        elif SRAN == 19:
            scol = (207, 251, 255)
        elif SRAN == 20:
            scol = (207, 251, 255)
        elif SRAN == 21:
            scol = (207, 251, 255)
        elif SRAN == 22:
            scol = (207, 238, 255)
        elif SRAN == 23:
            scol = (165, 196, 255)
        return scol


        # Add star to the stars array
        stars.append((x, y, z, scol))

        # Process next star
        i = i + 1
        sran = 0
        
    
    scale = CLUSRAD
    i = 0
    while i < NUMCLUS:
        
        # Choose a random distance from center
        dist = (random.random() * (HUBRAD + DISKRAD))

        # Any rotation (points are not on arms)
        theta = random.random() * 360

        # Convert to cartesian
        x = math.cos(theta * math.pi / 180.0) * dist
        y = math.sin(theta * math.pi / 180.0) * dist
        z = (random.random() * 2 - 1) * (CLUSRAD - scale * dist * dist)

        SRAN = random.randrange(0, 23)
        if SRAN == 0:
            scol = (255, 185, 201)
        elif SRAN == 1: 
            scol = (255, 204, 198)
        elif SRAN == 2:
            scol = (255, 204, 198)
        elif SRAN == 3:  
            scol = (255, 218, 198)
        elif SRAN == 4:
            scol = (255, 218, 198)
        elif SRAN == 5: 
            scol = (255, 219, 178)
        elif SRAN == 6: 
            scol = (255, 233, 178)
        elif SRAN == 7:
            scol = (255, 233, 178)
        elif SRAN == 8:
            scol = (255, 233, 178)
        elif SRAN == 9:
            scol = (255, 233, 178)
        elif SRAN == 10: 
            scol = (255, 246, 178)
        elif SRAN == 11: 
            scol = (255, 253, 178)
        elif SRAN == 12:
            scol = (255, 253, 178)
        elif SRAN == 13: 
            scol = (255, 254, 212)
        elif SRAN == 14:
            scol = (255, 254, 212)
        elif SRAN == 15: 
            scol = (254, 255, 248)
        elif SRAN == 16: 
            scol = (255, 255, 255)
        elif SRAN == 17:
            scol = (236, 255, 255)
        elif SRAN == 18:
            scol = (236, 255, 255)
        elif SRAN == 19:
            scol = (207, 251, 255)
        elif SRAN == 20:
            scol = (207, 251, 255)
        elif SRAN == 21:
            scol = (207, 251, 255)
        elif SRAN == 22:
            scol = (207, 238, 255)
        elif SRAN == 23:
            scol = (165, 196, 255)
        return scol

        # Add star to the stars array
        stars.append((x, y, z, scol))

        # Process next star
        i = i + 1
        sran = 0
    


def drawToPNG(filename):
    image = Image.new("RGB", (int(PNGSIZE), int(PNGSIZE)), PNGBGCOLOR)
    draw = ImageDraw.Draw(image)

    # Find maximal star distance
    max = 0
    for (x, y, z, scol) in stars:
        if abs(x) > max: max = x
        if abs(y) > max: max = y
        if abs(z) > max: max = z
        
    # Calculate zoom factor to fit the galaxy to the PNG size
    factor = float(PNGSIZE - PNGFRAME * 2) / (max * 2)
    for (x, y, z, scol) in stars:
        sx = factor * x + PNGSIZE / 2
        sy = factor * y + PNGSIZE / 2
        draw.point((sx, sy), fill=scol)

    # Save the PNG
    image.save(filename)
    print filename

# Generate the galaxy
generateStars()

# Save the galaxy as PNG to galaxy.png
drawToPNG("spiralgalaxy" + str(RAND) + "-" + str(NAME) + ".png")

# Create the galaxy's data galaxy.txt
with open("spiralgalaxy" + str(RAND) + "-" + str(NAME) + ".txt", "w") as text_file:
    text_file.write("Galaxy Number: {}".format(RAND))
    text_file.write("Galaxy Name: {}".format(NAME))
    text_file.write("Cluster Number: {}". format(NUMC))
    text_file.write("Hub Stars: {}".format(NUMHUB))
    text_file.write("Disk Stars: {}".format(NUMDISK))
    text_file.write("Stars Per Cluster: {}".format(NUMCLUS))
    text_file.write("Hub Radius: {}".format(HUBRAD))
    text_file.write("Disk Radius: {}".format(DISKRAD))
    text_file.write("Cluster Radius: {}".format(CLUSRAD))
    text_file.write("Arm Number: {}".format(NUMARMS))
    text_file.write("Arm Rotation: {}".format(ARMROTS))
    text_file.write("Arm Width: {}".format(ARMWIDTH))
    text_file.write("Hub Maximum Depth: {}".format(MAXHUBZ))
    text_file.write("Disk Maximum Depth: {}".format(MAXDISKZ))
    text_file.write("Maximum Outlier Distance: {}".format(FUZZ))
    text_file.write("Image Size: {}".format(PNGSIZE))
    text_file.write("Frame Size: {}".format(PNGFRAME))