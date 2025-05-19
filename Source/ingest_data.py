"""
Load raw transaction data, clean and save processed files.
"""
import pandas as pd
import yaml
from pathlib import Path

# Load configuration
with open(Path(__file__).parents[1] / 'config.yaml') as f:
    cfg = yaml.safe_load(f)

def load_data(path:str) -> pd.DataFrame:
    """Read csv file intoa pandas Dataframe"""
    return pd.read_csv(path)
 

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Clean data: drop IDs, parse dates, handle missing values"""
    df = df.copy()
    # Drop identifiers
    for col in ['TransactionID', 'CustomerID']:
        if col in df.columns:
            df.drop(col, axis=1, inplace=True)
    # Parse datetime
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
    # Fill missing values
    df.fillna({'DeviceType': 'Unknown'}, inplace=True)
    # Drop or impute other missing values as needed
    df.dropna(inplace=True)
    return df


def main():
    """
    Load raw transaction data, preprocess, and save as parquet file.
    """
    raw_path = cfg['data']['raw_path']
    out_dir = Path(cfg['data']['processed_path'])
    out_dir.mkdir(parents=True, exist_ok=True)

    df = load_data(raw_path)
    df_clean = preprocess(df)
    df_clean.to_parquet(out_dir / 'transactions.parquet')


if __name__ == '__main__':
    main()