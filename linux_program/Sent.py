import requests

class Connect:
    def __init__(self):
        self.url = 'http://192.168.123.64:6666/file'

    def sent(self,image_path):
        f = open(image_path,"rb")
        files = {
            'userfile':('temp.jpg',f)
        }
        data = {
            'device':'0'
        }
        try:
            requests.post(self.url,files=files,data=data)
            print('sent finish')
        except:
            print('sent failed')


