import os
from buildTasks.cp.cp import cp
from buildTasks.trimFileLeft.trimFileLeft import trimFileLeft

SOURCE_DIR = os.path.abspath("src/")
DIST_DIR = os.path.abspath("dist/")
if __name__ == "__main__":
    cp(SOURCE_DIR, DIST_DIR)
    trimFileLeft(DIST_DIR)
#end