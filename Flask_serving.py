from flask import Flask,request,json
from flask import send_file,send_from_directory
from SVM_model import Detection_api
import warnings
import time
import shutil
import os
import re

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

def get_list(time):
    all_image_list = os.listdir('Persion_image')
    result = []
    for path in all_image_list:
        try:
            _,n = re.search(time,path).span()
            if n == 15:
                result.append(path)
        except:
            None
    return result

@app.route('/download/<time>', methods=['POST', 'GET'])
def sent_image(time):
    if request.method == 'POST':
        all_image_path = get_list(time)
        m = len(all_image_path)

        #------define json_file------------
        all_info = {}
        all_info['nb_image'] = m

        if m == 0:
            result = json.dumps(all_info)
        if m!=0:
            for i in range(len(all_image_path)):
                path = persion_dir+all_image_path[i]
                f = open(path,'rb')
                all_info[str(i)] = f
            result = json.dumps(all_info)

        return result

#--------main--------------
def main():
    host = "192.168.123.64"
    port = 6666
    app.run(host=host,port=port)

if __name__ == '__main__':
    main()

