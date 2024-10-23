# Task 1: Ask the user to enter the temperature in Fahrenheit
fahrenheit_input = input("Enter the temperature in Fahrenheit: ")

# Task 2: Function for converting Fahrenheit to Celsius with error handling
def fahrenheit_to_celsius(fahrenheit):
    try:
        # Attempt to convert input to float and calculate Celsius
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
    except ValueError:
        # Handle the case where the input is not a valid number
        print("Error: Please enter a valid numeric value for the temperature.")
    else:
        # Task 3: If no exception, print the converted temperature in a user-friendly format
        print(f"{fahrenheit:.2f} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        # Task 4: Print a thank-you message regardless of the outcome
        print("Thank you for using the weather forecast application.")
      
fahrenheit_to_celsius(fahrenheit_input)
