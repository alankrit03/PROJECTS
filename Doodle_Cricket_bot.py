# @ Code Author: Alankrit Agarwal



from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import array

class co_ordinates():
    hit_button = (500 , 970)
    ball_check = ()

def restart_game():
    pyautogui.click(co_ordinates.hit_button)

def hit_the_ball():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def ballGrab():
    # box cordinates(top left corner , bottom right corner)
    # (left_x, top_y, right_x, bottom_y)
    check_box = (470 , 680 , 520 , 730)
    image = ImageGrab.grab(check_box)
    grey_image = ImageOps.grayscale(image)
    arr_sum = array(grey_image.getcolors()).sum()
    print(arr_sum)
    return arr_sum

def hit_ball_trial(): #just a trial function. Delete it afterwards
    while 1:
        pyautogui.keyDown('space')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        time.sleep(4.5)

def play_game():
    ball_point = ballGrab()
    if  (7000 < ball_point < 17000 ):
        hit_the_ball()

def check_ball_arrival():
    while 1:
        ballGrab()


def main():
    restart_game()
    while 1:
        #check_ball_arrival()
        play_game()


main()
