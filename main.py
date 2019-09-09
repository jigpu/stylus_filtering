import matplotlib.pyplot as plt
from point import *
import filters
import point_array
import noise
import os

def squared_difference(point_array_1, point_array_2):
	assert len(point_array_1) == len(point_array_2)
	squared_delta = 0
	for p_id, p1 in enumerate(point_array_1):
		p2 = point_array_2[p_id]
		squared_delta += squared_dist_points(p1, p2)
	return squared_delta / len(point_array_1)


def run_and_plot_filter(noisy_shape, filtered_shape, shape, run_name, name):
	
	comparison = squared_difference(filtered_shape, shape)
	
	plt.clf()
	
	filtered_shape_x, filtered_shape_y = point_array.point_array_to_axis_arrays(filtered_shape)
	shape_x, shape_y = point_array.point_array_to_axis_arrays(shape)
	noisy_shape_x, noisy_shape_y = point_array.point_array_to_axis_arrays(noisy_shape)

	plt.plot(shape_x, shape_y, 'g')
	plt.gca().set_autoscale_on(False)
	plt.plot(noisy_shape_x, noisy_shape_y, 'rx')
	plt.plot(filtered_shape_x, filtered_shape_y, 'b')

	plt.title(name + ' (Average Delta = {:.02f})'.format(comparison))
	
	directory = "output/{}".format(run_name)
	if not os.path.exists(directory):
		os.makedirs(directory)
	plt.savefig("{}/{}.png".format(directory, name))


def generate_box():
	""" Generates a predetermined zigzag line that can be used to test """
	points = []
	points.extend(point_array.generate_line_segment(Point(0, 0), Point(0, 5), 20))
	points.extend(point_array.generate_line_segment(Point(0, 5), Point(5, 5), 20))
	points.extend(point_array.generate_line_segment(Point(5, 5), Point(5, 0), 20))
	return points


def run_filters(shape, noisy_shape, run_name):
	test_cases = [
	  ("No Filter", filters.null_filter()),
	  ("Reference (Median Filter 4 Samples)", filters.mean_filter(4))
	]
	for smoothing in [0.5, 0.8]:
		for prediction in [0.5, 0.8]:
			test_cases.append(
			  ("Predictive Filter (predict={}, smooth={})".format(prediction, smoothing),
			   filters.simple_predictive_filter(prediction, smoothing))
			)
	for fc in [0.6]:
		test_cases.append(
		  ("Exp Filter {}".format(fc), filters.exp_filter(fc))
		)

	#for case in [*test_cases]:
	#	test_cases.append(("{} (Vector)".format(case[0]), filters.vector_filter(case[1])))
	test_cases.append(("Exp Vector 0.1", filters.vector_filter(filters.exp_filter(0.1))))
	test_cases.append(("Exp Vector 0.2", filters.vector_filter(filters.exp_filter(0.2))))
	test_cases.append(("Exp Vector 0.3", filters.vector_filter(filters.exp_filter(0.3))))
	test_cases.append(("Exp Vector 0.4", filters.vector_filter(filters.exp_filter(0.4))))
	test_cases.append(("Exp Vector 0.5", filters.vector_filter(filters.exp_filter(0.5))))
	test_cases.append(("Exp Vector 0.6", filters.vector_filter(filters.exp_filter(0.6))))

	for case in test_cases:
		run_and_plot_filter(noisy_shape, filters.filter_array(case[1], noisy_shape), shape, run_name, case[0])


if __name__ == "__main__":
	shape = generate_box()
	
	for seed in range(10):
		distortion = noise.generate_noise_array(noise.white_noise(seed, 0.2), len(shape))
		noisy_shape = point_array.sum_point_arrays(distortion, shape)
		
		run_filters(shape, noisy_shape, "seed={} Noise=0.2".format(seed))
	
	run_filters(shape, shape, "NoNoise")
