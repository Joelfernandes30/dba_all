# with open("hello.txt", "w") as file:
#     file.write("hello world good morning")

with open("hello.txt", "a") as file:
    file.write("\n good evening")

with open("hello.txt", "r") as file:
    read= file.read()
    print(read)