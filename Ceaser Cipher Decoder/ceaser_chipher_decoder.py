from functions import ceaser_cipher_encode, ceaser_cipher_decode, print_message

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = "IF HE HAD ANYTHING CONFIDENTIAL TO SAY, HE WROTE IT IN CIPHER, THAT IS, BY SO CHANGING THE ORDER OF THE LETTERS OF THE ALPHABET, THAT NOT A WORD COULD BE MADE OUT."
    cipher_text = ceaser_cipher_encode(plain_text=plain_text, alphabet=alphabet)
    plain_text = ceaser_cipher_decode(cipher_text=cipher_text, alphabet=alphabet)
    print_message(cipher_text=cipher_text, plain_text=plain_text)