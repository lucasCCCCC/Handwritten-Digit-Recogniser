# Handwritten Digit Recogniser

A neural network made using TensorFlow using the MNIST dataset to recognise handwritten digits

## Setting up the program

Run _Model.py_ to create and save the _minst.model_ file

#### Results:

```
Epoch 1/3
1875/1875 [==============================] - 4s 2ms/step - loss: 0.2715 - accuracy: 0.9220
Epoch 2/3
1875/1875 [==============================] - 3s 2ms/step - loss: 0.1093 - accuracy: 0.9663
Epoch 3/3
1875/1875 [==============================] - 3s 2ms/step - loss: 0.0738 - accuracy: 0.9773
313/313 [==============================] - 1s 1ms/step - loss: 0.0915 - accuracy: 0.9717
```


## Running the program

_Predict.py_ can now be run which opens up a pygame window where digits can be drawn onto a canvas, where the neural network predicts the drawn number

#### Demo:

<img src="Demo Animations/demo.gif" width="500">
