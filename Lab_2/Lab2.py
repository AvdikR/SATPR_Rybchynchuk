import math
import Functions

print("Work of vadym Rybchynchuk AP-31")
print("Lab 2")
print("Variant 3")
print("")

f1 = open("TableK1.txt", "r")
f2 = open("TableK2.txt", "r")
f3 = open("TableK3.txt", "r")

f4 = open("TableA11.txt", "r")
f5 = open("TableA12.txt", "r")
f6 = open("TableA13.txt", "r")

f7 = open("TableA21.txt", "r")
f8 = open("TableA22.txt", "r")
f9 = open("TableA23.txt", "r")

f10 = open("TableA31.txt", "r")
f11 = open("TableA32.txt", "r")
f12 = open("TableA33.txt", "r")

f13 = open("TableA41.txt", "r")
f14 = open("TableA42.txt", "r")
f15 = open("TableA43.txt", "r")


print("TableK1: ")
TableK1 = Functions.procCrit(f1)

print("TableK2: ")
TableK2 = Functions.procCrit(f2)

print("TableK3: ")
TableK3 = Functions.procCrit(f3)

print("TableK: ")
TableK = Functions.procAveGrade(TableK1, TableK2, TableK3)

TableA11 = Functions.procCrit1(f4)
TableA12 = Functions.procCrit1(f5)
TableA13 = Functions.procCrit1(f6)
TableA21 = Functions.procCrit1(f7)
TableA22 = Functions.procCrit1(f8)
TableA23 = Functions.procCrit1(f9)
TableA31 = Functions.procCrit1(f10)
TableA32 = Functions.procCrit1(f11)
TableA33 = Functions.procCrit1(f12)
TableA41 = Functions.procCrit1(f13)
TableA42 = Functions.procCrit1(f14)
TableA43 = Functions.procCrit1(f15)

print("TableMaxQA1: ")
TableQA1 = Functions.MaxVectorA(TableA11, TableA12, TableA13)

print("TableMaxQA2: ")
TableQA2 = Functions.MaxVectorA(TableA21, TableA22, TableA23)

print("TableMaxQA3: ")
TableQA3 = Functions.MaxVectorA(TableA31, TableA32, TableA33)

print("TableMaxQA4: ")
TableQA4 = Functions.MaxVectorA(TableA41, TableA42, TableA43)

print("Result: ")
Functions.CalGlobalPriorities(TableK, TableQA1, TableQA2, TableQA3, TableQA4)











   
    







