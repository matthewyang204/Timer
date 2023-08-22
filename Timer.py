import time

h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))
hr = str(h) + " hours, "
min = str(m) + " minutes, "
sec = str(s) + " seconds"
all = hr + min + sec
while s > 0:
  hr = str(h) + " hours, "
  min = str(m) + " minutes, "
  sec = str(s) + " seconds"
  all = hr + min + sec
  print(all)
  s = s - 1
  time.sleep(1)
while m > 0:
  m = m - 1
  s = 59
  hr = str(h) + " hours, "
  min = str(m) + " minutes, "
  sec = str(s) + " seconds"
  all = hr + min + sec
  print(all)
  while s > 0:
    hr = str(h) + " hours, "
    min = str(m) + " minutes, "
    sec = str(s) + " seconds"
    all = hr + min + sec
    print(all)
    s = s - 1
    time.sleep(1)
while h > 0:
  h = h - 1
  m = 59
  hr = str(h) + " hours, "
  min = str(m) + " minutes, "
  sec = str(s) + " seconds"
  all = hr + min + sec
  print(all)
  while m > 0:
    m = m - 1
    s = 59
    hr = str(h) + " hours, "
    min = str(m) + " minutes, "
    sec = str(s) + " seconds"
    all = hr + min + sec
    print(all)
    while s > 0:
      hr = str(h) + " hours, "
      min = str(m) + " minutes, "
      sec = str(s) + " seconds"
      all = hr + min + sec
      print(all)
      s = s - 1
      time.sleep(1)
s = 0
hr = str(h) + " hours, "
min = str(m) + " minutes, "
sec = str(s) + " seconds"
all = hr + min + sec
print(all)