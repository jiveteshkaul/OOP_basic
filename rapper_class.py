import sys, time

class rappers:
	def __init__(self,
				 complex,
				 fav_line,
				 stage_name,
				 dob,
				 worth,
				 origin,
				 last_song
				 ):				 	
				
		self.complexion=complex
		self.favourite_line=fav_line
		self.stage_name=stage_name
		self.dob=dob
		self.net_worth=worth
		self.origin=origin
		self.last_song=last_song
		
	def musical_details(self):
		print("Here are the musical details for your rapper: \n")
		print ("Last song was : {0}".format(self.last_song))
		print ("Originally From : {0}".format(self.origin))
		print ("favourite line is : {0}".format(self.favourite_line))
		print ("Thanks for your interest............Bye")
		
	def personal_details(self):
		print("Here are the personal details for your rapper: \n")
		print ("Last song was : {0}".format(self.last_song))
		print ("Complexion is : {0}".format(self.complexion))
		print ("DOB is : {0}".format(self.dob))
		print ("Current Worth is : {0}".format(self.net_worth))

	def farmaish(self,gana_bolo):
		print ("Lo fir farmaish: \n")
		print ("Yo .....yo.........yo......your boy {0} is here .....{1}".format(self.stage_name, gana_bolo))
		print ("Thanks Thanks")
	

		
		
		
		
		

		
				 