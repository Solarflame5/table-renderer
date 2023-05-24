import json

def calculate_column_width(column: dict) -> int:
	input_column = column.copy()
	input_column["contents"] = column["contents"].copy()
	input_column["contents"].insert(0, input_column["title"])
	# add column title to the column contents and find the longest item's width
	width = max([len(str(x)) for x in input_column["contents"]])
	return width

def generate_table(table_json: str, style: str) -> str:
	"""
	Generates a table string from the provided JSON\n
		Parameters:
			table_json: str
				The table contents in JSON format
			style: str
				The picked style to use for the box drawing characters
		
		Available styles:
			"ascii", "unicode_light", "unicode_heavy", "unicode_double"
		
		JSON format:
		```
		{
		    "columns": [
		        {
		            "title": "",
		            "type": "",
		            "contents": []
		        }
		    ]
		}
		```
	"""
	table_dict = json.loads(table_json)
	table = ""
	row_seperator = ""

	box_chars = { # dictionary of styles for the box characters
		"ascii": [
			"+", "+", "+", "+", "+", "+", "+", "+", "+", "-", "|"
		],
		"unicode_light": [
			"┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘", "─", "│"
		],
		"unicode_heavy": [
			"┏", "┳", "┓", "┣", "╋", "┫", "┗", "┻", "┛", "━", "┃"
		],
		"unicode_double": [
			"╔", "╦", "╗", "╠", "╬", "╣", "╚", "╩", "╝", "═", "║"
		]
	}

	column_widths = [] # get column widths
	for column in table_dict["columns"][0]: 
		column_widths.append(calculate_column_width(column))

	table += box_chars[style][0] # generate top borders
	for column_index, column in enumerate(table_dict["columns"][0]):
		table += (box_chars[style][9] * column_widths[column_index])
		if column_index == len(table_dict["columns"][0]) - 1:
			table += box_chars[style][2] + "\n"
		else:
			table += box_chars[style][1]
	
	row_seperator += box_chars[style][3] # generate seperator between rows
	for column_index, column in enumerate(table_dict["columns"][0]):
		row_seperator += (box_chars[style][9] * column_widths[column_index])
		if column_index == len(table_dict["columns"][0]) - 1:
			row_seperator += box_chars[style][5] + "\n"
		else:
			row_seperator += box_chars[style][4]

	current_row = box_chars[style][10]
	for column_index, column in enumerate(table_dict["columns"][0]):
		current_object = column["title"]
		current_object_spacing = column_widths[column_index] - len(current_object)
		current_row += current_object
		current_row += " "*current_object_spacing
		current_row += box_chars[style][10]
	current_row += "\n"
	table += current_row
	table += row_seperator
	for row_index, row in enumerate(table_dict["columns"][0][0]["contents"]):
		current_row = box_chars[style][10]
		for column_index, column in enumerate(table_dict["columns"][0]):
			current_object = str(table_dict["columns"][0][column_index]["contents"][row_index])
			current_object_spacing = column_widths[column_index] - len(current_object)
			if(table_dict["columns"][0][column_index]["type"] == "int"):
				current_row += " "*current_object_spacing
				current_row += current_object
			else:
				current_row += current_object
				current_row += " "*current_object_spacing
			current_row += box_chars[style][10]
		current_row += "\n"
		table +=current_row

		if row_index == len(table_dict["columns"][0][0]["contents"]) - 1:
			table += box_chars[style][6]
			for column_index, column in enumerate(table_dict["columns"][0]):
				table += (box_chars[style][9] * column_widths[column_index])
				if column_index == len(table_dict["columns"][0]) - 1:
					table += box_chars[style][8]
				else:
					table += box_chars[style][7]
		else:
			table +=row_seperator
			
	return table

# temporary code for testing
from pathlib import Path
json_path = Path(__file__).with_name("placeholder.json")
with json_path.open("r") as json_file:
	placeholder_json = json_file.read()

print(generate_table(placeholder_json, "unicode_light"))
