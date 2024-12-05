import pyautogui, time
# (700, 870, 330, 150)
region = (900, 1000, 100, 10)
target_color = (83, 83, 83)

time.sleep(1)
while True:
    screenshot = pyautogui.screenshot(region=region)
    # screenshot.save("screenshot_region.png")

    width, height = screenshot.size
    found = False
    for x in reversed(range(width)):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if pixel_color == target_color:
                pyautogui.press('space')
                found = True
                break
        if found:
            break
    time.sleep(0.05)

