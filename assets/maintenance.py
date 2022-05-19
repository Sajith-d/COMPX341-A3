import os
import sys

try:
    for root, dirs, files in os.walk("./src"):
        for name in files:
            path = os.path.join(root, name)
            if(path.endswith(".ts")):
                with open(path, 'r+') as f:
                    read = f.readlines()
                    if (read[0] != '// Sajith Dhambagolla - 1508789'):
                        f.seek(0, 0)
                        f.write('// Sajith Dhambagolla - 1508789' + '\n')
                f.close()
    sys.exit(0)
except:
    print("Error has occurred when running maintenance task, try again")
    sys.exit(0)

