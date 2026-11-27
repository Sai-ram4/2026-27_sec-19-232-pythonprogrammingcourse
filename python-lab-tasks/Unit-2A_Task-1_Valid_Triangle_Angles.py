# Unit 2A Task 1 - check if a triangle is valid using its three angles

angle1_in_degrees = float(input("Enter first angle in degrees: "))
angle2_in_degrees = float(input("Enter second angle in degrees: "))
angle3_in_degrees = float(input("Enter third angle in degrees: "))

# every angle must be more than 0 and all three must add up to 180
if angle1_in_degrees > 0 and angle2_in_degrees > 0 and angle3_in_degrees > 0 and angle1_in_degrees + angle2_in_degrees + angle3_in_degrees == 180:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is valid")
else:
    print(f"The triangle with angles {angle1_in_degrees}, {angle2_in_degrees}, and {angle3_in_degrees} is not valid")
