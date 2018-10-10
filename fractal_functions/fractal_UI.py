#fractal_UI.py
"""
-----------------------------------------------------------------------------------------
 Sets up an interface to control variables for any given fractal experiment
-----------------------------------------------------------------------------------------
One function named setup()
Parameters:
	fractal_type - the type of fractal that triggered the setup window
One function named sliders()
Parameters:
	-

Script by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017
"""

#************************* IMPORT MODULES *************************#
import maya.cmds as cmds
import numpy # numpy is imported to describe complex numbers and evaluate mathematical expressions later on

#******** DICTIONARY OF COMMENTS FOR ALL FRACTAL TYPES ********#
comments = {"Julia Set":["Based on the formula z' = z*z + c,\nwhere c is a constant complex number\nNamed after French mathematician\nGaston Julia", 10, 30, 0.0, 0.65, "c real part (constant):","c imaginary part (constant):"], 
			"Mandelbrot Set":["Based on the formula z' = z*z + c,\nwhere c is a complex number\nthat changes in relation to space\nNamed after French-American mathematician\nBenoit Mandelbrot", 10, 30, -0.5, 0.0, "c real part (start point):","c imaginary part (start point):"],
			"Barnsley Fern":["Named after British mathematician Michael Barnsley", 1000, 10],
			"Apollonean Gasket":["Named after Greek mathematician Apollon of Perga\n(Region of Apollonean Gasket)", 500, 100],
			"Sierpinski Triangle":["Named after Polish mathematician Waclaw Sierpinski", 1000, 100]}

#******** GLOBAL VARIABLES FOR SILDERS AND FRACTAL TYPE ********#
v_a = None
v_b = None
v_c_re = None
v_c_im = None
fractal = None

#************************* SETUP FRACTAL INTERFACE *************************#
def setup( fractal_type ):
	global v_a, v_b, fractal, v_c_re, v_c_im
	# Import appropriate fractal module
	if fractal_type == "Julia Set":
		import julia_set as fractal
	elif fractal_type == "Mandelbrot Set":
		import mandelbrot_set as fractal
	elif fractal_type == "Barnsley Fern":
		import barnsley_fern as fractal
	elif fractal_type == "Apollonean Gasket":
		import apollonean_gasket as fractal
	elif fractal_type == "Sierpinski Triangle":
		import sierpinski_triangle as fractal
	#reload(fractal)
	
	# Set dimension and name for the window
	cWindow = cmds.window(title=fractal_type, wh=(300,400), sizeable=False)
	cmds.columnLayout(adj=True)
	
	# Print comment for specific fractal
	cmds.columnLayout(adj=True)
	cmds.text("\n"+comments[fractal_type][0]+"\n",bgc=[0.2,0.2,0.2])
	cmds.separator( h=10, style='none' ) 
	cmds.setParent('..')
	
	# Layout standard sliders for all fractal types
	cmds.columnLayout(adj=True)
	cmds.text(label="Number of iterations: ")
	v_a = cmds.intSliderGrp(field=True,minValue=1,maxValue=100,fieldMinValue=1, fieldMaxValue=10000,value=comments[fractal_type][1])
	cmds.text(label="Canvas size: ")
	v_b = cmds.intSliderGrp(field=True,minValue=1,maxValue=100,fieldMinValue=1, fieldMaxValue=10000,value=comments[fractal_type][2])
	cmds.separator( h=10, style='none' ) 
	cmds.setParent('..')
	
	# Layout fractal specific sliders
	if fractal_type == "Julia Set" or fractal_type == "Mandelbrot Set" :
		cmds.columnLayout(adj=True)
		cmds.text(comments[fractal_type][5])
		v_c_re = cmds.floatSliderGrp(field=True,minValue=-3,maxValue=3,fieldMinValue=-100, fieldMaxValue=100,value=comments[fractal_type][3])
		cmds.text(comments[fractal_type][6])
		v_c_im = cmds.floatSliderGrp(field=True,minValue=-3,maxValue=3,fieldMinValue=-100, fieldMaxValue=100,value=comments[fractal_type][4])
		cmds.separator( h=10, style='none' ) 
		cmds.setParent('..')
	
	# Layout 'Run' button that triggers appropriate fractal function
	cmds.button(label= "Run!", command='fractal_generator.fractal_UI.sliders()')
	cmds.separator( h=10, style='none' ) 
	cmds.setParent('..')
	cmds.setParent('..')
	cmds.showWindow(cWindow)

#************************* GET SLIDER VALUES AND RUN EXPERIMENT *************************#
def sliders():
	global fractal
	global v_a , v_b, v_c_re, v_c_im
	# Get standard fractal variables
	VA = cmds.intSliderGrp(v_a,q=True,v=True)
	VB = cmds.intSliderGrp(v_b,q=True,v=True)
	# Get fractal specific variables
	if fractal.__name__ == "julia_set" or fractal.__name__ == "mandelbrot_set" :
		V_C_RE = cmds.floatSliderGrp(v_c_re,q=True,v=True)
		V_C_IM = cmds.floatSliderGrp(v_c_im,q=True,v=True)
		fractal.run(VA,VB,complex(V_C_RE,V_C_IM)) # Run appropriate fractal function
	else:
		fractal.run(VA,VB) # Run appropriate fractal function