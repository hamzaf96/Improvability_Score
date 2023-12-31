import streamlit as st
import pandas as pd
import os
from code.utils.vis import (
    vis_scatter_data,
)
from code.utils.data_processing import (
    remove_nan_values,
    convert_categorical_to_ohe,
    remove_duplicate,
    save_csv,
)
from code.utils.get_files import get_data_from_google_drive
from code.src.improvability_score import ImprovabilityScore


def main():
    # Define the folder path you want to check or create
    folder_path_download_data = "./data/dataset/"
    folder_path_save_data = "./data/processed_data/"
    # Check if the folder exists
    if not os.path.exists("./data/dataset/"):
        # If it doesn't exist, create it
        os.makedirs(folder_path_download_data)
        print(f"Folder '{folder_path_download_data}' created.")
        get_data_from_google_drive(
            file_id="1Tr-x8-8fe081d1woq98BBXIv9UA6tboF",
            file_path="./data/dataset/data.csv",
        )
    else:
        print(f"Folder '{folder_path_download_data}' already exists.")

    print("Start Processing the Data !")
    df = pd.read_csv("./data/dataset/data.csv")
    df = remove_duplicate(df)
    df = remove_nan_values(df)
    df = convert_categorical_to_ohe(df)
    df_filtered = df.drop(columns=["FirstName", "FamilyName"])
    print("Compute the Improvability Score: Start")
    improvability_score = ImprovabilityScore(data=df_filtered)
    improvability_score_list = improvability_score()
    print("Compute the Improvability Score: Done")
    df["Imrovability_Score"] = improvability_score_list
    # Check if the folder exists
    if not os.path.exists(folder_path_save_data):
        # If it doesn't exist, create it
        os.makedirs(folder_path_save_data)
        print(f"Folder '{folder_path_save_data}' created.")
        save_csv(file_path="./data/processed_data/processed_data.csv", data=df)
    else:
        print(f"Folder '{folder_path_save_data}' already exists.")

    # Set the title and description for your app
    st.title("Dashboard")
    st.write(
        "This is a the dashboard that will help choosen the student with the need to help."
    )

    figure = vis_scatter_data(
        data=df,
        x=df["FinalGrade"].name,
        y=df["Imrovability_Score"].name,
        label="StudentID",
    )

    # Display the chart in the Streamlit app
    st.plotly_chart(figure)

    # Add text or other components to your app
    st.write("This is a version1 deliverable.")


if __name__ == "__main__":
    main()
