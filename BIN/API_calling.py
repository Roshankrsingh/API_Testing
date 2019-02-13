from lib.APITEST import APITEST
import json
import os
import sys
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
syspaths = [basedir]
sys.path.extend(syspaths)

with open (basedir + "\Config\APICONFIG.json","r") as F:
    read_json=json.load(F)

class API_calling(APITEST):
    def Get_API(self):
        api_list = read_json["apitesting"]

        for k,v in api_list.items():
            if v[0] =="POST" or v[0]=="PUT":
                v.append(read_json["payload"][k])

        return api_list


    def Get_All_Api_Response(self):
        failed_apis = []
        api_list = self.Get_API()
        for apis, value in api_list.items():
            api_type=value[0]
            url="https://reqres.in" + value[1]
            if len(value)> 2:
                body = value[1]
            else:
                body = None
            print "calling api type {} and uri {} and body {}".format(api_type, url, body)
            statuscode=self.statuscode(api_type,url,body)
            responsecode=self.ApiResponseCode(api_type,url,body)
            print "The api type {} and uri {} and body {} and status {} and response {}".format(api_type, url, body,statuscode,responsecode)
            if statuscode != 200:
                failed_apis.append(url)
        if failed_apis:
            print failed_apis
            raise Exception

    def Call_Specific_api(self,apiname):
        api_list = self.Get_API()
        value=api_list[apiname]
        api_type=value[0]
        url="https://reqres.in" + value[1]
        if len(value)> 2:
            body = value[1]
        else:
            body = None
        print "calling api type {} and uri {} and body {}".format(api_type, url, body)
        statuscode=self.statuscode(api_type,url,body)
        responsecode=self.ApiResponseCode(api_type,url,body)
        print "The api type {} and uri {} and body {} and status {} and response {}".format(api_type, url, body,statuscode,responsecode)
        if statuscode != 200:
           print url
           raise Exception




D=API_calling()
# D.Get_All_Api_Response()
# D.Call_Specific_api("student_unknown")

