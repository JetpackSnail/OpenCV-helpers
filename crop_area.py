# crops an area, shows average color and histogram
import cv2
import numpy as np

points = [0,0]
crop = False

def onMouse(action, x, y, flags, userdata):
    global points
    global crop

    image = userdata
    imagecpy = image.copy()

    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        points[0] = (x,y)
        crop = True

    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_MOUSEMOVE:
        if crop == True:
            points[1] = (x,y)

            cv2.rectangle(imagecpy, points[0], points[1], (0,255,0), 2)
            cv2.imshow('img',imagecpy)


    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_LBUTTONUP:
        crop = False
        points.sort()

        # do a crop
        cropped = image[points[0][1]:points[1][1], points[0][0]:points[1][0]]
        cv2.namedWindow('cropped', cv2.WINDOW_NORMAL)
        cv2.imshow('cropped', cropped)

        print('The corner coordinates are {} and {}'.format(points[0], points[1]))

def main():
    img = cv2.imread('image.jpg')

    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('img', onMouse, param=img)
    cv2.imshow('img',img)

    k = cv2.waitKey(0) & 0xFF
    if k == ord('q'):
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


