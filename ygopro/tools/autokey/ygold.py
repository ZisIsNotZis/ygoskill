from time import sleep
sleep(3)
while True:
    mouse.click_relative(300, 317, 1) # 决斗者查卡器
    sleep(3)
    mouse.click_relative(273, 772, 1) # 决斗者查卡器
    sleep(1)
    mouse.click_relative(273, 772, 1) # 决斗者查卡器
    sleep(1)
    mouse.click_relative(291, 422, 1) # 决斗者查卡器
    sleep(1)
    mouse.click_relative(21, 35, 1) # 决斗者查卡器
    sleep(1)
    keyboard.send_keys("<down>")
    sleep(1)