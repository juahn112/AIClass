import numpy as np

class MultilayerPerceptron:
    def __init__(self, layer_list):
        self.layer_list = layer_list
        self.weight_list = []
        self.biases_list = []
        for i in range(len(layer_list) - 1):
            input_node = layer_list[i]
            output_node = layer_list[i + 1]

            w = np.random.randn(input_node, output_node)
            b = np.random.randn(output_node)

            self.weight_list.append(w)
            self.biases_list.append(b)
        self.num_layer = len(self.weight_list)
    
    def forward(self, input_data):
        current_input = input_data
        for i in range(self.num_layer):
            weight = self.weight_list[i]
            bias = self.biases_list[i]
            output = np.dot(current_input, weight) + bias
            activated_output = np.maximum(0, output)
            current_input = activated_output
        return current_input
    
    def calculate_loss(self, prediction, target):
        loss = np.mean((prediction - target) ** 2)
        return loss

if __name__ == "__main__":
    layer_list = [3, 5, 2]
    mlp = MultilayerPerceptron(layer_list)

    input_data = np.array([0.5, 0.2, 0.1])
    target = np.array([0.7, 0.3])

    prediction = mlp.forward(input_data)
    loss = mlp.calculate_loss(prediction, target)

    print("Prediction:", prediction)
    print("Loss:", loss)