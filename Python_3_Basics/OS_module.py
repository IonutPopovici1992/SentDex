import os
import time

currentDirectory = os.getcwd()
print(currentDirectory)

os.mkdir('newDirectory')

time.sleep(2)

os.rename('newDirectory', 'newDirectory2')

time.sleep(2)

os.rmdir('newDirectory2')
