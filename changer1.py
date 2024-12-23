# Recursive function to convert JSON to formatted XML
def json_to_xml_manual(json_obj, root_tag="root", indent="  "):
    def build_xml(obj, tag_name, level=0):
        spaces = indent * level
        xml = ""
        if isinstance(obj, dict):  # Handle dictionaries
            xml += f"{spaces}<{tag_name}>\n"
            for key, value in obj.items():
                xml += build_xml(value, key, level + 1)
            xml += f"{spaces}</{tag_name}>\n"
        elif isinstance(obj, list):  # Handle lists
            for item in obj:
                xml += build_xml(item, tag_name, level)
        else:  # Handle simple values
            xml += f"{spaces}<{tag_name}>{obj}</{tag_name}>\n"
        return xml

    # Start building XML
    return f"<{root_tag}>\n{build_xml(json_obj, 'content', level=1)}</{root_tag}>\n"


# Main function
def main():
    # Input and output file names
    input_file = "schedule.json"
    output_file = "schedule_manual.xml"

    try:
        # Read the JSON file
        with open(input_file, "r", encoding="utf-8") as infile:
            json_data = eval(infile.read())  # Avoid using json.load for no library use

        # Convert JSON to formatted XML
        xml_result = json_to_xml_manual(json_data, root_tag="schedule")

        # Write the XML result to the output file
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(xml_result)

        print(f"Conversion completed successfully. XML saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
