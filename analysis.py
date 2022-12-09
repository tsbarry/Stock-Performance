import csv
import statistics
import matplotlib.pyplot as plt 
#APPLE
AAPL_data = []
with open("AAPL.csv", "r") as infile:
  reader = csv.DictReader(infile)
 # save this dictReader object into a list of dictionaries to analyze
  for row in reader:
    AAPL_data.append(row)

print(AAPL_data)
    
i = 0
AAPL_std_data = []
while i < len(AAPL_data):
  try:
     day1 = float(AAPL_data[i]["Closing_Price"])
     day2 = float(AAPL_data[i + 1]["Closing_Price"])
     day3 = float(AAPL_data[i + 2]["Closing_Price"])
     day4 = float(AAPL_data[i + 3]["Closing_Price"])
     day5 = float(AAPL_data[i + 4]["Closing_Price"])
#calculate the population standard deviation
     pop_stdev = statistics.pstdev([day1,day2,day3,day4,day5])
     AAPL_std_data.append(pop_stdev)
     i += 5 
  except:
    break
print(AAPL_std_data)

#AMAZON
AMZN_data = []
with open("AMZN.csv", "r") as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    AMZN_data.append(row)

print(AMZN_data)
    
i = 0
AMZN_std_data = []
while i < len(AMZN_data):
  try:
     day1 = float(AMZN_data[i]["Closing_Price"])
     day2 = float(AMZN_data[i + 1]["Closing_Price"])
     day3 = float(AMZN_data[i + 2]["Closing_Price"])
     day4 = float(AMZN_data[i + 3]["Closing_Price"])
     day5 = float(AMZN_data[i + 4]["Closing_Price"])

     pop_stdev = statistics.pstdev([day1,day2,day3,day4,day5])
     AMZN_std_data.append(pop_stdev)
     i += 5 
  except:
    break
print(AMZN_std_data)

#CLOVER
CLOV_data = []
with open("CLOV.csv", "r") as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    CLOV_data.append(row)

print(CLOV_data)
    
i = 0
CLOV_std_data = []
while i < len(CLOV_data):
  try:
     day1 = float(CLOV_data[i]["Closing_Price"])
     day2 = float(CLOV_data[i + 1]["Closing_Price"])
     day3 = float(CLOV_data[i + 2]["Closing_Price"])
     day4 = float(CLOV_data[i + 3]["Closing_Price"])
     day5 = float(CLOV_data[i + 4]["Closing_Price"])

     pop_stdev = statistics.pstdev([day1,day2,day3,day4,day5])
     CLOV_std_data.append(pop_stdev)
     i += 5 
  except:
    break
print(CLOV_std_data)

#DINSNEY
DIS_data = []
with open("DIS.csv", "r") as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    DIS_data.append(row)

print(DIS_data)
    
i = 0
DIS_std_data = []
while i < len(DIS_data):
  try:
     day1 = float(DIS_data[i]["Closing_Price"])
     day2 = float(DIS_data[i + 1]["Closing_Price"])
     day3 = float(DIS_data[i + 2]["Closing_Price"])
     day4 = float(DIS_data[i + 3]["Closing_Price"])
     day5 = float(DIS_data[i + 4]["Closing_Price"])

     pop_stdev = statistics.pstdev([day1,day2,day3,day4,day5])
     DIS_std_data.append(pop_stdev)
     i += 5 
  except:
    break
print(DIS_std_data)

#GOOGLE
GOOGL_data = []
with open("GOOGL.csv", "r") as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    GOOGL_data.append(row)

print(GOOGL_data)
    
i = 0
GOOGL_std_data = []
while i < len(GOOGL_data):
  try:
     day1 = float(GOOGL_data[i]["Closing_Price"])
     day2 = float(GOOGL_data[i + 1]["Closing_Price"])
     day3 = float(GOOGL_data[i + 2]["Closing_Price"])
     day4 = float(GOOGL_data[i + 3]["Closing_Price"])
     day5 = float(GOOGL_data[i + 4]["Closing_Price"])

     pop_stdev = statistics.pstdev([day1,day2,day3,day4,day5])
     GOOGL_std_data.append(pop_stdev)
     i += 5 
  except:
    break
print(GOOGL_std_data)


#using matplotlib to graph the standard deviation of each stock
plt.plot(AAPL_std_data) 
plt.xlabel("Dates")
plt.ylabel("Standard dev")
plt.title("Apple stock")
plt.show()

plt.plot(AMZN_std_data) 
plt.xlabel("Dates")
plt.ylabel("Standard dev")
plt.title("Amazon stock")
plt.show()

plt.plot(CLOV_std_data) 
plt.xlabel("Dates")
plt.ylabel("Standard dev")
plt.title("Clover stock")
plt.show()

plt.plot(DIS_std_data) 
plt.xlabel("Dates")
plt.ylabel("Standard dev")
plt.title("Disney stock")
plt.show()

plt.plot(GOOGL_std_data) 
plt.xlabel("Dates")
plt.ylabel("Standard dev")
plt.title("Google stock")
plt.show()


