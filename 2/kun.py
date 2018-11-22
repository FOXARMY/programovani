rychlost = float(input("Jak rychle běží kůň: " ) )

if rychlost < 0:
	print ("Kůň couvá.")

elif rychlost == 0:
	print ("Kůň stojí.")
	
elif rychlost <= 8:
	print ("Kůň jde")	

elif rychlost <= 15:
	print ("Kůň kluše")
	
elif rychlost <= 30:
	print ("Kůň cválá")
	
elif rychlost <= 31:
	print ("Téda ten uhání.")
	
elif rychlost <= 60:
	print ("To snad není možné!")
	
elif rychlost <= 99:
	print ("Neblábol!")
	
else:
	print ("Tady končím!")
