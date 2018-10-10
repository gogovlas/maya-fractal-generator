#apollonean_gasket.py
"""
-----------------------------------------------------------------------------------------------------
 Generates a visualization of a region of the Apollonean Gasket by printing spheres in space in Maya
-----------------------------------------------------------------------------------------------------
One function named run()
Parameters:
	max_Iteration - maximum number of cubes to print
	size - the size of our printing canvas
	
Script modified by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017

Original script source:
	FB36, 2012. Active State [online]. 
	Available from: http://code.activestate.com/recipes/578016-apollonian-gasket-fractal-using-ifs/ 
	[Accessed 13 February 2017]
"""

#******** IMPORT MODULES ********#
import maya.cmds as cmds
import random, math, numpy

#******** RUN APOLLONEAN GASKET REGION VISUALIZATION ********#
def run(max_Iteration, size):
	"""
	Generates a visualization of a region of the Apollonean Gasket by printing spheres in space in Maya
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
	
	# Initialize fractal variables
	s = math.sqrt(3.0)
	def f(z):
		return 3.0 / (1.0 + s - z) - (1.0 + s) / (2.0 + s)
	ifs = ["f(z)", "f(z) * complex(-1.0, s) / 2.0", "f(z) * complex(-1.0, -s) / 2.0"]
	xa = -0.6
	xb = 0.9
	ya = -0.75
	yb = 0.75
	z = complex(0.0, 0.0)
	
	# Create shader to paint spheres with
	shader=cmds.shadingNode("blinn",asShader=True, name = "shader" + str(1))
	attr = shader + ".color"
	cmds.setAttr (attr, 1,1,1)
	
	# Draw max_Iteration number of spheres
	for i in range(max_Iteration):
		# Compute z and kx, ky
		z = eval(ifs[random.randint(0, 2)]) 
		kx = int((z.real - xa) / (xb - xa) * (size - 1))
		ky = int((z.imag - ya) / (yb - ya) * (size - 1))
		# Update progress bar
		cmds.progressBar(progressControl, edit=True, step=1)
		# If kx and kz are within our drawing canvas draw sphere:
		if kx >=0 and kx < size and ky >= 0 and ky < size:
			cmds.polySphere(n="sp"+str(i))
			cmds.move(kx,0,ky)
			cmds.scale(0.5,0.5,0.5)   
			cmds.hyperShade(assign="shader"+str(1))
			
			# Update viewport
			cmds.viewFit( 'top', all=True )
			cmds.dolly( 'top', os=1.5 )
			cmds.refresh()
			
	# Update progress bar and viewport		
	cmds.progressBar(progressControl, edit=True, step=1)
	cmds.refresh()
	cmds.toggleWindowVisibility(window)