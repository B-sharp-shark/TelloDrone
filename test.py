import djitellopy as tello
import KeyPressModule as kp
import cv2
global img

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

def getKeyboardInput():
    lr, fb, ud, yx = 0, 0, 0, 0
    speed = 50

    if kp.getKey('LEFT'):
        lr = -speed
    elif kp.getKey('RIGHT'):
        lr = speed
    if kp.getKey('UP'):
        fb = speed
    elif kp.getKey('DOWN'):
        fb = -speed
    if kp.getKey('u'):
        ud = speed
    elif kp.getKey('d'):
        ud = -speed
    if kp.getKey('t'):
        drone.takeoff()
    if kp.getKey('l'):
        drone.land()
    if kp.getKey('y'):
        yx = speed
    if kp.getKey('f'):
        drone.flip_forward()

    return [lr, fb, ud, yx]




while True:
    vals= getKeyboardInput()
    print(vals)
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("drone feed", img)
    cv2.waitKey(1)