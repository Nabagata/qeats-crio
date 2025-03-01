import os
import json
import requests

class Facebook:
    @staticmethod
    def get_access_token(token_name):
        access_token = os.getenv('PWD') + '/access_tokens.sh'
        f = open(access_token, 'r+')
        lines = f.readlines()
        for line in lines:
            tokens = line.strip().split('=')
            if tokens[0] == token_name:
                return tokens[1].strip()

        return 'Not found'

    def __init__(self):
        self.page_id = Facebook.get_access_token('FACEBOOK_PAGE_ID')
        self.page_access_token = Facebook.get_access_token('FACEBOOK_PAGE_ACCESS_TOKEN')
        # print(self.page_id)
        # print(self.page_access_token)

    #TODO: CRIO_TASK_MODULE_FACEBOOK_SHARE_FROM_CLI
    # Tasks:
    # 1) Complete the publish_photo_msg() function.
    #    This function should publish a post with the given message and photo.
    #    The post should be published to the QEats Facebook Page
    #    You can use the page ID and access tokens provided in self.page_id and self.page_access_token
    # 2) To find which API to hit, check out developer section of the Facebook API (https://developers.facebook.com/docs/graph-api/reference/page/photos/#publish)
    # 3) To know how to make an API request in Python have a look at - https://crio-assist.zendesk.com/hc/en-us/articles/360038676513-How-to-make-an-API-request-in-Python


    # Parameters
    # ----------
    # message : string
    #     message to be posted
    # image_url : string
    #     publicly accessible URL of the image to be posted
    # Return Type: None
    def publish_photo_msg(self, message, image_url):
        # write your code here
        # url=https://graph.facebook.com/v5.0/{self.page_id}/photos
        # files = {
        #     'url': (None, image_url),
        #     'published': (None, 'false'),
        #     'access_token': (None, self.page_access_token),
        #     'caption': (None, message)
        # }

        params = (
            ('access_token', self.page_access_token),
        )

        data = {
        'url': image_url,
        'published': 'true',
        'caption': message
        }

        # response = requests.post('https://graph.facebook.com/v5.0/{}/photos'.format(self.page_id), params=params, data=data)

        #NB. Original query string below. It seems impossible to parse and
        #reproduce query strings 100% accurately so the one below is given
        #in case the reproduced version is not "correct".
        response = requests.post('https://graph.facebook.com/v5.0/{}/photos?access_token={}'.format(self.page_id,self.page_access_token), data=data)


        # response = requests.post('https://graph.facebook.com/v5.0/{}/photos'.format(self.page_id), files=files)
        # print(response)
        print(response.status_code, response.json())
        return

if __name__ == '__main__':
    facebook = Facebook()
    # TODO: CRIO_TASK_MODULE_FACEBOOK_SHARE_FROM_CLI
    # Tasks:
    # 1) Search for your favorite ice-cream picture on images.google.com
    # 2) Copy the URL of the image and assign it to the 'image_url' variable
    #    Eg: image_url = 'http://ksmartstatic.sify.com/cmf-1.0.0/appflow/bawarchi.com/Image/oeturjecjjdah_bigger.jpg'
    # 3) Fill the 'my_name' variable with your name so that you know the posts you have created
    image_url = 'https://images.squarespace-cdn.com/content/v1/56c60ca67da24f92b1710ed4/1565112894755-HMADGHO4CFIURZHPTTNL/ke17ZwdGBToddI8pDm48kIGwwe6DACn7JEWA3wDy-FhZw-zPPgdn4jUwVcJE1ZvWQUxwkmyExglNqGp0IvTJZUJFbgE-7XRK3dMEBRBhUpzxTlVPFuGyTYmaued85OQCg-LrY9TyapXTYvHVc1wXyhnZTGcyMCr9BnDwEKONb6I/image-asset.jpeg'
    my_name = 'nabagata'

    message = my_name + ' likes this ice-cream!'
    facebook.publish_photo_msg(message, image_url)
