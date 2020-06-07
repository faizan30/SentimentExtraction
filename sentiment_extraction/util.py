import datetime
import os

def create_ser_folder(experiments_output_folder=".experiments/outputs/"):
    "create serialisation folder of deep learning model"
    time = datetime.now().strftime("%m_%d_%H_%M_%S")
    while os.path.exists(experiments_output_folder+"cnn%s" % time):
        time = datetime.now().strftime("%m_%d_%H_%M_%S")

    ser_fol = experiments_output_folder+"tweet%s" % time

    return ser_fol