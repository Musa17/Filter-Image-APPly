import numpy
from PIL import Image
import cv2

def median_filter(data, filter_size):
    temp = []
    indexer = filter_size // 2
    data_final = []
    data_final = numpy.zeros((len(data),len(data[0])))

    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(filter_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(filter_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(filter_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final


def main():

    print ("Please wait a little bit ...")
    img = cv2.imread('Pikachu.jpg')

    b, g, r = cv2.split(img)
    arr = numpy.array(b)/255
    Blue = median_filter(arr, 3) 

    arr = numpy.array(g)/255
    Green = median_filter(arr, 3)

    arr = numpy.array(r)/255
    Red = median_filter(arr, 3)	

    filteredImage = cv2.merge((Blue, Green, Red))

    cv2.namedWindow('Filtered Image')
    cv2.imshow('Filtered Image', filteredImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()
