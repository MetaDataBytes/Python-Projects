#import nltk
#nltk.download('words')
from nltk.corpus import words
from random import randint

def ceaser_cipher_encode(plain_text: str, alphabet: str) -> str:
    """
    PURPOSE: Create a ceaser cipher by shifting characters in the provided message a random number of positions
    ARGUMENT: plain_text: the plain text message to encript, alphabet: the charicters that make up the alphabet of the belived language
    RETURN: Encripted text
    """
    key = randint(1, len(alphabet) - 1)
    cipher_text = str()
    for character in plain_text.upper():
        if character in alphabet:
            idx = alphabet.find(character) + key
            if idx > 25: idx -= len(alphabet)
            cipher_text += alphabet[idx]
        else: cipher_text += character
    return cipher_text


def ceaser_cipher_decode(cipher_text: str, alphabet: str) -> None:
    """
    PURPOSE: Decode ceaser chipher text to plain text
    ARGUMENT: cipher_text: text to be decoded, alphabet: the alphabet to text against
    RETURN: None
    """
    decoded_messages = list()
    for key in range(len(alphabet)):
        plainText = str()
        for character in cipher_text: 
            if character in alphabet:
                idx = alphabet.find(character) - key
                if idx < 0: idx += len(alphabet)
                plainText = plainText + alphabet[idx]
            else: plainText = plainText + character
        decoded_messages.append({"key": key, "message": plainText, "score": 0})
    return score_decoded_messages(decoded_messages=decoded_messages)

def score_decoded_messages(decoded_messages: list) -> dict:
    """
    PURPOSE: Score the decoded messages and return the highest scored message (most english words)
    ARGUMENT: decoded messages: The decoded versions of the cipher text
    RETURN: The highest scored message
    """
    highest_score = 0
    for i in range(len(decoded_messages)):
        for word in decoded_messages[i]["message"].split():
            if word.lower() in words.words(): decoded_messages[i]["score"] += 1
        if decoded_messages[i]["score"] > decoded_messages[highest_score]["score"]: highest_score = i
    return decoded_messages[highest_score]

def print_message(cipher_text: str, plain_text: dict) -> None:
    """
    PURPOSE: Print the cipher and plain text with it's key
    ARGUMENT: cipher_text: The text in it's encryted form, plain_text: The text in it's plain form
    RETURN: None
    """
    print(f"CIPHER TEXT: {cipher_text}")
    print(f"PLAIN TEXT: {plain_text["message"]}")
    print(f"KEY: {plain_text["key"]}")