from greet import greet
import pytest

def test01():
    assert greet("Bob") == "Hello, Bob."

def test02():
    assert greet(None) == "Hello, my friend."

def test03():
    assert greet("JERRY") == "HELLO JERRY!"

def test04():
    assert greet(["Jill", "Jane"]) == "Hello, Jill and Jane."

def test05():
    assert greet(["Amy", "Brian", "Charlotte"]) == "Hello, Amy, Brian, and Charlotte."

def test06():
    assert greet(["Amy", "BRIAN", "Charlotte"]) == "Hello, Amy and Charlotte. AND HELLO BRIAN!"

def test07():
    assert greet(["Bob", "Charlie, Dianne"]) == "Hello, Bob, Charlie, and Dianne."

def test08():
    assert greet(["Bob", "\"Charlie, Dianne\""]) == "Hello, Bob and Charlie, Dianne."
