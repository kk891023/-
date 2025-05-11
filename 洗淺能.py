import pyautogui
import pydirectinput
import cv2
import numpy as np
import time

# 設定模板比對門檻值
THRESHOLD = 0.8

def press_keys():
    pyautogui.click(1219, 637)
    time.sleep(0.3)
    pyautogui.click(1219, 637)
    pydirectinput.press('enter')
    time.sleep(0.4)
    pydirectinput.press('enter')
    time.sleep(0.4)
    pydirectinput.press('y')
    time.sleep(0.3)

def has_red_color(image, red_threshold=180, diff_threshold=60):
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            if r > red_threshold and (r - g) > diff_threshold and (r - b) > diff_threshold:
                return True
    return False

def capture_and_check_red():
    region = (781, 402, 820 - 781, 419 - 402)
    screenshot = pyautogui.screenshot(region=region)
    return has_red_color(screenshot)

def check_diaobao_opencv():
    region = (851, 406, 32, 11)
    screenshot = pyautogui.screenshot(region=region)
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    template = cv2.imread("diaobao_template.png")
    if template is None:
        print("❌ 無法讀取模板圖 diaobao_template.png")
        return False

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)

    print(f"🧪 模板比對相似度：{max_val:.3f}")
    return max_val >= THRESHOLD

# 主迴圈
try:
    while True:
        press_keys()

        if capture_and_check_red():
            print("🎯 偵測到紅色，繼續執行...")
            pydirectinput.press('esc')
            time.sleep(0.5)
        else:
            print("🔍 沒偵測到紅色，改用 OpenCV 偵測『掉寶』中...")
            time.sleep(0.5)
            if check_diaobao_opencv():
                print("📦 OpenCV 偵測到『掉寶』，暫停")
                time.sleep(0.5)
                break
            else:
                print("❌ 沒有偵測到『掉寶』，繼續")
                pydirectinput.press('esc')
                time.sleep(0.5)
                
        time.sleep(0.1)

except KeyboardInterrupt:
    print("🛑 手動中止程式。")
