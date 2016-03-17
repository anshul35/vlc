import cv2
import numpy as np
import matplotlib.pyplot as plt

THRESHOLD = 150
def parse(filename):
    im_gray = cv2.imread(filename)
    im_gray = cv2.cvtColor(im_gray, cv2.COLOR_BGR2GRAY)
    signal_arr = np.sum(im_gray, 0)
    cv2.imshow('orig', im_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    signal_arr_channel = signal_arr
    low_values_indices = signal_arr_channel < THRESHOLD 
    high_values_indices = signal_arr_channel >= THRESHOLD

    signal_arr_channel[low_values_indices] = 0
    signal_arr_channel[high_values_indices] = 1

    plt.plot(signal_arr)
    plt.show()
    return signal_arr_channel

if __name__ == "__main__":
    parse("test.jpg")
    
