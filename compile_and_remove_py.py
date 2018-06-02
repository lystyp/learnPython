import compileall
import shutil
import sys
import os


def remove_py_file(dir, maxlevels):
    try:
        names = os.listdir(dir)
    except os.error:
        print "Can't list", dir
        names = []
    names.sort()
    success = 1
    for name in names:
        fullname = os.path.join(dir, name)
        if not os.path.isdir(fullname):
            if os.path.splitext(name)[-1] == ".py":
                os.remove(fullname)
        elif maxlevels > 0 and \
                name != os.curdir and \
                name != os.pardir and \
                os.path.isdir(fullname) and \
                not os.path.islink(fullname):
            if not remove_py_file(fullname, maxlevels - 1):
                success = 0
    return success


path = sys.argv[1]
maxlevels = 10
if sys.argv[2] is int :
    maxlevels = sys.argv[2]

release_path = path + "_release"

compileall.compile_dir(dir=path, force=1)

isExists = os.path.exists(release_path)
if isExists is True:
    print "Release directory exists, delete the directory and rebuild one."
    shutil.rmtree(release_path)
else:
    print "Generate a directory named " + release_path


shutil.copytree(path, release_path)
remove_py_file(release_path, maxlevels)
