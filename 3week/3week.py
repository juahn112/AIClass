# scores = [72,85,90,66,78]
# sum_1 = 0
# sum_2 = 0
# #for문만 사용하는 방법
# for i in scores:
#     sum_1 += i
# avg = sum_1 / len(scores)
# print("for문만 사용한 방법 :", avg)

# #range()를 사용하는 방법
# for i in range(len(scores)):
#     sum_2 += scores[i]
# avg = sum_2 / len(scores)
# print("range()를 사용한 방법 :", avg)

# # 조건문 사용하여 합격여부 판별
# scores_2 = [45, 68, 72, 59, 81]
# for score in scores_2:
#     if score >= 60:
#         print(f"{score}점 : Pass")
#     else:
#         print(f"{score}점 : Fail")

# # 가장 높은 값 구하기
# array = [3, 7, 2, 9, 5]
# max_value = array[0]
# for i in array:
#     if i > max_value:
#         max_value = i
# print("가장 높은 값 :", max_value)

# # 가장 낮은 값 구하기
# array_2 = [68, 72, 59, 81, 45]
# min_value = array_2[0]
# for i in array_2:
#     if i < min_value:
#         min_value = i
# print("가장 낮은 값 :", min_value)

# 리스트에서 두번 째로 높은 값 구하기
array_3 = [24, 56, 12, 89, 34]
print("원래 리스트 :", array_3)
# 버블 정렬을 사용하여 리스트를 오름차순으로 정렬
for i in range(len(array_3) - 1):
    for j in range(len(array_3) - 1 - i):
        if array_3[j] > array_3[j + 1]:
            array_3[j], array_3[j + 1] = array_3[j + 1], array_3[j]
print("정렬된 리스트 :", array_3)
print("두 번째로 높은 값 :", array_3[-2])

        
        
        

