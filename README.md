# chxtr
a python plus freefilesync app to spoof test data on your window real time and save it to a nifty text file, ready to google

i recommend installing files on [this commit](https://github.com/grawlix0/chxtr/commit/e22f3d81cf66659649b13211143d1161415cdd0e) and [this file](https://github.com/grawlix0/chxtr/blob/main/SAMPLEspoofer_outs_SyncSettings.ffs_batch) to keep things simple as you proceed with steps below


## How to use FreeFileSync and edit the ffs_batch file
- Install the software from freefilesync.org
- Plugin your mobile phone to your PC via USB
- Note your device name as seen on the application
- On **line 31** of `SAMPLE....ffs_batch` [(this file)](https://github.com/grawlix0/chxtr/blob/main/SAMPLEspoofer_outs_SyncSettings.ffs_batch), change the string to the source folder for ex. `"D:\usr\docs\chxtr\output"` (i.e, where out.txt is generated and stored by the app)
- On **line 32** of the the above file, change the string to the destination folder for ex. `"mtp:\SamsungA54\SD Card\docs\chxtrsaves"` (i.e, where out.txt from the PC will be synced on your phone by the freefilesync software)
- ⚠️ Change the path value on line 5 of [kawpier.py](https://github.com/grawlix0/chxtr/blob/main/kawpier.py) to the path value of this `ffs_batch` file
- ⚠️ program might require creating directories `output` and `dump-imgs` to function without errors (just make these two empty folders in the same level directory where the code files are)
  - `output` stores the `out.txt` text file
  - `dump-imgs` stores the screenshots of your window (you can chose to sync these images if tesseract setup is unsuccessful, and google lens them via your phone)

## Dependencies
- PyAutoGUI
- Pillow (PIL)
- win32api
- external software - FreeFileSync, Tesseract/PyTesseract
- ... maybe others too

I would basically dump this code into a folder then run `start.bat` or `agent.py` (remove the w from .pyw in the original files) and install the dependencies one by one. I'd appreciate if any of you come back and update this section of the README with your findings.

## How it works
- Double click `agent.pyw` or `start.bat`
- the app is now running in the background
- connect your phone via USB to your PC (watch for a system tray icon from FreeFileSync showing syncing between your phone and PC)
- the initial loading can take upto two minutes
- every right click you make stores a picture of your screen
- all discernible text is OCRd into an `out.txt` file
- the `out.txt` file is synced in sequence for every click you make (i.e, for every new output)
- you should see the text file in the designated folder on your phone after 2 - 3 seconds
- open the file on a convenient reader app and select and google away!
