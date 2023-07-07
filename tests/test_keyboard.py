import pytest
from src.keyboard import MixinLang, Keyboard

@pytest.fixture
def keyboard():
    return Keyboard("Dark Project KD87A", 9600, 5)

def test_Keyboard___init__():
    kb = Keyboard("Dark Project KD87A", 9600, 5)
    assert kb.name == "Dark Project KD87A"

def test_keyboard_language(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"
