# ret = vector1.vector2
def inner_product(vector1, vector2):
    return sum(vector1[i]*vector2[i] for i in range(0, len(vector1)))

# ret = value*vector1 + vector2
def dot_product_add(value, vector1, vector2):
    return [vector1[i]*value + vector2[i] for i in range(0, len(vector1))]
    