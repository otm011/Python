import functions #

coasters = ["Black Mamba", "Colorado Adventure", "Taron", "Raik", "Winjas", "Chiapas"]

remainder = coasters.pop()

enum = ", ".join(coasters)

enum2 = enum + " und " + remainder

print(enum2)

for coaster in coasters:
    print(coaster)

protolist = enum2.split(", ")

print(protolist)

rem1 = protolist.pop()

rem2 = rem1.split(" und ")

protolist.append(rem2[0]) #

protolist.append(rem2[1])

new_coasters = protolist

print(new_coasters)

new_coasters.sort()

print(new_coasters)

functions.multiprint("Hi", 3) #

print()

print("////////////////////////////")

print()

functions.reverse_rec(new_coasters)
