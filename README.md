# chxtr
a python plus freefilesync app to spoof test data on your window real time and save it to a nifty text file, ready to google

## How to use FreeFileSync and edit the ffs_batch file
- Install the software from freefilesync.org
- Plugin your mobile phone to your PC via USB
- Note your device name as seen on the application
- On **line 31** of `SAMPLE....ffs_batch`, change the string to the source folder for ex. `"D:\usr\docs\chxtr\output"` (i.e, where out.txt is stored)
- On **line 32** of the the above file, change the string to the destination folder for ex. `"mtp:\SamsungA54\SD Card\docs\chxtrsaves"` (i.e, where out.txt from the PC will be synced on your phone)

## Dependencies
- PyTesseract
- PyAutoGUI
- Pillow (PIL)
- win32api
- external software - FreeFileSync
... maybe others too

I would basically dump this code into a file then run `start.bat` or `agent.py` (remove the w from .pyw in the original files) and install the dependencies one by one. I'd appreciate if on of you come back and update this section of the README with your findings.
