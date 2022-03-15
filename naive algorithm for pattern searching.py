#Naive Algorithm For Pattern Searching
#using only loops
def search_naive(pattern, text):
    pattern_length = len(pattern)
    text_length = len(text)
    found = []
    c = 0
    for i in range((text_length - pattern_length) + 1):
        for j in range(pattern_length):
            if text[i + j] != pattern[j]:
                break
            c += 1
        if c == pattern_length:
            found.append(i)
        c = 0
    return found
print(search_naive('ABC',"ABCABC"))
#using  slicing operator []
def naive(pat, txt):
    pat1 = len(pat)
    txt1 = len(txt)
    arr = []
    for f in range((txt1 - pat1) + 1):
        if txt[f:f + pat1] == pat:
            arr.append(f)
    return arr
print(naive('ABC', "ABCAfgyhyiujjBCABC"))

            
    
    
