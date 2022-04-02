import pyautogui as auto
import time
import pyperclip

total_page = 521
book_name = 'ebook'
capture_pos = (686, 9)
ebook_screen_center_pos = (958, 500)
sleep_time = 1.0

time.sleep(5.)

##for i in range(int(total_page/2)):
for i in range(int(total_page)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)

    auto.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    auto.press('right')
    time.sleep(sleep_time)

    ##print(str(i+1), '/', int(total_page/2))
    print(str(i+1), '/', int(total_page))