from __future__ import print_function
from linux_program.Camera import Camera
from linux_program.Sent import Connect
import time

def main():
    camera = Camera()
    conn = Connect()
    while True:
        #-------do cut and sent iamge----------
        #path = cut.cut_image()
        path = camera.cut_image()
        conn.sent(path)
        time.sleep(0.5)




if __name__ == '__main__':
    main()