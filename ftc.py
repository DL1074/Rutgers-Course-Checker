
def find_stuff(a):
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(options=chrome_options)

    url = 'https://sis.rutgers.edu/soc/#keyword?keyword='+a+'&semester=12024&campus=NB&level=U'
    driver.get(url)

    s2out = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 's2out')))

    driver.execute_script("arguments[0].click();", s2out)

    try:
        course_data_parent = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'courseDataParent')))
    except:
        print("course don't exist try again")

    dc = driver.page_source

    s = BeautifulSoup(dc, 'html.parser')


    section = s.find('div', class_='sectionListings')
    if section:
        section_content = section.prettify()

        driver.quit()
        return section_content
    else:
        driver.quit()
        return "div '01:198:213.0.sectionListings' not found"

def extract(a,section_listings_content):
    import re

    file_path = section_listings_content

    pattern = r'<div class="section sectionStatus_(closed|open) courseType_.*?" id="({}\.0\.section\d+\.\d+)">'.format(re.escape(a))
    matches = re.findall(pattern, file_path)
    return matches
    
def extract2(section_listings_content):

    output = []
    pattern_found = False

    for line in section_listings_content.splitlines():
        if pattern_found:
            output.append(line.strip())
            pattern_found = False 
            
        if '<span class="sectionIndexNumber" style="margin-left:9px;text-align:center;vertical-align:middle;width:50px">' in line:
            pattern_found = True  

    return output
    
def combine(matches,output_lines):
    combined_list = []

    for i in range(len(matches)):
        combined_list.append((matches[i][0], matches[i][1], output_lines[i]))
    return combined_list
    
def filter1(combined_data):
    open_lines = [f"{status} {section_id} {index}" for status, section_id, index in combined_data if 'open' in status]
    return open_lines

def listit(b):
    c = [int(value.strip()) for value in b.split(',') if value.strip()]
    return c

def process_list(ids, lst):
    result = []

    if not ids:
        for item in lst:
            section_index = item.find('.section') + len('.section')
            if section_index == -1:
                return False  # If no match is found, return False
            section_number = item[section_index:section_index + 2]
            last_five = item[-5:]
            result.append(f"{section_number} {last_five}")
    else:
        for num in ids:
            search_str = f".section{num}."
            for item in lst:
                if search_str in item:

                    last_five = item[-5:]
                    result.append(f"{num:02d} {last_five}")
                    break

    return result if result else []  # If result is empty, return empty list

def codegen(d1,d):
    g = ""
    if d == "spring":
        g += "1"
    elif d == "fall": g+="9"
    
    g += d1
    return g
    
def filter3(input_list, consistent_number):
    result = {}
    files = 'finals.txt'
    for item in input_list:
        parts = item.split()
        if len(parts) != 2:
            continue  # Skip invalid formats

        key = parts[0]
        value = f"https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection={consistent_number}&indexList={parts[1]}"
        result[key] = value

    with open(files, 'w') as file:
        if result:
            for key, value in result.items():
                file.write(f"{key} {value}\n")
        else:
            file.write("") 

def doall(a1,b1,d11,d2):
    import sys
    d111 = listit(b1) #[56,57,58]
    d3 = codegen(d11,d2) # 12024 or 92024
    if len(d3) != 5:
        print("Try again, something went wrong")
        
        sys.exit()
    a = find_stuff(a1) # find html
    b = extract(a1,a) # 01:198:111 + html
    c = extract2(a) # find index id
    d = combine(b,c) # turn b and c into one
    e = filter1(d) # find open put into list refer to c1 in pre_run_package
    h = process_list(d111,e) # take e and b1 and turn into list ['12 06581', '50 06610...]
    filter3(h,d3) # save into file
    

