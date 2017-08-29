from flask import Flask,request
from svm_model import Detection_api
import warnings
import time
import shutil

#-------init flask_serving--------
app = Flask(__name__)
temp_path = "temp/temp.jpg"
persion_dir = "Persion_image/"
global model
model = Detection_api()

#--------func deftion------------

@app.route('/file', methods=['POST','GET'])
def process_func():
    if request.method == 'POST':
        model1 = model
        #save file
        f = request.files['userfile']
        f.save(temp_path)
        #detection face
        nb = model1.detectFaces(temp_path)
        print(nb)
        #copy image to our dir
        if nb!=0:
            name = time.strftime('%Y-%m-%d-%H%M%S',time.localtime(time.time()))
            image_path = persion_dir+name+'.jpg'
            shutil.copy(temp_path,image_path)


#--------main--------------
def main():
    host = "192.168.123.64"
    port = 6666
    app.run(host=host,port=port)

if __name__ == '__main__':
    main()

