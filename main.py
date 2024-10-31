from PIL import Image, ImageGrab
import pyautogui, mss.tools
import time

num_pages = 128
wait_time = 2

X1 = 135
Y1 = 164
X2 = 735
Y2 = 920

X3 = 735
Y3 = 164
X4 = 1334
Y4 = 918

buttonX = 1410
buttonY = 545

box1 = (X1, Y1, X2, Y2)
box2 = (X3, Y3, X4, Y4)
im_list = []


# Arbitrary wait to allow for user to open page
time.sleep(5)
  

for i in range(2, num_pages*2+2, 2):
    print(i)
    # Next page
    pyautogui.click(x=buttonX, y=buttonY)

    # Arbitrary wait for loading
    time.sleep(wait_time)


    with mss.mss() as sct:

        im = sct.grab(box1)
        im2 = sct.grab(box2)

        # Save it!
        mss.tools.to_png(im.rgb, im.size, output=f"{i}.png")
        mss.tools.to_png(im2.rgb, im2.size, output=f"{i+1}.png")

