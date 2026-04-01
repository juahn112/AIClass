input_x = [2.0, 3.0]
weight = [0.5, -1.0]
b = 0.7

def weighted_sum(x, y, z):
    first_product = x[0] * y[0]
    second_product = x[1] * y[1]
    third_product = first_product + second_product
    return third_product + z

output = weighted_sum(input_x, weight, b)
print(output)