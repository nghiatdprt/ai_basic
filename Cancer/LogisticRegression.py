import numpy as np
import csv
vector_x = []
vector_y = []
learning_rate = 0.1
pre_cost = cur_cost = 0.1
step = 0
def compute_hypothesis():
    global hypothesis
    temp = theta.dot(vector_x)
    hypothesis = 1/(1+np.exp(-temp))
def compute_J1():
    global J1
    J1 = -1/m * (vector_y*np.log(hypothesis) + (1-vector_y)*np.log(1-hypothesis))
def gradient_descent():
    global theta, pre_cost, cur_cost, step
    while(True):
        for i in range(n):
            temp = hypothesis - vector_y
            temp = temp.dot(vector_x[i].transpose())
            theta[i] = theta[i] - learning_rate*(1/m)*temp.sum()
        compute_hypothesis()
        compute_J1()
        pre_cost = cur_cost
        cur_cost = J1.sum()
        if(abs(cur_cost - pre_cost) <= 0.00001): break
        step += 1
        print(step, '\t\t', cur_cost)
with open('data.csv') as input_file:
    input_data = csv.reader(input_file)
    for line in input_data:
        if(line[1] == 'B') :
            vector_y.append(0)
        else :
            vector_y.append(1)
        line = line[2:]
        line = list(map(float, line))
        line.insert(0,1)
        vector_x.append(line)
m = len(vector_x)
n = len(vector_x[0])
vector_x = np.array(vector_x).transpose()
vector_y = np.array(vector_y)
max_col = np.max(vector_x, axis=1)

vector_x /= max_col[:,None]
theta = np.array([0.1] * n)
J1 = np.array([0.1] * m)
hypothesis = np.array([0.1] * m)
compute_hypothesis()
compute_J1()
gradient_descent()

# Test
vector_x = []
vector_y = []
with open('test.csv') as file_test:
    data_test = csv.reader(file_test)
    for line in data_test:
        if(line[1] == 'B') :
            vector_y.append(0)
        else :
            vector_y.append(1)
        line = line[2:]
        line = list(map(float, line))
        line.insert(0,1)
        vector_x.append(line)
m = len(vector_x)
n = len(vector_x[0])
vector_x = np.array(vector_x).transpose()
vector_y = np.array(vector_y)
vector_x /= max_col[:,None]
compute_hypothesis()
correct_ans = 0
result = [0] * m
for i in range(m):
    if(hypothesis[i] < 0.5): result[i] = 0
    else: result[i] = 1
for i in range(m):
    if(result[i] == vector_y[i]): correct_ans += 1
print(correct_ans,'/',m,' ~ ', round(correct_ans/m*100,2),'%')
