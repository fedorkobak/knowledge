program = """
variable = "This is initial valule of the variable"
"""
with open("temp.py", "w") as f:
    f.write(program)
import temp
print(temp.variable)

# now change value of the variable
program = """
variable = "This is changed value of the variable"
"""
with open("temp.py", "w") as f:
    f.write(program)
import importlib
importlib.reload(temp)
print(temp.variable)
