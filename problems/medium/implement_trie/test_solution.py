import pytest
from problems.medium.implement_trie.solution import Trie



@pytest.fixture
def trie():
    return Trie()


def test_empty_trie_basics(trie):
    assert trie.search("a") is False
    assert trie.startsWith("a") is False


def test_insert_and_search_single_word(trie):
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True


def test_insert_prefix_then_full_word(trie):
    trie.insert("app")
    assert trie.search("app") is True
    assert trie.startsWith("app") is True
    assert trie.search("apple") is False

    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is True
    assert trie.startsWith("pp") is False


def test_multiple_words_shared_prefix(trie):
    words = ["app", "apple", "apply", "apt", "bat", "batch"]
    for w in words:
        trie.insert(w)

    assert trie.search("app") is True
    assert trie.search("ap") is False
    assert trie.startsWith("ap") is True
    assert trie.startsWith("bat") is True
    assert trie.search("bath") is False


def test_reinserting_same_word_is_idempotent(trie):
    trie.insert("app")
    trie.insert("app")
    trie.insert("app")

    assert trie.search("app") is True
    assert trie.startsWith("app") is True
    assert trie.search("ap") is False


@pytest.mark.parametrize(
    "inserted, queries_search_true, queries_search_false, prefixes_true, prefixes_false",
    [
        (
            ["a"],
            ["a"],
            ["aa", "b"],
            ["a"],
            ["b"],
        ),
        (
            ["cat", "car", "cart"],
            ["cat", "car", "cart"],
            ["ca", "carts", "dog"],
            ["ca", "car"],
            ["do", "cats"],
        ),
        (
            ["hello", "helium"],
            ["hello", "helium"],
            ["hel", "help"],
            ["hel", "he"],
            ["ha", "hi"],
        ),
    ],
)

def test_parametrized_sets(
    trie, inserted, queries_search_true, queries_search_false, prefixes_true, prefixes_false,
):
    for w in inserted:
        trie.insert(w)

    for q in queries_search_true:
        assert trie.search(q) is True

    for q in queries_search_false:
        assert trie.search(q) is False

    for p in prefixes_true:
        assert trie.startsWith(p) is True

    for p in prefixes_false:
        assert trie.startsWith(p) is False