# Create the outher list for all devices
devices_list = []
# Read in the devices from the file
file = open('devices-06.txt', 'r')
line = file.readline()
while line:    
    # Get device info into list
    device_info_list = list.strip().split(',')

    # Put device information into dictionary dor this one device
    device_info = {} # Create the inner dictionary od device info
    device_info['name'] = device_info_list[0]
    device_info['os-type'] = device_info_list[1]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]   

    # Append device and its info onto our 'devices' list
    devices_list.append(device_info)

    # Read the lines manually
    line = file.readline()

# Display heading
print('')
print('Name        os_type         IP address           software')
print('-----       -------    ------------------     --------------')

# Manually iterate through the indexes of list devices
index = 0
while index < len(devices_list):
    device = devices_list[index]
    print('{0:8}    {1:8}   {2:8}     {3:8}'.format(device[0], device[1], device[2], device[3]))
    index += 1

# Display a blank line to make easier to read
print('')
# Close the file
file.close()    