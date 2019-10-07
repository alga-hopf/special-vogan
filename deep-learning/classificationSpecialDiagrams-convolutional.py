'''
   Train a convolutional neural network to predict special Vogan diagrams.

   Copyright (C) 2019  Alice Gatti

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import tensorflow as tf
import numpy as np
import time, os

# Train data and test data produced with the code prepareData.sage
# 0 = special, 1 = non-special
train_orbits=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/trainOrbits.npy'))
train_labels=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/trainLabels.npy'))
test_orbits=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/testOrbits.npy'))
test_labels=np.load(os.path.expanduser('~/special-vogan/deep-learning/data/dataProportion/testLabels.npy'))

# Shapes of the data
print("Shapes of training data:",train_orbits.shape)
print("Shapes of training labels:",len(train_labels))
print("Shapes of test data:",test_orbits.shape)
print("Shapes of test labels:",len(test_labels))

# Number of special diagrams
totalZeros=0
totalOnes=0
specialTrain=0
specialTest=0
nonSpecialTrain=0
nonSpecialTest=0
for i in range(len(train_labels)):
    if train_labels[i]==0:
        totalZeros=totalZeros+1
        specialTrain=specialTrain+1
    else:
        totalOnes=totalOnes+1
        nonSpecialTrain=nonSpecialTrain+1
for i in range(len(test_labels)):
    if test_labels[i]==0:
        totalZeros=totalZeros+1
        specialTest=specialTest+1
    else:
        totalOnes=totalOnes+1
        nonSpecialTest=nonSpecialTest+1
print("Total 0's:",totalZeros,"   Total 1's:",totalOnes)
print("Train 0's:",specialTrain,"   Train 1's:",nonSpecialTrain)
print("Test 0's:",specialTest,"   Test 1's:",nonSpecialTest)

# Model 

model=tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(20, 4, strides=1, activation='relu',input_shape=(train_orbits.shape[1],train_orbits.shape[2])),
    tf.keras.layers.MaxPooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last'),
    tf.keras.layers.Conv1D(40, 4, strides=1, activation='relu'),
    tf.keras.layers.MaxPooling1D(pool_size=2, strides=None, padding='valid', data_format='channels_last'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(1000, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(2,activation=tf.nn.softmax)
])
model.summary()
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Training the model
timestart=time.time()
model.fit(train_orbits, train_labels, batch_size=100,epochs=30,steps_per_epoch=30)
timeend=time.time()
print('Time:',timeend-timestart)

# Accuracy
test_loss, test_acc = model.evaluate(test_orbits, test_labels, steps=20)
print ('Test accuracy:', test_acc)

# Predictions using test data
predictions = model.predict(test_orbits)

# Total number of 0's
k0=0
k1=0
for i in range(len(test_labels)):
    if test_labels[i]==0:
        k0=k0+1
    else:
        k1=k1+1
# Number of wrong prediction of 0's and 1's
j0=0
j1=0
wrongWhite=[]
wrongBlack=[]
for i in range(len(test_labels)):
    if np.argmax(predictions[i])!=test_labels[i] and test_labels[i]==0:
        j0=j0+1
        wrongWhite.append(i)
    if np.argmax(predictions[i])!=test_labels[i] and test_labels[i]==1:
        j1=j1+1
        wrongBlack.append(i)
percWhite=np.around(float(j0*100)/float(k0),decimals=2)
percBlack=np.around(float(j1*100)/float(k1),decimals=2)
percTot=np.round(float((j0+j1)*100)/float((k0+k1)),decimals=2)
print("Wrong 0's:",j0,"over",k0,"(",percWhite,"%)")
print("Wrong 1's:",j1,"over",k1,"(",percBlack,"%)")
print("Total error:",j0+j1,"over",k0+k1,"(",percTot,"%)")



