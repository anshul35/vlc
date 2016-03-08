import cv2
import numpy as np
import matplotlib.pyplot as plt

def parse(filename):
    im_gray = cv2.imread(filename)
    signal_arr = np.sum(im_gray, 0)
    signal_arr_channel = signal_arr[:,1]
    low_values_indices = signal_arr_channel < 100
    high_values_indices = signal_arr_channel >= 100

    signal_arr_channel[low_values_indices] = 0
    signal_arr_channel[high_values_indices] = 1
#    import pdb; pdb.set_trace()

    plt.plot(signal_arr_channel)
#    plt.show()
    return signal_arr_channel

if __name__ == "__main__":
    parse("test.jpg")
    
