from abc import ABC
from typing import Union


class Translator(ABC):
    """
    Base class for the translator, the static variable alphabet defines the local translation
    """
    _alphabet = {}

    def __init__(self, s: Union[str, int]):
        """

        :param s: string|int to be translated,
        """
        if not isinstance(s, str):
            if not isinstance(s, int):
                raise ValueError('Only string and int types are accepted')
            self.string = str(s)
        else:
            self.string = s
        self.changed_characters: str = ''
        self.unchanged_characters: str = ''
        self._change_characters()

    def _change_characters(self):
        """Changes characters according to the alphabet defined in the class.
        If the character can be translated it is added to the local changed_characters variable,
        else it is added to the unchanged_characters variable

        :return: None
        """
        for c in self.string:
            try:
                self.changed_characters += self._alphabet[c]
            except KeyError:
                self.unchanged_characters += c

    @property
    def translated(self) -> str:
        """Getter for the changed_characters, returns changed_characters

        :return: string with translated characters
        """
        return self.changed_characters

    @property
    def non_translated(self) -> str:
        """Getter for the unchanged_characters, returns unchanged_characters

        :return: string with characters that could not be translated
        """
        return self.unchanged_characters


class SubscriptTranslator(Translator):
    """
    Extension of the base class aimed to translate to subscript
    """
    _alphabet = {
        '0': '\u2080',
        '1': '\u2081',
        '2': '\u2082',
        '3': '\u2083',
        '4': '\u2084',
        '5': '\u2085',
        '6': '\u2086',
        '7': '\u2087',
        '8': '\u2088',
        '9': '\u2089',
        '+': '\u208a',
        '-': '\u208b',
        '=': '\u208c',
        '(': '\u208d',
        ')': '\u208e',
        'a': '\u2090',
        'e': '\u2091',
        'o': '\u2092',
        'x': '\u2093',
        'i': '\u1d62',
        'r': '\u1d63',
        'u': '\u1d64',
        'v': '\u1d65',
        'h': '\u2095',
        'k': '\u2096',
        'l': '\u2097',
        'm': '\u2098',
        'n': '\u2099',
        'p': '\u209a',
        's': '\u209b',
        't': '\u209c'
    }


class SuperscriptTranslator(Translator):
    """
    Extension of the base class aimed to translate to superscript
    """
    _alphabet = {
        '0': '\u2070',
        '1': '\u00B9',
        '2': '\u00B2',
        '3': '\u00B3',
        '4': '\u2074',
        '5': '\u2075',
        '6': '\u2076',
        '7': '\u2077',
        '8': '\u2078',
        '9': '\u2079',
        '+': '\u207a',
        '-': '\u207b',
        '=': '\u207c',
        '(': '\u207d',
        ')': '\u207e',
        'a': '\u1d43',
        'A': '\u1d2c',
        'b': '\u1d47',
        'B': '\u1d2e',
        'c': '\u1d9c',
        'd': '\u1d48',
        'D': '\u1d30',
        'e': '\u1d49',
        'E': '\u1d31',
        'f': '\u1da0',
        'g': '\u1da2',
        'H': '\u1d34',
        'J': '\u1d36',
        'I': '\u1d35',
        'k': '\u1d4f',
        'K': '\u1d37',
        'L': '\u1d38',
        'm': '\u1d50',
        'M': '\u1d39',
        'n': '\u207f',
        'N': '\u1d3a',
        'o': '\u1d52',
        'O': '\u1d3c',
        'p': '\u1d56',
        'P': '\u1d3e',
        'R': '\u1d3f',
        't': '\u1d57',
        'T': '\u1d40',
        'u': '\u1d58',
        'U': '\u1d41',
        'v': '\u1d5b',
        'W': '\u1d42',
        'z': '\u1dbb'
    }
