from package import *

dir_result = dir()
print("Namesapce -", dir_result)

# if there are `square` name in namespace
# trying to run its' function
if "square" in dir_result:
    square.draw_square()    
