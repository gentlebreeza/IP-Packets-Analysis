from operator import itemgetter
size_of_package = 0 #initialize the size of the package
sourceIP = [['0', 0]] # initialize the source IP recorder
totalByte = 0 # to store the total byte

#open the file and read the lines into list
#test_bas.txt
#dec-pkt-1.tcp
file_object = open("dec-pkt-1.tcp")
while 1:
	line = file_object.readline()
	package = line.split()
	if not line:
		break
	size_of_package = int(package[-1]) + 40 # get the size of the package that is being executed
	totalByte += size_of_package
	source_ip = package[1] # get the source IP of the package that is being executed
	find_flag = False # setup a flag to test if the source IP has been recorded
	for item in sourceIP:
		if item[0] == source_ip: # if recorded, 
			item[1] += size_of_package
			find_flag = True
			break
	if not find_flag: #if not, add a new item to the source IP recorder
		new_item = [source_ip, size_of_package]
		sourceIP.append(new_item)

sourceIP.sort(key = itemgetter(1), reverse = True) # sort the source IP recorder

#output the answer for Task 1 D
print ' '
print 'Task 1 D)'
print 'The total Trafic is ' + str(totalByte) + ' bytes'
for x in range(3):
	print 'No.' + str(x + 1) + ' source IP: ' + sourceIP[x][0] + ' Traffic: ' + str(sourceIP[x][1]) + ' bytes' + ' Traffic Percentage: ' + '%.2f'%(sourceIP[x][1] * 100.0 / totalByte) + '%'