import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
# set environment log level
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
learn = tf.contrib.learn
tf.logging.set_verbosity(tf.logging.ERROR)
mnist = learn.datasets.load_dataset('mnist')
data = mnist.train.images
labels = np.asarray(mnist.train.labels, dtype=np.int32)
test_data = mnist.test.images
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)
max_examples = 100000
data = data[:max_examples]
labels = labels[:max_examples]

def display(i):
    img = test_data[i]
    plt.title('Example %d. Label: %d' % (i, test_labels[i]))
    plt.imshow(img.reshape((28,28)), cmap=plt.cm.gray_r)
    plt.show()

display(0)

feature_columns = learn.infer_real_valued_columns_from_input(data)
classifier = learn.LinearClassifier(feature_columns=feature_columns, n_classes=10)
classifier.fit(data, labels, batch_size=100, steps=1000)
classifier.evaluate(test_data, test_labels)
print(classifier.evaluate(test_data, test_labels)["accuracy"])
print(classifier.predict(np.array([test_data[0]], dtype=float), as_iterable=False))
#print("Predicted %d, Label: %d" % (classifier.predict(test_data[0]), test_labels[0]))
display(0)
