# for Task 1 A
totalByte = 0 #store the total byte
totalTime = 0 #store the total time

# for task 1 B
timeRound = 0 # to see how many 5 minutes have passed
byte_in_5_minute = 0 #store the bytes in 300 seconds
rate_per_5_minutes = [] # store the rate in every 5 minutes

#for task 1 C
totalNumber = 0 # the number of lines
distribution_of_package = {
	'0': 0,
	'1-127': 0,
	'128-255': 0,
	'256-383': 0,
	'384-511': 0,
	'512': 0
} 
def see_Distribution_of_size(size):
	if size == 0:
		distribution_of_package['0'] +=1
	if size >= 1 and size <= 127:
		distribution_of_package['1-127'] += 1
	if size >= 128 and size <= 255:
		distribution_of_package['128-255'] += 1
	if size >= 256 and size <= 383:
		distribution_of_package['256-383'] += 1
	if size >= 384 and size <= 511:
		distribution_of_package['384-511'] += 1
	if size == 512:
		distribution_of_package['512'] += 1

file_object = open("dec-pkt-1.tcp")
while 1:
	line = file_object.readline()
	if not line:
		totalTime = timeStamp
		average_bit_rate_5_minute = byte_in_5_minute * 8.0 / ((timeStamp - int(timeStamp)) * 1024) # get the average rate in the last round
		rate_per_5_minutes.append(average_bit_rate_5_minute) #store it
		break
	package = line.split()
	size_of_this_package = int(package[-1]) + 40 # get the size of the package that is being executed

	#for Task 1 A):
	totalByte += size_of_this_package  # calculate the total buytes

	#for Task 2 B)
	byte_in_5_minute += size_of_this_package
	timeStamp = float(package[0])
	if (timeStamp - 300 * timeRound) >= 300:
		average_bit_rate_5_minute = byte_in_5_minute * 8.0 / (300 * 1024) # get the average rate in the 5 minutes
		rate_per_5_minutes.append(average_bit_rate_5_minute) #store it
		byte_in_5_minute = 0 # reset the traffic counter
		timeRound += 1 # being through another 5 minutes

	# do the task of task 1 C
	totalNumber += 1
	see_Distribution_of_size(int(package[-1]))

#get the answer of Task 1 A

average_bit_rate = totalByte * 8.0 / totalTime

# output the answer of Task 1 A)
print 'Task 1 A): '
print 'The total time is ' + '%.2f'%totalTime + ' s'
print 'The total bytes is ' + str(totalByte) + ' Bytes'
print 'The average bit rate is ' + '%.2f'%average_bit_rate + ' bps'

# output the answer of Task 1 B)
print ' '
print 'Task 1 B): '
for t in rate_per_5_minutes:
	print 'the average bit rate in ' + str(0 + rate_per_5_minutes.index(t) * 300) + '-' + str(299 + rate_per_5_minutes.index(t) * 300) + 's is ' + '%.2f'%t + ' kbps'

#output the answer of Task 1 C
print ' '
print 'Task 1 C)'
for key in distribution_of_package:
	print 'the percentage of the package of size ' + key + ' is ' + '%.2f'%(distribution_of_package[key] * 100.0 / totalNumber) + '%'

