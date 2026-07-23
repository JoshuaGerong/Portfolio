Message = input("Write a message: ")
file = open("message.txt", "w")
file.write(Message)
file.close()
file = open("message.txt", "r")
print(file.read())
file.close()
file = open("message.txt", "a")
message = input("Write a  message: ")
file.write("\n" + message)

try:
    file = open("message.txt", "r")
except:
    print("File Not Found")
