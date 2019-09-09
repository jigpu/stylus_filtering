from collections import namedtuple
from math import sqrt, cos, sin, atan2, pi

from point import *

# Create a datatype to represent an immutable polar vector
Vector = namedtuple("Vector", ["r", "theta"])


def vector_from_point(p1, p2):
	""" Return a vector that points from Point p1 to p2 """
	pt = add_points(invert_point(p1), p2)
	r = sqrt(pt.x * pt.x + pt.y * pt.y)
	theta = atan2(pt.y, pt.x)
	if theta < 0:
		theta += 2*pi
	return Vector(r, theta)

def vector_to_point(v1):
	""" Get the cartesian coordinates of the head of a vector
	originating at (0,0) """
	return Point(v1.r * cos(v1.theta), v1.r * sin(v1.theta))

def vector_offset_point(p1, v1):
	return add_points(p1, vector_to_point(v1))

def vector_as_point(v1):
	return Point(v1.r, v1.theta)

def point_as_vector(p1):
	return Vector(p1.x, p1.y)

def vector_wind_up(v1, v2):
	""" Return a copy of v1 with its theta angle wound up or down
	by multiples of 2*pi until it is maximally close to v2.theta.
	Hides the 2*pi discontinuity from linear functions. """
	dt = (v1.theta / 2*pi) % 1
	
	return Vector(v1.r, v2.theta + 

	theta = v1.theta
	while theta - v2.theta > 2*pi:
		theta -= 2*pi
	while v2.theta - theta > 2*pi:
		theta += 2*pi
	return Vector(v1.r, theta)
