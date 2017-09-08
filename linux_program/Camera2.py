import os

class Camera:
    def __init__(self):
        None

    def cut_image(self):
        os.system('raspistill -t 500 -w 640 -h 480 -n -o temp/temp_image.jpg')
        print('cut finish')
        return 'temp/temp_image.jpg'