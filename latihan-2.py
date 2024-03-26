import cv2 as cv

def konvertMeganta(img_path):
    img = cv.imread(img_path)

    for i in range(0, 384):     # ukuran tinggi gambar
        for j in range(0, 512):     # ukuran lebar gambar
            # mengambil data piksel gambar
            img[i][j] = [255, 0, 255]

    cv.imshow("koversi gambar jadi full meganta", img)
    cv.waitKey(0)

# img = "./kucing-bg-hijau.jpg"
img = "./img_crop_1_1.png"
konvertMeganta(img)