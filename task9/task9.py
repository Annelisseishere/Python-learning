def roman2int(roman):
	# TODO: Given string representing a roman number convert it into decimal integer
	result: int = 0
	conversion_table={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
	
	for i in range(0, len(roman)-1):	
		if conversion_table[roman[i+1]] > conversion_table[roman[i]]:
			result -= conversion_table[roman[i]]
		else:
			result += conversion_table[roman[i]]
	result += conversion_table[roman[i+1]]		
			
	return result	

# Should print 1996
print(roman2int("MCMXCVI"))





###-----------------------------------------------------------------------------###

####--enumerate approach--####


#def roman2int(roman):
	# TODO: Given string representing a roman number convert it into decimal integer
	#result: int = 0
	#conversion_table={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
	
	#for i,ch in enumerate(roman[:-1]):	
		#if conversion_table[roman[i+1]] > conversion_table[ch]:
			#result -= conversion_table[ch]
		#else:
			#result += conversion_table[ch]
	#result += conversion_table[roman[i+1]]		
			
	#return result	

# Should print 1996
#print(roman2int("MCMXCVI"))