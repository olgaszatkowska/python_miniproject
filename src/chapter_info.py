from dataclasses import dataclass


@dataclass
class ChapterData:
    n_of_paragraphs: int
    n_of_word_in_first_chapter: int
    minimal_n_of_words_in_paragraph: int
    maximal_n_of_words_in_paragraph: int
    average_n_of_words: int

    def __str__(self):
        return (
            f"Number of paragraph: {self.n_of_paragraphs}\n"
            f"Number of words in the first chapter: {self.n_of_word_in_first_chapter}\n"
            f"Minimal number of words in paragraph: {self.minimal_n_of_words_in_paragraph}\n"
            f"Maximal number of words in paragraph: {self.maximal_n_of_words_in_paragraph}\n"
            f"Average number of words: {self.average_n_of_words}"
        )
