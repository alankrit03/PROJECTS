# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:19:25 2019

@author: Alankrit Agarwal
"""

from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import array


class coOrdinates():
    
    replay_button = (480,460)
    dinosuar = (189,439)    
    

def restartGame():
    pyautogui.click(coOrdinates.replay_button)
    
      
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    #  print('Jump')
    pyautogui.keyUp('space')
    
def imageGrab():
    box = (coOrdinates.dinosuar[0]+60,coOrdinates.dinosuar[1],coOrdinates.dinosuar[0]+100,coOrdinates.dinosuar[1]+30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a=array(grayImage.getcolors())
    print(a.sum())
    return(a.sum())
    
            
   
def main():    
    restartGame()
    while(True):
        if(imageGrab()!=1447):
            print(imageGrab())
            jump()
            time.sleep(0.1)
            
main()
