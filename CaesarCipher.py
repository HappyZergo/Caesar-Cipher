import math
from random import randrange

frequency = {
    'a': 0.08167,
    'b': 0.01492,
    'c': 0.02782,
    'd': 0.04253,
    'e': 0.130001,
    'f': 0.02228,
    'g': 0.02015,
    'h': 0.06094,
    'i': 0.06966,
    'j': 0.00153,
    'k': 0.00772,
    'l': 0.04025,
    'm': 0.02406,
    'n': 0.06749,
    'o': 0.07507,
    'p': 0.01929,
    'q': 0.00095,
    'r': 0.05987,
    's': 0.06327,
    't': 0.09056,
    'u': 0.02758,
    'v': 0.00978,
    'w': 0.02360,
    'x': 0.00150,
    'y': 0.01974,
    'z': 0.00074}


def check(words, char):
    k = 0
    for i in words:
        if i == char:
            k += 1
    return k

def cryptoanalyse(message):
    length = len(message)
    dicts = {i for i in message}
    frequence = []
    sym = []
    values = []
    stat = 0

    for symbol in dicts:
        if symbol.isalpha():
            stat = 100 * check(message, symbol) / length
            sym.append(symbol)
            frequence.append(stat)
    dictionary = dict(zip(sym, frequence))
    sortednames = sorted(dictionary.keys(), key=lambda x: x.lower())
    for i in sortednames:
        values.append(dictionary[i])

    return values, sortednames


def cipher(offset, message):
    offset = int(offset)
    if offset is False:
        offset = randrange(5, 25)
    alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z')
    ciphered_message_list = list(message.upper())
    for i, letter in enumerate(ciphered_message_list):
        if letter.isalpha():
            value = alphabet.index(letter)
            cipher_value = value + offset
            if cipher_value > 25 or cipher_value < 0:
                cipher_value = cipher_value % 26
            ciphered_message_list[i] = alphabet[cipher_value]
    message = ''.join(ciphered_message_list)
    return str(message)


def calculate_entropy(entropy_string):
    total = 0
    for char in entropy_string:
        if char.isalpha():
            prob = frequency[char.lower()]
            total += - math.log(prob) / math.log(2)
    return total


def cracked(message):
    entropy_values = {}
    attempt_cache = {}
    message = message
    for i in range(25):
        message = message
        offset = i * -1
        test_cipher = cipher(offset, message)
        entropy_values[i] = calculate_entropy(test_cipher)
        attempt_cache[i] = test_cipher

    sorted_by_entropy = sorted(entropy_values, key=entropy_values.get)
    offset = sorted_by_entropy[0] * -1
    cracked_text = attempt_cache[sorted_by_entropy[0]]

    return cracked_text, offset
