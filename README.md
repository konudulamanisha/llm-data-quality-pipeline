# LLM Training Data Quality Pipeline

## Overview
This project is a Python-based automated data quality pipeline designed for preprocessing LLM training datasets.

The pipeline performs:
- Duplicate removal
- Missing value handling
- Toxicity filtering
- Clean dataset generation

## Tech Stack
- Python
- Pandas
- CSV Processing

## Project Structure

```bash
llm-data-quality-pipeline
│
├── data/
│   └── sample_data.csv
│
├── output/
│   └── cleaned_data.csv
│
├── main.py
└── README.md
```

## Features
- Removes duplicate records
- Detects toxic content
- Cleans missing values
- Exports processed datasets

## How to Run

```bash
python main.py
```

## Sample Output

```bash
Original Rows: 5
Clean Rows: 3
Pipeline completed!
```

## Future Improvements
- AWS S3 integration
- Bedrock/OpenAI APIs
- LangChain integration
- Streamlit dashboard
- Docker support