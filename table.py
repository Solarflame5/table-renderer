import json

def generate_table(table_json: str):
	table_dict = json.loads(table_json)
	return table_dict
	
# temporary code for testing
from pathlib import Path
json_path = Path(__file__).with_name("placeholder.json")
with json_path.open("r") as json_file:
	placeholder_json = json_file.read()

table = generate_table(placeholder_json)
print(table)