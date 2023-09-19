# Test cases

# Test case 1: Using Example address takes 'Banashankari 3rd Stage' using strip and stored in area.
# Test case 2: Next function checking the state and pincode. Using regex takes only pincode.
# Test case 3: Installed roman and check the condition, If number is present or not. If number is there that number changed as roman.
# Test case 4: If updated_text haves data mean it go inside the function and checks the API compare the address of the name, deliverystatus and pincode.
# Test case 5: The pincode matches mean it print correct pincode. otherwise result will be print wrong pincode and gives correct pincode number.
# Test case 6: If updated_text is none it checks and compare API then print the result


import re
import roman  # Import the 'roman' module
import requests


def areaget():
    address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"
    address_parts = address.split(',')
    if len(address_parts) >= 5:
        area = address_parts[-4].strip()
        # print(area)
        return area
    else:
        print("Not enough elements to extract.")
        return None
def pincodedata():
    address = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"
    address_parts = address.split(',')
    if len(address_parts) >= 5:
        area = address_parts[-1].strip()
        print("area",area)
        pattern = r'(\d.+)' 
        match = re.search(pattern, area) 
        code = match.group(0) 
        return code
    else:
        print("Not enough elements to extract.")
        return None
result = areaget()
# print(result)
updated_text = None  # Initialize 'updated_text' outside the if statement
inputpincode= pincodedata()
if result is not None:
    pattern = r'\d' 
    match = re.search(pattern, result)  
    # print("match",match)
    if match:
        digit = match.group(0)
        roman_numeral = roman.toRoman(int(digit))
        if digit == '3': 
            updated_text = result.replace("3rd", roman_numeral)
            print("upda", updated_text)
        else:
            updated_text =result
            print("Digit is not 3 in the extracted text.")
    else:
        print("No digit found in the extracted text.")
else:
    print("Extraction failed.")

if updated_text is not None:
 print("sssssssssssssssss",updated_text)
 url = f"https://api.postalpincode.in/postoffice/{updated_text}"
 response = requests.get(url)
 if response.status_code == 200:
    data = response.json()
    PostOffice =data[0].get('PostOffice')
    finaldata =[]
    for name in PostOffice:
      nameof_data = name.get('Name')
      print("nnnnnnnnnnnn",nameof_data)
      print(nameof_data == updated_text,"udpd")
      if nameof_data  == updated_text:
           status =name.get('DeliveryStatus')
           finaldata.append(status)
           print(name)
           if status == "Delivery":
            outputPincode =  name.get('Pincode')  
            if inputpincode == outputPincode:
                print("correct pincode")
            else:
                print("wrong pincode")
                print("Incorrect pincode is", inputpincode,"Change to Correct pincode",outputPincode)
 else:
    print("Failed to fetch data. Status code:", response.status_code)
elif updated_text is None:
 print("runningggggggg")
 url = f"https://api.postalpincode.in/postoffice/{result}"
 response = requests.get(url)
 if response.status_code == 200:
    data = response.json()
    PostOffice =data[0].get('PostOffice')
    finaldata =[]
    for name in PostOffice:
      nameof_data = name.get('Name')
    #   print(nameof_data  , result)
      if nameof_data  == result:
           status =name.get('DeliveryStatus')
           finaldata.append(status)
           print(name)
           if status == "Delivery":
            outputPincode =  name.get('Pincode')  
            if inputpincode == outputPincode:
                print("correct pincode")
            else:
                print("wrong pincode",inputpincode,outputPincode)
 else:
    print("Failed to fetch data. Status code:", response.status_code)


