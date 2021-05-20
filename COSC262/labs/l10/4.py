

class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
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
    return signed_area(p, a, b) == 0 and (min(a.x,b.x) <= p.x <= max(a.x,b.x)) and (min(a.y,b.y) <= p.y <= max(a.y,b.y))

def classify_points(st, end, pts):
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
    return (is_ccw(a,d,b) != is_ccw(a,c,b)) \
    and (is_ccw(c,a,d) != is_ccw(c,b,d))


def is_strictly_convex(verts):
    l=len(verts);return all(is_ccw(verts[i%l],verts[(i+1)%l],verts[(i+2)%l]) for i in range(l))


        
def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if (candidate is None) or signed_area(hull[-1], candidate, p) < 0:  # ** FIXME **
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    assert is_strictly_convex(hull)
    return hull


from functools import cmp_to_key  # Converts a cmp function to a key function

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



def simple_poly(points, start):
    points = list(points)#copy
    points.remove(start)
    points.sort(key=cmp_to_key)
    return [start] + points



def grahams(points):

    assert is_strictly_convex(hull),"fail"
    return hull



def cool_plot():
    import matplotlib.pyplot as plt
    from random import randint as r

    points = [
        Vec(r(0, 1000), r(0,1000))
        for x in range(15)
    ]

    hull = gift_wrap(points)

    plt.scatter([p.x for p in points], [p.y for p in points])
    plt.plot([v.x for v in hull + [hull[0]]], [v.y for v in hull + [hull[0]]])
    plt.show()


cool_plot()

