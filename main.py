import math
import cmath
import numpy as np
import numpy.linalg as la
from geneticalgorithm import geneticalgorithm as ga
import cv2

sign_radius = 40
rescue_zone = 200 
yellow = (0,255,255)
s_blue = (255,255,0)
red = (0,0,255)

   
# function to display the coordinates of
# of the points clicked on the image 
def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print('Base coodinates:')
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'BASE', (x,y - sign_radius ), font,
                    .6, yellow, 1)
        cv2.circle(img, (x,y), sign_radius, s_blue, 1)
        cv2.circle(img, (x,y), 7, yellow, -1)
        cv2.imshow('image', img)
        
    if event == cv2.EVENT_RBUTTONDOWN:
      
        # displaying the coordinates
        # on the Shell
        print('Rescue zone coodinates:')
        print(x, ' ', y)
  
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'RESCUE ZONE', (x,y - rescue_zone - 3 ), font,
                    .6, red, 2)
        cv2.circle(img, (x,y), rescue_zone, red, 3)

        cv2.imshow('image', img)
  

    
def verySmartAI():
    print('shit im alive')





# driver function
if __name__=="__main__":
  
    # reading the image
    img = cv2.imread('satelite.png', 1)
  
    # displaying the image
    cv2.imshow('image', img)
  
    # setting mouse hadler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
  
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
  
    # close the window
    cv2.destroyAllWindows()