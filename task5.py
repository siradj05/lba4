# Function to recursively flatten JSON into a list of dictionaries
def flatten_json(json_obj, parent_key='', sep='.'):
    items = []
    for key, value in json_obj.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, (dict, list)):
                    items.extend(flatten_json(item, f"{new_key}[{i}]", sep=sep))
                else:
                    items.append((f"{new_key}[{i}]", item))
        else:
            items.append((new_key, value))
    return items


# Convert the flattened JSON to CSV format
def json_to_csv(json_obj, delimiter=','):
    import csv
    from io import StringIO

    # Flatten the JSON structure into rows
    if isinstance(json_obj, list):
        rows = [dict(flatten_json(item)) for item in json_obj]
    else:
        rows = [dict(flatten_json(json_obj))]

    # Extract CSV headers from the keys
    headers = {key for row in rows for key in row.keys()}

    # Write rows to CSV
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=sorted(headers), delimiter=delimiter)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

    return output.getvalue()


# Main function
def main():
    input_file = "schedule.json"
    output_file = "schedule.csv"

    try:
        # Read JSON input
        with open(input_file, "r", encoding="utf-8") as infile:
            json_data = eval(infile.read())  # Avoid using json.load for no library use

        # Convert JSON to CSV
        csv_result = json_to_csv(json_data)

        # Write CSV output
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(csv_result)

        print(f"Conversion completed successfully. CSV saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
