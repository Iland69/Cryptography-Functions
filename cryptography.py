from __future__ import annotations
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


def encrypt(string: str, k: str | int) -> str:
    """
    Encrypts a string using a key.
    Try to use a key that's longer than the string.
    The best practice is using a randomly generated key.
    """
    if isinstance(k, int):
        k = str(k)

    if isinstance(string, int):
        string = str(string)

    if not isinstance(string, str):
        raise TypeError("string must be a string")

    if not isinstance(k, str):
        raise TypeError("key must be a string or an integer")

    keyint = []
    for x in k:
        keyint.append(ord(x))

    strList = []
    for y in range(len(string)):
        try:
            strList.append(chr(ord(string[y]) + keyint[y]))
        except IndexError:
            strList.append(string[y])

    return "".join(strList)


def decrypt(string: str, k: str | int) -> str:
    """
    Decrypts a string using a key.
    """
    if isinstance(k, int):
        k = str(k)

    if isinstance(string, int):
        string = str(string)

    if not isinstance(string, str):
        raise TypeError("string must be a string")

    if not isinstance(k, str):
        raise TypeError("key must be a string or an integer")

    keyint = []
    for x in k:
        keyint.append(ord(x))

    strList = []
    for y in range(len(string)):
        try:
            strList.append(chr(ord(string[y]) - keyint[y]))
        except IndexError:
            strList.append(string[y])

    return "".join(strList)


def randStr(lenght: int) -> str:
    """
    Generates a random string of a given length.
    """
    if not isinstance(lenght, int):
        raise TypeError("lenght must be an integer")

    if lenght < 1:
        raise ValueError("lenght must be greater than 0")

    strList: list[chr] = []
    charList: str = ascii_lowercase + ascii_uppercase + digits
    for x in range(lenght):
        strList.append(choice(charList))

    return "".join(strList)


if __name__ == "__main__":
    msg = "Hello World!"
    print('Message: "Hello World!"')
    key = randStr(len(msg))
    print(f'Random key: "{key}"')
    enc = encrypt(msg, key)
    print(f'Encrypted: "{enc}"')
    dec = decrypt(enc, key)
    print(f'Decrypted: "{dec}"')
