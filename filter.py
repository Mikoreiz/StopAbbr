inputfile = open("stops.txt")                    
outputfile = open("output.txt","w+") 

abarray = ["Fs/Nb","Ns/Nb"]


for line in inputfile:
	for abbreviation in abarray:
		if abbreviation in line:
			print(abbreviation,'found in',line)


			# depending on abbr distinguish NB EB SB WB direction
			# direction

			#example Fs/Nb -> NB
			# direction = NB

			line = line.replace(abbreviation,'NB') # replace NB with direction
			outputfile.write(line)


			

