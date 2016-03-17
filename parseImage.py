import cv2
import numpy as np
import matplotlib.pyplot as plt


def parse(filename):
    im_gray = cv2.imread(filename, 0)
    #im_gray = cv2.GaussianBlur(im_gray, (5,5), 0)
    img = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 2)
    signal_arr = np.sum(img, 0)

    cv2.imshow('orig', img)
    THRESHOLD = np.median(signal_arr)
    signal_arr_channel = signal_arr
    low_values_indices = signal_arr_channel < THRESHOLD 
    high_values_indices = signal_arr_channel >= THRESHOLD

    signal_arr_channel[low_values_indices] = 0
    signal_arr_channel[high_values_indices] = 1

    plt.plot(signal_arr)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return signal_arr_channel

if __name__ == "__main__":
    parse("test.jpg")

