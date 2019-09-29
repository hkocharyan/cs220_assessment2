#!/usr/bin/python3
from shutil import copy 
from concurrent.futures import ThreadPoolExecutor
import os

search_dir = '/home/hkocharyan/Desktop/python_project/files'
destination = '/home/hkocharyan/Desktop/python_project/files_copy'
file_list = os.listdir(search_dir)
executor = ThreadPoolExecutor(5)
for file in file_list:
	file_full = os.path.join(search_dir, file)
	future = executor.submit(copy, file_full, destination)