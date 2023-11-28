category_weights = {"Attendance":0, "Homework":0, "Midterm_1":0, "Midterm_2":0, "Final":0}
category_grades = {"Attendance":0, "Homework":0, "Midterm_1":0, "Midterm_2":0, "Final":0}
symbol = "%"

# Just a simple intro to the program
def intro():
    print("So you're here to check how screwed you are. lol")
    print("Just a few notes:\nNo need for " + symbol+ " sign \nEnter 0 for any un-needed categories\n")

def collect_weights():

    # Loop through and update the dictionary
    for category in category_weights:
        # get input
        weight = input(f"Enter weight for " + category + ': ')

        # check if input includes %
        while symbol in weight:
            print("Bruh, I said no %")
            weight = input(f"Enter weight for " + category + ': ')
        
        # Update the dictionary values
        category_weights[category] = weight

    print(category_weights)

def collect_grades():
    print()

intro()
#collect_weights()