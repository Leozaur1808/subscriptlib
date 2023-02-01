from .base import SubscriptTranslator, SuperscriptTranslator
from typing import Union

def subscript(s: Union[int, str]) -> str:
    """Returns translated string excluding symbols that could not be translated

    :param s: string to be translated
    :return: string
    """
    translate = SubscriptTranslator(s)
    return translate.translated


def superscript(s: Union[int, str]) -> str:
    """Returns translated string excluding symbols that could not be translated

    :param s: string to be translated
    :return: string
    """
    translate = SuperscriptTranslator(s)
    return translate.translated
