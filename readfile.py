# file = open('text.txt')

# print(file.readline(7))

# line = file.readline()

# while line != "":
#   print(line)
#  line = file.readline()

# for i in file.readlines():
#    print(i)

# file.close()

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    with open('text.txt', 'w') as writer:
        writer.writelines(reversed(content))

with open('text.txt', 'r') as reader:
    content = reader.readlines()
    with open('text.txt', 'w') as writer:
        writer.writelines(reversed(content))

print("New branch")

print("New branch")

print("New branch")
