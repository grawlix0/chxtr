import subprocess

# Set the path of the FreeFileSync.exe command and the batch file
freefilesync_path = 'C:/Program Files/FreeFileSync/FreeFileSync.exe'
batch_file_path = 'D:/Work/backup configs/spoofer_outs_SyncSettings.ffs_batch'

# Run the FreeFileSync batch file
def do_copy():
    subprocess.run([freefilesync_path, batch_file_path])
    # k = subprocess.Popen([freefilesync_path, batch_file_path])
    # k.kill()

# do_copy()