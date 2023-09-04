# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 08:16:12 2023

@author: TonyHu
"""

import os 
import pandas as pd 
from PIL import Image
import torch
from torch.utils.data import Dataset
from torchvision import transforms,models,utils
from tqdm.notebook import tqdm
from torch import nn
import matplotlib.pyplot as plt
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter

train_path = "train/Patients"
test_path = "test"
data_root = "train"
csv_path = "result"
tensorboard_path = "../tensorboard"
model_save_path = "../model"

file_list = os.listdir(train_path)
for file_name in file_list:
    path = train_path + '/' + file_name
    img = Image.open(path)
    print(img.size)