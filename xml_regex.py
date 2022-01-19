import os
import sys
import re
from lxml import etree as ET


regexs = re.compile("('\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*|hp\_dbspi|hp\#\S*123|OBM10|admin|([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))", re.VERBOSE|re.IGNORECASE|re.DOTALL)

# for root, subFolders, files in os.walk(rootdir):
#     for file in files:
#       fileParts = file.split('.')
#       if len(fileParts) > 1:
#           fileList.append(os.path.join(root,file))
# good_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and not file.endswith( ('.xml','.zip','.tar','.jar') ) ]
# xml_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and file.endswith( (".xml" ) ) ]
# compressed_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and file.endswith( (".zip",".tar",".jar") ) ]

def read_print_xml(file_name):
    outfile = file_name + ".scrubbed"
    file_size = os.path.getsize(file_name)
    content= ET.parse(file_name)    
    xml_content= ET.tostring(content,encoding="unicode", pretty_print=True)
    print(outfile)
    #print(xml_content)
    # with open(file_name, 'rb') as open_file:
    #     try:
    #         content = open_file.read()
    #         bs_content = BeautifulSoup(content, 'xml')
    #     except Exception as e: print(f"exception in {file_name}")
    edited = re.sub(regexs,"xxxxxxxxxx",xml_content)
    with open(outfile,'w+') as f:
         f.write(edited)
    #     else:
    #         try:
    #             if file_size:
    #                 print(f"{file_name} :", f"has {file_size} but content was unreadable")
    #         except Exception as e: print(f"exception in {file_name}")

read_print_xml("C:/Users/Daniel/Downloads/Single_centos8.mshome.net_2022.01.11.12.28.58.logs/conf/LDAP-security.xml")
