import os
import shutil
import pandas as pd
from openai import OpenAI

def get_file_info(downloads_path):
    files = os.listdir(downloads_path)
    return pd.DataFrame({
        'filename': files,
        'extension': [os.path.splitext(f)[1].lower() for f in files]
    })

def classify_files(df):
    client = OpenAI()
    
    prompt = f"""Given the following list of files, suggest appropriate folder names for organization. 
    Use general categories that make sense for personal file organization.
    Respond with a CSV format: filename,suggested_folder
    
    Files:
    {df.to_string(index=False)}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    # Parse the CSV response
    classifications = pd.read_csv(pd.compat.StringIO(response.choices[0].message.content))
    return classifications

def organize_downloads():
    downloads_path = os.path.expanduser("~/Downloads")
    df = get_file_info(downloads_path)
    
    classifications = classify_files(df)
    
    for _, row in classifications.iterrows():
        file = row['filename']
        folder = row['suggested_folder']
        
        folder_path = os.path.join(downloads_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        try:
            shutil.move(os.path.join(downloads_path, file), os.path.join(folder_path, file))
            print(f"Moved {file} to {folder}")
        except Exception as e:
            print(f"Error moving {file}: {str(e)}")

    print("Organization complete!")

if __name__ == "__main__":
    organize_downloads()

# Considerations:
# 1. Error Handling: Basic error handling is included, but you might want to expand it.
# 2. API Key: Ensure you have set the OPENAI_API_KEY environment variable.
# 3. Rate Limiting: Be mindful of API rate limits and costs.
# 4. File Permissions: This script assumes it has permission to move all files.
# 5. Large Directories: For very large directories, you might need to batch the requests.