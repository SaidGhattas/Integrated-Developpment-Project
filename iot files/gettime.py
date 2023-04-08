import time


def get_time():
  localtime = time.localtime(time.mktime(time.localtime())+3600) 
  return f"{localtime[2]:0>2d}/{localtime[1]:0>2d}/{localtime[0]:0>2d} {localtime[3]:0>2d}:{localtime[4]:0>2d}:{localtime[5]:0>2d}"
