#########################################################################################################################################################################################
# For this assignment, you will be formatting data (numbers and strings) and printing the results to the screen. You will need to use formatting strings,                               #
# and you must use the str.format() method (see documentation and chart below). You will also need to print multiple items to a line.                                                   #
#                                                                                                                                                                                       #
# The Problem/Challenge                                                                                                                                                                 #
#                                                                                                                                                                                       #
# You are writing a program for a gas station, and one of the things they need is to be able to print out a receipt when someone fills up their car with gas.                           #
# Your task is to write a program that will print a receipt to the screen. (*Note, your program does not need to do the math since we have not covered this yet in class,               #
# but it does need to format the output. See the helpful information section of this page for help with the formatting.)                                                                #
#                                                                                                                                                                                       #
# Your receipt should show the following information:                                                                                                                                   #
# Display the station name and location                                                                                                                                                 #
# Date of the receipt is being issued/given                                                                                                                                             #
# Type of Gas                                                                                                                                                                           #
# Number of Gallons of Gas (a number that is displayed to three decimal places)                                                                                                         #
# Cost per gallon (this should be a number that is formatted as US currency)                                                                                                            #
# Total Cost (this should be a number that is formatted as US currency)                                                                                                                 #
#                                                                                                                                                                                       #
# Your receipt program must:                                                                                                                                                            #
# Use at least three literals.                                                                                                                                                          #
# Use at least three variables.                                                                                                                                                         #
# The number of gallons, cost per gallon, and total cost should all be displayed on one line.                                                                                           #
# Use the str.format() method to format all of your output.                                                                                                                             #
# Display all required information in a way that is well organized and easy to read.                                                                                                    #
# Be sure to use comments for both structure of the program and documentation of the code.                                                                                              #
#########################################################################################################################################################################################

import tkinter                                                                                          #import the gui module
from msvcrt import getch                                                                                #import the get character function from the msvcrt module
import time                                                                                             #import the time module

gasStationName = 'Koon Station'                                                                         #give your station name a variable
gasStationLocation = '1234 N. Koon Street, Endless, AZ'                                                 #give your station an address
gasCostPerGallon = 0.00                                                                                 #assign cost per gallon a variable of 0
gasType = ' '                                                                                           #assign a variable to type of gas
gasNumberOfGallons = 0.00                                                                               #assign a variable to number of gallons
gasTotalCost = 0.00                                                                                     #assign a variable to total cost (this is cost per gallon * number of gallons
yesNo = ' '                                                                                             #assign a variable to the yes/no questions
date = time.strftime('%d/%m/%Y')                                                                        #assign a variable to date receipt was printed
time = time.strftime('%H:%M:%S')                                                                        #assign a variable to the time receipt was printed

print('Welcome to', gasStationName)                                                                     #print welcome to name of station
yesNo = input('Would you like to pump gas? \n')                                                         #make decision yes/no and store it in the yesNo variable
if(yesNo.casefold().startswith('y')):                                                                   #if decision yes/no is yes then go to next line, remove case sensitivity and only look at first letter of answer
    while True:                                                                                         #this creates a simulated do loop, we do this to be sure it runs at least once
        gasType = input('Please select a type of gas: 87, 89, 93 \n')                                   #assign the variable gastype the value the user defines
        if(gasType=='87'):                                                                              #if gastype variable was 87
            gasCostPerGallon = 1.50                                                                     #assign 1.5 to gas cost per gallon
            print('You selected', gasType)                                                              #let user know they selected this type of gas
            break                                                                                       #break the loop, so some strange bug doesn't happen where it keeps looping
        elif(gasType=='89'):                                                                            #if gastype variable was 89
            gasCostPerGallon = 1.75                                                                     #assign 1.75 to gas cost per gallon
            print('You selected', gasType)                                                              #let user know they selected this type of gas
            break                                                                                       #break the loop, so some strange bug doesn't happen where it keeps looping
        elif(gasType=='93'):                                                                            #if gastype variable was 93
            gasCostPerGallon = 2.00                                                                     #assign 2 to gas cost per gallon
            print('You selected', gasType)                                                              #let user know they selected this type of gas
            break                                                                                       #break the loop, so some strange bug doesn't happen where it keeps looping
        else:                                                                                           #if the value selected for gastype was NOT 87, 89 or 93
            print('Invalid Selection')                                                                  #let user know they didn't pick a valid option
            print('You selected', gasType)                                                              #let user know what they did select and restart the loop. The loop is restarted because there was no
                                                                                                        
                                                                                                        
    while True:                                                                                         #Always true to ensure it is ran at least once
        print('Press Spacebar to Pump Gas.\nPress any other key when finished')                         #let the user know what they are supposed to do next
        char = getch()                                                                                  #store char as a variable assigned by a key that the user selects
        if(char==b' '):                                                                                 #if user selected char is 'spacebar'
            gasNumberOfGallons += .05                                                                   #add .05 to number of gallons
            gasTotalCost = gasNumberOfGallons * gasCostPerGallon                                        #assign total cost of gallons to be number of gallons times cost per gallon
            print('Gallons of gas:', '{:,.3f}'.format(gasNumberOfGallons))                              #tell the user how many gallons they have pumped so far and format that to the thrid decimal place
            print('Cost: ', '${:,.2f}'.format(gasTotalCost))                                            #tell the user how much it cost them and format it to 2 decimal places like the US standard
        elif(char!=b' '):                                                                               #if char selected is anything other than spacebar
            yesNo=input('Are you done pumping gas? \n')                                                 #ask if the user is done pumping gas
            if(yesNo.casefold().startswith('y')):                                                       #if they say yes
                break                                                                                   #break the loop. otherwise let the user continue pumping by restarting the loop and continue adding to the variables
            
    yesNo = input('Would you like a receipt? \n')                                                       #ask user if they want a receipt and save their answer in the yesNo variable
    if(yesNo.casefold().startswith('y')):                                                               #if the user answer yes continue to print their receipt
        print('\t Thank you for shoping at \n\t\t', gasStationName, '\n\t', gasStationLocation, sep='') #print thank you for shoping at gas station name and gas station location
        print(time, '\t\t\t\t', date)                                                                   #Print Date and Time on same line
        print('\n', 'Gallons', '\t\t', 'Cost/Gallon', '\t\t','Totals', sep='')                          #print the words gallons, cost/gallon and totals and remove seperators
        print(('{:,.3f}'.format(gasNumberOfGallons)), '\t\t',                                           #Format and print the number of gallons user pumped then go to next line
              ('${:,.2f}'.format(gasCostPerGallon)), '\t\t\t',                                          #format and print the cost per gallon user chose earlier then go to next line
              ('${:,.2f}'.format(gasTotalCost)))                                                        #format and print the total cost of gas and remove seperators
        input('Press Any Key to Close if not opened in IDLE')                                           #This is here to stop the .exe from closing
        
    else:
        print('Thank You for Shopping at', gasStationName)                                              #if the user doesn't want a receipt, thank them for shopping at your store
