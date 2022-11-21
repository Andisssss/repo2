
import os

# folder path
dir_path = r'./'

count = 0
    
for path in os.listdir(dir_path):

    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
print('File count:', count)