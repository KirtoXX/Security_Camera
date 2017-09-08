import tensorflow as tf
#from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import os
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy import misc

MODEL_NAME = 'ssd_mobilenet'

PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
print(PATH_TO_CKPT)

PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

detection_graph = tf.Graph()

with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

print('ssd_mobilenet load finish!')

#label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
#categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
#category_index = label_map_util.create_category_index(categories)

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


PATH_TO_TEST_IMAGES_DIR = 'test_images'
TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3) ]

# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)


with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    # Definite input and output Tensors for detection_graph
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    # Each box represents a part of the image where a particular object was detected.
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    # Each score represent how level of confidence for each of the objects.
    # Score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    image_path = 'test_images/image2.jpg'
    print(image_path)

    image = Image.open(image_path)
      # the array based representation of the image will be used later in order to prepare the
      # result image with boxes and labels on it.
    image_np = load_image_into_numpy_array(image)
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
      # Actual detection.

    (boxes, scores, classes, num) = sess.run(
          [detection_boxes, detection_scores, detection_classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})



    classes_np = np.squeeze(classes).astype(np.int32)
    boxes_np = np.squeeze(boxes)
    scores_np = np.squeeze(scores)

    persion_id = []
    for i in range(len(classes_np)):
        if classes_np[i]==1:
            persion_id.append(i)



    persion_boxs = boxes_np[persion_id,:]
    persion_score = scores_np[persion_id]
    persion_class = np.squeeze(persion_id)

    m = vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          persion_boxs,
          persion_id,
          persion_score,
          #category_index,
          use_normalized_coordinates=True,
          line_thickness=8)

    print(m)
    misc.imsave('temp/temp.jpg',image_np)








