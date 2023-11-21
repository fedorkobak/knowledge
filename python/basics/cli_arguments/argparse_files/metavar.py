import argparse

my_parser = argparse.ArgumentParser(
    description='Process some integers.'
)
my_parser.add_argument("--option")
my_parser.add_argument("--set_metavar", metavar = "this_is_metavar")
my_parser.add_argument(
    "--double_metavar",
    nargs=2,
    metavar=('value1', 'value2')
)

args = my_parser.parse_args()
for key, value in vars(args).items():
    print(key, value)
