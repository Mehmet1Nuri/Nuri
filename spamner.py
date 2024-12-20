import pyautogui
import time

# Kullanıcıya hazırlanması için zaman ver
print("5 saniye içinde metin girişi başlayacak. Hedef pencereye odaklanın.")
time.sleep(5)

# Girilecek metin
text = "WOIIIII SANTUYYY "
spammnumber = 500000

for i in range(spammnumber):
    pyautogui.typewrite(text)
    pyautogui.press('enter')
    time.sleep(0)  

print("Metin girişi tamamlandı.")
