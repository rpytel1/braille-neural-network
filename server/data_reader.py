import numpy as np


class DataReader:

    @staticmethod
    def read_training_data():
        input = np.loadtxt(r"./Resources/26/data_set26.txt",
                           dtype='i', delimiter=" ")
        x = input[:, :6]
        y = input[:, 6:32]

        return x, y

    @staticmethod
    def read_test_data():
        input = np.loadtxt(r"./Resources/26/test_set26.txt",
                           dtype='i', delimiter=" ")

        return input

    @staticmethod
    def get_letter_mapping():
        letters = { 'a': [1, 0, 0, 0, 0, 0],
                    'b': [1, 0, 1, 0, 0, 0],
                    'c': [1, 1, 0, 0, 0, 0],
                    'd': [1, 1, 0, 1, 0, 0],
                    'e': [1, 0, 0, 1, 0, 0],
                    'f': [1, 1, 1, 0, 0, 0],
                    'g': [1, 1, 1, 1, 0, 0],
                    'h': [1, 0, 1, 1, 0, 0],
                    'i': [0, 1, 1, 0, 0, 0],
                    'j': [0, 1, 1, 1, 0, 0],
                    'k': [1, 0, 0, 0, 1, 0],
                    'l': [1, 0, 1, 0, 1, 0],
                    'm': [1, 1, 0, 0, 1, 0],
                    'n': [1, 1, 0, 1, 1, 0],
                    'o': [1, 0, 0, 1, 1, 0],
                    'p': [1, 1, 1, 0, 1, 0],
                    'q': [1, 1, 1, 1, 1, 0],
                    'r': [1, 0, 1, 1, 1, 0],
                    's': [0, 1, 1, 0, 1, 0],
                    't': [0, 1, 1, 1, 1, 0],
                    'u': [1, 0, 0, 0, 1, 1],
                    'v': [1, 0, 1, 0, 1, 1],
                    'w': [0, 1, 1, 1, 0, 1],
                    'x': [1, 1, 0, 0, 1, 1],
                    'y': [1, 1, 0, 1, 1, 1],
                    'z': [1, 0, 0, 1, 1, 1]}
        return letters

    @staticmethod
    def get_output_mapping():
        letters_map = dict()
        for i in range(0, 26):
            letters_map[i] = chr(ord('a') + i)

        return letters_map

