import io
import requests
import logging
from zipfile import ZipFile
from pathlib import Path
import pandas as pd

# Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def setup_logging():
    # Console logging handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # File logging handler
    Path('output').mkdir(parents=True, exist_ok=True)  # Ensure the output directory exists
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(console_formatter)

    # Set up root logger
    logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])

def download_and_extract_zip(url, extract_to):
    """
    Downloads a ZIP file from the provided URL and extracts it to the specified directory.

    Parameters:
        url (str): URL of the ZIP file to download.
        extract_to (Path): Path to the directory where files should be extracted.

    Returns:
        Path: Path to the extracted directory.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(extract_to)
        logging.info(f"Downloaded and extracted ZIP file to {extract_to}")
        return extract_to
    except requests.RequestException as e:
        logging.error(f"Failed to download file: {e}")
        raise
    except Exception as e:
        logging.error(f"Failed to extract ZIP file: {e}")
        raise

def load_and_prepare_data(csv_path, columns, title_word_min=5, title_word_max=14):
    """
    Loads the CSV file into a DataFrame and performs data preprocessing.

    Parameters:
        csv_path (Path): Path to the CSV file.
        columns (list): Column names for the dataset.
        title_word_min (int): Minimum word count in titles to filter the data.
        title_word_max (int): Maximum word count in titles to filter the data.

    Returns:
        pd.DataFrame: Processed DataFrame with title, category, word count, and weights.
    """
    try:
        df = pd.read_csv(csv_path, sep='\t', names=columns)
        df = df[['title', 'category']]
        df['word_cnt'] = df['title'].apply(lambda txt: len(txt.split()))

        # Filter data by word count
        filtered_df = df.query(f'{title_word_min} < word_cnt < {title_word_max}')

        # Calculate sampling weights
        category_counts = filtered_df['category'].value_counts(normalize=True).round(2)
        inverse_weights = {k: int(1/v) for k, v in category_counts.items()}
        total = sum(inverse_weights.values())
        normalized_weights = {k: round(v/total, 2) for k, v in inverse_weights.items()}

        filtered_df['weights'] = filtered_df['category'].map(normalized_weights)

        logging.info("Data loaded and prepared successfully")
        return filtered_df
    except FileNotFoundError:
        logging.error("CSV file not found.")
        raise
    except pd.errors.ParserError:
        logging.error("Error parsing CSV file.")
        raise
    except Exception as e:
        logging.error(f"Error in data preparation: {e}")
        raise

def sample_data(df, sample_size=50000, random_state=19):
    """
    Samples the data based on calculated weights and returns the sampled DataFrame.

    Parameters:
        df (pd.DataFrame): DataFrame to sample from.
        sample_size (int): Number of samples to draw.
        random_state (int): Random state for reproducibility.

    Returns:
        pd.DataFrame: Sampled DataFrame.
    """
    try:
        samples = df.sample(sample_size, weights='weights', random_state=random_state)
        logging.info(f"Sampled {sample_size} entries from the dataset.")
        return samples[['title', 'category']]
    except ValueError as e:
        logging.error(f"Error during sampling: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during sampling: {e}")
        raise

def main(url_zipfile, output_csv, sample_size=50000):
    """
    Main function to execute the data pipeline: download, extract, process, sample, and save.

    Parameters:
        url_zipfile (str): URL of the dataset ZIP file.
        output_csv (Path): Path to save the output sampled CSV.
        sample_size (int): Number of samples to draw.
    """
    # Set paths and constants
    out_dir = Path('news_aggregator_dataset')
    csv_path = out_dir / 'newsCorpora.csv'
    col_names = ['id', 'title', 'url', 'publisher', 'category', 'story', 'hostname', 'timestamp']

    # Download and extract dataset
    download_and_extract_zip(url_zipfile, out_dir)

    # Load and prepare dataset
    df = load_and_prepare_data(csv_path, col_names)

    # Sample the data
    samples = sample_data(df, sample_size=sample_size)

    # Save the sampled data
    samples.to_csv(output_csv, index=False, encoding='utf-8')
    logging.info(f"Sampled data saved to {output_csv}")

# Parameters
url_zipfile = 'https://archive.ics.uci.edu/static/public/359/news+aggregator.zip'
output_csv = '/app/output/headlines_sample_50.csv'  # in docker
LOG_FILE = 'output/script.log'

# Run the main function
if __name__ == '__main__':
    setup_logging()
    main(url_zipfile, output_csv)
