import basic
import platform
import sys
import datetime as dt

date_and_hour = dt.datetime.now()
version_of_platform = platform.system()

print(f"""
gentle 0.1 (dev ver) | {date_and_hour.strftime('%H:%M:%S')} | {version_of_platform}
""")
for i in range(2):print("")
while True:
    text = input('gntl> ')
    result, error = basic.run('<stdin>', text)
    if text == "":pass
    else:
        if text.lower() == "exit":exit()
        else:
            if error: print(error.as_string())
            else:print(result)
