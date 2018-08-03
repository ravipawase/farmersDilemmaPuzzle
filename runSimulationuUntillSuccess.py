import puzzle
import runSimulation as rs


#success =0 
#fails = 0
#counter1 = 0
#while counter1 < 1000:
#	counter1 = counter1 + 1
#	result = rs.run_simulation()
#	if result:
#		success = success +1
#	else:
#		fails = fails +1
#print("success", "fails")
#print(success, fails)


print ("we are starting simulation")  #run untill success
counter1 = 0
result = False
#run series of simulations untill we get successful
while not result:
	counter1 = counter1 + 1
	result = rs.run_simulation()
	#print(counter1)
	
#result = rs.run_simulation()
