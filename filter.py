import re
inputfile = open("stops.txt")                    
outputfile = open("output.txt","w+") 


# abarray = ["Fs/Nb","Ns/Nb"]
#abarray = ["Fs/Nb","Ns/Nb", "Ns Nb", "Fs Nb", "Fs/ Nb","Ns/ Nb","Ns/Wb"]
abarray = ["Fs/Nb","Fs/ Nb", "Mb/Nb", "Mb Nb", "Ns/Nb", "Ns Nb",
		   "Nb Mb", "NbNs", "Nb Ns", "F/Nb", "Fs Nb", "Nb Fs", "FsNb","NsEb",
		   "Ns/Eb", "Ns Eb", "Mb/Eb", "Mb Eb", "Eb/Fs", "Eb Fs", "Fs/Eb",
           "Fs/ Eb", "Fs Eb", "FsEb", "Ns Sb", "NsSb", "Ns/Sb", "FsSb", "Fs/Sb",
           "Fs Sb", "Sb Fs", "Sb/Ns", "Sb Ns", "Mb/Sb", "Mb Sb", "Ns Wb", "NsWb",
           "Ns/Wb", "Wb/Ns", "Wb/Fs", "Fs Wb", "FsWb", "Fs/Wb", "Fs W", "Mb/Wb",
           "Mb Wb",]


for line in inputfile:
	for abbreviation in abarray:
		if abbreviation in line:
			# print(abbreviation,'found in',line)
			# depending on abbr distinguish NB EB SB WB direction
			# direction
			#example Fs/Nb -> NB
			# direction = NB
			splitAbbrev = re.split('/| ', abbreviation)
			
			
			
			#[nb eb sb wb]
	
			newAbbrev = splitAbbrev[-1].upper()
			print(newAbbrev)
			line = line.replace(abbreviation,newAbbrev) # replace NB with direction
			outputfile.write(line)
			


			

