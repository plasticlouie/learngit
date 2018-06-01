import tensorflow as tf
import numpy as np

slim = tf.contrib.slim

x = tf.placeholder(tf.float32, shape=(None,32,32,1))
net = slim.conv2d(x, 32, [3,3])
