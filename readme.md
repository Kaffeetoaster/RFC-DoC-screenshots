# Screenshot utility to create full map images of civ4 maps
This utility consists of two scripts to take and then stitch together screenshots from a civ4 game. (Although this should be usable for every game, that allows moving around with the arrow keys.)

### Preparations in game

1. CTRL+Z to reveal the map (i think you first need to set _CheatCode = chipotle_ in the CivilizationIV.ini)
2. CTRL+B to hide units
3. ALT+F to center the camera perpendicular to the ground. This prevents map warping.
4. ALT+I to hide the interface
5. Place a Satellite unit on your starting square.
6. scroll to the Zoomlevel you want to take pictures from.

### Taking screenshots:

In _config.py_ you can configure the process, by setting the number of screenshots you want to take, expected overlap and time to move up and right between the screenshots.

_Note: the screenshots move top and right_

The time to move depends on the overlap. So less expected overlap means the camera needs to move more for the next screenshot. I advise to first take only 2x2 screenshots to configure the values. Just open the 4 imgs in gimp or sth and give a guess for the vertical and horizontal overlap.

_execute take_screenshots.py_

After starting this script you have like 15 seconds to ALT + TAB back to civ4, and move to your starting point. The script will then take screenshots in the manner specified in _config.py_.
This will take some time, depending on the number of total screeshots. Taking 120 screenshots takes around 10 min for example. After thi is finished you can

### Stitching the results:
_execute stitch_images.py_

This script will stitch together all the screenshots taken. First columnwise, and then the columns together. For the 120 screenshots from above this took around 1 minute.

    Be careful! 
    Taking screenshots and stitching the images will overwrite older screenshots and stitching results! So move your result to a different fodler or rename it, if you want to keep it.

