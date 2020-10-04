from src.trie.trie import Trie


    
def test_trie_find():
    trie = Trie()

    trie.insert("hello trie")
    trie.insert("this is a string")
    trie.insert("this is another string")


    assert trie.find("hello trie")
    assert trie.find("this is a string")
    assert trie.find("this is another string")

    assert not trie.find("hello")
    assert not trie.find("this is an")


def test_trie_delete():
    trie = Trie()

    trie.insert("hello trie")
    trie.insert("this is a string")
    trie.insert("this is another string")

    assert not trie.delete("helo")
    assert not trie.delete("hello")
    assert trie.delete("hello trie")

    assert not trie.find("hello there")

    assert not trie.delete("this is an")
    assert trie.find("this is a string")

    assert trie.delete("this is a string")
    assert trie.find("this is another string")
    
    assert trie.delete("this is another string")
    assert not trie.find("this is another string")
