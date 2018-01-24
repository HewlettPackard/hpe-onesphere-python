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

Copy the ncsmodule into your Python project folder.

Example:

```
import json

# for Python 2.7.x, import the ncsmodule.ncsmodule2
import ncsmodule.ncsmodule3 as ncsm

def run():

    ncs = ncsm.NCSClient('https://ncs-host-url', 'username', 'password')

    print("GetStatus: " + json.dumps(ncs.GetStatus()))
    print("GetConnectApp: " + json.dumps(ncs.GetConnectApp()))
    print("GetSession: " + json.dumps(ncs.GetSession()))
    print("GetSessionIdp: " + json.dumps(ncs.GetSessionIdp("peng")))
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

```

## APIs

All the APIs return data in JSON format the same as those returned from HPE OneSphere composable APIs.

### Not Implemented Yet

Some APIs are not yet implemented. The following message will be returned in this case.

Example:

```
GetSessionIdp is not implemented yet.
```
