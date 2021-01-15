import os
import subprocess

path = os.path.realpath(__file__)
main_path = os.path.realpath(__file__)[:len(path) - 15]
log_path = main_path + 'logs/'
parsed_path = main_path + 'parsed/'
results_path = main_path + 'results/'

log_dir_check = os.path.isdir(main_path + 'logs')
parsed_dir_check = os.path.isdir(main_path + 'parsed')
results_dir_check = os.path.isdir(main_path + 'results')

if log_dir_check == False:
    cmd = 'mkdir ' + main_path + 'logs'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)
    print('It seems like you did not have a log folder set up yet.')
    question = input('Please provide your default.log absolute path: ')
    cmd2 = 'cp ' + question + ' ' + main_path + 'logs/default.log'
    splited_cmd2 = cmd2.split()
    subprocess.run(splited_cmd2)
    print("I've copied your default.log file to the logs folder you can now run the scripts")

if parsed_dir_check == False:
    cmd = 'mkdir ' + main_path + 'parsed'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)

if results_dir_check == False:
    cmd = 'mkdir ' + main_path + 'results'
    splited_cmd = cmd.split()
    subprocess.run(splited_cmd)


