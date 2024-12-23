from lark import Lark, Transformer

# Correct Grammar for JSON
json_grammar = r"""
    ?start: value
    ?value: object
          | array
          | STRING    -> string
          | SIGNED_NUMBER   -> number
          | "true"          -> true
          | "false"         -> false
          | "null"          -> null

    array  : "[" [value ("," value)*] "]"
    object : "{" [pair ("," pair)*] "}"
    pair   : STRING ":" value

    %import common.ESCAPED_STRING -> STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
"""

# Transformer to Convert Parsed JSON to XML
class JsonToXmlTransformer(Transformer):
    def string(self, s):
        return f"<string>{s[0][1:-1]}</string>\n"  # Remove quotes

    def number(self, n):
        return f"<number>{n[0]}</number>\n"

    def true(self, _):
        return "<boolean>true</boolean>\n"

    def false(self, _):
        return "<boolean>false</boolean>\n"

    def null(self, _):
        return "<null />\n"

    def array(self, items):
        return "<array>\n" + "".join(items) + "</array>\n"

    def pair(self, pair):
        key, value = pair
        return f"<{key[1:-1]}>\n{value}</{key[1:-1]}>\n"  # Remove quotes from keys

    def object(self, pairs):
        return "<object>\n" + "".join(pairs) + "</object>\n"

    def value(self, v):
        return v[0]

# Parse JSON and Convert to XML
def parse_json_to_xml(json_data):
    parser = Lark(json_grammar, start="start", parser="lalr")
    parsed = parser.parse(json_data)
    transformer = JsonToXmlTransformer()
    return transformer.transform(parsed)

def main():
    fn_in, fn_out = "schedule.json", "out_task3.xml"

    # Read JSON input
    with open(fn_in, "r", encoding="utf-8") as f_in:
        json_data = f_in.read()

    # Convert JSON to XML
    xml_data = parse_json_to_xml(json_data)

    # Write XML output
    with open(fn_out, "w", encoding="utf-8") as f_out:
        f_out.write(xml_data)

if __name__ == "__main__":
    main()
