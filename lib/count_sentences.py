#!/usr/bin/env python3

class MyString:
    def __init__(self, value=None):
        self.value = value
        if not isinstance(value, str):
            print("The value must be a string.")

    def is_sentence(self):
        if self.value is None:
            return False
        return self.value.endswith('.')

    def is_question(self):
        if self.value is None:
            return False
        return self.value.endswith('?')

    def is_exclamation(self):
        if self.value is None:
            return False
        return self.value.endswith('!')

    def count_sentences(self):
        if self.value is None:
            return 0
        sentences = self.value.split('.')
        sentences = [s for s in sentences if s.strip() != '']
        return len(sentences)
