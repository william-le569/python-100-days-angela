import functools
import string
import turtle
 
 
def key_handler(key):
    print(key)
 
 
for letter in string.ascii_letters:
    turtle.onkey(functools.partial(key_handler, letter), letter)
 
window = turtle.Screen()
window.listen()
window.mainloop()