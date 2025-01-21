#(0°C × 9/5) + 32 = 32°F
#(0°F − 32) × 5/9 = -17.78°C
print("Unit Conversion")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
choice = int(input("Enter your choice: "))
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
if choice == 1:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius: ", fahrenheit_to_celsius(fahrenheit))
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit: ", celsius_to_fahrenheit(celsius))
else:
    print("Invalid choice")




