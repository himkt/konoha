from konoha.konoha_token import Token
from konoha.word_tokenizers.tokenizer import BaseTokenizer


class SudachiTokenizer(BaseTokenizer):
    """Wrapper class for SudachiPy."""

    def __init__(self, mode: str, with_postag: bool, **kwargs):
        """
        Initializer for SudachiTokenizer

        Parameters
        ---
        mode (str)
            Splitting mode which controls a granuality ofkonoha.token.
            (mode should be `A`, `B` or `C`)
            For more information, see following links.
            - document: https://github.com/WorksApplications/Sudachi#the-modes-of-splitting  # NOQA
            - paper: http://www.lrec-conf.org/proceedings/lrec2018/summaries/8884.html  # NOQA
        with_postag (bool=False)
            flag determines ifkonoha.tokenizer include pos tags.
        **kwargs
            others.
        """
        super(SudachiTokenizer, self).__init__(
            name="sudachi ({})".format(mode),
            with_postag=with_postag,
        )

        try:
            from sudachipy import tokenizer
            from sudachipy import dictionary
        except ImportError:
            raise ImportError("sudachipy is not installed")
        try:
            self.tokenizer = dictionary.Dictionary().create()
        except KeyError:
            msg = "please install dictionary"
            msg += " ( see https://github.com/WorksApplications/SudachiPy#install-dict-packages )"  # NOQA
            raise KeyError(msg)

        _mode = mode.capitalize()
        if _mode == "A":
            self.mode = tokenizer.Tokenizer.SplitMode.A
        elif _mode == "B":
            self.mode = tokenizer.Tokenizer.SplitMode.B
        elif _mode == "C":
            self.mode = tokenizer.Tokenizer.SplitMode.C
        else:
            msg = "Invalid mode is specified. Mode should be 'A', 'B' or 'C'"
            raise ValueError(msg)

    def tokenize(self, text: str):
        """Tokenize."""
        result = []
        for token in self.tokenizer.tokenize(text, self.mode):
            surface = token.surface()
            if self.with_postag:
                postag, postag2, postag3, postag4, \
                    inflection, conjugation = token.part_of_speech()
                base_form = token.dictionary_form()
                normalized_form = token.normalized_form()
                yomi = token.reading_form()
                result.append(Token(
                    surface=surface,
                    postag=postag,
                    postag2=postag2,
                    postag3=postag3,
                    postag4=postag4,
                    inflection=inflection,
                    conjugation=conjugation,
                    base_form=base_form,
                    normalized_form=normalized_form,
                    yomi=yomi,
                ))

            else:
                result.append(Token(
                    surface=surface
                ))
        return result
