import djitellopy as tello
from time import sleep
drone = tello.Tello()
drone.connect()
battery = drone.get_battery()
print(battery)

