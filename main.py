# Name        : Mandelbrot Set Fractals Assignment
# Programmer  : Anbuselvan Ragunathan
# Date        : May 9, 2022
# Description : The program will plot the Mandelbrot set and display it
#               on an 800x800 tkinter window.

### PROGRAM START ###

# Importing tkinter library and ComplexNumbers class from complex_class.py
import tkinter
from complex_class import *

# Initializing the 800x800 tkinter window 
window = tkinter.Tk()
window.geometry("800x800")
canvas = tkinter.Canvas(window, height = 800, width = 800)

# Function to convert the pixel points to coordinates 
def convert_points(x_coord, y_coord):
    # Setting initial x and y coordinates based on length and width of the tkinter window
    inital_x_coord = 800 / 2
    initial_y_coord = 800 / 2
    # Calculating the scale factor for the x and y coordinates
    scaled_x_coord = (800/(2*scaled_height))
    scaled_y_coord = (800/(2*scaled_width))
    # Determining the coordinates that will be plottted onto the tkinter window
    final_x_coord = (x_coord - inital_x_coord) / scaled_x_coord
    final_y_coord = (y_coord - initial_y_coord) / scaled_y_coord
    # Returning the coordinates that will be plotted onto the tkinter window
    return final_x_coord, final_y_coord
# Setting scale values for the width and height (x and y)
scaled_width = 2
scaled_height = 2

# Setting up the output for colour to be portrayed depeding on if the point is a part of the Mandelbrot set or not
img = tkinter.PhotoImage(width = 800, height = 800)
canvas.create_image((800/2, 800/2), image=img, state = "normal")

# Looping through the x (represented by i) and y (represented by j) pixel coordinates
for i in range(800):
    for j in range(800):
        # Scoping the x and y pixel coordiates to the convert_points function 
        x,y = convert_points(i,j)
        # Accounting for the complex numbers so that they can be plotted as well
        current_number = ComplexNumbers(0,0)
        # Boolean value to satisfy or unsatisfy in order to carry out the while loop and to sure that the while loop does not go on forever
        limit = False
        # Counter variable to ensure that the while loop does not go on forever
        k = 0
        # While loop to plot the points 
        while (k < 60 and limit == False):
            # Increasing the counter variable by 1 each time
            k += 1
            # Calculating the real and imaginary numbers using the respective formula 
            current_number = current_number.multiply_numbers(current_number)
            # The Mandelbrot set has a "radius" or a limit length of 2
            # Thus when either the real or imaginary number value exceeds 2, the while loop ends
            # The remaining non-Mandelbrot set points are put as black
            if (current_number.imaginary_number > 2 or current_number.real_number > 2):
                img.put("black", (i, j))
                limit = True
            # Otherwise, as long as the values of the real and imaginary numbers is under 2
            # The Mandelbrot set points are put as white
            else:
                # Calculating the real and imaginary numbers using the respective formula 
                current_number = current_number.adding_numbers(ComplexNumbers(x,y))
                img.put("white", (i, j))
    # Prining the iteration of the x value coordinate for the purpose of the user to see the progress of the program
    print (i)
# Displaying a message to the user once the Mandelbrot set is ready to be displayed
print ("Presenting the Mandelbrot set!")
# Updating and running the tkinter window
canvas.pack()
window.mainloop()

### PROGRAM END ###
