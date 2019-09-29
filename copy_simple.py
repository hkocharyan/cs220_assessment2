#!/usr/bin/python
from shutil import copy 
import os

search_dir = '/home/hkocharyan/Desktop/python_project/files'
destination = '/home/hkocharyan/Desktop/python_project/files_copy'
file_list = os.listdir(search_dir)
for file in file_list:
	file_full = os.path.join(search_dir, file)
	copy(file_full, destination)