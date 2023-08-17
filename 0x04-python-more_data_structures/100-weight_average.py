#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    dominateur = 0
    summ = 0
    for i in range(0, len(my_list)):
        summ += my_list[i][2] * my_list[i][1]
        dominateur += my_list[i][2]
    return (summ / dominateur)
