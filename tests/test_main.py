from cc_pathplanner import coverage_path_planner

def main():
	n_clusters=4	#number of sections
	r=2	#radius for Dubins curves
	input_file='sample_area.txt' #location of the input file containing coordinates of the field
	width = 10	#distance between tracks
	driving_angle=90	#angle wrt X-axis in degrees
	no_hd=0	#number of margins around boundary (each with distance=0.5*width) if needed, otherwise 0
	
	op=coverage_path_planner.cpp(input_file,num_hd=no_hd,width=width,theta=driving_angle,num_clusters=n_clusters,radius=r,visualize=False)
	print('The trajectory for full coverage consists of the following waypoints:',op)
	min=coverage_path_planner.find_min(input_file)
	print('Angle for trajectory with minimum length:', min)

if __name__ == '__main__':
	main()