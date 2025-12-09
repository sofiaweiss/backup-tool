#!/usr/bin/env python3


import subprocess
import os 
import sys
from multiprocessing import Pool, cpu_count


src = "/mnt/c/Users/prod" 
dest = "/mnt/c/Users/backup"


def backup_directory(subfolder_name):
  if subfolder_name:
    src_path = os.path.join(src, subfolder_name)
    dest_path = os.path.join(dest, subfolder_name)
  else:
    src_path = src
    dest_path = dest

  os.makedirs(dest_path, exist_ok=True)

  subprocess.call(["rsync", "-arq", src_path + "/", dest_path + "/"])


if __name__ == "__main__":
  subfolders_to_copy = []
  for root, directories, files in os.walk(src):
    subfolders_to_copy = directories.copy()

    if files:
      subfolders_to_copy.append("")
    
    break 

  num_workers = cpu_count()
  p = Pool(num_workers) 
  p.map(backup_directory, subfolders_to_copy)

  print("backup terminado")
