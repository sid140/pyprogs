import webbrowser
import time
print("Netgear Router login".upper())
print("=" *20)
print("Developed by Sid".strip().title())
print("=" *20)
print("For options please type Netgear")
print("For direct link type 1")
print("For secondary link type 2")
print("For web link type 3")
print("For support type help")

user_input = input("Please enter the option: ")

url1 = "http://192.168.1.1"
url2= "http://www.routerlogin.net"
url3= "http://www.routerlogin.com"
chrome = webbrowser.Chrome("C:\Program Files\Google\Chrome\Application\Chrome.exe")
if user_input == "1":
    chrome.open_new("http://192.168.1.1")
else:
    pass
    if user_input == "2":
        chrome.open_new("http://www.routerlogin.net")
    else:
        pass

        if user_input == "3":
            chrome.open_new("http://www.routerlogin.com")
        else:
            pass
            if user_input == "Netgear":chrome.open_new("https://www.netgear.com/support")



















