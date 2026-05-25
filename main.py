import pandas as pd

# Load dataset
df = pd.read_csv("data/sample_data.csv")

print("Original Rows:", len(df))

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Toxic words list
bad_words = ["stupid", "hate", "idiot"]

# Function to detect toxic text
def is_toxic(text):
    text = text.lower()
    return any(word in text for word in bad_words)

# Create toxicity column
df["toxic"] = df["text"].apply(is_toxic)

# Keep only clean rows
clean_df = df[df["toxic"] == False]

print("Clean Rows:", len(clean_df))

# Save cleaned dataset
clean_df.to_csv("output/cleaned_data.csv", index=False)

print("Pipeline completed!")