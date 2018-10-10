#julia_set.py
"""
-----------------------------------------------------------------------------------------
 Generates a visualization of the Julia set by printing cubes in space in Maya
-----------------------------------------------------------------------------------------
One function named run()
Parameters:
	max_Iteration - maximum number of cubes to print 
	size - the size of our printing canvas
	c - constant complex variable of the formula z = z*z + c, which affects the result
	
Script modified by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017

Original script source:
	Burke, T., 2013. Batchloaf [online]. 
	Available from: https://batchloaf.wordpress.com/2013/02/10/creating-julia-set-images-in-python/ 
	[Accessed 13 February 2017]
"""

#******** IMPORT MODULES ********#
import maya.cmds as cmds
import numpy

#******** RUN JULIA SET VISUALIZATION ********#
def run(max_iteration, size, c):
	"""
	Generates a visualization of the Julia set by printing cubes in space in Maya
	Parameters:
		max_Iteration - maximum number of cubes to print 
		size - the size of our printing canvas
		c - constant complex variable of the formula z = z*z + c, which affects the result
	"""
	# Initialize scene
	cmds.file(new = True, force = True)
	cmds.lookThru( 'top' )
	cmds.grid(toggle=False)
	
	# Setup window for progress bar
	window = cmds.window()
	cmds.columnLayout()
	progressControl = cmds.progressBar(maxValue=size**2, width=300)
	cmds.showWindow(window)
	
	# Create shades of grey to paint cubes with based on depth
	for i in range(max_iteration+1):
		shader=cmds.shadingNode("blinn",asShader=True, name = "shader" + str(i))
		attr = shader + ".color"
		cmds.setAttr (attr, i/float(max_iteration), i/float(max_iteration), i/float(max_iteration))
	 
	# Specify real and imaginary range of image
	re_min, re_max = -2.0, 2.0
	im_min, im_max = -2.0, 2.0
	scX = (abs(re_min) + abs(re_max))/size
	scZ = (abs(im_min) + abs(im_max))/size
	 
	# Generate evenly spaced values over real and imaginary ranges
	real_range = numpy.arange(re_min, re_max, (re_max - re_min) / size)
	imag_range = numpy.arange(im_max, im_min, (im_min - im_max) / size)
	 
	# Run through the grid of our canvas size (size X size)
	for im in imag_range:
		for re in real_range:
			# Initialize z (according to complex plane) and number of iterations
			z = complex(re, im) 
			iteration = 0
			
			# While z is within our space boundaries and we have not exceeded our maximum iteration:
			while abs(z) < 10 and iteration < max_iteration:
				z = z*z + c
				iteration +=1
			
			# Draw appropriate cube in space
			cmds.polyCube(n="cube"+str(im)+str(re))
			cmds.move(im,0,re)
			cmds.scale(scX,0.1,scZ)   
			cmds.hyperShade(assign="shader"+str(iteration))
			
			# Update progress bar and viewport
			cmds.progressBar(progressControl, edit=True, step=1)
			cmds.viewFit( 'top', all=True )
			cmds.dolly( 'top', os=1.5 )
			cmds.refresh()
			
	# Update progress bar and viewport		
	cmds.progressBar(progressControl, edit=True, step=1)
	cmds.refresh()
	cmds.toggleWindowVisibility(window)