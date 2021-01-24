from numpy import dot
from numpy.linalg import norm

def soundex(query: str, constrainedLen = True):
    """
    https://en.wikipedia.org/wiki/Soundex
    :param query:
    :return:
    """
    # Step 0: Clean up the query string
    query = query.lower()
    letters = [char for char in query if char.isalpha()]

    # Step 1: Save the first letter. Remove all occurrences of a, e, i, o, u, y, h, w.
    # If query contains only 1 letter, return query+"000" (Refer step 5)
    if len(query) == 1:
        return query + "000"
    to_remove = ('a', 'e', 'i', 'o', 'u', 'y', 'h', 'w')

    first_letter = letters[0]
    letters = letters[1:]
    letters = [char for char in letters if char not in to_remove]
    if len(letters) == 0:
        return first_letter + "000"

    # Step 2: Replace all consonants (include the first letter) with digits according to rules
    to_replace = {  ('b', 'f', 'p', 'v'): 1, 
                    ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'): 2,
                    ('d', 't'): 3,
                    ('l',): 4,
                    ('m', 'n'): 5,
                    ('r',): 6}

    first_letter = [value for group, value in to_replace.items() if first_letter in group]
    letters = [value
               for char in letters
               for group, value in to_replace.items()
               if char in group]

    # Step 3: Replace all adjacent same digits with one digit.
    letters = [char for ind, char in enumerate(letters)
               if (ind == len(letters) - 1 or (ind+1 < len(letters) and char != letters[ind+1]))]

    # Step 4: If the saved letter’s digit is the same the resulting first digit, remove the digit (keep the letter)
    if first_letter == letters[0]:
        letters[0] = query[0] # replace first digit
    else:
        letters.insert(0, query[0])

    # Step 5: Append 3 zeros if result contains less than 3 digits.
    # Remove all except first letter and 3 digits after it.
    first_letter = letters[0]
    letters = letters[1:]
    if constrainedLen:
        letters = [char for char in letters if isinstance(char, int)][0:3]
    else:
        letters = [char for char in letters if isinstance(char, int)]
    while len(letters) < 3:
        letters.append(0)
    letters.insert(0, first_letter)
    string = "".join([str(l) for l in letters])
    return letters

def cosine_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def bagofwords(wordvec):
    bow = [0,0,0,0,0,0,0]
    for char in wordvec:
        if int(char)>0: # 0 not counted
            bow[int(char)]+=1
    return bow

def soundex_sim(word1soundex, word2soundex):
    if int(word1soundex[1:]) == 0 or int(word1soundex[2:]) == 0:
        return 0
    vec1 = [int(char) for char in word1soundex[1:]]
    vec2 = [int(char) for char in word2soundex[1:]]
    print("soundex_sim: vec1", vec1, "| vec2", vec2)
    return cosine_sim(vec1, vec2)

def soundexbow_sim(word1soundex, word2soundex):
    if int(word1soundex[1:]) == 0 or int(word1soundex[2:]) == 0:
        return 0
    if len(word1soundex) > len(word2soundex):
        for i in range(len(word1soundex)-len(word2soundex)):
            word2soundex.append(0)
    elif len(word2soundex) > len(word1soundex):
        for i in range(len(word2soundex)-len(word1soundex)):
            word1soundex.append(0)
    print("soundexbow_sim: word1soundex", word1soundex, "| word2soundex", word2soundex)
    vec1 = bagofwords([int(char) for char in word1soundex[1:]])
    vec2 = bagofwords([int(char) for char in word2soundex[1:]])
    print("soundexbow_sim: vec1", vec1, "| vec2", vec2)
    return cosine_sim(vec1, vec2)


if __name__=="__main__":
    word1 = "a"
    word2 = "ae"
    print(word1, soundex(word1, True))
    print(word2, soundex(word2, True))
    print("soundex_sim", soundex_sim(soundex(word1, True), soundex(word2, True)))
    print("soundexbow_sim", soundexbow_sim(soundex(word1, False), soundex(word2, False)))

