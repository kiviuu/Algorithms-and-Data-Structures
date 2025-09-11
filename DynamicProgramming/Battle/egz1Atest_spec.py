# egz1Atest_spec.py

ALLOWED_TIME = 100


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
    (0,0,0,0,0,3),
    (20, 40, 30, 4, 10, 6),
    (50, 40, 70, 10, 30, 12),
    (150, 40, 70, 20, 50, 45),
    (500, 40, 70, 20, 50, 150),
    (1500, 40, 70, 20, 150, 434),
    (5000, 20, 40, 20, 150, 907),
    (15000, 20, 40, 20, 150, 2772),
    (50000, 20, 40, 20, 150, 9063),
    (150000, 20, 40, 5, 10, 17947),
    (150000, 20, 40, 10, 20, 22769),
]


def gentest(nm, p, p1, r1, r2, hint):
    from testy import MY_random

    if nm==0:
        K = [2, 12, 4]
        R = [8,  5, 3]
        P = [14, 16, 0, 6, 10, 8]
        return [P,K,R], 3
    else:
        K = []
        R = []
        P = []

        POS = list(range(nm))
        KK = []
        for j in range(nm):
            ind = MY_random() % len( POS )
            i = POS[ind]
            POS[ind] = POS[-1]
            POS.pop()
            
            pos = 3*i + ( MY_random() % 3 )
            if MY_random() % 100 < p:
                # katapulta
                K.append( pos )
                if MY_random() % 100 < p1:
                    r = 1+MY_random() % r1
                else:
                    r = 1+MY_random() % r2
                R.append( r )
            else:
                P.append( pos )
            
    return [P,K,R],hint
    

