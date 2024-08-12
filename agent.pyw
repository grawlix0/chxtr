import seer
import reader
import time
import win32api
import kawpier
count = 0
state_left = win32api.GetKeyState(
    0x01
)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(
    0x02
)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)  # Left
    b = win32api.GetKeyState(0x02)  # Right

    if a != 0 and a != 1:  # Button state changed
        time.sleep(0.25)
        seer.take_screenshot(seer.get_file_path())
        count += 1
        time.sleep(1.5)
        # print("passing file"+ seer.latest_file_path)
        reader.read_text_from_image_and_append_to_file(
            seer.latest_file_path, reader.reads_file_path
        )
        a = state_left
        kawpier.do_copy()
        # print("total writes ---", count, end="\r")
    else:
        continue
