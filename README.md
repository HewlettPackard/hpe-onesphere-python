# Python Language Binding for HPE OneSphere APIs

The Python language binding package for Python developers to call HPE OneSphere APIs

## Prerequisites

Python 3.5.2 and above, or Python 2.7.x. 
You can install the latest version from:

```
https://www.python.org/downloads/
```

Install the Requests package

```
http://docs.python-requests.org/en/master/user/install/
```
or
```
sudo pip install requests
```

## Usage

Copy the onesphere into your Python project folder.

Example:

```
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
```

## APIs

All the APIs return data in JSON format the same as those returned from HPE OneSphere composable APIs.

### Not Implemented Yet

Some APIs are not yet implemented. The following message will be returned in this case.

Example:

```
GetSessionIdp is not implemented yet.
```
