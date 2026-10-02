from alternate_case import alternate_case 
def test_empty_string_returns_empty_string():
    assert alternate_case("")==""

def test_capital_letter():
    assert alternate_case("A")=="A"

def test_single_lowercase():
    assert alternate_case("a")== "A"

def test_capitalised_word():
    assert alternate_case("Hello") == "HeLlO"

def test_lowercased_word():
    assert alternate_case("hello")== "HeLlO"

def test_two_words():
    assert alternate_case("Hello world") == "HeLlO wOrLd"

def test_sentence():
    assert alternate_case("is it pub time") == "Is It PuB tImE"