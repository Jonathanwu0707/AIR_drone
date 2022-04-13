from asyncio import events
from cv2 import waitKey
from cvzone.SerialModule import SerialObject
from time import sleep
import keyboard as kbset
import pygame

pygame.init()
kbset.init()
pygame.joystick.init()

arduino = SerialObject("COM7", 9600)
clock = pygame.time.Clock()
joysticks = pygame.joystick.Joystick(0)
joysticks.init()
axiss= [0,0,0,0]

def getKeyBoardInput():
    global axiss
    # lr, fb, ud, yaw = 0, 0, 0, 0
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if(abs(event.value)<=1 and abs(event.value)>0.05):
                axiss[event.axis] = abs(int(event.value*50))
    if kbset.keyPressed("s"):
        axiss = [0,0,0,0]
    
    # if(abs(joysticks.get_axis(0))<=1 and abs(joysticks.get_axis(0))>=0.1):
    #     lr = joysticks.get_axis(0)*50
    # else: lr = 0
    # if(abs(joysticks.get_axis(1))<=1 and abs(joysticks.get_axis(1))>=0.1):
    #     fb = joysticks.get_axis(1)*50
    # else: fb = 0
    # if(abs(joysticks.get_axis(2))<=1 and abs(joysticks.get_axis(2))>=0.1):
    #     ud = joysticks.get_axis(2)*50
    # else: ud = 0
    # if(abs(joysticks.get_axis(3))<=1 and abs(joysticks.get_axis(3))>=0.1):
    #     yaw = joysticks.get_axis(3)*50
    # else: yaw = 0
    

        # another type to instore axis value(complex)
        '''if event.type == pygame.JOYAXISMOTION: 
            if event.axis == 0:
                fb = round(event.value, 2)       #move forward'''
        # elif event.type == pygame.JOYAXISMOTION: fb = -move      #move backward
        # else : fb = 0
        # if event.type == pygame.JOYAXISMOTION(3): ud = move         #up
        # elif event.type == pygame.JOYAXISMOTION(3): ud = -move      #down
        # if event.type == pygame.JOYAXISMOTION(2):yaw   = -move        #turn left
        # elif event.type == pygame.JOYAXISMOTION(2):yaw = move         #turn right
        # else : yaw = 0
    # #if kbset.keyPressed("l"):  drone.land()
    # #if kbset.keyPressed("f"): drone.takeoff()
    waitKey(500)
    return axiss
    



while True:
    '''for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            print(event)  #左搖桿 axis0:左右 axis1:前後; 右搖桿 axis2:左右 axis3:前後
        if event.type == pygame.JOYBUTTONDOWN:
            print(event)
        if event.type == pygame.JOYBUTTONUP:
            print(event)'''
    getKeyBoardInput()
    arduino.sendData(axiss)
    print(axiss)
    
    

    '''if(kbset.keyPressed("LEFT")):
        arduino.sendData([1])
        print("press light")
        sleep(1)
    elif(kbset.keyPressed("RIGHT")):
        arduino.sendData([0])
        print("press dark")
        sleep(1)
    else: 
        pass'''
    sleep(0.05)