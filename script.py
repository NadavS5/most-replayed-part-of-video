import matplotlib.pyplot as plt
import sys

videoLength = int(sys.argv[1:][0])


def getDataFromFile(name):
    with open(name, "r") as file:
        for line in file:
            return line


def preProcessData(data):

    tripletsArray = data.split("C ")

    dataPointsArray = []

    for triplets in tripletsArray:
        if triplets != "":

            pointsArray = triplets.split(" ")[:3]

            for points in pointsArray:
                p = points.split(",")

                # print(p)
                dataPointsArray.append([float(p[0]), float(p[1])])

    return dataPointsArray


def plotCurve(points, videoLength):
    x = [((p[0] - 1) * (videoLength) / (1000 - 1)) for p in points]
    y = [-p[1] for p in points]

    
    max_y = max(y)
    highest_peak_x = x[y.index(max_y)]
    # print(max_y)

    # print(f"y len = {len(y)} x len {len(x)}")

    # highest_peak_x = points.index(max_y)


    plt.scatter([highest_peak_x], [max_y], color='red', label=f'Highest Point ({highest_peak_x}, {max_y})')

    # Annotate the highest point
    plt.text(highest_peak_x, max_y, f'({highest_peak_x}, {max_y})', fontsize=12, verticalalignment='bottom')


    plt.plot(x, y)
    plt.show()

data = getDataFromFile("test.txt")

dataPointsArray = preProcessData(data)

plotCurve(dataPointsArray, videoLength)
