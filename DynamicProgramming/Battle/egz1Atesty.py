# egz1Atesty.py
from testy import *
from egz1Atest_spec import ALLOWED_TIME, TEST_SPEC, gentest

from copy import deepcopy


def copyarg( arg ):
    return deepcopy(arg)


def printarg(P,K,R):
    print("n             :\t", len(K))
    print("m             :\t", len(P))
    print("Procesory (P) :\t", limit(P))
    print("Katapulty (K) :\t", limit(K))
    print("Zasięgi   (R) :\t", limit(R))


def printhint( hint ):
    print("Prawidlowy wynik: ", hint)


def printsol( sol ):
    print("Wynik algorytmu : ", sol)


def check( K, P, R, hint, sol ):
    return hint == sol


def generate_tests(num_tests = None):
    global TEST_SPEC
    TESTS = []

    if num_tests is not None:
        TEST_SPEC = TEST_SPEC[:num_tests]

    for spec in TEST_SPEC:
        newtest = {}
        arg, hint = gentest(*spec)
        newtest["arg"] = arg
        newtest["hint"] = hint
        TESTS.append(newtest)


    return TESTS


def runtests( f, all_tests = True ):
    internal_runtests( copyarg, printarg, printhint, printsol, check, generate_tests, all_tests, f, ALLOWED_TIME )

