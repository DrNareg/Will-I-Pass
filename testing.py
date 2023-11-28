category_weights = {"Attendance":[0,0], "Homework":[0,0]}
#index 0 for weight then 1 for grade
#print(grades['pp'][0])
symbol = "%"
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

        while symbol in grade:
            print("Bruh, I said no %")
            grade = input(f"Enter grade for " + category + ': ')
        
        # Update the dictionary values
        category_weights[category][0] = weight
        category_weights[category][1] = grade

    print(category_weights)

collect_data()