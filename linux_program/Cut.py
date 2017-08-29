import cv2

class Camera:
    def __init__(self,camera_id=0):
        self.cap = cv2.VideoCapture(camera_id)
        self.save_path = 'temp/temp_iamge.jpg'

    def cut_image(self):
        _,frame = self.cap.read()
        cv2.imwrite(self.save_path,frame)
        return self.save_path

# def main():
#     cut = Cut_iamge()
#     cut.cut_image()
#
#
# if __name__ == '__main__':
#     main()