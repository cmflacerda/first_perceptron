from perceptron import initialization as init
from prettytable import PrettyTable as pt 

print('\n' + "---------- University of Sao Paulo ----------" + '\n' + "---- Neural Network and Machine Learning ----")
print("-------------- SEM5952/2021 --------------" + '\n\n')
print("What letter do you want to use for training the perceptron?" + '\n' + "Letters from A to X available" + '\n')

mytable = pt(["Letters", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                 "V", "W", "X"])
mytable.add_row(["Index", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                 "20", "21", "22", "23"])

print(mytable)
print("")

letter = int(input("Index: "))

w_final, y_final = init(letter)
print('\n' + "Final weights:")
print(w_final.T)
print('\n' + "Final outputs of the perceptron:")
print(y_final)