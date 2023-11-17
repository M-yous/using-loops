# Create the outer list for all devices
from os import close


devices_list = []

# Read in the devices from the file
file = open('devices-06.txt', 'r')
for line in file:
    # Get device info into list
    device_info_list = line.strip().split(',')
    devices_list.append(device_info_list)

# Display heading
print('')
print('Name        os_type         IP address           software')
print('-----       -------    ------------------     --------------')

# Go through the list of devices, printing out values in nice format
for device in devices_list:
    print('{0:8}    {1:8}   {2:8}     {3:8}'.format(device[0], device[1], device[2], device[3]))
# Close the file
file.close()
