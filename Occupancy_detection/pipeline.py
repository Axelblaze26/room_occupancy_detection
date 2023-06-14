import pickle
import pandas as pd
from tensorflow import keras
import numpy as np


def load_model():
    model = keras.models.load_model("model_det1.h5")
    return model


def drop_columns(dataframe):
    # drop target column along with other columns which are not useful.
    columns_to_drop = ["Occupancy", "Humidity", "date"]
    existing_columns = dataframe.columns.intersection(columns_to_drop)
    if len(existing_columns) == len(columns_to_drop):
        dataframe.drop(columns=existing_columns, inplace=True)


def predict():
    file_location = input("Enter the path to input file: ")

    # read csv
    df = pd.read_csv(file_location)

    # create a copy dataset
    df1 = df.copy()

    # load model
    model = load_model()

    # drop features that are not used in model training
    drop_columns(df1)

    # predict data
    occupancy = model.predict(df1)

    # merge "predicted occupancy" to copy dataset as well as original dataset
    df1["Predicted Occupancy"] = occupancy.astype(int)
    df["Predicted Occupancy"] = occupancy.astype(int)

    # export final csv along with predicted data
    df.to_csv("output_room-occupancy.csv")


predict()



