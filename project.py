def data_swap():
    first_file = input("Write the name of the first file: ")
    second_file = input("Write the name of the second file: ")
    
    
    with open(first_file, "r") as file1:
        data_1 = file1.read()

    with open(second_file, "r") as file2:
        data_2 = file2.read()

    with open(first_file, "w") as file1:
        file1.write(data_2)

    with open(second_file, "w") as file2:
        file2.write(data_1)

    file1.close()
    file2.close()
data_swap()