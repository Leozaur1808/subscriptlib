import pytest
from subscriptlib import *


def test_subscript_translator_int():
    st = SubscriptTranslator(1230)
    assert '₁₂₃₀' == st.translated


def test_subscript_translator_str():
    st = SubscriptTranslator('ae01ivod')
    assert 'ₐₑ₀₁ᵢᵥₒ' == st.translated and 'd' == st.non_translated


def test_superscript_translator_int():
    st = SuperscriptTranslator(102345)
    assert '¹⁰²³⁴⁵' == st.translated


def test_superscript_translator_str():
    st = SuperscriptTranslator('abc12q')
    assert 'ᵃᵇᶜ¹²' == st.translated and 'q' == st.non_translated


def test_subscript():
    exp = 'ₐ₁₂₃'
    assert exp == subscript('a123')


def test_superscript():
    exp = 'ᵃ¹²³'
    assert exp == superscript('a123')
