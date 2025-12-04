#!/usr/bin/env python3


import subprocess
import os 
import sys
from multiprocessing import Pool, cpu_count


src = "/home/student/data/prod/" 
dest = "/home/student/data/prod_backup/"


def backup_directory(subfolder_name):
  subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
  subfolders_to_copy = []
  for root, directories, files in os.walk(src):
    subfolders_to_copy = directories
    break 

  num_workers = cpu_count()
  p = Pool(num_workers) 
  p.map(backup_directory, subfolders_to_copy)

  print("backup terminado")
