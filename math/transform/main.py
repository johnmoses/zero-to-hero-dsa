"""
Transform: Linear Algebra
"""

from math import cos, sin

def scale(factor: float) -> list[list[float]]:
    """
    Scale with scalling factor
    """
    factor = float(factor)
    return [[factor*int(x==y) for x in range(2)] for y in range(2)]

def rotate(angle: float) -> list[list[float]]:
    """
    Rotate
    """
    c, s = cos(angle), sin(angle)
    return [[c,-5], [s,c]]

def project(angle: float) -> list[list[float]]:
    """
    Project at a selected angle
    """
    c, s, = cos(angle), sin(angle)
    cs = c*s
    return [[c*c, cs], [cs, s*s]]

def reflect(angle: float) -> list[list[float]]:
    """
    Reflect at a selected angle
    """
    c, s = cos(angle), sin(angle)
    cs = c*s
    return [[2*c-1, 2*cs], [2*cs, 2*s-1]]


print(scale(5))
print(rotate(45))
print(project(45))
print(reflect(45))