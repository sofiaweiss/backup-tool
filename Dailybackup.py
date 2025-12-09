#!/usr/bin/env python3


import subprocess
import os 
import sys
from multiprocessing import Pool, cpu_count


src = "/mnt/c/Users/prod"  # *The source directory to backup*
dest = "/mnt/c/Users/backup" # *The destination directory for the backup*


def backup_directory(subfolder_name):
  if subfolder_name:
    # *Build the full source and destination paths for a real subfolder*
    src_path = os.path.join(src, subfolder_name)
    dest_path = os.path.join(dest, subfolder_name)
  else:
    # *Used for top-level files located directly in the source directory*
    src_path = src
    dest_path = dest

  os.makedirs(dest_path, exist_ok=True) # *Creates the destination folder if it does not exist*

  subprocess.call(["rsync", "-arq", src_path + "/", dest_path + "/"]) # *Copies new and modified files, folders, subfolders, and their contents*


if __name__ == "__main__":
  subfolders_to_copy = [] # *Will store the first-level subfolders of the source directory*
  for root, directories, files in os.walk(src):
    subfolders_to_copy = directories.copy() # *Copy the first-level subfolders to the list*

    if files:
      subfolders_to_copy.append("") # *Represents top-level files located directly in the source directory*
    
    break # *Stop os.walk after the first iteration — deeper levels are handled by rsync, so we only collect top-level items*

  num_workers = cpu_count() # *Defines the number of workers based on available CPU cores*
  p = Pool(num_workers) # *Creates a pool of worker processes to execute tasks in parallel*
  p.map(backup_directory, subfolders_to_copy) # *Distributes backup tasks across workers*

  print("Backup completed")
