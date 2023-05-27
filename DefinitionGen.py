import requests
import sys

# Takes a list of words and outputs a text file with words on each line and a definition separated by a chosen delimiter

def get_definition(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
        return definition
    else:
        return "Definition not found"

if len(sys.argv) != 3:
    print("Usage: python DefintionGen.py input_list_name.txt output_list_name delimiter")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
delimiter = sys.argv[3]

if not output_file.endswith(".txt"):
    output_file += ".txt"

with open(input_file, "r") as f:
    words = f.read().splitlines()

with open(output_file, "w") as f:
    for word in words:
        definition = get_definition(word)
        f.write(f"{word}{delimiter}{definition}\n")
