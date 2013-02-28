#Python patchwork coursework

Python coursework for Year 1 Introduction to Programming (INTPROG). Known issues:

- Swapping of tiles (advanced) will not work when swapping tiles that have already been swapped.

Coursework spec:

	##Main program requirements
	
	Your program should begin by prompting the user to enter:
	
	- the sample dimensions (i.e. the width & height in terms of patches);
	- the desired four colours (which your program should ensure are all different from each 	other).
	
	The program’s user interface should be friendly and robust; e.g., on entering invalid data, 	the user should be re-prompted until the entered data is valid. (Valid widths and heights 	are integers between 2 and 8, and valid colours are red, green, blue, yellow, magenta and 	cyan.) Once these details have been entered, the sample should be drawn in a graphics window 	of the appropriate size. For example, if the user enters a width of 6, a height of 3, and 	colours red, green, blue and yellow, then (in the case that your student number ends in 56) 	the sample shown above should be drawn in a graphics window of width 600 pixels and height 	300 pixels.
	
	##Advanced program features

	The above requirements are what I expect most students to attempt, and carry the vast 	majority of the marks for functionality. If you would like a further challenge for a few 	additional marks, then I encourage you to attempt this additional part.
	After the patchwork design has been drawn, you should allow the user to change it by 	clicking on the window with the mouse. To make a change, the user clicks within two separate 	patches. This should cause those two patches to be swapped (i.e. both the design and the 	colour). The user should be able to make as many patch swaps as they wish.