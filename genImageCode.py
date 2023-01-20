""" Generate Import Code based on images and save to clipboard """

import os
import subprocess

def main():
  path='./images'
  code=''
  for filename in os.listdir(path):
    if ('.py' in filename):
      continue
    if ('copy' in filename):
      os.remove(path + filename)
    objectName = filename.replace('-', '_').upper().replace('.PNG', '') + ": require('./AppIcons/" + filename + "'),"
    code += objectName + '\n'
    print(objectName)
    subprocess.run("pbcopy", text=True, input=code)

if __name__ == '__main__':
  main()