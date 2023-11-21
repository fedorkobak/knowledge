import argparse

my_parser = argparse.ArgumentParser(
    description='Process some integers.'
)
my_parser.add_argument(
    "positional", 
    help = "Example of the positional argument.",
)
my_parser.add_argument(
    "--option",
    help = "Option that takes value."
)

args = my_parser.parse_args()
print(
    "positional : ", args.positional, "\n",
    "option : ", args.option,
    sep = ""
)
