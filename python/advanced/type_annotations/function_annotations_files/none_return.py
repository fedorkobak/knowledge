def annotated_function() -> None:
    print("I annotated to return None")

def empty_function():
    print("My output doesn't annotated")

my_value = annotated_function()
my_value = empty_function()
