

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

def rank_by_score(characters, top_n=None, rev=True):
    """
    Rank characters using a weighted score:
    score = 3 * saves + 2 * likes + comments
    """
    def compute_score(char):
        return 3* char["saves"] + 2 * char["likes"] + char["comments"]
    
    sorted_chars = sorted(characters, key=compute_score, reverse=rev)
    if top_n:
        sorted_chars = sorted_chars[:top_n]

    return sorted_chars