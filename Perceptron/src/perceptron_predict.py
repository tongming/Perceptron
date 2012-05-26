from math_op import inner_product

def perceptron_predict(test_set, model, threshold = 0.5):
    prediction = []
    for sample in test_set:
        sample.append(1)
        if inner_product(sample, model) > threshold:
            prediction.append(1)
        else:
            prediction.append(-1)
    return prediction
        
    
    
