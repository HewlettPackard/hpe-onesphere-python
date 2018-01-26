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

# sample.py

import json

# for Python 2 (2.7.x and above), import the onesphere.osbinding2
# for Python 3 (3.5.2 and above), import the onesphere.osbinding3
import onesphere.osbinding3 as osb

def run():

    osinst = osb.OSClient('https://onesphere-host-url', 'username', 'password')

    print("GetStatus: " + json.dumps(osinst.GetStatus()))
    print("GetConnectApp: " + json.dumps(osinst.GetConnectApp("windows")))
    print("GetSession: " + json.dumps(osinst.GetSession()))
    print("GetAccount: " + json.dumps(osinst.GetAccount()))
    print("GetProviderTypes: " + json.dumps(osinst.GetProviderTypes()))
    print("GetZoneTypes: " + json.dumps(osinst.GetZoneTypes()))
    print("GetServiceTypes: " + json.dumps(osinst.GetServiceTypes()))
    print("GetRoles: " + json.dumps(osinst.GetRoles()))
    print("GetUsers: " + json.dumps(osinst.GetUsers()))
    print("GetTagKeys: " + json.dumps(osinst.GetTagKeys()))
    print("GetTags: " + json.dumps(osinst.GetTags()))

    del osinst


if __name__ == '__main__':
    run()

