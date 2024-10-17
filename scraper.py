import csv

def get_clothing_brands_from_csv(file_path):
    clothing_brands = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                if row:
                    clothing_brands.append(row[0])
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return clothing_brands

def save_to_csv(brands, filename="clothing_brands_output.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Brand Name'])
        for brand in brands:
            writer.writerow([brand])
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Path to the sample data file
    file_path = "./data/clothing_brands_sample.csv"
    
    print("Fetching clothing brands from pre-downloaded dataset...")
    brands = get_clothing_brands_from_csv(file_path)
    
    if brands:
        print(f"Found {len(brands)} brands. Saving to CSV...")
        save_to_csv(brands)
    else:
        print("No brands found.")
