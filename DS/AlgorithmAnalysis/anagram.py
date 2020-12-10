from collections import defaultdict

s1 = 'pythonnn'
s2 = 'tpyhon'

#Here although there's not a single loop but the complexity is O(n^2) or nlog(n) as there are calls to sorted method.
def anagram_detect(s1, s2):
    l1 = sorted(list(s1))
    l2 = sorted(list(s2))
    if l1 == l2:
        return True
    else:
        return False


def make_char_dict(s):
    string_list = list(s)
    char_dict = defaultdict(int)
    for char in string_list:
        if char in char_dict:
            char_dict[char] = char_dict[char]+1
        else:
            char_dict[char] = 1
    return char_dict


def anagram_refined(s1, s2):
    dict1 = make_char_dict(s1)
    dict2 = make_char_dict(s2)
    if dict1 == dict2:
        return True
    else:
        return False


# print(anagram_detect(s1, s2))
print(anagram_refined(s1, s2))