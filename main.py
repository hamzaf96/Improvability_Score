import streamlit as st
import pandas as pd
import mplcursors
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
    get_data_from_google_drive(
        file_id="1Tr-x8-8fe081d1woq98BBXIv9UA6tboF", file_path="./data/dataset/data.csv"
    )

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
    save_csv(file_path="./data/processed_data/processed_data.csv", data=df)
    # Set the title and description for your app
    st.title("Dashboard")
    st.write(
        "This is a the dashboard that will help choosen the student with the need to help."
    )

    figure, scatter = vis_scatter_data(x=df["FinalGrade"], y=df["Imrovability_Score"])

    # Create a cursor to display information on hover
    cursor = mplcursors.cursor(scatter, hover=True)

    # Function to display information when hovering
    def on_hover(sel):
        index = sel.target.index
        sel.annotation.set_text(
            f"FirstName: {index}\nFamilyName: {df['FamilyName'][index]}\n"
        )

    cursor.connect("add", on_hover)

    # Display the chart in the Streamlit app
    st.pyplot(figure)

    # Add text or other components to your app
    st.write("This is a version1 deliverable.")


if __name__ == "__main__":
    main()
