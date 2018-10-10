#mandelbrot_set.py
"""
-----------------------------------------------------------------------------------------
 Generates a visualization of the Mandelbrot set by printing cubes in space in Maya
-----------------------------------------------------------------------------------------
One function named run()
Parameters:
	max_Iteration - maximum number of cubes to print 
	size - the size of our printing canvas
	c - complex variable of the formula z = z*z + c, which affects the result
	
Script modified by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017

Original script source:
	Borini, S., 2010. For The Science [online]. 
	Available from: http://forthescience.org/blog/2010/07/12/the-mandelbrot-set-in-python/ 
	[Accessed 13 February 2017]
"""

#******** IMPORT MODULES ********#
import maya.cmds as cmds
import numpy

#******** RUN MANDELBROT SET VISUALIZATION ********#
def run(max_iteration, size, c):
	"""
	Generates a visualization of the Mandelbrot set by printing cubes in space in Maya
	Parameters:
		max_Iteration - maximum number of cubes to print 
		size - the size of our printing canvas
		c - complex variable of the formula z = z*z + c, which affects the result
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
	
	# Set center of complex plane
	x_center = c.real
	y_center = c.imag
	# Run through the grid of our canvas size (size X size)
	for i in range(size):
		for j in range(size):
			# Re-evaluate c according to current 'pixel' to be drawn
			c = complex( x_center + 4.0*float(i-size/2)/size, y_center + 4.0*float(j-size/2)/size)
			
			# Initialize z and number of iterations
			z = 0 + 0j
			iteration = 0
			
			# While z is within our space boundaries and we have not exceeded our maximum iteration:
			while (abs(z) <= 2.0 and iteration < max_iteration):
				z = z**2 + c # Re-evaluate z, based on formula z = z*z + c
				iteration += 1  
				
			# Draw appropriate cube in space
			cmds.polyCube(n="cube"+str(i)+str(j))
			cmds.move(i,0,j) 
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

