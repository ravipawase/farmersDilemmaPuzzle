import puzzle


def run_simulation(logfile = True):

	#create a fileobject for logfile
	with open("puzzle.log", 'w') as logfile:
		#intiate puzzle
		p1 = puzzle.puzzle()
		p1.board_boat("farmer")
		#p1.print_status()
		logfile.write(",".join(p1.get_status(StatusContent = 'header')))		
		logfile.write(",".join(p1.get_status()))

		counter=0
		while 1:
			counter = counter + 1	
			#deboard 'content' if any
			c2 = p1.get_content_onboard()
			p1.deboard_boat(c2)
	
			#print("content is being boarded to boat")
			c1 = p1.let_the_dice_roll_boarding()
			#print(c1)
			p1.board_boat(c1)
			#p1.print_status()
			logfile.write(",".join(p1.get_status()))
			p1.toggle_boat_pos()
			#p1.print_status()
			logfile.write(",".join(p1.get_status()))
			p1.lord_of_the_flies()
			logfile.write(",".join(p1.get_status()))
			if not p1.all_is_well():
				#print("someone got killed")
				#print(counter)
				return False
				#break
	
	
			#print("content is de-boarding")
			d1 = p1.get_content_onboard()
			#print(d1)
			p1.deboard_boat(d1)
			#p1.print_status()
			logfile.write(",".join(p1.get_status()))
			#put check here about aliveness and completion
			if p1.is_it_succes():
				#print("Solved")
				#print(counter)
				return True
				#break


			if p1.board_or_not():
				#print("content is being boarded to boat from bank2")
				c1 = p1.let_the_dice_roll_boarding()
				#print(c1)
				p1.board_boat(c1)
			#p1.print_status()
			logfile.write(",".join(p1.get_status()))
	
	
			p1.toggle_boat_pos()
			p1.lord_of_the_flies()
			#p1.print_status()
			logfile.write(",".join(p1.get_status()))
			if not p1.all_is_well():
				#logfile.write(",".join(p1.get_status()))
				#print("someone got killed")
				#print(counter)
				return False
				#break
