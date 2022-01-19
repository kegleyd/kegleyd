import os
import sys
import re
from multiprocessing import Pool, cpu_count , Manager
from time import perf_counter




#regexs = re.compile("(([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*|hp[_#]dbspi.*\s)",re.VERBOSE|re.IGNORECASE|re.DOTALL)
#regexs = re.compile("(([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*|hp[_#]dbspi.*\s)",re.VERBOSE|re.IGNORECASE|re.DOTALL)

regexs = re.compile("('\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*|hp\_dbspi|hp\#\S*123|OBM10|admin|([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)|(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))", re.VERBOSE|re.IGNORECASE|re.DOTALL)

 
 

def read_write(file_name):
    content = ""
    file_size = os.path.getsize(file_name)
    with open(file_name, 'r') as open_file:
        try:
            content = open_file.readlines()
        except Exception as e: print(f"exception in {file_name}")
    if content:
        with open(file_name, 'w') as open_file:
            try:
                #print(f"File Size of {file_name} is :", file_size, "bytes")
                for line in content:
                    newline = re.sub(regexs,"XXXXXXXX ",line)
                    #print(newline) 
                    open_file.write(newline)
            except Exception as e: print(f"exception in {file_name}")
    else:
        os.remove(file_name)           
        print(f"{file_name} :", file_size, "bytes removed")

def read_write_xml(file_name):
    content = ""
    file_size = os.path.getsize(file_name)
    with open(file_name, 'r') as open_file:
        try:
            content = open_file.readlines()
        except Exception as e: print(f"exception in {file_name}")
    if content:
        with open(file_name, 'w') as open_file:
            try:
                #print(f"File Size of {file_name} is :", file_size, "bytes")
                for line in content:
                    newline = re.sub(regexs,"XXXXXXXX ",line)
                    #print(newline) 
                    open_file.write(newline)
            except Exception as e: print(f"exception in {file_name}")
    else:
        os.remove(file_name)           
        print(f"{file_name} :", file_size, "bytes removed")


def read_print(file_name):

    content = ""

    file_size = os.path.getsize(file_name)

    with open(file_name, 'r') as open_file:
        try:
            content = open_file.readlines()
        except Exception as e: print(f"exception in {file_name}")
        if content:
            try:
                for line in content:
                    match=   re.findall(regexs,line)
                    if match:
                        return match           
            except Exception as e: print(f"exception in {file_name}")
        else:
            try:
                if file_size:
                    print(f"{file_name} :", f"has {file_size} but content was unreadable")
            except Exception as e: print(f"exception in {file_name}")

def read_print_xml(file_name):

    content = ""

    file_size = os.path.getsize(file_name)

    with open(file_name, 'r') as open_file:
        try:
            content = open_file.readlines()
        except Exception as e: print(f"exception in {file_name}")
        if content:
            try:
                for line in content:
                    match=   re.findall(regexs,line)
                    if match:
                        return match           
            except Exception as e: print(f"exception in {file_name}")
        else:
            try:
                if file_size:
                    print(f"{file_name} :", f"has {file_size} but content was unreadable")
            except Exception as e: print(f"exception in {file_name}")

    

 

def main():

    t1_start = perf_counter()
    fileList = []
    rootdir = input("Please input directory to scrub: ")
    answer = input(f"is {rootdir} the correct directory? (Y/N) ")  

    if answer == "Y" or "y" or "yes" or "YES":
        pass
    else:
        sys.exit()

    mode = input(f"enter 1 for search mode or 2 for redact mode (1 or 2) : ")

    for root, subFolders, files in os.walk(rootdir):
        for file in files:
          fileParts = file.split('.')
          if len(fileParts) > 1:
              fileList.append(os.path.join(root,file))
    good_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and not file.endswith( ('.xml','.zip','.tar','.jar') ) ]
    xml_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and file.endswith( (".xml" ) ) ]
    compressed_files = [ file for file in fileList if os.path.isfile(file) and os.access(file, os.R_OK) and file.endswith( (".zip",".tar",".jar") ) ]

    if mode == "1":
        print("search selected")
        with Pool(processes=cpu_count()) as pool:
            results = pool.map(read_print, good_files)
            print("For the moment, the pool remains available for more work")
    else:
        with Pool(processes=8) as pool:
            results = pool.map(read_write, good_files)
            print("For the moment, the pool remains available for more work")
    # exiting the 'with'-block has stopped the pool
    #print("Now the pool is closed and no longer available")
    
    t1_stop = perf_counter()
    print("Elapsed time during the whole program in seconds:", (t1_stop-t1_start)/60)
    

if __name__ == '__main__':
    main()
