import pytest
from problems.medium.design_add_and_search_words_data_structure.solution import WordDictionary



@pytest.fixture
def wd():
    return WordDictionary()


def wd_insert_basic(wd):
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")


def test_empty_dictionary(wd):
    assert wd.search("a") is False
    assert wd.search("") is False
    assert wd.search("abc") is False


def test_add_and_exact_search(wd):
    wd_insert_basic(wd)

    assert wd.search("bad") is True
    assert wd.search("dad") is True
    assert wd.search("mad") is True
    assert wd.search("pad") is False


def test_single_dot_wildcard(wd):
    wd_insert_basic(wd)


    assert wd.search(".ad") is True
    assert wd.search("b.d") is True
    assert wd.search("ba.") is True
    assert wd.search("..d") is True

    assert wd.search("ad") is False


def test_multiple_dots_wildcard(wd):
    wd_insert_basic(wd)

    assert wd.search("...") is True
    assert wd.search("....") is False


def test_prefix_is_not_a_word(wd):
    wd.addWord("apple")

    assert wd.search("app") is False
    assert wd.search("app..") is True
    assert wd.search("app..e") is False
    assert wd.search("apple") is True


def test_shared_prefix_branching(wd):
    wd.addWord("bat")
    wd.addWord("batch")
    wd.addWord("bad")

    assert wd.search("ba.") is True
    assert wd.search("bat..") is True
    assert wd.search("b.t") is True
    assert wd.search("b..") is True
    assert wd.search('ba..') is False


def test_readding_word_does_not_break(wd):
    wd_insert_basic(wd)

    assert wd.search("bad") is True
    assert wd.search("b..") is True
    assert wd.search("..d") is True


def test_dot_only_querires(wd):
    wd.addWord("a")
    wd.addWord("to")
    wd.addWord("tea")

    assert wd.search(".") is True
    assert wd.search("..") is True
    assert wd.search("...") is True
    assert wd.search("....") is False