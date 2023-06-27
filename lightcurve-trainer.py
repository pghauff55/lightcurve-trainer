import random
import numpy as np
import tensorflow as tf
import sys
import time
from select import select

def prompt(timeout):
     print ("Press any key to configure or wait 5 seconds...")
     rlist, wlist, xlist = select([sys.stdin], [], [], timeout)
     if rlist:
         
         return 1
     else:
         
         return 0
     
     
def commandlinearguments():
     if __name__ == "__main__":
          print(f"Arguments count: {len(sys.argv)}")
          for i, arg in enumerate(sys.argv):
               print(f"Argument {i:>6}: {arg}")
     return sys.argv

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
def shuffle2(inputs_train,labels_train):
    counter=0
    step=0
    inputs_train_shuffled=[]
    labels_train_shuffled=[]
    while counter<len(inputs_train):
        step+=random.randint(1,100)
        if(step>len(inputs_train)):
             break
        inputs_train_shuffled.append(inputs_train[step])
        labels_train_shuffled.append(labels_train[step])
        counter+=1
    inputs_train_shuffled=np.array(inputs_train_shuffled)
    labels_train_shuffled=np.array(labels_train_shuffled)
    return (inputs_train_shuffled, labels_train_shuffled)
def shuffle3(inputs_train,labels_train):
    # UNTESTED METHOD

    # Each data element is randomly assigned an index between 0 and 1 using uniform probability
    # After that, the index array is sorted and the inputs and the targets will be indexed by the sorted indices - which rearranges them randomly
    # This could reduce the number of swaps a lot and will be way faster
    labels_train_shuffled=[]
    inputs_train_shuffled=[]
    data_indices = np.arange(len(inputs_train))
    np.random.shuffle(data_indices)
    for data_index in data_indices:
        inputs_train_shuffled.append(inputs_train[data_index])
        labels_train_shuffled.append(labels_train[data_index])
    inputs_train_shuffled=np.array(inputs_train_shuffled)
    labels_train_shuffled=np.array(labels_train_shuffled)
    return (inputs_train_shuffled, labels_train_shuffled)




argv=commandlinearguments()
if (len(argv)==2):
    if(argv[1]=="start"):
        inputs = tf.keras.Input(shape=(98,))
        dense = tf.keras.layers.Dense(128,activation="relu")
        x = dense(inputs)
        x = tf.keras.layers.Dense(64)(x)
        x = tf.keras.layers.Dense(64)(x)
        outputs = tf.keras.layers.Dense(7,activation="sigmoid")(x)
        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        model.compile(
            loss=tf.keras.losses.Poisson(),
            optimizer=tf.keras.optimizers.SGD(),
            metrics=["accuracy"])
        counter=0
        inputs_train=np.load("inputs_train_data.npy")
        labels_train=np.load("labels_train_data.npy")
        print(len(labels_train[0]))
        print(len(inputs_train[0]))
    else:
          print("Loading light_curve_model.keras"+argv[1])
          model = tf.keras.models.load_model("./light_curve_model"+argv[1]+".keras")
          checkpoint = tf.train.Checkpoint(model)
          load_status = model.load_weights("./checkpoint"+argv[1])
          status=checkpoint.restore("./checkpoint"+argv[1])
          print(status)
          print(load_status)
          print(model.summary())
          inputs_train=np.load("inputs_train_data"+argv[1]+".npy")
          labels_train=np.load("labels_train_data"+argv[1]+".npy")
          counter=int(argv[1])

else:
     if( len(argv)==3):
          model = tf.keras.models.load_model(argv[2])
     else:
          print("Loading light_curve_model.keras")
          model = tf.keras.models.load_model("./light_curve_model.keras")
          checkpoint = tf.train.Checkpoint(model)
          load_status = model.load_weights("./checkpoint")
          status=checkpoint.restore("./checkpoint")
          print(status)
          load_status.assert_consumed()
          print(load_status)
          print(model.summary())
          inputs_train=np.load("inputs_train_data.npy")
          labels_train=np.load("labels_train_data.npy")
          counter=0

(inputs_train,labels_train)=shuffle3(inputs_train,labels_train)


print(len(inputs_train))


while counter<1000:
    print("##########################"+repr(counter)+"#############################")
    counter_shuffle=0
    while counter_shuffle<5:
         (inputs_train,labels_train)=shuffle3(inputs_train,labels_train)
         counter_shuffle+=1
   # (inputs_train,labels_train)=shuffle2(inputs_train,labels_train)
    hist=model.fit(inputs_train, labels_train, epochs=2)
    
    
    if(counter%10==0):
        model.save("./light_curve_model"+repr(counter)+".keras")
        model.save_weights("./checkpoint"+repr(counter))
        np.save("inputs_train_data"+repr(counter)+".npy",inputs_train)
        np.save("labels_train_data"+repr(counter)+".npy",labels_train)
    #if(prompt(5)>0):
    #    break
    counter+=1
