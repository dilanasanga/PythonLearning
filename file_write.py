with open("write.txt", "w") as write_file:
     with open("test.txt", "r") as read_file:
        read_file_conent = read_file.read()
        print(read_file_conent)
        write_file.write(read_file_conent)

with open("write.txt", "w") as write_file:
    write_file.write("Test")