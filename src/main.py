
"""
  __  __          _____  ______   ______     __  _____          _____  _  ________ ______   __
 |  \/  |   /\   |  __ \|  ____| |  _ \ \   / / |  __ \   /\   |  __ \| |/ /  ____/ __ \ \ / /
 | \  / |  /  \  | |  | | |__    | |_) \ \_/ /  | |  | | /  \  | |__) | ' /| |__ | |  | \ V / 
 | |\/| | / /\ \ | |  | |  __|   |  _ < \   /   | |  | |/ /\ \ |  _  /|  < |  __|| |  | |> <  
 | |  | |/ ____ \| |__| | |____  | |_) | | |    | |__| / ____ \| | \ \| . \| |   | |__| / . \ 
 |_|  |_/_/    \_\_____/|______| |____/  |_|    |_____/_/    \_\_|  \_\_|\_\_|    \____/_/ \_\

Date: 4/22/21
Copyright (C) <2021>  <Zachery Uporsky>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.                                                                                                                                                                               
"""

from __future__ import print_function
import calibrate 
import cv2 as cv 
import argparse



max_value = 255
max_type = 4
max_binary_value = 255
trackbar_type = 'Type: \n 0: Binary \n 1: Binary Inverted \n 2: Truncate \n 3: To Zero \n 4: To Zero Inverted'
trackbar_value = 'Value'
window_name = 'Threshold Demo'



## [Threshold_Demo]
def Threshold_Demo(val):
    #0: Binary
    #1: Binary Inverted
    #2: Threshold Truncated
    #3: Threshold to Zero
    #4: Threshold to Zero Inverted
    threshold_type = cv.getTrackbarPos(trackbar_type, window_name)
    threshold_value = cv.getTrackbarPos(trackbar_value, window_name)
    _, dst = cv.threshold(src_gray, threshold_value, max_binary_value, threshold_type )
    cv.imshow(window_name, dst)
## [Threshold_Demo]

parser = argparse.ArgumentParser(description='Code for Basic Thresholding Operations tutorial.')
parser.add_argument('--input', help='Path to input image.', default='stuff.jpg')
args = parser.parse_args()

## [load]
# Load an image
src = cv.imread(cv.samples.findFile(args.input))
if src is None:
    print('Could not open or find the image: ', args.input)
    exit(0)
# Convert the image to Gray
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
## [load]

## [window]
# Create a window to display results
cv.namedWindow(window_name)
## [window]

## [trackbar]
# Create Trackbar to choose type of Threshold
cv.createTrackbar(trackbar_type, window_name , 3, max_type, Threshold_Demo)
# Create Trackbar to choose Threshold value
cv.createTrackbar(trackbar_value, window_name , 0, max_value, Threshold_Demo)
## [trackbar]

# Call the function to initialize
Threshold_Demo(0)
# Wait until user finishes program
cv.waitKey()