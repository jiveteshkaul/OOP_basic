import rapper_class
import sys


def main():
	print("Inside Main")
	print("Initializing 1st rapper")
	
	gul=rapper_class.rappers("Bhura","kya bolte","Gully_Boy","20-12-1997",1234567,"Dharavi","azadi")
	sher=rapper_class.rappers("Fair","Hard","MC Sher","12-11-1991",23345152,"Bombay 70","Kalam")
	
	gul.musical_details()
	gul.personal_details()
	sher.musical_details()
	sher.personal_details()

	gul.farmaish("Meri Gully me")
	sher.farmaish("Wide awake")
	
if __name__ == '__main__':
	main()