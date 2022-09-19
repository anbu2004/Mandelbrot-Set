# Name        : Complex Numbers Class
# Programmer  : Anbuselvan Ragunathan
# Date        : May 9, 2022
# Description : ComplexNumbers class for the Anbu_fractal program.

### PROGRAM START ###

# Structuring the ComplexNumbers class
class ComplexNumbers():
    # Initializing the real and imaginary numbers
    def __init__(self, real_number = 0, imaginary_number = 0):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def adding_numbers(self, second_number):
        # Adding the real and imaginary numbers and returning it to the Anbu_fractal program
        # This is used when a point is found in the Mandelbrot set
        real_number = self.real_number + second_number.real_number
        imaginary_number = self.imaginary_number + second_number.imaginary_number
        # Returning the real and imaginary numbers
        return ComplexNumbers(real_number, imaginary_number)

    def multiply_numbers(self, second_number):
        # Multiplying the real and imaginary numbers and returning it to the Anbu_fractal program
        # This is used as a check until the value of the real or imaginary number exceeds 2
        real_number = (self.real_number * second_number.real_number) - (self.imaginary_number * second_number.imaginary_number)
        imaginary_number = (self.imaginary_number * second_number.real_number) + (self.real_number * second_number.imaginary_number)
        # Returning the real and imaginary numbers
        return ComplexNumbers(real_number, imaginary_number)

    def show_nums(self):
        return real_number, imaginary_number

### PROGRAM END ### 
