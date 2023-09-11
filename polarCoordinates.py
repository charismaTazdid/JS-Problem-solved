# Problem: https://www.hackerrank.com/challenges/polar-coordinates

import cmath


def polarCoordinates(z):
    r = abs(complex(z))
    varphi = cmath.phase(complex(z))
    print(r)
    print(varphi)


if __name__ == '__main__':
    z = complex(input())
    result = polarCoordinates(z)
