#!/usr/bin/python3
import sys


count = 1
filesize = 0
my_dict = {
    202: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
my_list = [202, 301, 400, 401, 403, 404, 405, 500]
try:
    for line in sys.stdin:
        if count % 10 == 0:
            print("File size: {}".format(filesize))
            for key, value in sorted(my_dict.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
        for i in my_list:
            if str(i) in line:
                my_dict[i] = my_dict[i] + 1
        size = line.rsplit(' ', 1)[1]
        filesize += int(size)
        count += 1
except KeyboardInterrupt:
    print("File size: {}".format(filesize))
    for key, value in sorted(my_dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))
