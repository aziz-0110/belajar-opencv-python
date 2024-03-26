import cv2 as cv


imgPath = "./img_crop_1_1.png"
img = cv.imread(imgPath)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(0, 384):
    for j in range(0, 512):
        px = 255 if img[i][j] > 150 else 0      # operator ternary
        img[i][j] = px

kucing = cv.imread("./kucing-bg-hijau.jpg")
print(kucing.shape)     # untuk mengambil data baris, colom dan jumlah kenal(R, G, B)
print(img.shape)        # jika gambar abu"" tidak akan membawa nilai kernal
cv.imshow("bray", img)
cv.waitKey(0)