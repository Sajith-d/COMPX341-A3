import os
import sys

try:
    for root, dirs, files in os.walk("./src"):
        for name in files:
            path = os.path.join(root, name)
            if(path.endswith(".ts")):
                with open(path, 'r') as f:
                    read = f.readlines()
                f.close()             
                read[0] = "// Sajith Dhambagolla - 1508789" + '\n'
                with open(path, 'w') as w:
                    w.writelines(read)
                w.close()
    sys.exit(0)
except Exception as e: 
    print(e)
    sys.exit(1)

