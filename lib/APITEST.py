import requests
import json

class APITEST():
    def statuscode(self,Apitype,url,body):
        if Apitype=="GET":
            statuscode=requests.get(url,headers=None).status_code

        elif Apitype=="POST":
            statuscode=requests.post(url,body,headers=None).status_code

        elif Apitype=="PUT":
            statuscode=requests.put(url,body,headers=None).status_code

        else:
            print "Invalid API"
            raise Exception
        return statuscode

    def ApiResponseCode(self,Apitype,url,body=None):
        if Apitype=="GET":
            response=requests.get(url,headers=None).json()

        elif Apitype=="POST":
            response=requests.post(url,body,headers=None).json()

        elif Apitype=="PUT":
            response=requests.put(url,body,headers=None).json()

        else:
            print "Invalid"

        return response



#
# body={"name":"morpheus","job":"leader"}
# payload=json.dumps(body)
#
#
# obj=APITEST()
# obj.statuscode("POST","https://reqres.in/api/users","body")

