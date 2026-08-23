from templates import get_template

print(get_template("main.py"))
print(get_template("main.cpp"))

print(get_template("main.py", "./templates"))
print(get_template("main.cpp", "./templates"))
print(get_template("main.xyz", "./templates"))