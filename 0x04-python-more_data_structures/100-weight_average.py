#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        dominateur = 0
        summ = 0
        for k in my_list:
            summ += k[0] * k[1]
            dominateur += k[1]
        return (summ / dominateur)
