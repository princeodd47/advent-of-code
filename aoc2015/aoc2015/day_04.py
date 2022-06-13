from . import common

import hashlib


def part1():
    secret_prefix = "ckczppom"
    print(_find_hash(secret_prefix, 5))
    # answer: 117946


def part2():
    secret_prefix = "ckczppom"
    print(_find_hash(secret_prefix, 6))
    # answer: 3938038


def _find_hash(secret_prefix, leading_zeroes):
    i = 1
    while True:
        secret = secret_prefix + str(i)
        m = hashlib.md5(secret.encode('ascii'))
        if _hash_meets_criteria(m, leading_zeroes):
            return i
        i += 1
    return 0


def _hash_meets_criteria(m, leading_zeroes):
    h = m.hexdigest()
    criteria = "0" * leading_zeroes
    if h.startswith(criteria):
        return True
    return False
