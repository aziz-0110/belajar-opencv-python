import cv2

def showImg(imgPath):
    # cv2.IMREAD_COLOR == 1 => tidak membawa informasi apapun
    # img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    # img = cv2.imread(imgPath, 1)

    # cv2.IMREAD_GRAYSCALE == 0 => gambar di konvert ke skala abu""
    img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread(imgPath, 0)

    # cv2.IMREAD_UNCHANGED == -1 => gambar di muat dengan skala apa adanya
    # img = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED)
    # img = cv2.imread(imgPath, -1)

    if not img is None:
        cv2.imshow("pertemuan 1", img)
        cv2.waitKey(0)
    else:
        print("path gambar salah")

showImg("./img_crop_1_1.png")