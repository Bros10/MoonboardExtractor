import requests
from bs4 import BeautifulSoup
import json
import re

def extract_climb_details(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the script tag containing the problem data
            script_tag = soup.find('script', text=re.compile('var problem = JSON.parse'))

            if script_tag:
                # Extract the JSON string
                #json_string = re.search(r'JSON.parse\(\'(.*?)\'\);', script_tag.string).group(1)
                # Convert JSON string to Python dictionary
                #json_string = json_string.replace('\\', '')
                #climb_data = json.loads(json_string)
                climb_data = script_tag
                return climb_data  # Return the entire problem JSON object
        else:
            print(f"Failed to retrieve climb details for URL: {url}")
            print(f"HTTP Status Code: {response.status_code}")
            print(f"HTTP Response Content: {response.content[:500]}")  # Print first 500 characters of the response content
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None

# Function to process all climbs from the file
def process_climbs(file_path):
    climbs = []
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]  # Remove any empty lines

    for url in urls:
        problem_data = extract_climb_details(url)
        if problem_data:
            climbs.append(problem_data)
    return climbs

# Path to the moonboard_climb_urls.txt file
file_path = 'moonboard_climb_urls.txt'

# Process all climbs and print out the details
problems = process_climbs(file_path)
for problem in problems:
    print(problem)  # Print the entire problem JSON object pretty-printed

