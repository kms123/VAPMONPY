def PressureAverage(pressure_readings, percentage = 85): #Percentage is an optional argument

	peak_pressure = max(pressure_readings) #Finds peak pressure value from input list
	percent_mult = percentage/100 
	
	dataset = [] #Create empty list
	for value in pressure_readings: #Iterate list of pressure_readings
		if (value >= percent_mult*peak_pressure): #If a value is within percentage of peak_pressure then accumulate into dataset
			dataset.append(value)
	
	average = sum(dataset)/len(dataset) #Take average of dataset
	
	return average
	
test = 0

if (test == 1):
	testlist = list(range(1,101))
	print(pressure_averager(testlist))
	

