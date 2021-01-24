from numpy import dot
from numpy.linalg import norm

def soundex(query: str):
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

    to_replace = {('b', 'f', 'p', 'v'): 1, ('c', 'g', 'j', 'k', 'q', 's', 'x', 'z'): 2,
                  ('d', 't'): 3, ('l',): 4, ('m', 'n'): 5, ('r',): 6}
    lst = []
    for group, value in to_replace.items():
        if first_letter in group:
            if first_letter:
                lst.append(value)
            else:
                lst.append(first_letter)



    first_letter = [value if first_letter else first_letter for group, value in to_replace.items()
                    if first_letter in group]
    letters = [value if char else char
               for char in letters
               for group, value in to_replace.items()
               if char in group]

    # Step 3: Replace all adjacent same digits with one digit.
    letters = [char for ind, char in enumerate(letters)
               if (ind == len(letters) - 1 or (ind+1 < len(letters) and char != letters[ind+1]))]

    # Step 4: If the saved letter’s digit is the same the resulting first digit, remove the digit (keep the letter)
    if first_letter == letters[0]:
        letters[0] = query[0]
    else:
        letters.insert(0, query[0])

    # Step 5: Append 3 zeros if result contains less than 3 digits.
    # Remove all except first letter and 3 digits after it.

    first_letter = letters[0]
    letters = letters[1:]

    letters = [char for char in letters if isinstance(char, int)][0:3]

    while len(letters) < 3:
        letters.append(0)

    letters.insert(0, first_letter)

    string = "".join([str(l) for l in letters])

    return string


def cosine_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))

def pronounciation_sim(word1, word2):
    vec1 = [int(char) for char in soundex(word1)[1:]]
    vec2 = [int(char) for char in soundex(word2)[1:]]
    print("vec1", vec1, "| vec2", vec2)
    return cosine_sim(vec1, vec2)

if __name__=="__main__":
    word1 = "olevia"
    word2 = "livia"
    print(word1, soundex(word1))
    print(word2, soundex(word2))
    print(pronounciation_sim(word1, word2))
    # print(cosine_sim(1, 2))
    