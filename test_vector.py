from math import pi, sqrt
from vector import *

def _almost_equal(p1, p2, epsilon=1e-10):
	pt = add_points(p1, invert_point(p2))
	return abs(pt.x) < epsilon and abs(pt.y) < epsilon

def test_vector_from_point():
	assert vector_from_point(Point(3, 5), Point(5, 5)) == Vector(2, 0)
	assert vector_from_point(Point(3, 5), Point(3, 7)) == Vector(2, pi/2)
	assert vector_from_point(Point(3, 5), Point(1, 5)) == Vector(2, pi)
	assert vector_from_point(Point(3, 5), Point(3, 3)) == Vector(2, 3*pi/2)

def test_vector_to_point():
	assert _almost_equal(vector_to_point(Vector(1, 0)), Point(1, 0))
	assert _almost_equal(vector_to_point(Vector(1, pi/2)), Point(0, 1))
	assert _almost_equal(vector_to_point(Vector(1, pi)), Point(-1, 0))
	assert _almost_equal(vector_to_point(Vector(1, 3*pi/2)), Point(0, -1))

def test_vector_offset_point():
	assert _almost_equal(vector_offset_point(Point(3, 5), Vector(1, 0)), Point(4, 5))
	assert _almost_equal(vector_offset_point(Point(3, 5), Vector(1, pi/2)), Point(3, 6))
	assert _almost_equal(vector_offset_point(Point(3, 5), Vector(1, pi)), Point(2, 5))
	assert _almost_equal(vector_offset_point(Point(3, 5), Vector(1, 3*pi/2)), Point(3, 4))

def test_vector_wind_up():
	assert vector_wind_up(Vector(1, 0.1), Vector(1, 2*pi)) == Vector(1, 2*pi+0.1)
	assert vector_wind_up(Vector(1, 0), Vector(1, 2*pi)) == Vector(1, 2*pi)
	assert vector_wind_up(Vector(1, -0.1), Vector(1, 2*pi)) == Vector(1, 2*pi - 0.1)
	
	assert vector_wind_up(Vector(1, 20*pi+0.1), Vector(1, 2*pi)) == Vector(1, 2*pi+0.1)
	assert vector_wind_up(Vector(1, 20*pi), Vector(1, 2*pi)) == Vector(1, 2*pi)
	assert vector_wind_up(Vector(1, 20*pi-0.1), Vector(1, 2*pi)) == Vector(1, 2*pi - 0.1)

if __name__=="__main__":
	test_vector_from_point()
	test_vector_to_point()
	test_vector_offset_point()
	test_vector_wind_up()
