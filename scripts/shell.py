import basic
import platform
import sys
import datetime

date_and_hour = datetime.datetime.now()
version_of_platform = platform.system()

print(f"""
gentle 0.1 (dev ver) | {date_and_hour.strftime('%H:%M:%S')} | {version_of_platform}
""")
for i in range(2):print("")
while True:
    text = input('[G]>> ')
    result, error = basic.run('<stdin>', text)
    if text == "":pass
    else:
        if text.lower() in ["exit", "exit "]:exit()
        else:
            if error: print(error.as_string())
            else:print(result)
