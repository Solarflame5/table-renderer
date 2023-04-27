import json

def calculate_column_width(column):
	input_column = column
	input_column["contents"].insert(0, input_column["title"])
	width = max([len(x) for x in input_column["contents"]])
	return width

def generate_table(table_json: str):
	table_dict = json.loads(table_json)
	calculate_column_width(table_dict["columns"][0][0])
	return

# temporary code for testing
from pathlib import Path
json_path = Path(__file__).with_name("placeholder.json")
with json_path.open("r") as json_file:
	placeholder_json = json_file.read()

table = generate_table(placeholder_json)
print(table)