
def matching_characters(string1, string2):
    return (len((set(string1)).intersection(set(string2))))

print(matching_characters("VISHAV", "VANSHIKA"))