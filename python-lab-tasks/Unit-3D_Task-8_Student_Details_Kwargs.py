# Unit-3D Task-8: Display a student's name and subject marks using **kwargs

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


student_details(name="Anu", maths=85, science=90)
