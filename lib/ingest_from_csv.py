import pandas as pd
import os


def ingest_and_clean_csv(csv_file_path):
    df = pd.read_csv(csv_file_path)

    df.columns = df.columns.str.strip()

    df.fillna("Unknown", inplace=True)

    df.drop_duplicates(inplace=True)

    return df


csv_file_path = os.path.join(os.path.dirname(__file__), "../seeds/users.csv")

print(ingest_and_clean_csv(csv_file_path))
