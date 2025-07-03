import json
from taxonomy import filter_by_tags, rank_characters

with open("characters.json", "r") as file:
    characters = json.load(file)






#for char in characters:
#    print(f"Name: {char['name']}")
#    print("Tags:", ", ".join(char['tags']))
#    print("-" * 40)

#search_tags = ["dominant","0001"]

#matched = filter_by_tags(characters, search_tags)

#print(f"\nCharacters matching tags {search_tags}:\n")
#for char in matched:
#    print(f"Name: {char['name']}")
#    print("Tags:", ", ".join(char['tags']))
#    print("-" * 40) 

# rank_characters(characters, by="saves", top_n = 10)