

def filter_by_tags(characters, required_tags):
    """
    Return character who have all required tags
    """
    res = []
    for char in characters:
        if all(tag in char['tags'] for tag in required_tags):
            res.append(char)
    return res

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
