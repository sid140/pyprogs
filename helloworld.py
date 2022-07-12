
import ctypes
import errno
from urllib import response
#Defining DLL 
user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("kernel32.dll")

HWnd = None
IpText = "Hello World"
IpCaptions = "Hello Students"
uType = 0x00000003
Response = user_handle.MessageBoxW(HWnd,IpText,IpCaptions,uType)
error = k_handle.GetLastError()

if error != 0:
    print("Error".format(error))
exit(1)

if response == 1:
    print("User clicked OK")

elif response == 2:
    print("User cancelled")