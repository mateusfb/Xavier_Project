import numpy as np
import pandas as pd
from ntpath import split, basename
import matplotlib.pyplot as plt
import json
import sys

def file_name_from_path(path):
    head, tail = split(path)
    filename = tail or basename(head)
    i = -1
    while(filename[i] != '.'):
      i -= 1
    return filename[:i]

def split_programs(programs):
  programs = programs[1:-1]
  return programs.split('-')

def count_qualis_occurances_for_programs(src):
  dataframe = pd.read_csv(src)
  programs_dict = {}
  programs_list = []

  for i in dataframe.index:
    qualis = dataframe["qualis"][i]
    programs_list = split_programs(dataframe["programas"][i])
    for program in programs_list:
      if program in programs_dict:
        if qualis in programs_dict[program]:
          programs_dict[program][qualis] += 1
        else:
          programs_dict[program][qualis] = 1
      else:
        programs_dict[program] = {qualis : 1}
  return programs_dict

def dict_to_json(filename, dictionary):
  json_dict = json.dumps(dictionary)
  
  with open(filename, "w") as file:
    file.write(json_dict)

def dict_from_json(src):
  with open(src) as json_file:
    dictionary = json.load(json_file)

    return dictionary

def make_dict(csv_file, json_filename = None):
  if json_filename is None:
    json_filename = file_name_from_path(csv_file) + ".json"

  dict_to_json(json_filename, count_qualis_occurances_for_programs(csv_file))


def plot_program(dict_src, program_code, image_name = None):
  program = dict_from_json(dict_src)[program_code]
  labels, values = zip(*program.items())
  total = sum(values)
  plt.title("Distribuição de qualis por programa", bbox={'facecolor':'1', 'pad':5})
  wedges, text, autotext = plt.pie(values, startangle=90,
  autopct=lambda p : "{:.1f}%\n({:d})".format(p,int(round((p*total)/100))))
  plt.axis('equal')
  plt.legend(wedges, labels, title="Qualis", loc="center left", bbox_to_anchor=(0.85, 0, 0.5, 1))

  if image_name is None:
    image_name = file_name_from_path(dict_src) + "_" + program_code + ".png"
  plt.savefig(image_name)

if __name__ == '__main__':
  globals()[sys.argv[1]](*sys.argv[2:])