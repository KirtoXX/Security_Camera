from __future__ import print_function
from Camera2 import Camera
from Sent import Connect
import time

def main():
    camera = Camera()
    conn = Connect()
    while True:
        #-------do cut and sent iamge----------
        path = camera.cut_image()
        conn.sent(path)
        time.sleep(0.1)





if __name__ == '__main__':
    main()