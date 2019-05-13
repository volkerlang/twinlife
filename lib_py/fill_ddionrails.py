import shutil

import pandas as pd
from ddi.onrails.repos import convert_r2ddi, copy, dor1, merge_instruments

STUDY = "twinlife"
VERSION = "v3-0-0"


def questions_variables():

    questions_variables = pd.read_csv("metadata/logical_variables.csv")
    questions_variables.rename(
        columns={
            "study": "study_name",
            "dataset": "dataset_name",
            "variable": "variable_name",
            "questionnaire": "instrument_name",
            "question": "question_name",
        },
        inplace=True,
    )
    questions_variables = questions_variables[
        [
            "study_name",
            "dataset_name",
            "variable_name",
            "instrument_name",
            "question_name",
        ]
    ]

    questions_variables.dropna(axis=0, how="any", inplace=True)
    questions_variables.drop_duplicates(inplace=True)
    questions_variables.to_csv("ddionrails/questions_variables.csv", index=False)


def main():
    shutil.copy("metadata/study.md", "ddionrails/study.md")
    dor1.variables()
    shutil.copy("metadata/datasets.csv", "ddionrails/datasets.csv")
    # questions_variables()
    merge_instruments.main()
    # convert_r2ddi.Parser(STUDY, version=VERSION).write_json()


if __name__ == "__main__":
    main()
