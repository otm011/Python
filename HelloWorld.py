TEST_TXT = "test.txt"


def multiprint(message, a):
    for i in range(0, a):
        print(message + "\n")

def get_line (filename, position):
    with open(filename, "r") as file:
        counter = 0
        for line in file:
            if counter == position:
                return line
            else:
                counter += 1
        return "line not found:" + str(position)

# multiprint("Hello world", 26)

# with open("test.txt","r") as file:
#     for line in file:
#         multiprint(line.strip(), 2)
#     print(get_line("test.txt", 1))

def print_file_perm(txt=TEST_TXT):
    with open(txt, "r") as file:
        for line in file:
            liste = line.split(" ")
            print(get_line(txt, int(liste[0]) - 1))


print_file_perm("test2.txt")
