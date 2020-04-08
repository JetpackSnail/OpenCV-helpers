# displays the BGR, HSV values of clicked point
# H: 0-179 - colour information
# S: 0-255 - grayness value
# V: 0-255 - brightness

import cv2
import numpy as np
from matplotlib import pyplot as plt


def onMouse(action, x, y, flags, userdata):
    image = userdata[0]
    hsv_image = userdata[1]

    # Action to be taken when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        color_bgr = image[y,x,:]
        color_hsv = hsv_image[y,x,:]
        print('XY coordinates are ({},{})'.format(x,y))
        print('BGR color is {}'.format(color_bgr))
        print('HSV color is {}'.format(color_hsv))

        color_sample = np.zeros((255,255,3), dtype = np.uint8)
        for i in range(3):
            color_sample[:,:,i] = image[y,x,i]

        cv2.namedWindow('bgr_color', cv2.WINDOW_NORMAL)
        cv2.imshow('bgr_color', color_sample)


        toprange = np.clip(color_hsv + [70, 50, 75], 0, 255)    # edit this
        btmrange = np.clip(color_hsv - [50, 35, 145], 0, 255)    # edit this

        print('\nTop range is {}'.format(toprange))
        print('Btm range is {}'.format(btmrange))

        # mask of the selected color and get inverse mask
        mask = cv2.inRange(hsv_image, btmrange, toprange)
        mask_inv = cv2.bitwise_not(mask)

        # original image - mask
        img1 = cv2.bitwise_and(hsv_image, hsv_image, mask = mask_inv)
        img1 = cv2.cvtColor(img1, cv2.COLOR_HSV2BGR)

        # mask in original colours
        img2 = cv2.bitwise_and(hsv_image, hsv_image, mask = mask)
        img2 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)



        hh,ss,vv = cv2.split(hsv_image)
        hh[hh!=0] += 50

        restored_image = cv2.merge([hh,ss,vv])
        #h[mask] = h[mask] + 50
        #res = cv2.merge([h,s,v])
        #res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)



        # manipulation of mask in original colours
        # mask_h, mask_s, mask_v = cv2.split(img2)

       # restored_image = cv2.add(img1, img2)
       # restored_image = cv2.cvtColor(restored_image, cv2.COLOR_HSV2BGR)



        # hsv image of selected colour for manipulation
        #image_after_mask = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)

        # manipulation
        #image_after_mask = np.clip(image_after_mask - np.array([0,0,200]), 0, 255)

        # add back to original image
        #img1_bg = cv2.bitwise_and(image, image, mask = mask_inv)
       # new_image = cv2.add(img1_bg, new_mask)
        #new_image = cv2.cvtColor(new_image, cv2.COLOR_HSV2BGR)

        cv2.imshow('x',restored_image)

        print('\n')

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