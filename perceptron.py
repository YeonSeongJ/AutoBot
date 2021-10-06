import random as rd

#####andGate#####
#make training data
train_data = []
test_data = []
for i in range(1000):
    insArr = []
    for k in range(2):
        insArr.append(rd.randint(0,1))
    
    insArr.append(1) if insArr[0] == 1 and insArr[1] == 1 else insArr.append(0)
    train_data.append(insArr)
    if i % 25 == 0:
        test_data.append(insArr[:2])

#Default valuables
WEIGHTS = [0.0, 0.0]
BIAS = 0
ERROR_RATE = 0.1

#calculate
def calculate(inputs):
    global WEIGHTS, BIAS
    result = BIAS
    for i in range(2):
        result += inputs[i] * WEIGHTS[i]

    return 1 if result >= 0 else 0



#traing function
def training(train_data, times):
    global WEIGHTS, BIAS, ERROR_RATE
    for time in range(times):
        errors = 0
        count = 0
        for data in train_data:
            count += 1
            cals = calculate(data[:2])
            error = data[2] - cals
            BIAS += error * ERROR_RATE
            errors += error ** 2
            # if error != 0:
            #     print('BIAS :', BIAS, 'count :', count)
            for k in range(2):
                WEIGHTS[k] += ERROR_RATE * error * data[k]
        print('WEIGHTS :', WEIGHTS, 'BIAS : %.3f' %(BIAS))
        print('시도 횟수 = %d 학습률 = %.3f 에러율 = %.3f' % (time, time/times, errors/len(train_data)))

    return 1

training(train_data, 3)

for i in test_data:
    input('실행하시려면 엔터하세요')
    print('data :', i, 'answer :', calculate(i))
    