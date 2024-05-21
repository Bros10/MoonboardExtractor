import json
import re

def extract_climb_data(input_string):
    pattern = r"var problem = JSON.parse\('(.+?)'\);"
    match = re.search(pattern, input_string, re.DOTALL)
    
    if match:
        json_string = match.group(1).encode('utf-8').decode('unicode_escape')
        try:
            climb_data = json.loads(json_string)
            return climb_data
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            print(f"Problematic JSON string: {json_string[:500]}")  # Print a portion of the problematic string
            return None
    else:
        print("No matching problem found in the input string.")
        return None

def process_climbs(file_path, output_file_path):
    climbs_list = []  # List to store all valid climb data

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    climbs = content.split('<script type="text/javascript">')
    
    for climb_script in climbs:
        climb_data = extract_climb_data(climb_script)
        if climb_data:
            name = climb_data.get('Name', 'Unknown')
            grade = climb_data.get('Grade', 'Unknown')
            moves = [move['Description'] for move in climb_data.get('Moves', [])]
            
            # Add valid climb data to the list
            climbs_list.append({
                "Name": name,
                "Grade": grade,
                "Moves": moves
            })

    # Save the climbs list to a JSON file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(climbs_list, output_file, indent=4, ensure_ascii=False)

# File paths
file_path = 'climb_details_output.txt'
output_file_path = 'processed_climbs.json'

# Process the climbs from the file and save to a JSON file
process_climbs(file_path, output_file_path)
