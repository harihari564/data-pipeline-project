import csv
import json
import logging
import sys

# 1. Setup error logging (saves errors to a file instead of just printing them)
logging.basicConfig(filename='pipeline.log', level=logging.INFO,format='%(asctime)s - PYTHON - %(levelname)s - %(message)s')

def process_data():
    input_file = 'raw_data.csv'
    output_csv = 'filtered_data.csv'
    output_json = 'summary.json'

    try:
        # 2. Read the CSV file
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        if not data:
            raise ValueError("CSV file is empty or malformed.")

        # 3. Clean and Transform Data
        filtered_data = []
        survivor_count = 0
        total_count = len(data)
        for row in data:
            # Only keep passengers who survived (Survived == '1')
            if row.get('Survived') == '1':
                survivor_count += 1
                filtered_data.append({
                    'Name': row.get('Name'),
                    'Age': row.get('Age'),
                    'Class': row.get('Pclass')
                })
# 4. Produce filtered CSV
        with open(output_csv, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['Name', 'Age', 'Class'])
            writer.writeheader()
            writer.writerows(filtered_data)
 # 5. Produce JSON summary
        summary = {
            "total_passengers_evaluated": total_count,
            "total_survivors": survivor_count,
            "survival_rate_percentage": round(survivor_count / total_count * 100, 2)
        }

        with open(output_json, mode='w', encoding='utf-8') as f:
            json.dump(summary, f, indent=4)
        logging.info("Data processed successfully. JSON and CSV created.")
        print("Python data processing complete!")
    except FileNotFoundError:
        logging.error(f"Critical Error: {input_file} not found. Did the download fail?")
        sys.exit(1) # Tells Bash the script failed
    except Exception as e:
        logging.error(f"Unexpected data error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    process_data()
