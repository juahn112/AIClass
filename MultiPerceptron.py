import numpy as np

class MultilayerPerceptron: # 다층 퍼셉트론 클래스 정의
    def __init__(self, layer_list): # 생성자 메서드, layer_list는 각 층의 노드 수를 담은 리스트
        self.layer_list = layer_list # 입력층, 은닉층, 출력층의 노드 수를 담은 리스트
        self.weight_list = [] # 각 층의 가중치를 담는 리스트 
        self.biases_list = [] # 각 층의 편향을 담는 리스트
        for i in range(len(layer_list) - 1): # 각 층의 가중치와 편향을 초기화, 층과 층 사이에서 가중치와 편향이 존재하기 때문에, 가중치 리스트의 길이는 모든 층 - 1과 같다
            input_node = layer_list[i] # 현재 층의 노드 수
            output_node = layer_list[i + 1] # 다음 층의 노드 수

            w = np.random.randn(input_node, output_node)# 가중치를 랜덤 값으로 초기화
            b = np.random.randn(output_node) # 편향을 랜덤 값으로 초기화

            self.weight_list.append(w) # 가중치를 리스트에 추가
            self.biases_list.append(b) # 편향을 리스트에 추가
        self.num_layer = len(self.weight_list) # 층의 수 (입력층 제외), 가중치 리스트의 길이로 계산(입력층은 가중치가 없으므로), 가중치는 층과 층 사이에 존재하기 때문에, 가중치 리스트의 길이는 모든 층 - 1과 같다
    
    def forward(self, input_data): # 순전파 메서드, input_data는 입력 데이터
        self.activations = [input_data] # 각 층의 활성화 값을 담는 리스트, 순전파 과정에서 각 층의 활성화 값을 저장하기 위해 사용
        current_input = input_data # 현재 입력값을 초기 입력 데이터로 설정
        for i in range(self.num_layer): # 각 층에 대해 순전파 계산, 가중치와 편향을 사용하여 출력값을 계산하고, ReLU 활성화 함수를 적용하여 다음 층의 입력값으로 설정, 층과 층 사이에서 가중치와 편향이 존재하기 때문에, 가중치 리스트의 길이만큼 반복
            weight = self.weight_list[i] # 현재 층의 가중치
            bias = self.biases_list[i] # 현재 층의 편향
            output = np.dot(current_input, weight) + bias # 현재 입력값과 가중치를 곱하고(행렬 곱) 편향을 더하여 출력값 계산
            activated_output = np.maximum(0, output) # ReLU 활성화 함수 적용, 음수는 0으로, 양수는 그대로 유지
            current_input = activated_output # 다음 층의 입력값으로 설정
            self.activations.append(activated_output) # 현재 층의 활성화 값을 리스트에 저장
            print(f"Now layer : {i}, output : {activated_output}") # 현재 층의 번호와 활성화 값을 출력하여 디버깅 정보 제공
        return current_input # 최종 출력값 반환 (출력층의 활성화 함수는 적용하지 않음, 회귀 문제에서는 출력층에 활성화 함수를 적용하지 않는 경우가 많음)
    
    def calculate_loss(self, prediction, target): # 손실 계산 메서드, prediction은 모델의 예측값, target은 실제 값(정답)
        loss = np.mean((prediction - target) ** 2) # 평균 제곱 오차(MSE) 손실 계산, 예측값과 실제 값의 차이를 제곱하여 평균을 구함
        return loss # 계산된 손실값 반환
    
    def backward(self, input_data, target, learning_rate=0.01): # 역전파 메서드, input_data는 입력 데이터, target은 실제 값(정답), learning_rate는 학습률
        
        pass 

if __name__ == "__main__": # 메인 블록, 이 부분은 모듈이 직접 실행될 때만 실행됨(테스트 코드)
    layer_list = [3, 5, 2] # 입력층 3개 노드, 은닉층 5개 노드, 출력층 2개 노드로 구성된 다층 퍼셉트론 모델을 생성하기 위한 층 리스트
    mlp = MultilayerPerceptron(layer_list) # 다층 퍼셉트론 모델 생성, layer_list를 인자로 전달하여 모델 초기화

    input_data = np.array([0.5, 0.2, 0.1]) # 입력 데이터, 3개의 노드에 해당하는 값으로 구성된 배열, 입력층의 노드 수와 일치해야 함
    target = np.array([0.7, 0.3]) # 실제 값(정답), 2개의 노드에 해당하는 값으로 구성된 배열, 출력층의 노드 수와 일치해야 함

    prediction = mlp.forward(input_data) # 순전파를 통해 예측값 계산, input_data를 인자로 전달하여 모델의 예측값을 얻음
    loss = mlp.calculate_loss(prediction, target) # 예측값과 실제 값(정답)을 사용하여 손실 계산, prediction과 target을 인자로 전달하여 모델의 손실값을 얻음

    print("Prediction:", prediction) # 예측값 출력
    print("Loss:", loss) # 손실값 출력