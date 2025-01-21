# velocity = displacement / time
# acceleration = velocity / time
# Inputs: displacement, time
print("This program calculates velocity and acceleration")
print("Enter the following values")
displacement = float(input("Enter displacement in meter : "))
time = float(input("Enter time in sec : "))
# Validate inputs
while time == 0:
    print("Time cannot be zero")
    time = float(input("Enter time: "))

while displacement == 0:
    print("Displacement cannot be zero")
    displacement = float(input("Enter displacement: "))

# Calculate velocity
def velocity (dispalcement, time):
    return dispalcement / time
# Calculate acceleration
def acceleration (velocity, time):
    return velocity / time
#printing outputs
print(f"Displacement: {displacement} m")
print(f"Time: {time} s")
print(f"Velocity: {velocity(displacement, time)} m/s")
print(f"Acceleration: {acceleration(velocity(displacement, time), time)} m/s^2")

# Output