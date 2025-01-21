#The power of radiation, or radiative power, can be calculated using the Stefan-Boltzmann law, which is given by:
# P = σAT^4
# where:
# P = power of radiation
# σ = Stefan-Boltzmann constant = 5.67 x 10^-8 W/m^2K^4
# A = surface area of the object
# T = temperature of the object in Kelvin
# Inputs: surface_area, temperature
# Outputs: power_of_radiation
#********************************************************************************************************************

print("This program calculates the power of radiation using the Stefan-Boltzmann law")
print("Enter the following values")
#inputs assigned to variables
surface_area = float(input("Enter surface area in m^2 : "))
temperature = float(input("Enter temperature in Kelvin : "))
# Validate inputs
while temperature == 0:
    print("Temperature cannot be zero")
    temperature = float(input("Enter temperature: "))
while surface_area == 0:
    print("Surface area cannot be zero")
    surface_area = float(input("Enter surface area: "))
# Calculate power of radiation
def power_of_radiation (surface_area, temperature):
    return 5.67 * 10**-8 * surface_area * temperature ** 4
#printing outputs
print(f"Surface area: {surface_area} m^2")
print(f"Temperature: {temperature} K")
print(f"Power of radiation: {power_of_radiation(surface_area, temperature)} W/m^2")

