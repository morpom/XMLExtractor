import fitz  
import os
import xml.dom.minidom

def extract_embedded_files(pdf_path):
    doc = fitz.open(pdf_path)
    for i in range(doc.embfile_count()):
        file_name = doc.embfile_names()[i]
        file_data = doc.embfile_get(file_name)
        foldername = pdf_path.replace('.pdf', '')
        try:
            os.mkdir(foldername)
        except:
            pass
        if file_name.endswith('.xml'):
            xml_content = xml.dom.minidom.parseString(file_data)
            pretty_xml_as_string = xml_content.toprettyxml()
            with open(foldername + '/' + file_name, "w", encoding="utf-8") as f:
                f.write(pretty_xml_as_string)
        else:
            with open(foldername + '/' + file_name, "wb") as f:
                f.write(file_data)
