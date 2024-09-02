#Assignment
#Create a function
#Create a function Convert meters to cm
#Create a function convert inches to mm
#Create a function convert feet to meters
#Create a function convert meters to kilometers
#Create a function convert kilometers to miles
#Then create a program -- create an option based on the function that you created
#the calculation will happen on the body of the function
#just return the converted values


def unit_converter():
    print('Choose the number of desired conversion: ')
    print('1. Meters to Centimeters / cm')
    print('2. Inches to Millimeter / mm')
    print('3. Feet to Meters')
    print('4. Meters to Kilometers / km')
    print('5. Kilometers to Miles')
    unit_value = float(input('Enter value to convert: '))
    chosen_conversion = input('Enter the conversion of your choice: ')
    if chosen_conversion == str(1):
        return str(unit_value) + ' meters -> ' + str(unit_value * 100) + ' centimeters'
    elif chosen_conversion == str(2):
        return str(unit_value) + ' inches -> ' + str(unit_value * 25.4) + ' milimeters'
    elif chosen_conversion == str(3):
        return str(unit_value) + ' feet -> ' + str(unit_value * 0.3048) + ' meters'
    elif chosen_conversion == str(4):
        return str(unit_value) + ' meters -> ' + str(unit_value / 1000) + ' kilometers'
    elif chosen_conversion == str(5):
        return str(unit_value) + ' kilometers -> ' + str(unit_value / 1.609) + ' miles'
    else:
        return 'Unsupported conversion. Please choose from 1 to 5 and try again.'

unit_converter()