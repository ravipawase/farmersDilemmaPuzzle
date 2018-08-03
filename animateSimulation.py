# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib.patches as mpatches
import pandas as pd
import matplotlib

def getAnimation(df):
	#set the coordinates of the elements/content
	bank1Draw=20
	bank2Draw=80

	bank1X = 5
	bank2x = 82
	bank1InBoatX = 25
	bank2InBoatX = 65

	wolfY = 35
	goatY = 40
	cabbageY = 45 
	farmerY = 50

	boatBank1XY = (21, 21)
	boatBank2XY = (59, 21)
	boatWidth = 20
	boatHeight = 35

	# First set up the figure, the axis, and the plot element we want to animate
	fig = plt.figure()
	plt.clf()
	ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
	plt.vlines(bank1Draw,0, 100, lw=1)
	plt.vlines(bank2Draw,0, 100, lw=1)
	plt.xticks([])
	plt.yticks([])
	ax.axvspan(0, 20, alpha=0.8, color='green')
	ax.axvspan(80, 100, alpha=0.8, color='green')
	ax.axvspan(20, 80, alpha=0.5, color='blue')

	ax.text(3,5,"Bank1", color='k', fontsize=16, weight='bold' )
	ax.text(40,5,"River", color='k', fontsize=18, weight='bold' )
	ax.text(83,5,"Bank2", color='k', fontsize=16, weight='bold' )


	# wolf = ax.text(bank1X,wolfY, "Wolf", color='b')
	# goat = ax.text(bank1X,goatY, "Goat", color='r')
	# cabbage = ax.text(bank1X,cabbageY, "Cabbage", color='y')
	# rect = mpatches.Rectangle(boatBank1XY, boatWidth, boatHeight, angle=0.0, color='brown')
	# boat = ax.add_patch(rect)
	# farmer = ax.text(bank1X,farmerY, "Farmer", color='m')

	wolf = ax.text(bank1X,wolfY, "Wolf", color='k', fontsize=12 )
	goat = ax.text(bank1X,goatY, "Goat", color='k', fontsize=12)
	cabbage = ax.text(bank1X,cabbageY, "Cabbage", color='k', fontsize=12)
	rect1 = mpatches.Rectangle(boatBank1XY, boatWidth, boatHeight, angle=0.0, color='brown')
	boat = ax.add_patch(rect1)
	farmer = ax.text(bank1X,farmerY, "Farmer", color='k', fontsize=12)
	status = ax.text(21,90,"Simulation Status : Ongoing", color='k', fontsize=12 )
	rect2 = mpatches.Rectangle( (55, 88), 20, 8, angle=0.0, color='blue', alpha = 0.01)
	highlightPatch = ax.add_patch(rect2);

	#print(type(wolf))
	#print(type(goat))
	#print(type(cabbage))
	#print(type(rect))
	#wolf.set_data(20,20)
	#boat.set_xy((50,50))


	#read in the output log of simulation
	#df =pd.read_csv('puzzle.log')
	#print(df.head())
	#print(df.columns)

	#dfRow = df.iloc[0]
	#print(dfRow)
	#content = 'boat_pos'
	#if(dfRow[content] == 'bank1'):
	#	print("sucess")
	#else:
	#	print("double sucess")


	def getPos(content, df, rowNo):
		"""
		from log dataframe find out the position of the content
		Either bank1, bank2, bank1InBoat, bank2InBoat
		"""

		#add suffix pos if already does not exist
		if len(content.split('_')) == 2:
			if (content.split('_')[1] == 'pos'):
				pass
		else:
			content = content + '_pos'

		#get x coordinate
		#print(content)
		#print(dfRow[content])
		# print(dfRow[content].tolist())
		if content != 'boat_pos':
			if (df.iloc[rowNo][content] == 'bank1'):
				x = bank1X
			elif (df.iloc[rowNo][content] == 'bank2'):
				x = bank2x
			elif (df.iloc[rowNo][content] == 'boat'):
				if (df.iloc[rowNo]['boat_pos'] ==  'bank1'):
					x = bank1InBoatX
				else:
					x = bank2InBoatX
		else:
			if (df.iloc[rowNo][content] == 'bank1'):
				x, y = boatBank1XY
				#print(x,y)
			else:
				x, y = boatBank2XY
			#print(x,y)

		#get y coordinate
		if (content == 'wolf_pos'):
			y = wolfY
		elif (content == 'goat_pos'):
			y = goatY
		elif (content == 'cabbage_pos'):
			y = cabbageY
		elif (content == 'farmer_pos'):
			y = farmerY

		return x,y

	def getAnimationStatus(df, rowNo):
		if int(rowNo) == (len(df)-1):
			if(df.iloc[rowNo]['goat_pos'] == 'bank2' and df.iloc[rowNo]['wolf_pos'] == 'bank2' and df.iloc[rowNo]['cabbage_pos'] == 'bank2'):
				return 'Success'
			else:
				return 'Fail'
		else:
			return 'Ongoing'

	def getWhoIsDead(df, rowNo):
		if (df.iloc[rowNo]['goat_life_status'] == 'dead'):
			return 'goat'
		if (df.iloc[rowNo]['cabbage_life_status'] == 'dead'):
			return 'cabbage'

	def strikeout(text):
		result = ''
		for c in text:
			result = result + c + '\u0336'
		return result

	def animate(i):
		#print(getPos('boat', df, i))
		boat.set_xy((getPos('boat', df, i)))
		wolf.set_position(getPos('wolf', df, i))
		goat.set_position(getPos('goat', df, i))
		cabbage.set_position(getPos('cabbage', df, i))
		farmer.set_position(getPos('farmer', df, i))
		if (getAnimationStatus(df, i) == 'Success'):
			status.set_text("Simulation Status : Success")
			highlightPatch.set_color("green")
			highlightPatch.set_alpha(1)
		if (getAnimationStatus(df, i) == 'Fail'):
			status.set_text("Simulation Status : Fail")
			highlightPatch.set_color("red")
			highlightPatch.set_alpha(1)

			if (getWhoIsDead(df, i) == 'goat'):
				goat.set_text(strikeout('Goat'))
			if (getWhoIsDead(df, i) == 'cabbage'):
				cabbage.set_text(strikeout('Cabbage'))



	ani = matplotlib.animation.FuncAnimation(fig, animate, frames=len(df), interval=2000)
	os.remove('./puzzle.log')
	return ani

