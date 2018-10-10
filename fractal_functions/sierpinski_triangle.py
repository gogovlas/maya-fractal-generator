#sierpinski_triangle.py
"""
-------------------------------------------------------------------------------------------
 Generates a visualization of the Sierpinski triangle by printing spheres in space in Maya
-------------------------------------------------------------------------------------------
One function named run()
Parameters:
	max_Iteration - maximum number of cubes to print 
	size - the size of our printing canvas
	
Script by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017
"""

#******** IMPORT MODULES ********#
import maya.cmds as cmds
import numpy as np
from random import randint

#******** RUN SIERPINSKI TRIANGLE VISUALIZATION ********#
def run(max_Iteration, size):
	"""
	Generates a visualization of the Sierpinski triangle by printing cubes in space in Maya
	Parameters:
		max_Iteration - maximum number of cubes to print 
		size - the size of our printing canvas
	"""
	# Initialize scene
	cmds.file(new = True, force = True)
	cmds.lookThru( 'top' )
	cmds.grid(toggle=False)
	
	# Setup window for progress bar
	window = cmds.window()
	cmds.columnLayout()
	progressControl = cmds.progressBar(maxValue=max_Iteration, width=300)
	cmds.showWindow(window)
	
	# Create shader to paint spheres with
	shader=cmds.shadingNode("blinn",asShader=True, name = "shader" + str(1))
	attr = shader + ".color"
	cmds.setAttr (attr, 1,1,1)
	
	# Calculates the midpoint of point1 and point2 and returns result
	def midpoint(point1, point2):
		return [(point1[0] + point2[0])/2, (point1[1] + point2[1])/2]
	
	# Set starting point for Sierpinski algorithm
	curr_point = [0,0]  

	# Define an equilateral triangle in space
	v1 = [0,0]
	v2 = [1,0]
	v3 = [.5,np.sqrt(3)/2]

	# Draw max_Iteration number of spheres 
	for i in range(max_Iteration):
		val = randint(0,2) # Select random vertex of our equilateral triangle
		# Calculate midpoint of above vertex and our current point:
		if val == 0:
			curr_point = midpoint(curr_point, v1)
		if val == 1:
			curr_point = midpoint(curr_point, v2)
		if val == 2:
			curr_point = midpoint(curr_point, v3)
			
		# Draw corresponding sphere in space
		cmds.polySphere(n="sp"+str(i))
		cmds.move(size*curr_point[0], 0, size*curr_point[1])
		cmds.scale(0.5,0.5,0.5)   
		cmds.hyperShade(assign="shader"+str(1))
		
		# Update progress bar and viewport
		cmds.progressBar(progressControl, edit=True, step=1)
		cmds.viewFit( 'top', all=True )
		cmds.dolly( 'top', os=1.5 )
		cmds.refresh()
	# Update progress bar and viewport	
	cmds.progressBar(progressControl, edit=True, step=1)
	cmds.refresh()
	cmds.toggleWindowVisibility(window)