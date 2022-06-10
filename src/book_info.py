from dataclasses import dataclass


@dataclass
class BookInfo:
    title: str
    author: str
    first_chapter: list

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Begginign of first page: {self.first_chapter[0]} {''.join(self.first_chapter[1:15])}"
        )
