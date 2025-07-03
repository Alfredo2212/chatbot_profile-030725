import json

with open("characters.json", "r") as file:
    characters = json.load(file)

for char in characters:
    print(f"Name: {char['name']}")
    print("Tags:", ", ".join(char['tags']))
    print("-" * 40)

def filter_characters_by_tags(characters, required_tags):
    """
    Return character who have all required tags
    """
    res = []
    for char in characters:
        if all(tag in char['tags'] for tag in required_tags):
            res.append(char)
    return res

search_tags = ["dominant","0001"]

matched = filter_characters_by_tags(characters, search_tags)

print(f"\nCharacters matching tags {search_tags}:\n")
for char in matched:
    print(f"Name: {char['name']}")
    print("Tags:", ", ".join(char['tags']))
    print("-" * 40) 