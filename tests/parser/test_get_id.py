def test_no_id(fake_parser):
    text = (
        'Deck: Abraham\n'
        '\n'
        'Tags: one two-three\n'
        '\n'
        '1. Some question?\n'
        '\n'
        '> Answer'
    )

    assert fake_parser._get_id(text) is None


def test_empty_id(fake_parser):
    text = (
        'Deck: Abraham\n'
        '\n'
        'Tags: one two-three\n'
        '\n'
        '<!--ID:-->\n'
        '1. Some question?\n'
        '\n'
        '> Answer'
    )

    assert fake_parser._get_id(text) is None


def test_correct_id(fake_parser):
    anki_id = '1235523'
    text = (
        'Deck: Abraham\n'
        '\n'
        'Tags: one two-three\n'
        '\n'
        f'<!--ID:{anki_id}-->\n'
        '1. Some question?\n'
        '\n'
        '> Answer'
    )

    assert fake_parser._get_id(text) == anki_id