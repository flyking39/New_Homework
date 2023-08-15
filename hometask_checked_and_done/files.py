import os
# path = 'C:\\Users\\Philippp\\PycharmProjects\\python itterators, generators, decorators'
# all_files = os.listdir(path)
# for file in all_files:
#     print(os.path.abspath(file))


directory = 'C:\\Users\\Philippp\\PycharmProjects'
for links, dirs, files in list(os.walk(directory)):
    print(links)

# path to directory
