#barnsley_fern.py
"""
-------------------------------------------------------------------------------------------
 Generates a visualization of the Barnsley Fern by printing spheres in space in Maya
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
import random, math, numpy

#******** RUN BARNSLEY FERN VISUALIZATION ********#
def run(max_Iteration, size):
	"""
	Generates a visualization of the Barnsley Fern by printing spheres in space in Maya
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
	
	# Setup matrix A containing appropriate affine transformations
	A=[]
	mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
		[0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
		[0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
		[-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]
	# Set starting point (x,y) = (0,0)
	x=0.0
	y=0.0
	
	# Draw max_Iteration number of spheres
	for iteration in range(max_Iteration):
		# Select random transformation to compute
		p=random.random()
		if p <= mat[0][6]:
			i=0
		elif p <= mat[0][6] + mat[1][6]:
			i=1
		elif p <= mat[0][6] + mat[1][6] + mat[2][6]:
			i=2
		else:
			i=3
		# Compute above transformation:
		x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
		y  = x * mat[i][2] + y * mat[i][3] + mat[i][5]
		x = x0
		
		# Draw corresponding sphere in space
		cmds.polySphere(n="sp"+str(iteration))
		cmds.move(size*x,0,-size*y)
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