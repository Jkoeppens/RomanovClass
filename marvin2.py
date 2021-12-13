import csv
from dicttoxml import dicttoxml
with open(r"C:\\Users\\mrvng\\Downloads\\settlements_copy.csv","r", encoding="utf-8") as file:
    csv_reader = csv.reader(file,delimiter = "\t")
    csv_list = [item for item in csv_reader]
    file.close()
    labels_list = [item for item in csv_list][0]
    items_list = [item for item in csv_list][1:]
    new_database = {item[0]: dict(zip(labels_list[1:], item[1:]))
                   for item in items_list}
    xml = dicttoxml(new_database, custom_root='test', attr_type=False)
    with open(r"C:\\Users\\mrvng\\Downloads\\settlements.xml","w", encoding="utf-8") as xml_file:
        xml_file.write(str(xml))
        xml_file.close()

