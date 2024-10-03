import pyautogui
import time

# Kullanıcıya hazırlanması için zaman ver
print("2 saniye içinde metin girişi başlayacak. Hedef pencereye odaklanın.")
time.sleep(5)

# Girilecek metin
text = "WOIIIII SANTUYYY "
spammnumber = 500000


for i in range(spammnumber):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(0)  # Her girişten sonra kısa bir bekleme

print("Metin girişi tamamlandı.")



# import pyautogui
# import time


# time.sleep(5)

# for i in range(2029):
#     pyautogui.typewrite("woaaaw")
#     pyautogui.hotkey('enter')
#     # pyautogui.press('tab')
#     time.sleep(0)  # Her girişten sonra kısa bir bekleme