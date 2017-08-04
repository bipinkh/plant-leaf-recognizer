# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 08:36:06 2017
The document is copyright of Authors.
@author: bipin
"""
import os
#importing Keras, Library for deep learning 
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from keras.preprocessing.image import  img_to_array
from keras import backend as K
from keras.models import model_from_json
K.set_image_dim_ordering('th')
import numpy as np
 # Image manipulations and arranging data
from PIL import Image
import theano
theano.config.optimizer="None"
#Sklearn to modify the data
from sklearn.cross_validation import train_test_split


def main():
    print("model building started")
    algorithm = build()
    algorithm.buildModel("F:/minorproject/data/train")
    algorithm.test("F:/minorproject/data/test/IMG_20170629_123403.jpg")


class build:
    #image dimension
    m,n = 50,50

    def buildModel(self,trainfolderlocation):
        #os.chdir("F:/minorproject/data");
        # input image dimensions
        os.chdir(trainfolderlocation)
        #trainfolder="train"
        classes=os.listdir(trainfolderlocation)
        print(classes)
        x=[]
        y=[]
        for fol in classes: #fol for folder
            print (fol)
            imgfiles=os.listdir(trainfolderlocation+'/'+fol);
            for img in imgfiles:
                if (img != "Thumbs.db"):
                    im=Image.open(trainfolderlocation+'/'+fol+'/'+img);
                    im=im.convert(mode='RGB')
                    imrs=im.resize((build.m,build.n))
                    imrs=img_to_array(imrs)/255;
                    imrs=imrs.transpose(2,0,1);
                    imrs=imrs.reshape(3,build.m,build.n);
                    x.append(imrs)
                    y.append(fol)
        x=np.array(x);
        y=np.array(y);

        batch_size=32
        nb_classes=len(classes)
        nb_epoch=20
        nb_filters=32
        nb_pool=2
        nb_conv=3

        x_train, x_test, y_train, y_test= train_test_split(x,y,test_size=0.2,random_state=4)

        uniques, id_train=np.unique(y_train,return_inverse=True)
        Y_train=np_utils.to_categorical(id_train,nb_classes)
        uniques, id_test=np.unique(y_test,return_inverse=True)
        Y_test=np_utils.to_categorical(id_test,nb_classes)

        self.model= Sequential()
        self.model.add(Convolution2D(nb_filters,nb_conv,nb_conv,border_mode='same',input_shape=x_train.shape[1:]))
        self.model.add(Activation('relu'));
        self.model.add(Convolution2D(nb_filters,nb_conv,nb_conv));
        self.model.add(Activation('relu'));
        self.model.add(MaxPooling2D(pool_size=(nb_pool,nb_pool)));
        self.model.add(Dropout(0.5));
        self.model.add(Flatten());
        self.model.add(Dense(128));
        self.model.add(Dropout(0.5));
        self.model.add(Dense(nb_classes));
        self.model.add(Activation('softmax'));
        self.model.compile(loss='categorical_crossentropy',optimizer='adadelta',metrics=['accuracy']) #LR=1 default
        nb_epochs=10;
        batch_size=16;
        self.model.fit(x_train,Y_train,batch_size=batch_size,epochs=nb_epochs,verbose=1,validation_data=(x_test, Y_test))


    
    def storemodel(self):
        # serialize model to JSON
        model_json = self.model.to_json()
        with open("F:/minorproject/plantleafrecognition/model/model.json", "w") as json_file:
            json_file.write(model_json)
        # serialize weights to HDF5
        self.model.save_weights("F:/minorproject/plantleafrecognition/model/model.h5")
        print("Saved model to disk")
    
    def reawakemodel(self):
        try:
            # load json and create model
            json_file = open('F:/minorproject/plantleafrecognition/model/model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            self.model = model_from_json(loaded_model_json)
            # load weights into new model
            self.model.load_weights("F:/minorproject/plantleafrecognition/model/model.h5")
            print("Loaded model from disk")
            return True
        except:
            return False

    def test(self,testimagepath):
        im=Image.open(testimagepath)
        imrs = im.resize((build.m,build.n))
        imrs=img_to_array(imrs)/255;
        imrs=imrs.transpose(2,0,1);
        imrs=imrs.reshape(3,build.m,build.n);
        x=[]
        x.append(imrs)
        x=np.array(x);
        try:
            predictions = self.model.predict(x)
            print("predictions:")
            print(predictions)
            return predictions[0]
        except:
            return "Error1" #for not building model

        
if __name__ == "__main__":
   main()
