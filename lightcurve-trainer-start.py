import random
import numpy as np
import tensorflow as tf



def shuffle(inputs_train,labels_train,N_counter):
    counter=0
    while counter<N_counter:
        index1=random.randint(0,len(inputs_train)-1)
        index2=random.randint(0,len(inputs_train)-1)
        temp1=inputs_train[index1]
        temp2=labels_train[index1]
        labels_train[index1]=labels_train[index2]
        labels_train[index2]=temp2
        inputs_train[index1]=inputs_train[index2]
        inputs_train[index2]=temp1
        counter+=1
        #print(inputs_train,labels_train)
    return (inputs_train,labels_train)


inputs = tf.keras.Input(shape=(99,))
dense = tf.keras.layers.Dense(128,activation="relu")
x = dense(inputs)
x = tf.keras.layers.Dense(64)(x)
x = tf.keras.layers.Dense(64)(x)
outputs = tf.keras.layers.Dense(5,activation="sigmoid")(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile(
    loss=tf.keras.losses.Poisson(),
    optimizer=tf.keras.optimizers.SGD(),
    metrics=["accuracy"],
)

inputs_train=np.load("inputs_train_data.npy")
labels_train=np.load("labels_train_data.npy")


(inputs_train,labels_train)=shuffle(inputs_train,labels_train,5*128000)





N=len(inputs_train)
K=128000
counter=0
while counter<1000:
    print("##########################"+repr(counter)+"#############################")
    (inputs_train,labels_train)=shuffle(inputs_train,labels_train,20*N)
    hist=model.fit(inputs_train, labels_train, epochs=2)
    model.save("./light_curve_model.keras")
    counter+=1
