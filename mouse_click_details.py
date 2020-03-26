# displays the BGR, HSV values of clicked point

import cv2
import numpy as np

def onMouse(action, x, y, flags, userdata):
    image = userdata[0];            bgr = ['B','G', 'R']
    hsv_image = userdata[1];        hsv = ['H','S', 'V']

    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        print('x coordinate is {}'.format(x))
        print('y coordinate is {}\n'.format(y))

        for i in range(3):
            print('{} coordinate is {}'.format(bgr[i], image[y,x,i]))

        print('\n')

        color_sample = np.zeros((255,255,3), dtype = np.uint8)

        for i in range(3):
            print('{} coordinate is {}'.format(hsv[i], hsv_image[y,x,i]))
            color_sample[:,:,i] = image[y,x,i]

        print('\n')
        cv2.namedWindow('bgr_color', cv2.WINDOW_NORMAL)
        cv2.imshow('bgr_color', color_sample)

    # Action to be taken when left mouse button is released
    elif action == cv2.EVENT_LBUTTONUP:
        pass


def main():
    img = cv2.imread('image.jpg')
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('img', onMouse, param=[img,hsv_image])
    cv2.imshow('img',img)


    k = cv2.waitKey(0) & 0xFF
    if k == ord('q'):
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()


