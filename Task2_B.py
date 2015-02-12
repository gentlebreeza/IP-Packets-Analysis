bytes_in_5_minutes_set = [0, 0, 0, 0] #initialize a list to calculate the bytes
set_of_rate = [0, 0, 0, 0]
#lastline = package[-1]
#totalTime = float(lastline[0]) # the last timeStamp is the total time
timeRound = 0 # to see how many 5 minutes have passed
rate_per_5_minutes = []
port_number = 0
port_number_recorder = {'0': 0}
#open the file and put it into list
#test_bas.txt
#dec-pkt-1.tcp
file_object = open("dec-pkt-1.tcp")
while 1:
	line = file_object.readline()
	if not line:
		for x in range(4):
			rate = bytes_in_5_minutes_set[x] * 8.0 / ((timeStamp - int(timeStamp)) * 1024)
			set_of_rate[x] = rate
		rate_per_5_minutes.append(set_of_rate)
		break
	package = line.split()
	size_of_this_package = int(package[-1]) + 40 # get the size of the package that is being executed
	hash_r = package[1] + package[2] + package[3] + package[4]
	timeStamp = float(package[0])
	if hash_r in port_number_recorder:
		bytes_in_5_minutes_set[port_number_recorder[hash_r]] += size_of_this_package
	else:
		port_number_recorder[hash_r] = port_number
		bytes_in_5_minutes_set[port_number] += size_of_this_package
		port_number += 1
		port_number = port_number % 4
	if (timeStamp - 300 * timeRound) >= 300:
		for x in range(4):
			rate = bytes_in_5_minutes_set[x] * 8.0 / (300 * 1024)
			set_of_rate[x] = rate
		rate_per_5_minutes.append(set_of_rate)
		set_of_rate = bytes_in_5_minutes_set = [0, 0, 0, 0]
		timeRound += 1


print 'Task 2 B)'
for t in rate_per_5_minutes:
	diff = max(t) - min(t)
	print 'the average bit rate in ' + str(0 + rate_per_5_minutes.index(t) * 300) + '-' + str(299 + rate_per_5_minutes.index(t) * 300) + 's is p1: ' + '%.2f'%t[0] + ' kbps p2: ' + '%.2f'%t[1] + ' kbps p3: ' + '%.2f'%t[2] + ' kbps p4: ' + '%.2f'%t[3] + ' kbps Max Diff: ' + '%.2f'%diff +' kbps'

