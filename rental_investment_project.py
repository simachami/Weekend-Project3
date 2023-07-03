class RealEstateApp:
    #Member Variables - These can be accessed in any class method
    main_menu = "" #Variable we can user every time we need to print the main menu

    #Constructor to Initialize the class
    def __init__(self):
        #Multi Line String for easier Readability
        #The indentation below will ident the same output. So we move string all the way left in code so it outputs all the way left
        self.main_menu = '''
---------------Main Menu-----------------
[1] - Calculate Return on Investment
[2] - Annual Cash Flow
[3] - Calculate Cash on Cash 
[Q] - Quit Application

'''
    #  --Methods-- 

    #-Driver Methods-s
    def driver(self):
        #Main program loop. Program ends when this loop breaks
        while True:
            #Will keep looping for user input until they choose a valid menu option
            user_choice_main_menu = self.main_menu_driver()
 
            #First Check if user wants to quit
            if user_choice_main_menu in ['q', 'quit']:
                print("\nExiting application. . .")
                break

            if user_choice_main_menu == "1":
                #Calculate roi
                returned_roi = self.roi_driver()
                #Format calculated value as a percentage
                formatted_roi = '{:.1%}'.format(returned_roi[1])
                if returned_roi[0] == True:
                    print(f'\nCalculated return: {formatted_roi}')
                elif returned_roi[0] == False:
                    print("\nExiting application. . .")
                    break

            elif user_choice_main_menu == "2":
                #Calculate Annual Cash Flow
                returned_cash_flow = self.annual_cash_flow_driver()
                if returned_cash_flow[0] == True:
                    print(f' Your Annual Cash Flow is : {returned_cash_flow[1]}')
                elif returned_cash_flow[0] == False:
                    print("\nExiting application. . .")
                    break

            elif user_choice_main_menu == "3":
                returned_cash_on_cash = self.cash_on_cash_driver()
                formatted_cash_on_cash = '{:.12%}'.format(returned_cash_on_cash[1])
                if returned_cash_on_cash[0] == True:
                    print(f'\nYour Cash on Cash is: {formatted_cash_on_cash}')
                elif returned_cash_on_cash[0] == False:
                    print("\n Exiting application. . .")
                    break
            else:
                print("Invalid Menu Option. Please Enter a Valid Option\n")


    def main_menu_driver(self):
        #Print Main Options List
        #Ask user to make a choice
        while True:
            user_choice_main_menu = self.get_user_input_string(self.main_menu)
            if user_choice_main_menu in ['1', '2', '3', 'q', 'quit']:
                return user_choice_main_menu
            else:
                print("\n****Invalid Input. Please Select a Valid Option****\n")

           

    def roi_driver(self):
        print("\t\t--Return On Investment-- \nROI = (Investment Gain − Investment Cost) ÷ Investment Cost)")
        #Get user input. If valid, run calculation and print result
        while True:
            #Returns a tuple of (True, float) if the input was successfully converted to a float
            #Else returns (False, -1) if the user tries to quit using the current calculation method
            gain_input = self.get_user_input_float("Please enter the expected investment gain: ")
            cost_input = self.get_user_input_float("Please enter the expected investment cost: ")
            if gain_input[0] == True and cost_input[0] == True:
                #Returns calculated float value to whoever called roi_driver()
                return (True, self.roi_calculation(gain_input[1], cost_input[1]))
            #If user wants to quit during the input phase
            elif gain_input[0] == False and gain_input[1] == -1:
                print("Returning to main menu. . .")
                return (False, -1)
            elif cost_input[0] == False and cost_input[1] == -1:
                print("Returning to main menu. . .")
                return (False, -1)


    def annual_cash_flow_driver(self):
        print("--Annual Cash Flow: Monthly Cash Flow * 12")
        #Get user input. If valid, run calculation and print result
        #while True:
        #Returns a tuple of (True, float) if the input was successfully converted to a float
        #Else returns (False, -1) if the user tries to quit using the current calculation method
        cash_flow = self.get_user_input_float("What is Your Monthly Cash Flow: ")
        if cash_flow[0] == True:
            #Returns calculated float value to whoever called roi_driver()
            return (True, self.annual_cash_flow_calculation(cash_flow[1]))
        #If user wants to quit during the input phase
        elif cash_flow[0] == False and cash_flow[1] == -1:
            print("Returning to main menu. . .")
            return (False, -1)

    def cash_on_cash_driver(self):
        print("--Cash on Cash ROI: Annual Cash Flow / Total Investment")
        #Get user input. If valid, run calculation and print result
        #while True:
        #Returns a tuple of (True, float) if the input was successfully converted to a float
        #Else returns (False, -1) if the user tries to quit using the current calculation method
        annual_cash_flow_input = self.get_user_input_float("What is your Annual Cash Flow: ")
        total_investment_input = self.get_user_input_float("What is the total investment: ")
        if annual_cash_flow_input[0] == True and total_investment_input[0] == True:
            #Returns calculated float value to whoever called roi_driver()
            return (True,self.cash_on_cash_calculation(annual_cash_flow_input[1], total_investment_input[1]))
            #If user wants to quit during the input phase
        elif annual_cash_flow_input[0] == False and annual_cash_flow_input[1] == -1:
            print("Returning to main menu. . .")
            return (False, -1)
        elif total_investment_input[0] == False and total_investment_input[1] == -1:
            print("Returning to main menu. . .")
            return (False, -1)
            

    #-Input Methods-
    #Takes in a string to be the message to print to user, returns the user input as a string
    def get_user_input_string(self, message_to_user : str) -> str:
        user_input_string = input(message_to_user).lower()
        return user_input_string

    #Takes in a string to be the message to print to user, returns the user input as a float
    def get_user_input_float(self, message_to_user : str):
        while True:
            #Get Input from user
            user_input_float = input(message_to_user)
            if user_input_float.lower() in ['q', 'quit']:
                #If user wants to quit, return false and -1. In the main loop we will check these and quit if we find False and -1
                return (False, -1)
            
            #Validate the input. Make sure it converts to a float
            result_tuple = self.validate_float(user_input_float)
            #Returned value is a tuple, with the first value being the boolean and the second being the float value as a float
            if(result_tuple[0] == True):
                #Returns to where the function was called. Same as breaking out of the loop but also sends a value
                return result_tuple
            else:
                print(f'Error - Invalid Input: {result_tuple[1]} is not a number')
    
    #-Calculation Methods-
    #Return on Investment Calculation calculates the roi and returns it as a float
    def roi_calculation(self, investment_gain : float, investment_cost: float) -> float:
    #ROI = (Investment Gain − Investment Cost) ÷ Investment Cost
        roi = (investment_gain - investment_cost) / investment_cost
        return roi

    def annual_cash_flow_calculation(self, monthly_cash_flow: float) -> float:
        #Annual cash flow  -> monthly cash flow * 12 
        return monthly_cash_flow * 12
    
    def cash_on_cash_calculation(self, annual_cash_flow, total_investment: float) -> float: 
        #cash on cash roi -> annual cash flow / total investment
        return annual_cash_flow / total_investment


    #-Data Validation Methods
    #Gets user input string and tries to convert it to a float.
    #If success, return True and the value
    #If fail, return False and 0
    def validate_float(self, float_to_validate: str):
        temp_float = 0
        try:
            temp_float = float(float_to_validate)
            return (True, temp_float)
        except ValueError:
            return (False, float_to_validate)
        
        """ if (float(float_to_validate)):
            temp_float = float(float_to_validate)
            return (True, temp_float)
        else:
            return (False, 0) """

#Create Object and Call driver()
realEstateObject = RealEstateApp()
realEstateObject.driver()