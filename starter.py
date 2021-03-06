# # PROBLEM 1
# # Create a variable that holds the value of your first name.
# first_name = "james"

# # PROBLEM 2
# # Create a variable that holds the value of your favorite number.
# fav_num = 17

# # PROBLEM 3
# # Create a variable that holds a boolean value representing if your hair is brown.
# brown_hair = True

# # PROBLEM 4
# # Print your first name, by printing the variable created in problem 1.
# print(first_name)

# # PROBLEM 5
# #  Create a variable called `loves_code` and set it equal to true. 
# #  Check to see if `loves_code` is equal to true or false. 
# #  If it is true, print "I love to code!"
# #  If it is not, print "Coding has it's challenges."

# loves_code = True

# if loves_code == True:
#     print("I love to code!")
# else:
#     print("Coding has its challenges.")
# # PROBLEM 6
# # Create an array called `colors` and set it equal to a list of at least five colors.
# colors =["red", "blue", "green","black", "yellow"]

# # Problem 7
# # Using bracket syntax, print out the last item in your colors array.
# print(colors[4])

# # For problems 8-9, use the following line of code:
# numbers = [1,2,3,4,5,6,7,8,9,10]

# # Problem 8
# # Use a for-in loop to iterate over the `numbers` array and print each number.
# for x in numbers:
#     print(x)

# # Problem 9
# # Create an empty array called `even_numbers`.
# # Use a for-in loop to iterate over the `numbers` array, and if a number is even, add  it to the `even_numbers` array.
# even_numbers = []

# for x in numbers:
#     if x%2 == 0:
#         even_numbers.append(x)


# print(even_numbers)
# # Problem 10
# # Do not edit the code below.
# score = 74
# # Do not edit the code above.

# # Determine if the letter grade of the given variable 'score'. If the variable is a 90 or above, console-log an 'A', between 80 and 89, console-log a 'B', between 70 and 79, 'C', between 60 and 69, 'D', and anything below 60 should console-log an 'F'.
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("A")
# elif score >= 70:
#     print("A")
# elif score >= 60:
#     print("A")    
# else:
#     print("F")

# # Problem 11
# # Create a variable called 'changeMyMind' and set it equal to true. 
# # Check to see if changeMyMind is set to true or false, if it is true, change the status to false, if it is false, change the status to true.
# change_my_mind = True

# if change_my_mind == True:
#     change_my_mind = False
# else:
#     change_my_mind = True 

# # ADVANCED

# # For problems 12-15, use the following line of code:
# friends = ['Joe', 'Sally', 'Camilo', 'Perry', 'Susan']

# # Problem 12
# # Research to find the Python method that allows you to add an element to the end of the array (similar to push() in javascript), then add a name to the end of the `friends` array.
# friends.append("Billy")

# # Problem 13
# # Print out the total amount of elements in the `friends` array. The Python method you are looking for is similar to the javascript property `.length`.
# print(len(friends))

# # Problem 14
# # Add a name into the third position in the array (index 2). Make sure you are not overwriting the value that is already there.
# friends.insert(2, first_name)
# print(friends)
# # Problem 15
# # Remove the last item in the array (try to think about how you can do this dynamically, meaning, if the array contents were to change, your code would still work).

# del friends[-1]
# print(friends)


file1 = open("CupcakeInvoices.csv")

# for line in file1:
#     print(line)

chocolates = 0
vanillas = 0
strawberries = 0

for line in file1:
    line2 = line.rstrip('\n').split(',')
    for value in line2: 
        if value == "Chocolate":
            chocolates+=((float(line2[3])*float(line2[4])))
        if value == "Vanilla":
            vanillas += (float(line2[3])*float(line2[4]))
        if value == "Strawberry":
            strawberries += (float(line2[3])*float(line2[4]))


chocolates = round(chocolates,2)
vanillas = round(vanillas,2)
strawberries = round(strawberries,2)
# total = 0
# for line in file1:
#     line2 = line.rstrip('\n').split(',')
#     total += (float(line2[3])*float(line2[4]))


# limited_total = round(total,2)
# print(limited_total)
print(chocolates)
print(vanillas)
print(strawberries)
file1.close()

from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import inferno
from bokeh.plotting import figure

output_file("bars.html")

cupcakes = ["Chocolate","Strawberry","Vanilla"]
sales = [chocolates,strawberries,vanillas]

source = ColumnDataSource(data=dict(cupcakes=cupcakes, sales=sales, color=inferno(3)))

p = figure(x_range=cupcakes, y_range=(0,500), title="Cupcake sales",toolbar_location=None,tools="")

p.vbar(x='cupcakes',top='sales',width=0.9,color='color', legend_field="cupcakes", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"

show(p)