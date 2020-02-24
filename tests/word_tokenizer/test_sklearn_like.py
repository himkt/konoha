from konoha import WordTokenizer

import pytest


DOCUMENTS = [
    '私は猫である',
    '私は猫ではない'
]
VOCABULARY = {'私', 'は', '猫', 'で', 'ある', 'は', 'ない'}


def test_sklearn_like_interface():
    try:
        tk = WordTokenizer('mecab')
    except ImportError:
        pytest.skip('skip fit/transform test')

    tk.fit(DOCUMENTS)
    assert set(tk.vocabulary) == VOCABULARY

    test_input = '私は猫である'
    ids = tk.transform(test_input)
    assert isinstance(ids, list)

    for id in ids:
        assert isinstance(id, int)

    words = tk.itransform(ids)
    assert test_input == ''.join(words)


def test_tf_options():
    try:
        tk = WordTokenizer('mecab')
    except ImportError:
        pytest.skip('skip fit/transform test')

    tk.fit(DOCUMENTS, min_tf=2)
    assert set(tk.vocabulary) == {'私', 'は', '猫', 'で'}
