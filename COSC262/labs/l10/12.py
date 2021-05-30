

class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        "e"
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        ":)"
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        ":)"
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        ":)"
        return self.dot(self)

    def __str__(self):
        ":)"
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y


def is_on_segment(p, a, b):
    ":)"
    return signed_area(p, a, b) == 0 and (min(a.x,b.x) <= p.x <= max(a.x,b.x)) and (min(a.y,b.y) <= p.y <= max(a.y,b.y))

def classify_points(st, end, pts):
    ":))"
    lefts = 0
    rights = 0
    
    # left = AC+ve when signed_area(st, end, p).
    for p in pts:
        if signed_area(st, end, p) > 0:
            lefts += 1
        else:
            rights += 1
    return (rights, lefts)



def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def is_ccw_inc(a,b,c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area >= 0 


def intersecting(a,b,c,d):
    ":))))"
    return (is_ccw(a,d,b) != is_ccw(a,c,b)) \
    and (is_ccw(c,a,d) != is_ccw(c,b,d))


def is_strictly_convex(verts):
    ":)))"
    lenn=len(verts)
    return all(is_ccw(verts[i%lenn],verts[(i+1)%lenn],verts[(i+2)%lenn]) for i in range(lenn))


        

import matplotlib.pyplot as plt

from functools import cmp_to_key  # Converts a cmp function to a key function


def plot_poly(points):
    """Plot the given set of points as a closed polygon"""
    plt.plot([v.x for v in points + [points[0]]], [v.y for v in points + [points[0]]])
    plt.show()

def simple_polygon(points):
    "ret simple polyyyyyyyyyy"
    points = type(points)(points) # make copy
    anchor = min(points, key = lambda p: (p.y, p.x))

    def cmp(p1, p2):
        """Compares two points with respect to a globally defined anchor point.
        Returns a negative, zero or positive value according to whether p1 is
        to the right of p2 ("p1 < p2"), collinear with it ("p1 == p2") or to
        the left ("p1 > p2").
        """
        v1 = p1 - anchor
        v2 = p2 - anchor
        if v1.lensq() == 0:   # Is p1 the anchor point (or a copy of it)?
            return -1         # Yes. Make sure anchor point < everything else
        elif v2.lensq() == 0: # Is p2 the anchor point (or a copy of it)?
            return +1         # Yes, Make sure all other points > anchor
        else:  # In all other cases, return the negative of the usual area
            return v2.x * v1.y - v1.x * v2.y  # This is negative if p1 < p2

    points.sort(key=cmp_to_key(cmp))
    return points


def graham_scan(points):
    ":)"
    poly = simple_polygon(points)
    assert len(poly)>=3, "EH? scuse me ?"
    stack = [poly[0],poly[1],poly[2]]

    searched = set()
    i=2
    while poly[-1] not in searched and i<len(poly):
        searched.add(poly[i])
        while not is_ccw(stack[-2],stack[-1],poly[i]):
            # then its a right turn
            stack.pop()
        stack.append(poly[i])
        i+=1
    return stack
