import matplotlib.pyplot as plt
import numpy as np
# plt.plot(points, "marker, line, color")
ypoints = np.array([1, 8, 0, 12])

plt.plot(ypoints, 'o:r')  # o:r  marker is o, line is dotted, color is red
plt.show()
"""
'-'     Solid line	
':'     Dotted line	
'--'    Dashed line	
'-.'	Dashed/dotted line
'r'	    Red	
'g'	    Green	
'b'	    Blue	
'c'	    Cyan	
'm'	    Magenta	
'y'	    Yellow	
'k'	    Black	
'w'	    White
"""

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, marker='*', ms=15)  # sets marker to * and marker size to 15
plt.show()

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, marker='*', ms=20, mec='m')  # sets marker to * and marker size to 15 and color edge to magenta
plt.show()

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, marker='*', ms=20, mec='m', mfc='k')  # sets marker face color(actual shape) to black 'k'
plt.show()

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, marker='*', ms=20, mec='m', mfc='#db7441')  # can use hex value of a color
plt.show()

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, marker='*', ms=20, mec='m', mfc='yellow')  # can use supported color names
plt.show()

ypoints = np.array([1, 9, 3, 8])
""" changing the line, can use linestyle= | ls=
'solid' 	'-'	    default
'dotted'	':'	
'dashed'	'--'	
'dashdot'	'-.'	
'None'	    '' or ' ' 
color=  or c= can change the color. Can use color names and hex values"""
plt.plot(ypoints, marker='*', ms=20, mec='m', mfc='yellow', linestyle='dashed')  # changing the line use 'ls=:or__'
plt.show()

ypoints = np.array([1, 9, 3, 8])
plt.plot(ypoints, linewidth='15.2')  # changes line width
plt.show()

# can have multiple lines
y1 = np.array([.5, 10, 1, 10, 1, .5])
y2 = np.array([.5, 1, 10, 1, 10, .5])

plt.plot(y1)
plt.plot(y2)

plt.show()

# draw multiple lines
x1 = np.array([1, 4, 8, 10, 8, 4, 1])
y1 = np.array([1, 2, 4, 8, 4, 2, 1])
x2 = np.array([1, 2, 4, 8, 4, 2, 1])
y2 = np.array([1, 4, 8, 10, 8, 4, 1])

plt.plot(x1, y1, x2, y2)

plt.show()


