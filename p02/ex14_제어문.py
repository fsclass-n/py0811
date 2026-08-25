# 제어문
# 반복문: for~in
# 조건문: if~else

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
	if i % 2 is not 0:
		print(i, '홀수')
	else:
		print(i, '짝수')

#----------------------------------
price = [23, 40, 67]

for i in price:
	print(i * 1.1)