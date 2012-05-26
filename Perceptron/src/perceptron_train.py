from math_op import inner_product, dot_product_add

def perceptron_train(training_set, label, learning_rate = 1.0):
    num = len(training_set)
    if num == 0:
        raise "the training set is empty"
    if len(label) != num:
        raise "the number of training sample is not the same with labels"
    for sample in training_set:
        sample.append(1)
    dim = len(training_set[0])
    model = [0] * dim
    while True:
        error_count = 0
        for i in range(0, dim):
            if label[i]*inner_product(model, training_set[i]) <= 0:
                model = dot_product_add(label[i]*learning_rate, training_set[i], model)
                error_count = error_count + 1
        if error_count == 0:
            return model
    
                