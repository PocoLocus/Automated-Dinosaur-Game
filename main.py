import pyautogui, time

region = (700, 870, 400, 150)
target_color = (83, 83, 83)

time.sleep(1)
while True:
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot_region.png")

    width, height = screenshot.size
    found = False
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if pixel_color == target_color:
                pyautogui.press('space')
                found = True
                break
        if found:
            break
    time.sleep(0.1)

