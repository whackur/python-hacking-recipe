def generator():
    for i in range(3):
        yield i


gen = generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # StopInteration Error
