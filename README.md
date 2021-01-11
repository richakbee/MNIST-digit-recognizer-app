# MNIST-digit-recognizer-app
This is a deep learning demo app in Flutter .


# Image Page

<img src="https://github.com/richakbee/MNIST-digit-recognizer-app/blob/master/screenshotImagePage2.png" width="200" height="400" />

# Draw Page

<img src="https://github.com/richakbee/MNIST-digit-recognizer-app/blob/master/screenshotsImagePage.png" width="200" height="400" />   <img src="https://github.com/richakbee/MNIST-digit-recognizer-app/blob/master/screenshotDrawPage.png" width="200" height="400" />     <img src="https://github.com/richakbee/MNIST-digit-recognizer-app/blob/master/screenshotsImagePage2.png" width="200" height="400" />


- <b>Data set </b>:http://yann.lecun.com/exdb/mnist/

- <b>Model Accuracy </b> 99.8%  on Training & 99.1% on Validation 


- <b>Model Summary </b>
Model: "sequential"
<p>
_________________________________________________________________<br>
Layer (type)                 Output Shape              Param #   <br>
=================================================================<br>
conv2d (Conv2D)              (None, 26, 26, 32)        320       <br>
_________________________________________________________________<br>
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         <br>
_________________________________________________________________<br>
conv2d_1 (Conv2D)            (None, 11, 11, 32)        9248      <br>
_________________________________________________________________<br>
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 32)          0         <br>
_________________________________________________________________<br>
flatten (Flatten)            (None, 800)               0         <br>
_________________________________________________________________<br>
dense (Dense)                (None, 512)               410112    <br>
_________________________________________________________________<br>
dense_1 (Dense)              (None, 10)                5130      <br>
=================================================================<br>
Total params: 424,810<br>
Trainable params: 424,810<br>
Non-trainable params: 0<br>
_________________________________________________________________
</p>

- <b>Tool & Technologies </b>: Tensorflow , Tflite , Flutter ,Dart , Emulator 

- <b>#shout out to </b> https://github.com/am15h/tflite_flutter_plugin for tflite_flutter plugin
- <b> UI inspiration & credits </b> https://github.com/PuzzleLeaf 

