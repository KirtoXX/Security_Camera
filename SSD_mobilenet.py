import tensorflow as tf
from ssd_mobilenet.object_detection.utils import visualization_utils as vis_util
import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy import misc


class Detection_api:

    def __init__(self):
        MODEL_NAME = 'ssd_mobilenet/ssd_mobilenet'
        self.PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
        self.NUM_CLASSES = 90
        self.detection_graph = tf.Graph()

    def buid_ssdmobilenet(self):
        #----------build graph------------
        with self.detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        self.sess = tf.Session(graph=self.detection_graph)

        self.image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
        # Each box represents a part of the image where a particular object was detected.
        self.detection_boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
        # Each score represent how level of confidence for each of the objects.
        # Score is shown on the result image, together with the class label.
        self.detection_scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
        self.detection_classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
        self.num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
        #---------init_sess----------------

        print('ssd_mobilenet load finish!')

    def load_image_into_numpy_array(self,image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

    def inference(self,image_np_expanded):
        (boxes, scores, classes, num) = self.sess.run(
            [self.detection_boxes, self.detection_scores, self.detection_classes, self.num_detections],
            feed_dict={self.image_tensor: image_np_expanded})
        return boxes,scores,classes

    def decode_inference(self,boxes,scores,classes):
        classes_np = np.squeeze(classes).astype(np.int32)
        boxes_np = np.squeeze(boxes)
        scores_np = np.squeeze(scores)
        persion_id = []
        for i in range(len(classes_np)):
            if classes_np[i] == 1:
                persion_id.append(i)
        persion_boxs = boxes_np[persion_id, :]
        persion_score = scores_np[persion_id]
        persion_class = np.squeeze(persion_id)
        return persion_boxs,persion_score,persion_class

    def detectFaces(self, image_path):
        #-------read_image--------
        image = Image.open(image_path)
        image_np = self.load_image_into_numpy_array(image)
        image_np_expanded = np.expand_dims(image_np, axis=0)

        #------do inference--------
        boxes, scores, classes = self.inference(image_np_expanded)
        boxes, scores, classes = self.decode_inference(boxes, scores, classes)

        #------viual---------------
        nb_persion = vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          boxes,
          classes,
          scores,
          #category_index,
          use_normalized_coordinates=True,
          line_thickness=8)

        return nb_persion,image_np

def main():
    model = Detection_api()
    model.buid_ssdmobilenet()
    nb,image_np = model.detectFaces('test_image/001.jpg')
    misc.imsave('temp/temp.jpg',image_np)
    print(nb)

if __name__ == '__main__':
    main()

