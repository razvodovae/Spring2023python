import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if not i.isalpha():
            ciphertext += i
            continue
        wasupper = False
        if i.isupper():
            wasupper = True
        i = i.lower()
        n = ord(i)
        if n + shift <= 122:
            candidate = chr(n + shift)
        else: candidate = chr(n - 26 + shift)
        if wasupper:
            candidate = candidate.upper()
        ciphertext += candidate

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if not i.isalpha():
            plaintext += i
            continue
        wasupper = False
        if i.isupper():
            wasupper = True
        i = i.lower()
        n = ord(i)
        if n - shift >= 97:
            candidate = chr(n - shift)
        else: candidate = chr(n + 26 - shift)
        if wasupper:
            candidate = candidate.upper()
        plaintext += candidate

    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    return best_shift