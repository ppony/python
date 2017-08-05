

from shutil import copytree, ignore_patterns



copytree(r"../../work/present/", r"../../work/present/pytest/", ignore=ignore_patterns('*.txt'))
