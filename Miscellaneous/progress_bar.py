# 2 Ways to implement real-time progress bars

import sys
import progressbar  # pip install progressbar
from time import sleep

# Using progressbar library
bar = progressbar.ProgressBar(maxval=20,
                              widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(20):
    bar.update(i+1)
    sleep(0.1)  # Some Task
bar.finish()

# Using basic sys library
for i in range(21):
    # the exact output you're looking for:
    sys.stdout.write("\r[%-20s] %d%%" % ('='*i, 5*i))
    sys.stdout.flush()
    sleep(0.1)  # Some Task
