import os

walk_dir = "/Users/lucamartini/Downloads/temp4"
root_len = len(walk_dir)

new_dir = "/Users/lucamartini/Desktop/gcc-4"

print('walk_dir = ' + walk_dir)

for root, subdirs, files in os.walk(walk_dir):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_path = file_path[root_len:]
        new_file_path = new_dir + file_path
        dirname = os.path.dirname(new_file_path)
        #        print dirname
        print file_path
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        if os.path.exists(file_path):
            print "move ", file_path, " to ", new_file_path
            os.rename(file_path, new_file_path)
