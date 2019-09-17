from math import exp
# 0 to 1
def sigmoid(x):
    x = 1.0*x
    return 1/ (1+exp(-x))

def dsigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

ALFA = 0.5
w = [[0 for i in range(2)] for j in range(2)]
w_0 = [0 for i in range(2)]
v = [[0 for i in range(2)] for j in range(81)]
v_0 = [0 for i in range(2)]

# hidden layer, 2

datas = open('data', 'r').read().split('\n')
train_data = []
for i in datas:
    train_data.append((i[0], i[1:]))

target = {
    'A': [1, 0],
    'B': [0, 1]
}

for epoch in range(1000):
    if epoch % 100 == 0: print "epoch-{}".format(epoch)
    for datas in range(len(train_data)):
        z_in = [0 for j in range(2)]
        y_in = [0 for j in range(2)]
        z = [0 for j in range(2)]
        y = [0 for j in range(2)]
        
        t = target[train_data[datas][0]]
        x = [int(inp) for inp in train_data[datas][1]]
        for j in range(2):
            sumxv = 0
            for i in range(len(x)):
                sumxv += x[i]*v[i][j]
            z_in[j] = v_0[j] + sumxv

        for j in range(2):
            z[j] = sigmoid(z_in[j])

        for k in range(2):
            sumzw = 0
            for j in range(len(z)):
                sumzw += z[j]*w[j][k]
            y_in[k] = w_0[k] + sumzw

        for k in range(2):
            y[k] = sigmoid(y_in[k])

        delta = [0 for k in range(2)]
        delta_w = [[0 for i in range(2)] for j in range(2)]
        delta_w_0 = [0 for i in range(2)]
        for k in range(2):
            delta[k] = (t[k]-y[k]) * dsigmoid(y_in[k])
        
        for k in range(2):
            for j in range(2):
                delta_w[j][k] = ALFA * delta[k] * z[j]

        for j in range(len(delta)):
            delta_w_0[j] = ALFA * delta[j]
        
        delta_in = [[0 for i in range(2)] for j in range(2)]
        for j in range(len(w)):
            sumdeltaw = 0
            for k in range(len(delta)):
                sumdeltaw += delta[k]*w[j][k]
            delta_in[j] = sumdeltaw
            delta[j] = delta_in[j]*dsigmoid(z_in[j])
        
        delta_v = [[0 for i in range(2)] for j in range(81)]
        delta_v_0 = [0 for i in range(2)]

        for i in range(81):
            for j in range(len(delta)):
                delta_v[i][j] = ALFA * delta[j] * x[i]
        for j in range(len(delta)):
            delta_v_0[j] = ALFA * delta[j]

        for j in range(2):
            for k in range(2):
                w[j][k] += delta_w[j][k]

        for j in range(len(delta)):
            w_0[j] += delta_w_0[j]

        for i in range(81):
            for j in range(len(delta)):
                v[i][j] += delta_v[i][j]
        for j in range(len(delta)):
            v_0[j] += delta_v_0[j]


# bobot akhir
w_final = [w_0]+w
v_final = [v_0]+v

print '*'*10+'Bobot W'+'*'*10
for i in w_final:
    print i
print 
print '*'*10+'Bobot V'+'*'*10

for i in v_final:
    print i