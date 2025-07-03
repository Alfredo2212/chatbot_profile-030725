import json

with open("characters.json", "r") as file:
    characters = json.load(file)

#for char in characters:
#    print(f"Name: {char['name']}")
#    print("Tags:", ", ".join(char['tags']))
#    print("-" * 40)

def filter_characters_by_tags(characters, required_tags):
    """
    Return character who have all required tags
    """
    res = []
    for char in characters:
        if all(tag in char['tags'] for tag in required_tags):
            res.append(char)
    return res

#search_tags = ["dominant","0001"]

#matched = filter_characters_by_tags(characters, search_tags)

#print(f"\nCharacters matching tags {search_tags}:\n")
#for char in matched:
#    print(f"Name: {char['name']}")
#    print("Tags:", ", ".join(char['tags']))
#    print("-" * 40) 

def rank_characters(characters, by="likes", top_n=None, rev=True):
    """
    Rank characters by a given key (likes, saves, comments)
    """
    sorted_chars = sorted(
        characters,
        key = lambda x : x[by],
        reverse = rev
    )

    if top_n:
        sorted_chars = sorted_chars[:top_n]
        
    print(f"\nCharacter names ranked by {by}: \n")
    for i, char in enumerate(sorted_chars, 1):
        print(f"{i}. {char['name']} ({by}:{char[by]})")

rank_characters(characters, by="saves", top_n = 10)