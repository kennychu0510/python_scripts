import os

def main():
  path='./images/'
  for filename in os.listdir(path):
    newName = 'apple-' + filename
    print(newName)
    os.rename(path + filename, path + newName)

if __name__ == '__main__':
  main()