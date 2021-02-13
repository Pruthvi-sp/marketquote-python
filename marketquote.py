from datetime import datetime, timedelta

file = open("python_exercise_input.txt","r")
searchDate="01/07/2020"
convertedSDate= datetime.strptime(searchDate, '%Y/%m/%d')
instrumentName=[]
for line in file: 
  fields = line.split(";") 
  instrument = fields[0]
  iDate = fields[1]
  cDate=datetime.iDate.strftime('%Y/%m/%d')
  value = fields[2]
  if convertedSDate<cDate:
	count += 1
	instrumentName.append(instrument)
   else:
	print(instrument,"0")
file.close()
countnames = {}
for name in instrumentName:
    if name in countnames:
        countnames[name] += 1
    else:
        countnames[name] = 1

print(countnames) 