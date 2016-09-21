import os
import sys

robot_path = "D:\Testing\Robot\WSH\Web\Beta"
walk_dir = robot_path

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    root=root.decode("gbk").encode("utf-8")
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')

    #list_file_path=list_file_path.decode("gbk").encode("utf-8")
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            subdir=subdir.decode("gbk").encode("utf-8")
            print('\t- subdirectory ' + subdir)

        for filename in files:

            filename=filename.decode("gbk").encode("utf-8")
            file_path = os.path.join(root, filename)
            #file_path=file_path.decode("gbk").encode("utf-8")


            print('\t- file %s (full path: %s)' % (filename, file_path))


            with open(file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')

