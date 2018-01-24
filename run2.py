# (C) Copyright 2018 Hewlett Packard Enterprise Development LP.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# run2.py

import json

import ncsmodule.ncsmodule2 as ncsm

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

