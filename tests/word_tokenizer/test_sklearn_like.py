from konoha import WordTokenizer


def test_sklearn_like_interface():
    documents = [
        '私は猫である',
        '私は猫ではない'
    ]
    vocabulary = {'私', 'は', '猫', 'で', 'ある', 'は', 'ない'}

    tk = WordTokenizer('mecab')

    tk.fit(documents)
    assert set(tk.vocabulary) == vocabulary

    test_input = '私は猫である'
    ids = tk.transform(test_input)
    assert isinstance(ids, list)

    for id in ids:
        assert isinstance(id, int)

    words = tk.itransform(ids)
    assert test_input == ''.join(words)
