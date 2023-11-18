def find_most_frequent_word(string)->tuple:
    if not string:
        return ()
    
    string_list = string.split()
    word_dict = {}
    
    for word in string_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    res = []
    max_value = max(word_dict.values())
    for word, value in word_dict.items():
        if value == max_value:
            res.append((word, value))
    
    return tuple(res)

def test_find_most_frequent_word():
    try:
        assert find_most_frequent_word("") == ()
        assert find_most_frequent_word("hello world") == (('hello', 1), ('world', 1))
        assert find_most_frequent_word("hello hello world world") == (('hello', 2), ('world', 2))
        assert find_most_frequent_word("hello hello world world world") == (('world', 3),)
        assert find_most_frequent_word("hello hello world world world world") == (('world', 4),)
        assert find_most_frequent_word("This is a test. This is only a test.") == (('This', 2), ('is', 2), ('a', 2), ('test.', 2))
    except AssertionError:
        print("Fail")
    else:    
        print("Your code is correct!")
    
test_find_most_frequent_word()