import cv2

def parse(filename):
    im_gray = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    im_gray = cv2.resize(im_gray, 0.25)
    cv2.imshow('orig', im_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #(thresh, im_bw) = cv2.threshold(im_gray, 20, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, im_bw) = cv2.threshold(im_gray, 20, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(filename+"_converted.jpg", im_bw)
    return

if __name__ == "__main__":
    parse("test.jpg")
    
