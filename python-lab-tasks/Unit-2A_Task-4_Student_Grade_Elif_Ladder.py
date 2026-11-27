# Unit 2A Task 4 - student grade using elif ladder

marks = float(input("Enter marks: "))

# checking from the highest grade first, so no need of "and marks < 90" etc.
if marks >= 90:
    print(f"Marks {marks}: Grade A")
elif marks >= 80:
    print(f"Marks {marks}: Grade B")
elif marks >= 70:
    print(f"Marks {marks}: Grade C")
else:
    print(f"Marks {marks}: Grade D")
