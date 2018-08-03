import copy
import random

class puzzle:

	def __init__(self):
		"""
		Initialize the environment of puzzle
		"""
		self.goat_pos = "bank1"			#possible/allowed positions will be bank1, bank2, boat
		self.wolf_pos = "bank1"
		self.cabbage_pos = "bank1"
		self.farmer_pos = "bank1"
		self.boat_pos = "bank1"		#possible/allowed positions will be bank1, bank2, river

		#add attributes to represent the status of each being as live, dead
		self.goat_life_status = "alive"
		self.cabbage_life_status = "alive"



	def board_boat(self, passenger):
		"""
		Simulate the boarding of passenger by updating the data structure
		"""
		
		if passenger == "goat":
			if self.goat_pos == self.boat_pos:
				self.goat_pos = "boat"
				
		if passenger == "wolf":
			if self.wolf_pos == self.boat_pos:
				self.wolf_pos = "boat"
			
		if passenger == "cabbage":
			if self.cabbage_pos == self.boat_pos:
				self.cabbage_pos = "boat"
		
		if passenger == "farmer":
			if self.farmer_pos == self.boat_pos:
				self.farmer_pos = "boat"



	def deboard_boat(self, passenger):
		"""
		Simulate the deboarding of passenger by updating the data structure
		"""
		
		if passenger == "goat":
			if self.goat_pos == "boat":
				self.goat_pos = copy.deepcopy(self.boat_pos)
				
		if passenger == "wolf":
			if self.wolf_pos == "boat":
				self.wolf_pos = copy.deepcopy(self.boat_pos)
			
		if passenger == "cabbage":
			if self.cabbage_pos == "boat":
				self.cabbage_pos = copy.deepcopy(self.boat_pos)
		
		if passenger == "farmer":
			if self.farmer_pos == "boat":
				self.farmer_pos = copy.deepcopy(self.boat_pos)



	def toggle_boat_pos(self):
		"""
		Simulate the boat moving from one bank of river to other by updating the data structure
		"""
		if self.boat_pos == "bank1":
			self.boat_pos = "bank2"
		
		else:
			if self.boat_pos == "bank2":
				self.boat_pos = "bank1"



	def __iter__(self):
		for attr, value in self.__dict__.items():
			yield (attr, value)



	def get_pos_lists(self):
		"""
		get the list of 'content' on each  bank and boat
		"""
		
		bank1 = []
		bank2 = []
		boat =[]
		for (attr, value) in iter(self):
			if value == "bank1":
				bank1.append(attr)
			if value == "bank2":
				bank2.append(attr)
			if value == "boat":
				boat.append(attr)
			
		bank1_content = [attr.split('_')[0] for attr in bank1]
		bank2_content = [attr.split('_')[0] for attr in bank2]
		boat_content = [attr.split('_')[0] for attr in boat]
	
		return bank1_content, bank2_content, boat_content

	def get_status(self, StatusContent = 'body'):
		"""
		get the status of each "content"
		"""
		if StatusContent == 'body':
			attrList = []
			valueList = []
			for (attr, value) in iter(self):
				attrList.append(attr)
				valueList.append(value)
			#print(attrList)
			return valueList+["\n"]
			#return attrList+valueList+["\n"]
		else:
			if StatusContent == 'header':
				attrList = []
				for (attr, value) in iter(self):
					attrList.append(attr)	
				return attrList+["\n"]


	def print_status(self):
		"""
		Print the positional status on the screen
		"""
		bank1_content, bank2_content, boat_content = self.get_pos_lists()
		
		#break this function into get headcount
		
		bank1_content = " ".join(bank1_content)
		bank2_content = " ".join(bank2_content)
		boat_content = " ".join(boat_content)
		print ("bank1 ", bank1_content)
		print ("boat ", boat_content)
		print ("bank2 ", bank2_content)
		print("*"*80)
		

		


	def lord_of_the_flies(self):
		"""
		Let "contents" on the banks interact according to their natural behavior" 
		"""
		
		bank1_content, bank2_content, boat_content = self.get_pos_lists()
		
		#list all the conditions which can result into violence
		
		#check on bank1
		if ((all(x in bank1_content for x in ['wolf', 'goat'])) and not (self.farmer_pos == "bank1" or (self.boat_pos == "bank1" and self.farmer_pos == 'boat'))):
			self.goat_life_status = "dead"
		if ((all(x in bank1_content for x in ['goat', 'cabbage'])) and not (self.farmer_pos == "bank1" or (self.boat_pos == "bank1" and self.farmer_pos == 'boat'))):
			self.cabbage_life_status = "dead"

		#check on bank2
		if ((all(x in bank2_content for x in ['wolf', 'goat'])) and not (self.farmer_pos == "bank2" or (self.boat_pos == "bank2" and self.farmer_pos == 'boat'))):
			self.goat_life_status = "dead"
		if ((all(x in bank2_content for x in ['goat', 'cabbage'])) and not (self.farmer_pos == "bank2" or (self.boat_pos == "bank2" and self.farmer_pos == 'boat'))):
			self.cabbage_life_status = "dead"



	def board_or_not(self):
		"""
		Decide to board any 'content' or not
		"""
		return random.choice([False, True])



	def let_the_dice_roll_boarding(self):
		"""
		Randomly choose what 'content' to board the boat
		Consider on which bank boat is currently while doing that
		"""
		
		#get 'content on that bank'
		bank1_content, bank2_content, boat_content = self.get_pos_lists()
		
		if self.boat_pos == "bank1":
			current_bank_list = bank1_content
		if self.boat_pos == "bank2":
			current_bank_list = bank2_content
		if "boat" in current_bank_list:
			current_bank_list.remove("boat")
		
		#choose one content randmly from that bank
		if(len(current_bank_list) >=1):
			return random.choice(current_bank_list)
		else:
			return None


	def get_content_onboard(self):
		"""
		Get what 'content' is onboard, so it can be passed to deboard method
		"""
		bank1_content, bank2_content, boat_content = self.get_pos_lists()
		if(len(boat_content) > 1):
			boat_content.remove("farmer")
			return boat_content[0]
		else:
			return None



	def all_is_well(self):
		"""
		Check if all 'content' is alive
		"""
		status_list = [value for attr, value in self.__dict__.items()  if  attr.endswith('status')]
		if 'dead' in status_list:
			return False
		else:
			return True


	def is_it_succes(self):
		"""
		Check if number of 'contents' on bank2 is 3
		"""
		bank1_content, bank2_content, boat_content = self.get_pos_lists()
		
		if("boat" in bank2_content):
			bank2_content.remove("boat")
			
		if (len(bank2_content) == 3):
			return True
		else:
			return False
