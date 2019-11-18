import requests


def initUser(token):
    url = "https://api.snowbank.me/init-user"
    payload = ""
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    return str(response.text)

def createUser(password,userHash,token):
    url = "https://api.snowbank.me/create-user"

    payload = "{ \"password\": '%s', \"userHash\": '%s' }"%(password,userHash)
    headers = {
    'Content-Type': "application/json",
    'Authorization': "%s"%(token),
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def unlockUser(password,userHash,token):
    url = "https://api.snowbank.me/user/unlock"

    payload = "{ \"password\": '%s', \"userHash\": '%s' }"%(password,userHash)
    headers = {
    'Content-Type': "application/json",
    'Authorization': "%s"%(token),
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def userBalance(userHash,token):
    url = "https://api.snowbank.me/user/balance"
    payload = "{\"userHash\":'%s' }"%(userHash)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def generateAddress(userHash,token):
    url = "https://api.snowbank.me/user/generate-address"
    payload = "{\"userHash\": '%s'}"%(userHash)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def publicKey(userHash,token):
    url = "https://api.snowbank.me/user/public-key"
    payload = "{\"userHash\": '%s'}"%(userHash)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def getUsers(token):
    url = "https://api.snowbank.me/get-users"
    payload = ""
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("GET", url, data=payload, headers=headers)
    return response.text

def createChannel(fromUserHash,toUserHash,satoshi,token):
    url = "https://api.snowbank.me/create-channel"
    payload = "{\"fromUserHash\": '%s', \"toUserHash\": '%s', \"satoshi\": '%s'}"%(fromUserHash,toUserHash,satoshi)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def sendCoin(fromUserHash,toUserHash,satoshi,token):
    url = "https://api.snowbank.me/send-coin"
    payload = "{\"fromUserHash\": '%s' , \"toUserHash\": '%s', \"satoshi\": '%s'}"%s(fromUserHash,toUserHash,satoshi)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def deleteChannel(fromUserHash,toUserHash,token):
    url = "https://api.snowbank.me/delete-channel"
    payload = "{\"fromUserHash\": '%s', \"toUserHash\": '%s'}"%(fromUserHash,toUserHash)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def deletePeer(fromUserHash,toUserHash,token):
    url = "https://api.snowbank.me/delete-peer"
    payload = "{\"fromUserHash\": '%s', \"toUserHash\": '%s'}"%(fromUserHash,toUserHash)
    headers = {
    'Authorization': "%s"%(token),
    'Content-Type': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text

def changePassword(currentPassword,newPassword,userHash,token):
    url = "https://api.snowbank.me/create-user"

    payload = "{ \"currentPassword\": '%s', \"newPassword\": '%s', \"userHash\": '%s' }"%(currentPassword,newPassword,userHash)
    headers = {
    'Content-Type': "application/json",
    'Authorization': "%s"%(token),
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.text