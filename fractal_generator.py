#fractal_generator.py
"""
-----------------------------------------------------------------------------------------
 Sets up the main interface for the Fractal Generator
-----------------------------------------------------------------------------------------
One function named help_Card()
Parameters:
	-
One function named home_Card()
Parameters:
	-

Script by Vlasis Gogousis [vgogousis@gmail.com]

MA3D o 2017
"""

#************************* IMPORT MODULES *************************#
import maya.cmds as cmds
import sys

#******** SETUP PATH VARIABLES TO CALL FILES AND MODULES LATER ON ********#
runtime_env = cmds.internalVar(usd =True)
icons = runtime_env + 'icons' # This is where the icons for the GUI are
fractals = runtime_env + 'fractal_functions' # This is where fractal functions are organized

sys.path.insert(0, fractals) # Add the fractals folder to Maya path

import fractal_UI # Import fractal UI module

#************************* HELP CARD *************************#
def help_Card():
	cmds.text("\nINTRODUCTION:\n", font = "boldLabelFont")
	cmds.text("Fractals are awesome!")
	cmds.text("Fractals are mathematical sets that exhibit a repeating pattern \ndisplayed at every scale",h=40,w=100,ww=1,al='center')
	cmds.text("What's wonderful about them -apart from their visual appeal- is the \nmathematical beauty and simplicity which describes them:\n",al='center')
	cmds.text("the mighty element of recursiveness\n",al='center', font = "obliqueLabelFont")
	cmds.text("Thanks to mathematical elegance, all fractals in this script\n are generated with just a few lines of code",al='center')
	cmds.text("\nINSTRUCTIONS:\n", font = "boldLabelFont")
	cmds.text("Select a fractal set from the \"Home\" tab\nSet parameters and generate results")
	cmds.text("\n\n\n\nby Vlasis Gogousis",al='center', font = "obliqueLabelFont")
	cmds.text("vgogousis@gmail.com",al='center', font = "obliqueLabelFont")
	cmds.text("\nMA3D o 2017",al='center', font = "obliqueLabelFont")
	
#************************* HOME CARD *************************#
def home_Card():
	# Layout a row element to insert text as column labels
	cmds.rowLayout( numberOfColumns=2)
	cmds.text("FRACTAL SETS", al='center',w = 300, font = "obliqueLabelFont")
	cmds.text("SAMPLE",al='center',w = 80, font = "obliqueLabelFont")
	cmds.setParent('..')
	# Layout a row element and insert fractal button and sample image in it
	cmds.rowLayout( numberOfColumns=2)
	cmds.button(label= "Julia Set", command='fractal_generator.fractal_UI.setup("Julia Set")', w = 300, h = 80)
	cmds.image(image=icons + '/julia_icon.png')
	cmds.setParent('..')
	# Layout a row element and insert fractal button and sample image in it
	cmds.rowLayout( numberOfColumns=2)
	cmds.button(label= "Mandelbrot Set", command='fractal_generator.fractal_UI.setup("Mandelbrot Set")', w = 300, h = 80)
	cmds.image(image=icons + '/mandelbrot_icon.png')
	cmds.setParent('..')
	# Layout a row element and insert fractal button and sample image in it
	cmds.rowLayout( numberOfColumns=2)
	cmds.button(label= "Barnsley Fern", command='fractal_generator.fractal_UI.setup("Barnsley Fern")', w = 300, h = 80)
	cmds.image(image=icons + '/fern_icon.png')
	cmds.setParent('..')
	# Layout a row element and insert fractal button and sample image in it
	cmds.rowLayout( numberOfColumns=2)
	cmds.button(label= "Apollonean Gasket", command='fractal_generator.fractal_UI.setup("Apollonean Gasket")', w = 300, h = 80)
	cmds.image(image=icons + '/apollonean_icon.png')
	cmds.setParent('..')
	# Layout a row element and insert fractal button and sample image in it
	cmds.rowLayout( numberOfColumns=2)
	cmds.button(label= "Sierpinski Triangle", command='fractal_generator.fractal_UI.setup("Sierpinski Triangle")', w = 300, h = 80)
	cmds.image(image=icons + '/sierpinski_icon.png')
	cmds.setParent('..')
	
	cmds.setParent('..')

#************************* GUI WINDOW *************************#
# Set dimension and name for the window
cWindow = cmds.window(title="Fractal Generator", width = 380, sizeable=False)

# Define somes tabs and format of them
tabs = cmds.tabLayout(innerMarginWidth=5,innerMarginHeight=5)

# Insert home card
Home = cmds.columnLayout(adj=True)
home_Card()

# Insert help card
HelpCard = cmds.columnLayout(adj=True)
help_Card()

# Set column hierarchy
cmds.setParent('..')
cmds.setParent('..')

# Set tab layout and name tabs
cmds.tabLayout(tabs,edit=True,tabLabel=((Home,"Home"),(HelpCard,"Help")))
cmds.showWindow(cWindow)