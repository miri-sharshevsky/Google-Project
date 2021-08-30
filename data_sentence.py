import os
import re
from trie import Trie
from auto_complete_data import Auto_complete_data


def clear_sentence(sentence_to_clear):
    """
    Clear the sentence from space spaces and special chars
    :param sentence_to_clear:
    :return:  The cleared sentence
    """
    sentence_to_clear = sentence_to_clear.replace('\n', "")
    sentence_to_clear = re.sub(r'[^\w]', ' ', sentence_to_clear)
    return re.sub(' +', ' ', sentence_to_clear).lower()


class Data_Sentence:
    """
    this class is reading the files and holding the sentences data base
    Firstly dictionary, witch the keys are all the words and the values are trie from all the
    sentences witch contains this word from the word till the end of the trie
    """
    __instance = None
    __data_dict_tree = {}
    __words_trie = Trie()

    def __new__(cls, *args, **kwargs):
        if not Data_Sentence.__instance:
            Data_Sentence.__instance = object.__new__(cls)
        return Data_Sentence.__instance

    def load_data(self, file_path):
        """
        Load the data from the file
        :param file_path: Path of folder ro load the file from
        """
        files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(file_path) for f in filenames if
                 os.path.splitext(f)[1] == '.txt']
        for file in files:
            with open(file, 'r', encoding="utf8") as f:
                while True:
                    sentence = f.readline()
                    if not sentence:
                        break
                    self.add_new_sentence_to_dict(clear_sentence(sentence), sentence.replace('\n', ''), file,
                                                  sentence.index(sentence))

    def add_new_sentence_to_dict(self, clear_sentence, real_sentence, file, line_number):
        """
        Add a new sentence to the data base
        :param clear_sentence: The sentence after clear space spaces and signs
        :param real_sentence: The sentence before clearing
        :param file: File name the sentence were in it
        :param line_number:The number line witch the sentence were in the file
        """
        sentence_list = clear_sentence.split(" ")
        for word in sentence_list:
            if word not in self.__data_dict_tree.keys():
                self.__data_dict_tree[word] = Trie()
                self.__words_trie.insert((word, word))
            sentence_value = Auto_complete_data(real_sentence, file, line_number)
            self.__data_dict_tree[word].insert(
                (clear_sentence[clear_sentence.index(word) + len(word) + 1:], sentence_value))

    def get_trie_by_word(self, word):
        """
        Get the trie of a given word
        :param word: Word to get trie
        :return: The trie
        """
        try:
            return self.__data_dict_tree[word]
        except Exception:
            raise Exception("this word is not in")

    def get_sub_word(self, sub_word):
        """
        Search a sub sentence in the words trie
        :param sub_word:
        :return:
        """
        return self.__words_trie.get_search(sub_word, self.__words_trie.root, False)[0]



