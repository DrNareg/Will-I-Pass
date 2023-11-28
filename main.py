category_weights = {"Attendance":[20,100], "Homework":[50,100], "Final":[30,0]}
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
    goal = float(input("What is your target grade?(ex:100) "))
    Att = category_weights["Attendance"][0] * category_weights["Attendance"][1] *.01
    HW = category_weights["Homework"][0] * category_weights["Homework"][1] *.01
    Final_weight = category_weights["Final"][0]
    x = (goal-(Att+HW))/(Final_weight*.01)
    print(x)
    

the_math()
#collect_data()