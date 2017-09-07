import os

class Camera:
    def __init__(self):
        None

    def cut_image(self):
        os.system('raspistill -t 100 -n -o temp/temp_image.jpg')
        return 'temp/temp_image.jpg'