def predict(new_radio, weight, bias):
    return new_radio * weight + bias


def loss_function(X, y, weight, bias):
    '''
    Loss function and cost function is the same 

    caculate the MSE (Mean Square Error) as low as possible 
'''
    n = len(X)
    sum_error = 0

    for i in range(n):
        sum_error += (y[i] - (weight * X[i] + bias)) ** 2

    return sum_error / n


def update_weight(X, y, weight, bias, learning_rate):
    '''
    Để tối ưu hàm lossfunction thì chúng ta cần tính lại weight bà bias mới tối ưu hơn

    Chúng ta thực hiện tính weight và bias bằng cách

    lấy weight và bias hiện tại - (tính weight và bias với mối điểm dữ liệu rồi lấy trung
    bình của tất cả các điểm dữ liệu sau đó nhân với learning rate)

    learning rate là tốc độ học
    '''
    n = len(X)
    weight_temp = 0.0
    bias_temp = 0.0

    for i in range(n):
        weight_temp += 2*X[i] * ((weight * X[i] + bias) - y[i])
        bias_temp += 2*((weight * X[i] + bias) - y[i])

    weight -= (2*weight_temp/(n))*learning_rate
    bias -= (2*bias_temp/(n))*learning_rate

    return weight, bias


def train(X, y, weight, bias, learning_rate, iter):
    loss_his = []
    for i in range(iter):
        weight, bias = update_weight(X, y, weight, bias, learning_rate)
        loss = loss_function(X, y, weight, bias)
        loss_his.append(loss)

    return weight, bias, loss_his


if __name__ == '__main__':

    houses = [
        (50, 600),
        (70, 800),
        (75, 860),
        (80, 930),
        (90, 1040),
        (100, 1150),
        (105, 1200),
        (60, 700),
        (85, 970),
        (65, 750),
    ]

    # prepare data
    areas = list(map(lambda x: x[0], houses))
    prices = list(map(lambda x: x[1], houses))

    weight, bias, loss_his = train(X=areas,
                                   y=prices,
                                   weight=0.03,
                                   bias=0.001,
                                   learning_rate=0.00001,
                                   iter=600)

    print(predict(40, weight=weight, bias=bias))
    # Như vậy thì khi mà nhà tầm 40 m2 thì giá tầm 460 (100 * USD)