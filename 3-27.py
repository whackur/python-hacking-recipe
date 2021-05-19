import random

word_list = ["가", "나", "다", "라", "마"]

# 0 ~ 1 사이의 무작위 소수점 숫자 반환
print(random.random())

# 50 ~ 100 이하의 무작위 소수점 숫자 반환
print(random.uniform(50, 100))

# 0 ~ 3 미만의 무작위 소수점 숫자 반환
print(random.randrange(0, 3))

# shuffle 함수로 리스트 무작위로 섞기
print(word_list)
random.shuffle(word_list)
print(word_list)

# 배열에서 무작위로 2개의 요소를 뽑기
print(random.sample(word_list, 2))
