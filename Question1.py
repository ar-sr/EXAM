# """
# create a new  array of dictionary by extracting data from data,json
# new dictionay thus created should be as shown below


# [
#     {
#      "name": "Organic Honeycrisp Apples Bag",
#      "categories": ["Produce","Fruits","Apples",
#      "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
#      "base_price":0.64,
#      "availability_status":true
#     },
#     {
#      "name": "Granny Smith Apples",
#      "categories": ["Produce","Fruits","Apples",
#      "image":"https://d2d8wwwkmhfcva.cloudfront.net/800x/filters:fill(FFF,true):format(jpg)/d2lnr5mha7bycj.cloudfront.net/product-image/file/large_fda52644-51b7-40cd-8322-c698b7ea30c1.png",
#      "base_price":0.64,
#      "availability_status":true
#     }
#     .
#     .
#     .
#     .
    
# ]


# Remember to extract all items above illustrated are just sample
# """


# #ANSWER-1


import json



with open("/home/arya/EXAM/rotech_exam/Set 1/data.json","r") as file:
    data=json.load(file)
    # print(data)
    # print(data.keys())

    items=data["items"]
    fetched_list= [""]
    for i in items:
        name=i["name"]
        categories=i["categories"]
        images=i["images"]
        base_price=i["base_price"]
        availability_status=i["availability_status"] 
        fetched={
                "name":name,
                "categories":categories,
                "images":images,
                "base_price":base_price,
                "availability_status":availability_status
            }
  
        fetched_list.append(fetched)
        print(f"{fetched_list}")
        
            #   print(fetched)
        
        
        
        
        