#function to gather patient information
def patient_info():
    #individual's name
    name = input("Enter patient name: ")

    #age of individual in years
    age = int(input("Enter age of individual in years: "))

    #0 for female, 1 for male
    sex = int(input("Enter gender of individual; 0 for female, 1 for male: "))

    #individual's body mass index
    bmi = float(input("Enter individual's body mass index: "))

    #number of children individual has
    children = int(input("Enter number of children of individual: "))

    #0 for non-smoker, 1 for smoker
    smoker = int(input("Is the individual a smoker? 0 for no, 1 for yes: "))

    #return values
    return name, age, sex, bmi, children, smoker

#function to calculate cost of individual's insurance
def calculate_cost(age, sex, bmi, children, smoker):
    cost = 250 * age - 128 * sex + 370 * bmi + 425 * children + 24000 * smoker - 12500
    return cost

#calculate the effect age has on the cost of medical insurance
def adjust_age(cost, name, age, sex, bmi, children, smoker, adjustment):
    #the individual won't be getting any younger
    if adjustment <= 0:
        print("Adjustment must be a positive number.")
        return

    #adjust age
    age += adjustment

    #calculate new cost
    new_cost = calculate_cost(age, sex, bmi, children, smoker)

    #find the difference between new cost and old cost
    cost_change = round(new_cost - cost, 2)

    #print message giving information on how much the insurance cost changed
    print(f"In {adjustment} years {name}'s medical insurance cost will have increased by ${str(cost_change)}0.")


#calculate the effect bmi has on the cost of medical insurance
def adjust_bmi(cost, name, age, sex, bmi, children, smoker, adjustment):
    #check whether bmi is being increased or decreased and return string for output
    adjust_str = "increased" if adjustment >= 0 else "decreased"

    #adjust bmi
    bmi += adjustment

    #calculate new cost
    new_cost = calculate_cost(age, sex, bmi, children, smoker)

    #find the difference between new cost and old cost
    cost_change = new_cost - cost

    #check to see if the difference was positive or negative, if negative the cost decreased, if positive it increased
    change_str = "increased" if cost_change >= 0 else "decreased"

    #print message giving user info on how much the insurance cost changed
    print(f"If {name}'s BMI is {adjust_str} by {adjustment}, medical insurance cost will be {change_str} by ${str(abs(cost_change))}0.")

#calculate the effect sex has on the cost of medical insurance
def adjust_sex(cost, name, age, sex, bmi, children, smoker):
    #change the sex from male to female or female to male (1 - 1 = 0, 1 - 0 = 1)
    sex = 1 - sex

    #determine whether sex after change is male or female and create string for output
    sex_str = "male" if sex == 1 else "female"

    #calculate new cost
    new_cost = calculate_cost(age, sex, bmi, children, smoker)

    #find the difference between new cost and old cost
    cost_change = new_cost - cost

    #check to see if the difference was positive or negative, if negative the cost decreased, if positive it increased
    change_str = "increased" if cost_change >= 0 else "decreased"

    #print message giving user info on how much the insurance cost changed
    print(f"If {name}'s sex was {sex_str}, medical insurance cost would be {change_str} by ${str(abs(cost_change))}0.")

#calculate the effect smoking status has on the cost of medical insurance
def adjust_smoker(cost, name, age, sex, bmi, children, smoker):
    #change smoking status from smoker to non-smoker or vice versa (1 - 1 = 0, 1 - 0 = 1)
    smoker = 1 - smoker

    #calculate new cost
    new_cost = calculate_cost(age, sex, bmi, children, smoker)

    #find the difference between new cost and old cost
    cost_change = new_cost - cost

    #check to see if the difference was positive or negative, if negative the cost decreased, if positive it increased
    change_str = "increased" if cost_change >= 0 else "decreased"

    #adjust output message based on how smoking status changed, then print message
    if smoker == 1:
        print(f"If {name} picks up smoking, medical insurance cost will be {change_str} by ${str(abs(cost_change))}0.")
    else:
        print(f"If {name} stops smoking, medical insurance cost will be {change_str} by ${str(abs(cost_change))}0.")

#calculate the effect number of children has on the cost of medical insurance
def adjust_children(cost, name, age, sex, bmi, children, smoker, adjustment):

    #you hopefully aren't going to be losing children
    if adjustment >=0:
        print("Adjustment must be a positive number.")
        return
    
    #adjust number of children individual has
    children += adjustment

    #calculate new cost
    new_cost = calculate_cost(age, sex, bmi, children, smoker)

    #find the difference between new cost and old cost
    cost_change = new_cost - cost

    #check to see if the difference was positive or negative, if negative the cost decreased, if positive it increased
    change_str = "increased" if cost_change >= 0 else "decreased"

    #print message giving user info on how much the insurance cost changed
    print(f"If {name} were to have {children} more children, insurance cost would be {change_str} by ${str(abs(cost_change))}0.")


def main():
    #gather patient info
    name, age, sex, bmi, children, smoker = patient_info()

    #calculate cost of insurance
    cost = calculate_cost(age, sex, bmi, children, smoker)
    
    #print the cost of the individual's insurance
    print(f"\n {name}'s insurance cost is estimated to be ${str(cost)}0. \n")

    #give user the option to test different insurance factors
    choices = input("Would you like to adjust insurance factors to see how they affect the overall cost of your insurance and see how much it could change if you make different lifestyle adjustments? Enter yes or no.")
    choices = True if choices == "yes" else False

    #start a while loop to run while user is testing factors
    while choices:
        #ask user which factor they wish to adjust
        choice = int(input("Which factor would you like to adjust? Enter number 1-5 \n 1. age \n 2. sex \n 3. bmi \n 4. number of children \n 5. smoking status \n"))

        #call functions based on user input
        if choice == 1:
            adjustment = int(input(f"By how many years would you like to adjust {name}'s age?"))
            adjust_age(cost, name, age, sex, bmi, children, smoker, adjustment)
        elif choice == 2:
            adjust_sex(cost, name, age, sex, bmi, smoker, children)
        elif choice == 3:
            adjustment = float(input(f"By how much do you wish to adjust {name}'s BMI?"))
            adjust_bmi(cost, name, age, sex, bmi, children, smoker, adjustment)
        elif choice == 4:
            adjustment = int(input(f"By how many more children do you wish to adjust {name} to have?"))
            adjust_children(cost, name, age, sex, bmi, smoker, children, adjustment)
        elif choice == 5:
            adjust_smoker(cost, name, age, sex, bmi, smoker, children)
        else:
            print("Invalid input.")

        #ask user if they wish to test another factor
        choices = input("Would you like to adjust by another factor? Enter yes or no.")
        choices = True if choices == "yes" else False
    
    #print a thank you message
    print("Thank you for using my calculator!")

if __name__ == "__main__":
    main()