import os
import random
from PIL import Image

img_strings = []
for folder in os.listdir(os.getcwd()):
    if folder.startswith('test'):
        continue
    for file in os.listdir(os.getcwd()+'/{}/'.format(folder)):
        img_strings.append(os.getcwd()+'/{}/{}'.format(folder,file))

correct_count = 0
city_input_dict = {'1':'new_york', '2':'amsterdam', '3':'tokyo', '4':'boulder'}
number_questions_in_test = 20
for img_string in random.sample(img_strings, number_questions_in_test):
    img = Image.open(img_string)
    img.show()
    city_input = input('Name that city! [1] New York [2] Amsterdam [3] Tokyo [4] Boulder ')
    city_gt = img_string.split('/')[-2]

    print(city_input_dict[city_input])
    print(city_gt)
    if city_gt == city_input_dict[city_input]:
        correct_count += 1

print('You answered {} of {} correct. ({}%)'.format(correct_count, number_questions_in_test, correct_count/number_questions_in_test))