# backup-tool 
A Python-based backup tool that improves performance by using the multiprocessing module to run file copy operations in parallel. The project focuses on optimizing backup speed, improving code structure, and ensuring safe concurrent execution.

This script copies folders, subfolders, and files from the source path to the destination path, including any new or modified files. 
For safety, it does not delete any files or folders in the destination; deletions must be handled manually.

