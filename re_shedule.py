import json
import re

def validate_filename(filename, pattern):
    """Validate the filename using the provided regex pattern."""
    if not re.match(pattern, filename):
        raise ValueError(f"Invalid filename: {filename}. It must match the pattern: {pattern}")

def json_to_xml(data, root_tag="schedule", indent="  "):
    """Convert a JSON dictionary to a formatted XML string."""
    def dict_to_xml(tag, d, level=0):
        spaces = indent * level
        elements = []
        for key, value in d.items():
            if isinstance(value, dict):
                elements.append(f"{spaces}<{key}>\n{dict_to_xml(key, value, level + 1)}\n{spaces}</{key}>")
            elif isinstance(value, list):
                for item in value:
                    elements.append(f"{spaces}<{key}>\n{dict_to_xml(key, item, level + 1)}\n{spaces}</{key}>")
            else:
                elements.append(f"{spaces}<{key}>{value}</{key}>")
        return "\n".join(elements)

    root_spaces = indent * 0
    return f"{root_spaces}<{root_tag}>\n{dict_to_xml(root_tag, data, 1)}\n{root_spaces}</{root_tag}>"

def main():
    fn_in, fn_out = 'schedule.json', 'out_re.xml'
    
    # Validate filenames
    json_pattern = r'^[a-zA-Z0-9_-]+\.json$'
    xml_pattern = r'^[a-zA-Z0-9_-]+\.xml$'
    validate_filename(fn_in, json_pattern)
    validate_filename(fn_out, xml_pattern)

    with open(fn_in, 'r', encoding='utf-8') as f_in:
        data = json.load(f_in)
    
    xml_data = json_to_xml(data)
    
    with open(fn_out, 'w', encoding='utf-8') as f_out:
        print(xml_data, file=f_out)

if __name__ == '__main__':
    main()
