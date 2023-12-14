import math

#Побудова таблиць та знаходження нормованого вектору
def procCrit(table_in_file):
    table = list()
    tmpL = list()
    Wnorm = list()

    for l in table_in_file:
        table.append([float(i) for i in l.split()])

    for row in table:
        print(row)

    for i in range(len(table)):
        tmpL.append(math.prod(table[i]) ** (1 / len(table[i])))

    s = sum(tmpL)
    for i in range(len(tmpL)):
        tmpL[i] = tmpL[i] / s
        Wnorm.append(round(tmpL[i], 5))

    print("Wнорм: ", Wnorm)
    print("")

    return tmpL

#Знаходження нормованого вектора
def procCrit1(table_in_file):
    table = list()
    tmpL = list()
    Wnorm = list()

    for l in table_in_file:
        table.append([float(i) for i in l.split()])

    for i in range(len(table)):
        tmpL.append(math.prod(table[i]) ** (1 / len(table[i])))

    s = sum(tmpL)
    for i in range(len(tmpL)):
        tmpL[i] = tmpL[i] / s
        Wnorm.append(round(tmpL[i], 5))

    return tmpL

#Обчислення пріоритетів та вектора
def procAveGrade(table1, table2, table3):
    TableK0 = [table1, table2, table3]
    TableK = list()
    resultK = list()

    for i in range(len(TableK0)):
        row = [round(value, 4) for value in TableK0[i]]
        TableK.append(row)

    for row in TableK:
        print(row)

    for i in range(len(table1)):
        value1 = table1[i]
        value2 = table2[i]
        value3 = table3[i]

        Wi = (value1 * value2 * value3) ** (1/4)
        Wi = round(Wi, 5)

        resultK.append(Wi)

    print("Wi: ", resultK)

    return resultK

#Найбільших значень серед нормованого вектора альтернатив
def MaxVectorA(tableA1, tableA2, tableA3):
    MaxQA = list()

    num_elements = len(tableA1)

    for i in range(num_elements):
        # Отримуємо значення з кожного масиву за поточним індексом
        value1 = tableA1[i]
        value2 = tableA2[i]
        value3 = tableA3[i]

        # Знаходимо максимальне значення серед трьох
        max_value = max(value1, value2, value3)

        # Додаємо максимальне значення до списку MaxQA
        MaxQA.append(max_value)
    print(MaxQA)

    return MaxQA


#Пошук глобальних пріоритетів
def CalGlobalPriorities(TableK, MaxQA1, MaxQA2, MaxQA3, MaxQA4):
    CP = list()

    for i in range(len(TableK)):
        value = (
            TableK[0] * MaxQA1[i] +
            TableK[1] * MaxQA2[i] +
            TableK[2] * MaxQA3[i] +
            TableK[3] * MaxQA4[i]
        )
        CP.append(value)

    # Знаходимо максимальне значення серед результатів
    max_value = max(CP)
    print("Max: " , max_value , " in A" , CP.index(max(CP)) + 1)
    
