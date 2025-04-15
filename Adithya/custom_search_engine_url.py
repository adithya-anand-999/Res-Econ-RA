# This is a code file for working on the custom search engine google API to create a more robust system for URL collections. 
 
 # <script async src="https://cse.google.com/cse.js?cx=e04e3429da6a744ab">
 # </script>
 # <div class="gcse-search"></div>
 
import requests
# import json
import string

API_KEY = ""
CX = ""

def clean_string(input_string):
    lower_string = input_string.lower()
    remove_chars = string.punctuation + " "
    translator = str.maketrans("", "", remove_chars)
    cleaned_string = lower_string.translate(translator)
    return cleaned_string

def custom_SE(addr, key=API_KEY, cx=CX):
    # print(1)
    url=f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={addr}"
    # print(2)
    # try:
    response = requests.get(url=url).json()
    # print(response)
    clean_addr = clean_string(addr)
    for obj in response['items']:
        clean_obj_addr = obj['title'].split(" |")[0]
        print(clean_obj_addr)
        if(clean_addr==clean_string(clean_obj_addr)):
            print(f"{addr} -> {obj['link']}")
            return(obj['link'])
    print("matching obj address not found")
    return None
    # except Exception as err:
    #     print(f"{err} occurred when processing address: {addr}")
    #     return None



addrs = ["6 STANDISH CIR, ANDOVER, MA, 01810", "150 TRAINCROFT ST, MEDFORD, MA, 02155"]
custom_SE(addrs[1])