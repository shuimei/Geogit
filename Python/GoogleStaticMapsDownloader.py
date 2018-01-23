from Google import GoogleStaticImage
import geopandas as gpd
import os
import time

def mainFunc(shp):
    try:
        fishnet = gpd.read_file(shp)
        x, y = fishnet.shape
        for i in range(63000, 70000):
            outputPath = r"G:\Chenzuoqi\FunnyJob\DengShunqiang\GOOGLEimages-shanghai\{0}.png".format(i + 1)
            if os.path.exists(outputPath):
                continue
            p = fishnet.iloc[i, :].values
            # print(p)

            params = {
                'center': "{0},{1}".format(p[1], p[0]),
                'zoom': '16',
                'size': "250x300",
                'scale': "2",
                'maptype': "satellite",
                'format': "png32",
                'key': "AIzaSyBqQyY3xOOopxX3gRJw-OfkgbfmuIBw76c",
            }
            gsi = GoogleStaticImage("https://maps.googleapis.com/maps/api/staticmap",
                                    params)
            if i % 20 == 0:
                print(i)
            gsi.store(outputPath)
    except:
        print("Wrong!")
        time.sleep(5)
        mainFunc(shp)

if __name__ == "__main__":
    shp = "../shanghai_lights_viirs_fishnet_label_value.shp"
    mainFunc(shp)