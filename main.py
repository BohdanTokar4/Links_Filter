# Link Filter. Filters links from text

import re

# unfiltered text reading from file
with open ('list.txt', 'r') as links_file:
    content = links_file.read()

# filtering
links = re.findall(r'[^a-zA-Z0-9]?(http[s]?://\S+)[^a-zA-Z0-9]?', content)

# writing filtered links in new file
with open('list_filtered.txt', 'w') as list_filtered:
    for link in links:
        list_filtered.write(link + '\n')