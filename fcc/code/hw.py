import os,sys,pandas as pd

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

hw = pd.read_csv(os.path.join(currentdir,'datasets','hw_25000.csv'))
hw.info()