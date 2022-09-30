import mss
import mss.tools
import time

import win32api

while True:
    a = win32api.GetKeyState(0x26)  # up arrow key
    if a < 0:
        break

print('loop broken')

# # auto screenshot
# for i in range(20):
#     with mss.mss() as sct:
#         monitor = {"top":0, "left":0, "width":1920, "height":1080}
#         sct_img = sct.grab(monitor)

#         output = "D:\\important shit\\Python shit\\Aimlab_tf\\full_image_data_set\\sct" + str(i) + ".png".format(**monitor)

#         mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#     time.sleep(2.5)

# # input screenshot
# i = 0
# while True:
#     a = win32api.GetKeyState(0x26)  # up arrow key
#     if a < 0:
#         print('screenshot')
#         with mss.mss() as sct:
#             monitor = {"top":0, "left":0, "width":1920, "height":1080}
#             sct_img = sct.grab(monitor)

#             output = "D:\\important shit\\Python shit\\Aimlab_tf\\full_image_data_set\\sct_custom" + str(i) + ".png".format(**monitor)
#             mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
#         i += 1
#         time.sleep(0.5)
    