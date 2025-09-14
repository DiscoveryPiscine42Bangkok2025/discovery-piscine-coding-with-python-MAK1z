import sys
import re

pattern = sys.argv[1]
text = sys.argv[2]

result = re.findall(pattern, text)
print(len(result))