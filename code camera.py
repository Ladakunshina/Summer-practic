# Import OpenCV module 
from pickletools import uint8
#from turtle import left
import cv2 
import numpy as np

class array_col:
    pass

def Coord_file(cent):    
    #file = open("/home/lada/Рабочий стол/coordinates/coordinates.txt", "w")
    file.write(str(cent) + '\n')
    #file.close()

#file_count = 0

#def mask(lower,upper):
 #   video = cv2.VideoCapture(0)
 #   flag, img = video.read() 

  #  image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   # mask = cv2.inRange(image, lower, upper)
   # cv2.imshow('camera', img)

def cont(lower, upper):
    hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV )
    thresh = cv2.inRange(hsv, lower, upper)      #contoures
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(mask, contours, -1, (255,0,0), 3, cv2.LINE_AA, hierarchy, 1 )
    #cv2.imshow('contours', mask) 
    return contours

def center(cnt):
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    center = (int(rect[0][0]),int(rect[0][1]))
    area = int(rect[1][0]*rect[1][1])
    Coord_file(center)
    #print(center)
    return center, area, box

def coords():
    #cv2.drawContours(mask,[box],0,(0, 255, 0),2)
    cv2.circle(mask, cent, 2, (0, 255, 255), 2)
    text = "(" + str(cent[0]) + ", " + str(cent[1]) + ")"
    cv2.putText(mask, text, (cent[0] + 10, cent[1] + 10), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 220, 225), 1, 1, 0)

if __name__ == '__main__':

    file = open("/home/lada/Рабочий стол/coordinates/coordinates.txt", "a")
    #cv2.namedWindow( "camera" ) #create window
    cap = cv2.VideoCapture(0)

    lower_blue = np.array((80, 50, 150), np.uint8)
    upper_blue = np.array((120, 255, 255), np.uint8)

    lower_yellow = np.array((15, 100, 150), np.uint8)
    upper_yellow = np.array((30, 255, 255), np.uint8)

    lower_green= np.array([30, 52, 150], np.uint8)
    upper_green = np.array([75, 255, 255], np.uint8)

    lower_red = np.array((130, 50, 150), np.uint8)
    upper_red = np.array((180, 255, 255), np.uint8)

    while True:
        flag, mask = cap.read()
        mask = cv2.flip(mask,1)
        try:
            
            any_yellow = cont(lower_yellow, upper_yellow)
            any_blue = cont(lower_blue, upper_blue)
            any_red = cont(lower_red, upper_red)
            any_green = cont(lower_green, upper_green)

            for cnt_y in any_yellow:

                cent, ar, box = center(cnt_y)
                if ar > 1000: #coordinates
                    coords()

            for cnt_b in any_blue:

                cent, ar, box = center(cnt_b)
                if ar > 1000: 
                    coords() 

            for cnt_r in any_red:

                cent, ar, box = center(cnt_r)
                if ar > 1000: 
                    coords() 

            for cnt_g in any_green:

                cent, ar, box = center(cnt_g)
                if ar > 1000: 
                    coords() 


            cv2.imshow('camera', mask)
             

        except:
            cap.release()
            raise
        butt = cv2.waitKey(5)
        if butt == 27:          #ECS 
            break

    cap.release()
    cv2.destroyAllWindows()
    file.close()

lower = np.array([225, 250, 250]) # set colour
upper = np.array([230, 255, 255])
