from keras.datasets import mnist
from keras import Sequential
from keras import layers
import tensorflow as tf

(x_train_data, y_train_data), (x_test_data, y_test_data) = mnist.load_data()

x_train_data = tf.keras.utils.normalize(x_train_data, axis=1)
x_test_data = tf.keras.utils.normalize(x_test_data, axis=1)

model = Sequential()

model.add(layers.Flatten(input_shape=(28, 28)))

model.add(layers.Dense(units=128, activation=tf.nn.relu))
model.add(layers.Dense(units=128, activation=tf.nn.relu))
model.add(layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

model.fit(x_train_data, y_train_data, epochs=4)

accuracy, loss = model.evaluate(x_test_data, y_test_data)

model.save("mnist.model")
