# (C) Copyright 2018 Hewlett Packard Enterprise Development LP.

# run.py

import json

import ncsmodule.ncsmodule3 as ncsm

def run():

    #ncs = ncsm.NCSClient('https://tme-beta-p1.stackbeta.hpe.com', 'peng.liu@hpe.com', 'Passw0rd!')
    ncs = ncsm.NCSClient('https://onespheretme1.stackbeta.hpe.com', 'peng.liu@hpe.com', 'Passw0rd!')

    print("--- GetStatus: " + json.dumps(ncs.GetStatus()))
    print("--- GetConnectApp: " + json.dumps(ncs.GetConnectApp("windows")))
    print("--- GetSession: " + json.dumps(ncs.GetSession()))
    print("--- GetSessionIdp: " + json.dumps(ncs.GetSessionIdp("peng")))
    print("--- GetAccount: " + json.dumps(ncs.GetAccount()))
    print("--- GetProviderTypes: " + json.dumps(ncs.GetProviderTypes()))
    print("--- GetZoneTypes: " + json.dumps(ncs.GetZoneTypes()))
    print("--- GetServiceTypes: " + json.dumps(ncs.GetServiceTypes()))
    print("--- GetRoles: " + json.dumps(ncs.GetRoles()))
    print("--- GetUsers: " + json.dumps(ncs.GetUsers()))
    print("--- GetTagKeys: " + json.dumps(ncs.GetTagKeys()))
    print("--- GetTags: " + json.dumps(ncs.GetTags()))

    del ncs


if __name__ == '__main__':
    run()

