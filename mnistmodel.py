import tensorflow as tf
#load dataset
mnist=tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test)=mnist.load_data()

#preprocessing
x_train=x_train.reshape(60000,28,28,1)
x_test=x_test.reshape(10000,28,28,1)
x_train=x_train/255.0
x_test=x_test/255.0

#define the model
model_cnn=tf.keras.models.Sequential([
tf.keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=(28,28,1)),
tf.keras.layers.MaxPooling2D((2,2)),
tf.keras.layers.Conv2D(32,(3,3),activation="relu"),
tf.keras.layers.MaxPooling2D((2,2)),
tf.keras.layers.Flatten(),
tf.keras.layers.Dense(512,activation="relu"),
tf.keras.layers.Dense(10,activation="softmax")])

#define a callback
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self,epochs,logs={}):
      if (logs.get('accuracy')>0.998):
        print('reached 99% accuracy ,so stopping!')
        self.model.stop_training=True

callback=myCallback()
#compile & train the model
model_cnn.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])
history=model_cnn.fit(x_train,y_train,epochs=10,callbacks=[callback])

loss, acc = model_cnn.evaluate(x_test,y_test)
print(loss , acc )


model_cnn.save("model")