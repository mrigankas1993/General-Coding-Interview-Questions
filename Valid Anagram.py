# Check Valid Anagram by mriganka
def check_if_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    occurance_in_1 = {}
    occurance_in_2 = {} # Dictionary or simply hash map
    
    for character in string1:
        if character in occurance_in_1:
            occurance_in_1[character] += 1
        occurance_in_1[character] = 1
    for character in string2:
        if character in occurance_in_2:
            occurance_in_2[character] += 1
        occurance_in_2[character] = 1
    for j in occurance_in_1:
        if j not in occurance_in_2 or occurance_in_1[j] != occurance_in_2[j]:
            return False
    return True
print(check_if_anagram("danger", 'garden'))
