import split_folders
import os

folder = os.getcwd()+'/imgs'
split_folders.ratio(folder, output="output", seed=1337, ratio=(.8, .1, .1))