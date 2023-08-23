s = "pwwkew"

window = ""
max_len = 0

for i in s:
    print("i: ",i," window: ",window)
    if len(window) > max_len:
        max_len = len(window)
    if window.__contains__(i):
        print("same element found")
        window = window.replace(window[0], "")
    window += i

print(max_len)