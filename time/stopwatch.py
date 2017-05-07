#! python3
# stopwatch.py - a simple stopwatch

import time

print('Press ENTER to begin. Afterwards, press ENTER again to stop. Press Ctrl-C to exit.')
input()
print('Started')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #{}: {} ({})'.format(lap_num, total_time, lap_time))
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone')
