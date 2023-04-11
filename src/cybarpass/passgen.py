from sys import exit
from typing import Union
from secrets import choice


class PassGen:
    def __init__(self, filename: Union[str, None] = None, char_limit: int = 16):
        self.char_limit = char_limit
        if filename is not None:
            self.word_list = filename

    @property
    def char_limit(self) -> int:
        return self.__char_limit

    @char_limit.setter
    def char_limit(self, value: int) -> None:
        if value < 16:
            print("Character limit must be at least 16 for security reasons.")
        else:
            self.__char_limit = value

    @property
    def word_list(self):
        return self.__word_list

    @word_list.setter
    def word_list(self, filename) -> None:
        try:
            with open(filename, "r") as file:
                # ensure file is not empty by checking existence of first char
                file.seek(0)
                if not file.read(1):
                    raise FileNotFoundError(f"File is empty: '{filename}'")
                else:
                    # reset pointer to start of file
                    file.seek(0)

                # load words from file into local list
                self.__word_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError as fnf_err:
            print(fnf_err)
            exit(1)

    def __word_gen(self, word_list: list[str], char_limit: int):
        char_count = 0
        while char_count < char_limit:
            word = choice(word_list)
            char_count += len(word)
            yield word

    @property
    def passphrase(self) -> str:
        return " ".join(self.__word_gen(self.word_list, self.char_limit))
