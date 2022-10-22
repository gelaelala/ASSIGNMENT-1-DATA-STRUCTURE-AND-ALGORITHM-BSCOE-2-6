# Assignment 1
#     - create a program that will print your nickname using only asterisk character (*)

from colorama import Fore, Back, Style 

G = [[" " for row in range (6)] for column in range (6)]

for g_row in range (6):
    for g_column in range (6):
        if (g_row == 0 and g_column != 0) or ((g_column == 0 and g_row != 0 and g_row != 5)) or ((g_row ==5 and g_column != 0 and g_column != 5)) or ((g_row == 3 or g_row == 4) and g_column == 5) or (g_row == 3 and g_column != 0 and g_column != 1):
            G [g_row][g_column]= "*"

for row in range (6):
    for column in range (6):
        print (Fore.BLUE + G [row][column], end = "  ")
    print (" ")