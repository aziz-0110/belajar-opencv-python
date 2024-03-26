import cv2

def canny(imgPath):
    img = cv2.imread(imgPath)

    # kalibrasi canny untuk histologi
    edges = cv2.Canny(img, 280, 300)

    cv2.imshow("Canny", edges)

    # waitKey berdasarkan waktu
    # cv2.waitKey(5000)
    # waitKey berdasarkan tombol
    cv2.waitKey(0)


pth =  "./img_crop_1_1.png"
canny(pth)