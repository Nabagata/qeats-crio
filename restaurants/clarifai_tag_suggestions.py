import json
import requests

#TODO: CRIO_TASK_MODULE_TAG_SUGGESTION
# As part of this module you are expected to complete the get_tags_suggestions() function
# Tasks:
# 1) You need to register as Clarifai developer to obtain an API Key to the Food Model
#    The Food model can be found here:
#    https://www.clarifai.com/models/food-image-recognition-model-bd367be194cf45149e75f01d59f77ba7
#    A sample request and response can be found in the above link
# 2) Use the food model to get implement tag suggestions

# Parameters
# ----------
# api_key : string
#     API Key for Clarifai
# image_url : string
#     publicly accessible URL of the image to get tag suggestions
# Return Type: list()
#   return a list of tags provided by the Clarifai API
def get_tags_suggestions(api_key, image_url):
    # write your code here
    headers = {
        'Authorization': "Key {}".format(api_key),
        'Content-Type': "application/json",
    }

    data = '\n    {\n      "inputs": [\n        {\n          "data": {\n            "image": {\n              "url": "'+image_url+'"\n            }\n          }\n        }\n      ]\n    }\n'
    # data = {
    #     "inputs": [
    #         {
    #             "data": {
    #                 "image": {
    #                     "url": image_url
    #                 }
    #             }
    #         }
    #     ]
    # }


    response = requests.post('https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs', headers=headers, data=data)
    # print(response)
    sz = len(response.json()['outputs'][0]['data']['concepts'])
    tags = []
    # print(response.json()['outputs'][0]['data']['concepts'])
    for i in range(sz):
      tags.append(response.json()['outputs'][0]['data']['concepts'][i]['name'])
    return tags

def get_access_token(token_name):
    file_handle = open('access_tokens.sh', 'r+')
    lines = file_handle.readlines()
    file_handle.close()
    for line in lines:
        tokens = line.strip().split('=')
        if tokens[0] == token_name:
            return tokens[1].strip()
    return 'Not found'

if __name__ == '__main__':
    clarify_api_key = get_access_token('CLARIFAI_API_KEY')
    # print(clarify_api_key)
    test_image_url = "https://i.imgur.com/dlMjqQe.jpg"
    test1 = "https://www.browneyedbaker.com/wp-content/uploads/2013/05/buttermilk-waffles-8-1200.jpg"
    tags_suggessted = get_tags_suggestions(clarify_api_key, test_image_url)
    print(tags_suggessted)
