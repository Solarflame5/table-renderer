import json

def calculate_column_width(column):
	input_column = column.copy()
	input_column["contents"] = column["contents"].copy()
	input_column["contents"].insert(0, input_column["title"])
	width = max([len(str(x)) for x in input_column["contents"]])
	return width

def generate_table(table_json: str):
	table_dict = json.loads(table_json)
	table = ""

	column_widths = []
	for column in table_dict["columns"][0]: # get column widths
		column_widths.append(calculate_column_width(column))

	row_seperator = "+"
	for column_index, column in enumerate(table_dict["columns"][0]):
		row_seperator += ("-" * column_widths[column_index]) + "+"
	row_seperator += "\n"
	
	table += row_seperator
	current_row = "|"
	for column_index, column in enumerate(table_dict["columns"][0]):
		current_object = column["title"]
		current_object_spacing = column_widths[column_index] - len(current_object)
		current_row += current_object
		current_row += " "*current_object_spacing
		current_row += "|"
	current_row += "\n"
	table += current_row
	table += row_seperator
	for row_index, row in enumerate(table_dict["columns"][0][0]["contents"]):
		current_row = "|"
		for column_index, column in enumerate(table_dict["columns"][0]):
			current_object = str(table_dict["columns"][0][column_index]["contents"][row_index])
			current_object_spacing = column_widths[column_index] - len(current_object)
			if(table_dict["columns"][0][column_index]["type"] == "int"):
				current_row += " "*current_object_spacing
				current_row += current_object
			else:
				current_row += current_object
				current_row += " "*current_object_spacing
			current_row += "|"
		current_row += "\n"
		table +=current_row
		table +=row_seperator
	return table

# temporary code for testing
from pathlib import Path
json_path = Path(__file__).with_name("placeholder.json")
with json_path.open("r") as json_file:
	placeholder_json = json_file.read()

table = generate_table(placeholder_json)
print(table)