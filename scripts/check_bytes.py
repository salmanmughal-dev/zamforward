with open('user_prompt_10.txt', 'rb') as f:
    raw = f.read()

import re
# Look for byte patterns around "Search rashguards"
idx = raw.find(b'Search rashguards')
if idx != -1:
    print("Bytes around Search rashguards:")
    print(raw[idx:idx+80])

idx2 = raw.find(b'Batch 43')
if idx2 != -1:
    print("Bytes around Batch 43:")
    print(raw[idx2-30:idx2+50])
