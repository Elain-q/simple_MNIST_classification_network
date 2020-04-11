# simple_MNIST_classification_network
The first and simplist network for MNIST classification by Keras(Tensorflow)

This is my first project for machine learning in keras,so it's really simple for most people,if you are skilled,just skip this project.If you just would like to run the program,you just need to put this line of command in your terminal

```
python3 simplist_MNIST_classification.py
```

Before you run the program,you also need to provide such a environment for it.

1.python3

2.keras

3.tensorflow

4.numpy

And finally,after we run the whole program,we can get the result below.

```
60000 TRAIN samples
10000 TEST samples
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 10)                7850      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 7,850
Trainable params: 7,850
Non-trainable params: 0
_________________________________________________________________
Train on 48000 samples, validate on 12000 samples
……
Test score: 0.2773810029923916
Test accuracy 0.9225000143051147
```