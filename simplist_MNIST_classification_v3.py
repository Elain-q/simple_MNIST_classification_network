import numpy as np
from keras.layers.core import Dense,Activation,Dropout
from keras.models import Sequential
from keras.datasets import mnist
from keras.optimizers import SGD
from keras.utils import np_utils

np.random.seed(1671)
NB_EPOCH = 250
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10
OPTIMIZER = SGD()
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2
DROPOUT = 0.3
(X_TRAIN,Y_TRAIN),(X_TEST,Y_TEST) = mnist.load_data()
RESHAPED = 784
X_TRAIN = X_TRAIN.reshape(60000,RESHAPED)
X_TEST = X_TEST.reshape(10000,RESHAPED)
X_TRAIN = X_TRAIN.astype('float32')
X_TEST = X_TEST.astype('float32')
X_TRAIN /= 255
X_TEST /= 255
print(X_TRAIN.shape[0],'TRAIN samples')
print(X_TEST.shape[0],'TEST samples')
Y_TRAIN = np_utils.to_categorical(Y_TRAIN,NB_CLASSES)
Y_TEST = np_utils.to_categorical(Y_TEST,NB_CLASSES)

model = Sequential()
model.add(Dense(N_HIDDEN,input_shape = (RESHAPED,)))
model.add(Activation('relu'))
model.add(Dropout(DROPOUT))
model.add(Dense(N_HIDDEN))
model.add(Activation('relu'))
model.add(Dropout(DROPOUT))
model.add(Dense(NB_CLASSES))
model.add(Activation('softmax'))
model.summary()

model.compile(loss = 'categorical_crossentropy',optimizer = OPTIMIZER,metrics = ['accuracy'])
history = model.fit(X_TRAIN,Y_TRAIN,batch_size = BATCH_SIZE,epochs = NB_EPOCH,verbose = VERBOSE,validation_split = VALIDATION_SPLIT)
score = model.evaluate(X_TEST,Y_TEST,verbose = VERBOSE)
print('Test score:',score[0])
print('Test accuracy',score[1])

