from time import sleep
sleep(3)
while True:
    for i in range(4):
        mouse.click_relative(850, 604+i*70, 1) # 决斗者查卡器
        sleep(3.5)
        mouse.click_relative(1467, 1096, 1) # 决斗者查卡器
        sleep(1)
        mouse.click_relative(1467, 1096, 1) # 决斗者查卡器
        sleep(1)
        mouse.click_relative(1467, 1096, 1) # 决斗者查卡器
        sleep(1)
        mouse.click_relative(971, 609, 1) # 决斗者查卡器
        sleep(1)
    mouse.click_relative(850, 604, 5) # 决斗者查卡器
    sleep(1)
