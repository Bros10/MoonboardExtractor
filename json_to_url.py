import json
# Path to the JSON file
json_file_path = 'moonboard.json'


# Now let's read the file back and create the URLs
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Base URL for the climb pages
base_url = "https://www.moonboard.com/Problems/View/"

# Extract the ProblemId and generate URLs
urls = [base_url + str(climb["ProblemId"]) + "/" + climb["Url"] for climb in data["Data"]]

# Path to the output text file
output_file_path = 'moonboard_climb_urls.txt'

# Write the URLs to the text file
with open(output_file_path, 'w') as file:
    for url in urls:
        file.write(url + "\n")

