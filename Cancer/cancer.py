import tensorflow as tf
import numpy as np
import csv

def load_data(inp_path):
	samples = []
	labels = []
	with open(inp_path, 'r') as inp_file:
		inp_data = csv.reader(inp_file)
		for line in inp_data:
			if(line[1] == 'B'):
				labels.append([1,0])
			else:
				labels.append([0,1])
			samples.append(list(map(float, line[2:])))
	max_col = np.max(samples, axis = 0)
	samples = np.divide(samples, max_col)
	return samples, labels

samples, labels = load_data('data.csv')

# input
x = tf.placeholder(dtype = tf.float32, shape= [None, 30])

#layer 1

W1 = tf.Variable(tf.zeros([30,50]))
b1 = tf.Variable(0.1)
y1 = tf.matmul(x, W1) + b1

# #layer 2

# W2 = tf.Variable(tf.zeros([150,20]))
# b2 = tf.Variable(0.1)
# y2 = tf.matmul(y1, W2) + b2

#layer 3 ( output layer)

W3 = tf.Variable(tf.zeros([50,2]))
b3 = tf.Variable(0.1)
y = tf.matmul(y1, W3) + b3

#labels

y_ = tf.placeholder(dtype = tf.float32, shape=[None, 2])

#loss

cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(labels= y_, logits= y)
cross_entropy = tf.reduce_mean(cross_entropy)

#train op
train_op = tf.train.AdamOptimizer(1e-2).minimize(cross_entropy)

# init
init = tf.global_variables_initializer()

#worker
sess = tf.Session()
sess.run(init)


for epoch in range(2000):
    loss, _ = sess.run([cross_entropy, train_op], {x : samples, y_ : labels})
    if(epoch % 500 == 0):
    	print(loss)	
# test

samples, labels = load_data('test.csv')

predictions = tf.argmax(y, 1)
true_labels = tf.argmax(y_, 1)
correct_prediction = tf.equal(predictions, true_labels)
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('accuracy = ', sess.run(accuracy, {x : samples, y_: labels}))