# Assignment 1
#     - create a program that will print your nickname using only asterisk character (*)

from colorama import Fore, Back, Style 

G = [[" " for row in range (5)] for column in range (5)]
E = [[" " for row in range (5)] for column in range (4)]
L = [[" " for row in range (5)] for column in range (4)]
A = [[" " for row in range (5)] for column in range (5)]

for g_row in range (5):
    for g_column in range (5):
        if (g_row == 0 and g_column != 0) or ((g_row != 0 and g_row != 4) and g_column == 0) or (g_row == 4 and (g_column != 0 and g_column != 4)) or ((g_row == 2 or g_row == 3) and g_column == 4) or (g_row == 2 and g_column != 0 and g_column != 1):
            G [g_column][g_row]= "*"

for e_row in range (5):
    for e_column in range (4):
        if e_row == 0 or e_row == 2 or e_row == 4 or ((e_row == 1 or e_row ==3) and e_column == 0):
            E [e_column][e_row] = "*"

for l_row in range (5):
    for l_column in range (4):
        if l_column == 0 or l_row == 4:
            L [l_column][l_row] = "*"

for a_row in range (5):
    for a_column in range (5):
        if a_row == 2 or (a_row == 0 and (a_column == 1 or a_column == 2 or a_column == 3)) or ((a_row == 1 or a_row == 3 or a_row == 4) and (a_column == 0 or a_column == 4)):
            A [a_column][a_row] = "*"

for row in range (5):
    for column in range (5):
        print (G [column][row], end = " ")
    print (end = "   ")
    for column in range (4):
        print (E [column][row], end = " ")
    print (end = "   ")
    for column in range (4):
        print (L [column][row], end = " ")
    print (end = "   ")
    for column in range (5):
        print (A [column][row], end = " ")
    print ()