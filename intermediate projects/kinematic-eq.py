# kinematic equation calculation for physics
#v = u + at
#s = ut + 0.5 * a * t^2
#v^2 = u^2 + 2as
#inputs : u, a, t
#outputs : v, s,t
# u = initial velocity
# v = final velocity
# a = acceleration
# t = time
# s = displacement
# Inputs: initial_velocity, acceleration, time

#********************************************************************************************************************
print("This program calculates velocity and displacement using kinematic equations")
print("Enter the following values")
#inputs assigned to variables
initial_velocity = float(input("Enter initial velocity in m/s : "))
acceleration = float(input("Enter acceleration in m/s^2 : "))
time = float(input("Enter time in sec : "))
# Validate inputs
while time == 0:
    print("Time cannot be zero")
    time = float(input("Enter time: "))
while initial_velocity == 0:
    print("Initial velocity cannot be zero")
    initial_velocity = float(input("Enter initial velocity: "))
while acceleration == 0:
    print("Acceleration cannot be zero")
    acceleration = float(input("Enter acceleration: "))
# Calculate final velocity
def final_velocity (initial_velocity, acceleration, time):
    return initial_velocity + (acceleration * time)
# Calculate displacement
def displacement (initial_velocity, acceleration, time):
    return (initial_velocity * time) + (0.5 * acceleration * time ** 2)
#printing outputs
print(f"Initial velocity: {initial_velocity} m/s")
print(f"Acceleration: {acceleration} m/s^2")
print(f"Time: {time} s")
print(f"Final velocity: {final_velocity(initial_velocity, acceleration, time)} m/s")
print(f"Displacement: {displacement(initial_velocity, acceleration, time)} m")
# Output
