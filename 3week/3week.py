scores = [72,85,90,66,78]
sum_1 = 0
sum_2 = 0
#for문만 사용하는 방법
for i in scores:
    sum_1 += i
avg = sum_1 / len(scores)
print("for문만 사용한 방법 :", avg)

#range()를 사용하는 방법
for i in range(len(scores)):
    sum_2 += scores[i]
avg = sum_2 / len(scores)
print("range()를 사용한 방법 :", avg)