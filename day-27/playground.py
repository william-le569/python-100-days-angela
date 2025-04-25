# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(1, 3, 5, 8))

# Learn about keyword arguments

# class Car:
#     def __init__(self, **st):
#         self.make = st["make"]
#         self.model = st["model"]

# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)

# To observe behaviour of END, 0
from tkinter import *

window = Tk()

entry = Entry(width=30)
entry.pack()

entry.insert(END, "Hello")
entry.insert(0, "Start: ")
entry.insert(END, " World!")  # Kết quả: "Start: Hello World!"

window.mainloop()