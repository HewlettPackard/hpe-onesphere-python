# (C) Copyright 2018 Hewlett Packard Enterprise Development LP.

# sample.py

import json

# for Python 2.7.x, import the ncsmodule.ncsmodule2
import ncsmodule.ncsmodule3 as ncsm

def run():

    ncs = ncsm.NCSClient('https://ncs-host-url', 'username', 'password')

    print("GetStatus: " + json.dumps(ncs.GetStatus()))
    print("GetConnectApp: " + json.dumps(ncs.GetConnectApp("windows")))
    print("GetSession: " + json.dumps(ncs.GetSession()))
    print("GetSessionIdp: " + json.dumps(ncs.GetSessionIdp("username")))
    print("GetAccount: " + json.dumps(ncs.GetAccount()))
    print("GetProviderTypes: " + json.dumps(ncs.GetProviderTypes()))
    print("GetZoneTypes: " + json.dumps(ncs.GetZoneTypes()))
    print("GetServiceTypes: " + json.dumps(ncs.GetServiceTypes()))
    print("GetRoles: " + json.dumps(ncs.GetRoles()))
    print("GetUsers: " + json.dumps(ncs.GetUsers()))
    print("GetTagKeys: " + json.dumps(ncs.GetTagKeys()))
    print("GetTags: " + json.dumps(ncs.GetTags()))

    del ncs


if __name__ == '__main__':
    run()

