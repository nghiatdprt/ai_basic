import numpy as np
import csv

vector_x = []
vector_y = []
learning_rate = 0.1
pre_cost = cur_cost = 0.1
step = 0
def compute_hypothesis():
    global hypothesis
    hypothesis = theta.dot(vector_x)
def compute_J1():
    global J1
    J1 = hypothesis - vector_y
def cost_func():
    temp = np.multiply(J1,J1)
    return temp.sum()
def gradient_descent():
    global theta, pre_cost, cur_cost, step
    while(True):
        for i in range(n):
            temp = J1.dot(vector_x[i].transpose())
            theta[0,i] = theta[0,i] - learning_rate*(1/m)*temp.sum()
        compute_hypothesis()
        compute_J1()
        pre_cost = cur_cost
        cur_cost = cost_func()
        if(abs(cur_cost - pre_cost) <= 0.001): break
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
vector_x = np.matrix(vector_x).transpose()
vector_y = np.matrix(vector_y)
max_col = np.max(vector_x, axis=1)
vector_x[0:] = vector_x[0:]/max_col
theta = np.matrix([0.1] * n)
J1 = np.matrix([0.1] * m)
hypothesis = np.matrix([0.1] * m)
compute_hypothesis()
compute_J1()
gradient_descent()

#Test
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
vector_x = np.matrix(vector_x).transpose()
vector_y = np.matrix(vector_y)
vector_x[0:] = vector_x[0:]/max_col
compute_hypothesis()
correct_ans = 0
result = [0] * m
for i in range(m):
    if(hypothesis[0,i] < 0.5): result[i] = 0
    else: result[i] = 1
for i in range(m):
    if(result[i] == vector_y[0,i]): correct_ans += 1
print(correct_ans,'/',m,' ~ ', round(correct_ans/m*100,2),'%')
