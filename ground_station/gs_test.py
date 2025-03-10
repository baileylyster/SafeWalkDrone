'''
Run this script once MAVProxy has alread been started up on the RPi to check that everything on the groundstation
side is working and to check the status of the drone
'''

print( "Start simulator (SITL)") 
import dronekit_sitl
sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()
#connection_string = "tcp:10.242.25.163:1204" #get rpi zerotier ip and port
connection_string = "tcp:10.242.215.212:14550" #get rpi zerotier ip and port
#connection_string = "tcp:127.0.0.1:12000"
# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.
print(("Connecting to vehicle on: %s" % (connection_string,))) 
vehicle = connect(connection_string, wait_ready=True)

# Get some vehicle attributes (state)
print( "Get some vehicle attribute values:") 
print( " GPS: %s" % vehicle.gps_0) 
print( " Battery: %s" % vehicle.battery) 
print( " Last Heartbeat: %s" % vehicle.last_heartbeat) 
print( " Is Armable?: %s" % vehicle.is_armable) 
print( " System status: %s" % vehicle.system_status.state) 
print( " Mode: %s" % vehicle.mode.name )   # settable

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator
sitl.stop()
print("Completed")