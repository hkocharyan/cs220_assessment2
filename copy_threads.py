#!/usr/bin/python3
from shutil import copy 
from concurrent.futures import ThreadPoolExecutor
import os

# search_dir = '/home/hkocharyan/Desktop/python_project/files'
# destination = '/home/hkocharyan/Desktop/python_project/files_copy'
# file_list = os.listdir(search_dir)
# executor = ThreadPoolExecutor(5)
# for file in file_list:
# 	file_full = os.path.join(search_dir, file)
# 	future = executor.submit(copy, file_full, destination)
# 	#copy(file_full, destination)

search_dir = '/home/hkocharyan/Desktop/python_project/files'
destination = '/home/hkocharyan/Desktop/python_project/files_copy'
file_list = os.listdir(search_dir)
with ThreadPoolExecutor(max_workers=5) as e:
    jobs = [e.submit(copy, os.path.join(search_dir, file), destination) for file in file_list]