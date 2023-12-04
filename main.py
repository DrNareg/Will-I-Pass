category_weights = {"Attendance":[10,100], "Homework":[70,100], "Final":[20,0]}
symbol = "%"

# Just a simple intro to the program
def intro():
    print("So you're here to check how screwed you are. lol")
    print("Just a few notes:\nNo need for " + symbol+ " sign \nEnter 0 (weight) for any un-needed categories\n")

# Function to collect important data for the dictionary
def collect_data():

    # Loop through and update the dictionary with weights
    for category in category_weights:
        
        # get weight
        weight = input(f"Enter weight for " + category + ': ')
        # check if input includes %
        while symbol in weight:
            print("Bruh, I said no %")
            weight = input(f"Enter weight for " + category + ': ')   

        # Get grade
        grade = input(f"Enter current grade for " + category + ': ')
        # check if input includes %
        while symbol in grade:
            print("Bruh, I said no %")
            grade = input(f"Enter grade for " + category + ': ')
        
        # Update the dictionary values
        category_weights[category][0] = weight
        category_weights[category][1] = grade

    #print(category_weights)

def the_math():
    goal = input("What is your target grade?(ex:100) ")
    # check if input includes %
    while symbol in goal:
        print("No more % \signs!")
        goal = input("Enter your target grade(ex:100) ")
    #float_goal = float(goal)

    # The math part:
    Att = int(category_weights["Attendance"][0]) * int(category_weights["Attendance"][1]) *.01
    HW = int(category_weights["Homework"][0]) * int(category_weights["Homework"][1]) *.01
    Final_weight = int(category_weights["Final"][0])
    x = (float(goal)-(Att+HW))/(Final_weight*.01)
    # Rounding
    str_x = str(round(x, 2))
    print(f"To get an overall grade of " + goal + "you will need " + str_x + " on the final!")
    
intro()
collect_data()
the_math()