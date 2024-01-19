import shutil

# The shutil module offers a number of high-level operations on files and collections of files. In particular, functions
# are provided which support file copying and removal. For operations on individual files, see also the os module.
# Functions
# shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.
#
# shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.
#
# shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.
#
# shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.
#
# shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.
# shutil.copy("87_shutil_Module.py", "87_shutil_Module_copied.txt")
# shutil.copytree("../Ex/Ex8_MergeThePDF", "CopiedUsing_Copytree")  # used to copy whole file
# shutil.move("87_shutil_Module_copied.txt", "..\..\Python")
# shutil.rmtree("") to remove a directory

