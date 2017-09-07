from flask import json
import os
import re

persion_dir = "Persion_image/"

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

def make_json(time):
    all_image_path = get_list(time)
    m = len(all_image_path)

    # ------define json_file------------
    all_info = {}
    all_info['nb_image'] = m

    if m == 0:
        result = json.dumps(all_info)
    if m != 0:
        for i in range(len(all_image_path)):
            path = persion_dir + all_image_path[i]
            f = open(path, 'rb')
            all_info[str(i)] = f
            f.close()
        #result = json.dumps(all_info)
    print(all_info)
    result = json.jsonify(all_info)
    return result


def main():
    t = get_list('2017-09-07-1644')
    make_json('2017-09-07-1644')
    print(t)

if __name__ == '__main__':
    main()

