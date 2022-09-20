#!/user/bin/env python3
#create a list
my_list = [ "192.168.0.5", 5060, "UP" ]

# print the first item of the list we created
print("The first item in the list (IP): " + my_list[0] )

# print the second item of the list
print("The second item in the list (port): " + str(my_list[1]) )

# print the last item of the list
print("The last item in the list (state): " + my_list[2] )

#create another list
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display only the IP addresses
print(f"IP addresses: {iplist[3]}, and {iplist[4]}")
