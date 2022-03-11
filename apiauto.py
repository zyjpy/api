
import json
import logging
import time
import requests
logging.basicConfig(level=logging.INFO)
class Apiauto(object):
    
    def loginInvitee(self):
        
        proxies = {
            "http": "http://127.0.0.1:8888",
            "https": "http://127.0.0.1:8888",
        }
        global token
        url="https://staging.www.qiaojian.vip/auth/oauth/token?grant_type=password&username=15349536837&password=536837"
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1(UnityWebRequest/1.0,libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity',
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Accept-Language':'zh-CN,zh;',
            'Authorization':'Basic cGFkOnBhZA==',
            'X-Unity-Version':'2020.3.4f1c1',
            'Content-Length':'0',
        }

        timeout=2
        logging.info("登录")
        r = requests.post(url, headers=header, timeout=timeout)
        token = r.json()['access_token']
        logging.info(token)
    def get_pageInvite(self):
        global data,header
        time.sleep(3)
        url="https://staging.www.qiaojian.vip/admin/pad/team/pageInvite?page=1&pageSize=99999&status=UNCHECK"
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        timeout=2
        logging.info("获取邀请列表中的applyid")
        params={
            "page":1,
            "pageSize":99999,
            "status":"UNCHECK",
        }
        r = requests.get(url,params=params,headers=header)
        logging.info(r.text)
        apply_id2 = r.json()['data']["records"]
        logging.info(f"apply_id2:{apply_id2}")
        apply_id = r.json()['data']["records"][0]["id"]

        logging.info(apply_id)
        time.sleep(3)
        logging.info(isinstance(apply_id,int))
        data = {"applyId":apply_id,"inviteStatus":1}
        data = json.JSONEncoder().encode(data)
    def agreeInvite(self):
        global data,header
        url="https://staging.www.qiaojian.vip/admin/pad/team/answerInvite"
        # header={
        #     'Host':'staging.www.qiaojian.vip',
        #     'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
        #     'Accept':'*/*',
        #     'Accept-Encoding':'identity',
        #     'Content-Type':'application/json;charset=utf-8',
        #     'FROM-TYPE':'PAD',
        #     'Authorization':f'Bearer {token}',
        #     'X-Unity-Version':'2020.3.4f1c1',
        #     'Content-Length':'32',
        #     'Expect':'100-continue',
        # }

        timeout=3
        logging.info("同意邀请")
        r = requests.put(url, headers=header,data=data,timeout=timeout)
        logging.info(r.text)
        
    def exitTeam(self):

        timeout=2
        url="https://staging.www.qiaojian.vip/admin/personal/team/exit/11019"
        r = requests.put(url, headers=header,timeout=timeout)
        logging.info(r.text)
    def applyJoin(self):


        data ={"teamNumber":"37108012"}
        data = json.JSONEncoder().encode(data)
        timeout=2
        url="https://staging.www.qiaojian.vip/admin/pad/team/applyJoin"
        r = requests.post(url, headers=header,data = data,timeout=timeout)
        logging.info(r.text)
    def creat_team_apply(self):
        data = {"userName":"创建","enterpriseName":"创建企业","templateCode":"TEAM_PRO"}
        data = json.JSONEncoder().encode(data)
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        timeout=2
        url="https://staging.www.qiaojian.vip/admin/pad/team/createTeamApply"
        r = requests.post(url, headers=header,data = data,timeout=timeout)
        logging.info(r.text)
    def cancel_team_apply(self):
        
        timeout=2
        url = "https://staging.www.qiaojian.vip/admin/pad/team/cancelTeamApply"
        r = requests.post(url, headers=header,timeout=timeout)
        logging.info(r.text)
    def save_product(self):
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        url_1 = "https://staging.www.qiaojian.vip/admin/oss/upload_sync_callback"        
        url_2 = "https://staging.www.qiaojian.vip/admin/pad/product/save"
        filename = dir
        # logging.info(f"135{filename}")
        data1 = {f"filename":filename,"originFileName":"defaultcover.png","fileType":"COVER","height":"","mimeType":"","size":"","width":"","storeType":"OSS","url":f"https://cdn.zhuquev2.preprod.qiyukeji.cn/{filename}","updater":11074,"updaterType":"PERSONAL"}
        logging.info(f"136{data1}")
        data1 = json.JSONEncoder().encode(data1)
        response_upload_callback = requests.post(url_1, headers=header,data = data1)
        # logging("140"+str(response_upload_callback.json()['data']))
        logging.info(response_upload_callback.text)
        avater = response_upload_callback.json()['data']["url"]
        avater = str(avater)
        # fileId=response_upload_callback.json()['data']["fileId"]

        logging.info(f"avater:{avater}")
        data2 = {"title":"mypr","introduction":"","typeId":0,"open":1,"coverUrl":avater,"fileDescId":"0","team":0}
        # data2 = json.JSONEncoder().encode(data2)
        
        data2 = {"title":"我的3D作品","introduction":"","typeId":0,"open":1,"coverUrl":"https://cdn.zhuquev2.preprod.qiyukeji.cn/zhuque/tenant1/user11074/cover/2022/03/01/20220301125641516_defaultcover.png","fileDescId":"0","team":0}
        data2 = json.JSONEncoder().encode(data2)
        response_save_product = requests.post(url_2, headers=header,data = data2)
        logging.info(response_save_product.text)
        time.sleep(3)
        logging.info("保存作品成功")
    def get_product_list(self):
        global product_id
        url = "https://staging.www.qiaojian.vip/admin/pad/product/pageLocalProduct?page=1&pageSize=19&typeId=&title=&category=PERSONAL"
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        params={
            "page":1,
            "pageSize":19,
        }
        r = requests.get(url,headers=header,params = params)
        logging.info(f"169行{r.text}")        
        r = r.json()["data"]["records"]
        logging.info(r)
        product_id = r[0]['productId']
        
        # productId = r["data"]
        # logging.info(r.productId)
    def del_product(self):
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }        
        url = f"https://staging.www.qiaojian.vip/admin/pad/product/{product_id}"
        r = requests.delete(url,headers=header)
        logging.info(r.text)
    def apply_product(self):
        url = "https://staging.www.qiaojian.vip/admin/pad/product/apply"
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }  
    
        data = {"title":"qwe","introduction":"","productId":product_id,"portalTypeId":2}
        r = requests.post(url,headers=header,data=data)
    def get_upload_sign(self):
        global dir
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity', 
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'Authorization':f'Bearer {token}',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        parmas = {
            'fileType':'COVER',
            'fileName':'defaultcover.png',
            'sceneName':'%E6%88%91%E7%9A%843D%E4%BD%9C%E5%93%81',
            'userId':'11074',
            'encrypted':'0',
            'uploadSource':'PAD',
            'fileSize':'9015',
            'teamId':'',
            'suffixHide':'0',
            'appEncryptKey':'',
            'appEncryptType':'0',
            'appEncrypt':'0',
        }
        url = "https://staging.www.qiaojian.vip/admin/oss/get_upload_sign?fileType=COVER&fileName=defaultcover.png&sceneName=%E6%88%91%E7%9A%843D%E4%BD%9C%E5%93%81&userId=11074&encrypted=0&uploadSource=PAD&fileSize=9015&teamId=&suffixHide=0&appEncryptKey=&appEncryptType=0&appEncrypt=0"
        r = requests.get(url,headers=header,params=parmas)
        dir = r.json()["data"]["dir"]
        # logging.info(f"234{dir}")
        dir = str(dir[:-16])
        dir = dir.replace(",cover","")
        # logging.info(f"237{dir}")
    def get_online_product_firsgroup(self):
        global r_product_online
        url = "https://staging.www.qiaojian.vip/admin/pad/productonline/page?page=1&pageSize=20&typeId=2&title=&selection="
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity',
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        parmas = {
            'page':'1',
            'pageSize':'20',
            'typeId':'2',

        }
        r = requests.get(url,headers=header,params=parmas)
        r_title = r.json()["data"]["records"][-1]["title"]
        r_product_online = r.json()["data"]["records"][-1]["productOnlineId"]
        # return r_title,r_product_online
    def cancel_online_product(self):
        url = "https://staging.www.qiaojian.vip/admin/pad/productonline/onOff"
        header={
        'Host':'staging.www.qiaojian.vip',
        'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
        'Accept':'*/*',
        'Accept-Encoding':'identity',
        'Content-Type':'application/json;charset=utf-8',
        'FROM-TYPE':'PAD',
        'Authorization':f'Bearer {token}',
        'X-Unity-Version':'2020.3.4f1c1',
        }
    
        data = {"productOnlineIds":[r_product_online],"status":"OFFLINE"}
        data = json.JSONEncoder().encode(data)           
        r = requests.put(url,headers=header,data=data)
        logging.info(r.text)
    # def del_my_product(self):
    #     url = f"https://staging.www.qiaojian.vip/admin/pad/product/{product_id}"
    #     header={
    #     'Host':'staging.www.qiaojian.vip',
    #     'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
    #     'Accept':'*/*',
    #     'Accept-Encoding':'identity',
    #     'Content-Type':'application/json;charset=utf-8',
    #     'FROM-TYPE':'PAD',
    #     'Authorization':f'Bearer {token}',
    #     'X-Unity-Version':'2020.3.4f1c1',
    #     }  
    
    #     data = {"productOnlineIds":[r_product_online],"status":"OFFLINE"}
    #     data = json.JSONEncoder().encode(data)           
    #     r = requests.put(url,headers=header,data=data)
    #     logging.info(r.text)
    def get_choiceness_list(self):
        url = "https://www.qiaojian.vip/admin/pad/productonline/page?page=1&pageSize=20&typeId=&title=&selection=1"
        header={
            'Host':'staging.www.qiaojian.vip',
            'User-Agent':'UnityPlayer/2020.3.4f1c1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept':'*/*',
            'Accept-Encoding':'identity',
            'Content-Type':'application/json;charset=utf-8',
            'FROM-TYPE':'PAD',
            'X-Unity-Version':'2020.3.4f1c1',
        }
        parmas = {
            'page':'1',
            'pageSize':'20',
            'selection':'1',
        }
        r = requests.get(url,headers=header,params=parmas)
        r_title = r.json()["data"]["records"][0]["title"]
        logging.info(f"r_title{r_title}")
if __name__ == "__main__":
    apiauto = Apiauto()
    # apiauto.loginInvitee()
    # apiauto.get_pageInvite()
    # apiauto.agreeInvite()
    # apiauto.exitTeam()
    # apiauto.applyJoin()
    # apiauto.creat_team_apply()
    # apiauto.cancel_team_apply()
    # apiauto.get_upload_sign()
    # apiauto.save_product()
    # apiauto.get_product_list()
    # apiauto.apply_product()
    # apiauto.del_product()
    # apiauto.get_online_product_firsgroup()
    # apiauto.cancel_online_product()
    # apiauto.del_product()
    apiauto.get_choiceness_list()