import requests
import os

# List of file URLs
file_urls = [
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/be55e2fe-2e34-4667-89e8-a266c456c534",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/c64da2b3-9044-418a-a1fa-701acb3d2aeb",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/04c6f4f0-e1fb-4b62-bffa-1007f4c81cf3",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/6d111096-d565-48d7-b181-56aa87a38a97",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/c79eb1ea-db66-4af1-b235-0d54f55db5e1",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/37e7353a-78e3-4583-92f3-d91ffb8592ad",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/206e2b7c-66d3-4fdc-aa1a-5fc408578a74",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/902b9358-e399-45ad-81ef-6ea2b69f58e4",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/329dda38-4aea-42d8-b5f6-23714709e2f5",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/d3c46479-7873-4bd6-9092-ed25744980fe",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/8dd85d6d-4ba4-4bc0-8ded-07d0e6a2f7ad",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/292b1861-e05c-4df9-8303-b49678c9f924",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/a8b203a0-a466-465d-8805-339966298a54",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/ba92d160-4cf6-4776-b674-40f9c95d6898",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/68049f54-7ea6-45b7-89a8-4f131a843744",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/b256eb19-70bb-41a2-b3fb-45faf359a82b",
    "https://catalog.data.gov/dataset/national-student-loan-data-system-722b0/resource/beb4a736-6c6a-41b4-aa29-333802b9aafa"
]

# Directory to save downloaded files
download_dir = "downloaded_files"
os.makedirs(download_dir, exist_ok=True)

# Function to download a file
def download_file(url, directory):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Derive filename from URL (modify if necessary)
        filename = url.split("/")[-1] + ".xls"  # Adds .xls to end for saving
        file_path = os.path.join(directory, filename)

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Downloaded: {filename}")
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")

# Download each file
for url in file_urls:
    download_file(url, download_dir)
