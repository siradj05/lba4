from json2xml import json2xml
from json2xml.utils import  readfromjson


def main():
    fn_in, fn_out = 'schedule.json', 'out_lib.xml'
    with open(fn_out, 'w', encoding='utf-8') as f_out:
        data = readfromjson(fn_in)

        print(json2xml.Json2xml(data, wrapper='main',
                                attr_type=False).to_xml(), file=f_out)


if __name__ == '__main__':
    main()