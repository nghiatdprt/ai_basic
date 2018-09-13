import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot= True)


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev= 0.1)
    return tf.Variable(initial)

def conv2d(_x, _w):
    return tf.nn.conv2d(_x, _w, strides = [1,1,1,1], padding = "SAME")

def max_pool2d(_x):
    return tf.nn.max_pool(_x, ksize = [1,2,2,1], strides = [1,2,2,1] , padding = "SAME")

x_ = tf.placeholder(dtype = tf.float32, shape= [None, 784], name='Input_Image')
x = tf.reshape(x_, shape = [-1,28,28,1])

y_ = tf.placeholder(dtype = tf.float32, shape= [None, 10], name='Labels')

#first conv
w_conv1 = weight_variable([3,3,1,32])
b_conv1 = tf.Variable(0.1)
y_conv1 = tf.nn.relu(conv2d(x,w_conv1) + b_conv1)
y_pool1 = max_pool2d(y_conv1)

#2ns conv
w_conv2 = weight_variable([2,2,32,64])
b_conv2 = tf.Variable(0.2)
y_conv2 = tf.nn.relu(conv2d(y_pool1, w_conv2) + b_conv2)
y_pool2 = max_pool2d(y_conv2)

#fully connected layer
y_pool_flat = tf.reshape(y_pool2, shape = [-1, 7*7*64])

w_pre1 = weight_variable([7*7*64, 1024])
b_pre1 = tf.Variable(0.1)
y_pre1 = tf.nn.sigmoid(tf.matmul(y_pool_flat, w_pre1) + b_pre1)

y_drop = tf.nn.dropout(y_pre1, 0.75)

w_out = weight_variable([1024, 10])
b_out = tf.Variable(0.1)
y = tf.matmul(y_drop, w_out) + b_out

#cross entropy
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels= y_, logits= y))

#train op
train_op = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
init = tf.global_variables_initializer()

step = 0
limit = 1000
saver = tf.train.Saver()
#train
with tf.Session() as sess:
    # writer = tf.summary.FileWriter('/tmp/logs', sess.graph)
    sess.run(init)
    try:
        saver.restore(sess, '/tmp/mnist_cnn/my_model')
    except Exception as ex:
        print("Saving file doesn't exist")
    for epoch in range(limit):
        step += 1
        batch_x, batch_y = mnist.train.next_batch(100)
        loss, _ = sess.run([cross_entropy, train_op], {x_ : batch_x, y_: batch_y})
        if(step % 500 == 0):
            print('local step : ', step, ' ; loss = ', loss)
        if(step == limit):
            save_path = saver.save(sess, '/tmp/mnist_cnn/my_model')
            print('Training Completed')
            print('Saving successful, save path : ', save_path)

#test
# with tf.Session() as sess:
#     try:
#         saver.restore(sess, '/tmp/mnist_cnn/my_model')
#         prediction = tf.argmax(y,1)
#         true_label = tf.argmax(y_,1)
#         pre = tf.equal(prediction, true_label)
#         accuracy = tf.reduce_mean(tf.cast(pre, tf.float32))
#         accuracy = sess.run(accuracy, {x_ : mnist.test.images, y_: mnist.test.labels})
#         print('accuracy : ',accuracy)
#     except Exception as ex:
#         print('Saver not found')