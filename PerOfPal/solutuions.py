from operator import le


def is_permutation_of_palindrome(phrase: str) -> bool:
    hash = {}
    conta_impar = 0
    for letter in phrase:
        if letter.lower() in hash:
            hash[letter.lower()] += 1
        else:
            if letter.isalpha():
                hash[letter.lower()] = 1

    for value in hash.values():
        if value % 2 != 0:
            conta_impar += 1

    # print(hash)
    if conta_impar <= 1:
        return True
    else:
        return False


print(is_permutation_of_palindrome("?qsSV  Vq<a>> ds!*DV :o;Ao"))
