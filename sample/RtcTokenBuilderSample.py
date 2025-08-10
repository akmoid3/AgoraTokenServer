#! /usr/bin/python
# ! -*- coding: utf-8 -*-

import sys
import os
import time
from random import randint
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.RtcTokenBuilder import RtcTokenBuilder, Role_Publisher

# Need to set environment variable AGORA_APP_ID
appId = "4703d12de1af47eb94294a750641a314"
# Need to set environment variable AGORA_APP_CERTIFICATE
appCertificate = "fe14c8552166435c9ea3a9b0693d1c78"

channelName = "Unity_Channel"
uid = 2882341273
userAccount = "2882341273"
expireTimeInSeconds = 3600
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


def main():
    print("App Id: %s" % appId)
    print("App Certificate: %s" % appCertificate)
    if not appId or not appCertificate:
        print("Need to set environment variable AGORA_APP_ID and AGORA_APP_CERTIFICATE")
        return

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, Role_Publisher, privilegeExpiredTs)
    print("Token with int uid: {}".format(token))

    token = RtcTokenBuilder.buildTokenWithAccount(appId, appCertificate, channelName,
                                                  userAccount, Role_Publisher, privilegeExpiredTs)
    print("Token with user account: {}".format(token))


if __name__ == "__main__":
    main()
