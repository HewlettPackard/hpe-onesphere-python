# (C) Copyright 2018 Hewlett Packard Enterprise Development LP.

# ncsmodule/ncsmodule.py

import requests
import json


# Module level decorators

def notimplementedyet(func):
    def new_func(*args):
        msg = func.__name__ + " is not implemented yet."
        print(msg)
        return msg
    return new_func

def stringnotempty(arguments):
    def check_wrapper(func):
        def check_args(*args, **kwargs):
            code = func.__code__
            names = list(code.co_varnames[:code.co_argcount])
            print(names)
            print(args)
            for argument in arguments:
                num = names.index(argument)
                value = args[num]
                #if isinstance(value, str) and value.strip(): # not change user's input
                if isinstance(value, str) and value:
                    return func(*args, **kwargs)
                else:
                    raise Exception(argument + " should be a non-empty string.")
        return check_args
    return check_wrapper


# Class NCSClient

class NCSClient:

    URI_SESSION                     = "/session"
    URI_SESSION_IDP                 = "/session/idp"
    URI_STATUS                      = "/status"
    URI_CONNECT_APP                 = "/connect-app"
    URI_ACCOUNT                     = "/account"
    URI_PROVIDER_TYPES              = "/provider-types"
    URI_PROVIDERS                   = "/providers"
    URI_REGIONS                     = "/regions"
    URI_ZONE_TYPES                  = "/zone-types"
    URI_ZONES                       = "/zones"
    URI_CATALOGS                    = "/catalogs"
    URI_SERVICE_TYPES               = "/service-types"
    URI_SERVICES                    = "/services"
    URI_VIRTUAL_MACHINE_PROFILES    = "/virtual-machine-profiles"
    URI_NETWORKS                    = "/networks"
    URI_WORKSPACES                  = "/workspaces"
    URI_DEPLOYMENTS                 = "/deployments"
    URI_MEMBERSHIPS                 = "/memberships"
    URI_ROLES                       = "/roles"
    URI_USERS                       = "/users"
    URI_METRICS                     = "/metrics"
    URI_EVENTS                      = "/events"
    URI_VOLUMES                     = "/volumes"
    URI_TAG_KEYS                    = "/tag-keys"
    URI_TAGS                        = "/tags"
    URI_KEYPAIRS                    = "/keypairs"

    HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, host_url, username, password):
        self.host_url = host_url
        self.rest_prefix = host_url + "/rest"
        self.username = username
        self.password = password
        self.Connect()

    def __del__(self):
        # raising exception in the destructor will be ignored
        # raise Exception("raising exception in NCSClient destructor")
        pass

    def Connect(self):
        full_url = self.rest_prefix + NCSClient.URI_SESSION
        data = {'userName': self.username, 'password': self.password}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        r_json = r.json()
        if r.status_code != 200:
            raise Exception(r_json["message"])
        else:
            self.token = r_json["token"]
            self.user_uri = r_json["userUri"]
            NCSClient.HEADERS["Authorization"] = r_json["token"]

    def GetStatus(self):
        full_url = self.rest_prefix + NCSClient.URI_STATUS
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # os: windows or mac
    @stringnotempty(['os'])
    def GetConnectApp(self, os="windows"):
        full_url = self.rest_prefix + NCSClient.URI_CONNECT_APP
        params = {"os": os}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Session APIs

    def GetSession(self, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_SESSION
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @notimplementedyet
    @stringnotempty(['user_name'])
    def GetSessionIdp(self, user_name):
        full_url = self.rest_prefix + NCSClient.URI_SESSION_IDP
        params = {"userName": user_name}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Account APIs

    @notimplementedyet
    def GetAccount(self, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_ACCOUNT
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Providers APIs

    def GetProviderTypes(self):
        full_url = self.rest_prefix + NCSClient.URI_PROVIDER_TYPES
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    def GetProviders(self, parent_uri, provider_type_uri):
        full_url = self.rest_prefix + NCSClient.URI_PROVIDER_TYPES
        params = {"parentUri": parent_uri, "providerTypeUri": provider_type_uri}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['provider_id'])
    def CreateProvider(self, provider_id, provider_type_uri, access_key, 
                       secret_key, s3_cost_bucket, parent_uri, 
                       payment_provider=True, state="Enabled"):
        full_url = self.rest_prefix + NCSClient.URI_PROVIDERS
        data={"id": provider_id, 
              "providerTypeUri": provider_type_uri, 
              "accessKey": access_key, 
              "secretKey": secret_key, 
              "paymentProvider": payment_provider, 
              "s3CostBucket": s3_cost_bucket, 
              "parentUri": parent_uri, 
              "state": state}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['provider_id'])
    def GetProvider(self, provider_id, view="full", discover=False):
        full_url = self.rest_prefix + NCSClient.URI_PROVIDERS + "/" + provider_id
        params={"view": view, "discover": discover}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['provider_id'])
    def DeleteProvider(self, provider_id):
        full_url = self.rest_prefix + NCSClient.URI_PROVIDERS + "/" + provider_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # info_array: [{os, path, value}]
    @stringnotempty(['provider_id'])
    def UpdateProvider(self, provider_id, info_array):
        if (len(info_array) == 0):
            raise Exception("info_array should be a non-empty array.")
        try:
            json.loads(info_array)
        except ValueError:
            raise Exception("info_array should be in JSON format.")
        full_url = self.rest_prefix + NCSClient.URI_PROVIDERS + "/" + provider_id
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=info_array)
        return r.json()

    # Regions APIs

    def GetRegions(self, provider_uri, view):
        full_url = self.rest_prefix + NCSClient.URI_REGIONS
        params={"providerUri": provider_uri, "view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name'])
    def CreateRegion(self, name, provider_uri, loc_latitude, loc_longitude):
        full_url = self.rest_prefix + NCSClient.URI_REGIONS
        data = {"name": name, 
                "providerUri": provider_uri, 
                "location": {
                    "latitude": loc_latitude, 
                    "longitude": loc_longitude}}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['region_id'])
    def GetRegion(self, region_id, view, discover=True):
        full_url = self.rest_prefix + NCSClient.URI_REGIONS + "/" + region_id
        params = {"view": view, "discover": discover}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # info is in json format
    @notimplementedyet
    @stringnotempty(['region_id'])
    def UpdateRegion(self, region_id, info):
        try:
            json.loads(info)
        except ValueError:
            raise Exception("info should be in JSON format.")
        full_url = self.rest_prefix + NCSClient.URI_REGIONS + "/" + region_id
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=info)
        return r.json()

    # Zone Types APIs

    def GetZoneTypes(self):
        full_url = self.rest_prefix + NCSClient.URI_ZONE_TYPES
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Zones APIs

    def GetZones(self, region_uri, query):
        full_url = self.rest_prefix + NCSClient.URI_ZONES
        params = {"regionUri": region_uri, "q": query}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name'])
    def CreateZone(self, name, provider_uri, region_uri, zone_type_uri):
        full_url = self.rest_prefix + NCSClient.URI_ZONES
        data = {"name": name, 
                "providerUri": provider_uri, 
                "regionUri": provider_uri, 
                "zoneTypeUri": zone_type_uri}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['zone_id'])
    def GetZone(self, zone_id, view):
        full_url = self.rest_prefix + NCSClient.URI_ZONES + "/" + zone_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['zone_id'])
    def UpdateZone(self, zone_id, info_array):
        if (len(info_array) == 0):
            raise Exception("info_array should be a non-empty array.")
        try:
            json.loads(info_array)
        except ValueError:
            raise Exception("info_array should be in JSON format.")
        full_url = self.rest_prefix + NCSClient.URI_ZONES + "/" + zone_id
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=info_array)
        return r.json()

    @stringnotempty(['zone_id'])
    def DeleteZone(self, zone_id, force=True):
        full_url = self.rest_prefix + NCSClient.URI_ZONES + "/" + zone_id
        params = {"force": force}
        r = requests.delete(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # action: e.g. "reset"
    @stringnotempty(['zone_id', 'action'])
    def ActionOnZone(self, zone_id, action):
        full_url = self.rest_prefix + NCSClient.URI_ZONES + "/" + zone_id + "/actions"
        data = {"type": action}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['zone_id'])
    def GetZoneApplianceImage(self, zone_id):
        full_url = self.rest_prefix + NCSClient.URI_ZONES + "/" + zone_id + "/appliance-image"
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Catalogs APIs

    def GetCatalogs(self, query):
        full_url = self.rest_prefix + NCSClient.URI_CATALOGS
        params = {"q": query}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name', 'url'])
    def CreateCatalog(self, name, url):
        full_url = self.rest_prefix + NCSClient.URI_CATALOGS
        data = {"name": name, "url": url}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['catalog_id'])
    def GetCatalog(self, catalog_id):
        full_url = self.rest_prefix + NCSClient.URI_CATALOGS + "/" + catalog_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    @notimplementedyet
    @stringnotempty(['catalog_id'])
    def UpdateCatalog(self, catalog_id, name, status, 
                      uri, url, service_type_uri, 
                      time_created, time_modified):
        full_url = self.rest_prefix + NCSClient.URI_CATALOGS + "/" + catalog_id
        data = {"created": time_created,
                "id": catalog_id, 
                "modified": time_modified,
                "name": name,
                "status": status,
                "uri": uri,
                "url": url,
                "serviceTypeUri": service_type_uri}
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    # Service Types APIs

    def GetServiceTypes(self):
        full_url = self.rest_prefix + NCSClient.URI_SERVICE_TYPES
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    @stringnotempty(['service_type_id'])
    def GetServiceType(self, service_type_id):
        full_url = self.rest_prefix + NCSClient.URI_SERVICE_TYPES + "/" + service_type_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Services APIs

    def GetServices(self, query, user_query, 
                    service_type_uri, zone_uri, workspace_uri, catalog_uri, 
                    view="full"):
        full_url = self.rest_prefix + NCSClient.URI_SERVICES
        params = {"query": query,
                  "userQuery": user_query,
                  "serviceTypeUri": service_type_uri,
                  "zoneUri": zone_uri,
                  "workspaceUri": workspace_uri,
                  "catalogUri": catalog_uri,
                  "view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # view: "full", "deployment"
    @stringnotempty(['service_id'])
    def GetService(self, service_id, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_SERVICES + "/" + service_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Virtual Machine Profiles APIs

    def GetVirtualMachineProfiles(self, query, zone_uri, service_uri):
        full_url = self.rest_prefix + NCSClient.URI_VIRTUAL_MACHINE_PROFILES
        params = {"q": query, 
                  "zoneUri": zone_uri,
                  "serviceUri": service_uri}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['vm_profile_id'])
    def GetVirtualMachineProfile(self, vm_profile_id):
        full_url = self.rest_prefix + NCSClient.URI_VIRTUAL_MACHINE_PROFILES + "/" + vm_profile_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Networks APIs

    def GetNetworks(self, query, zone_uri):
        full_url = self.rest_prefix + NCSClient.URI_NETWORKS
        params = {"q": query, "zoneUri": zone_uri}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['network_id'])
    def GetNetwork(self, network_id):
        full_url = self.rest_prefix + NCSClient.URI_NETWORKS + "/" + network_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Worksapces APIs

    @stringnotempty(['query'])
    def GetWorkspaces(self, query, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_WORKSPACES
        params = {"q": query, "view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name'])
    def CreateWorkspace(self, name, description, tag_uris_array):
        full_url = self.rest_prefix + NCSClient.URI_WORKSPACES
        data = {"name": name, "description": description, "tagUris": tag_uris_array}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['workspace_id'])
    def GetWorkspace(self, workspace_id, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_WORKSPACES + "/" + workspace_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['workspace_id'])
    def UpdateWorkspace(self, workspace_id, name, description, tag_uris_array):
        full_url = self.rest_prefix + NCSClient.URI_WORKSPACES + "/" + workspace_id
        data = {"name": name, "description": description, "tagUris": tag_uris_array}
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['workspace_id'])
    def DeleteWorkspace(self, workspace_id):
        full_url = self.rest_prefix + NCSClient.URI_WORKSPACES + "/" + workspace_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Deployments APIs

    @stringnotempty(['query'])
    def GetDeployments(self, query, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS
        params = {"query": query, "view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    def CreateDeployment(self, info):
        try:
            json.loads(info)
        except ValueError:
            raise Exception("info should be in JSON format.")
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=info)
        return r.json()

    @stringnotempty(['deployment_id'])
    def GetDeployment(self, deployment_id, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS + "/" + deployment_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['deployment_id'])
    def UpdateDeployment(self, deployment_id, info):
        try:
            json.loads(info)
        except ValueError:
            raise Exception("info should be in JSON format.")
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS + "/" + deployment_id
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=info)
        return r.json()

    @stringnotempty(['deployment_id'])
    def DeleteDeployment(self, deployment_id):
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS + "/" + deployment_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # action_type: e.g. "restart"
    @stringnotempty(['deployment_id', 'action_type'])
    def ActionOnDeployment(self, deployment_id, action_type, force=True):
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS + "/" + deployment_id + "/actions"
        data = {"force": force, "type": action_type}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['deployment_id'])
    def GetDeploymentConsole(self, deployment_id):
        full_url = self.rest_prefix + NCSClient.URI_DEPLOYMENTS + "/" + deployment_id + "/console"
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Memberships APIs

    @stringnotempty(['query'])
    def GetMemberships(self, query):
        full_url = self.rest_prefix + NCSClient.URI_MEMBERSHIPS
        params = {"query": query}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    def CreateMembership(self, user_uri, role_uri, workspace_uri):
        full_url = self.rest_prefix + NCSClient.URI_MEMBERSHIPS
        data = {"userUri": user_uri, "roleUri": role_uri, "workspaceUri": workspace_uri}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    def DeleteMembership(self, user_uri, role_uri, workspace_uri):
        full_url = self.rest_prefix + NCSClient.URI_MEMBERSHIPS
        data = {"userUri": user_uri, "roleUri": role_uri, "workspaceUri": workspace_uri}
        r = requests.delete(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    # Roles APIs

    def GetRoles(self):
        full_url = self.rest_prefix + NCSClient.URI_ROLES
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Users APIs

    def GetUsers(self):
        full_url = self.rest_prefix + NCSClient.URI_USERS
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    def CreateUser(self, name, password, email, role):
        full_url = self.rest_prefix + NCSClient.URI_USERS
        data = {"name": name, "email": email, "password": password, "role": role}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['user_id'])
    def GetUser(self, user_id):
        full_url = self.rest_prefix + NCSClient.URI_USERS + "/" + user_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    @stringnotempty(['user_id'])
    def UpdateUser(self, user_id, name, password, email, role):
        full_url = self.rest_prefix + NCSClient.URI_USERS + "/" + user_id
        data = {"name": name, "email": email, "password": password, "role": role}
        r = requests.put(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['user_id'])
    def DeleteUser(self, user_id):
        full_url = self.rest_prefix + NCSClient.URI_USERS + "/" + user_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Metrics APIs

    def GetMetrics(self, resource_uri_array, category_array, query_array, name_array, 
                   period_start, period, period_count, view, start, count):
        full_url = self.rest_prefix + NCSClient.URI_METRICS
        params = {"resourceUri": resource_uri_array, 
                "category": category_array,
                "query": query_array,
                "name": name_array,
                "periodStart": period_start,
                "period": period,
                "periodCount": period_count,
                "view": view,
                "start": start,
                "count": count}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Events APIs

    @notimplementedyet
    def GetEvents(self, resource_uri):
        full_url = self.rest_prefix + NCSClient.URI_EVENTS
        params = {"resourceUri": resource_uri}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    # Volumes APIs

    def GetVolumes(self, query):
        full_url = self.rest_prefix + NCSClient.URI_VOLUMES
        params = {"query": query}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['volume_id'])
    def GetVolume(self, volume_id):
        full_url = self.rest_prefix + NCSClient.URI_VOLUMES + "/" + volume_id
        r = requests.get(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Tag Keys APIs

    def GetTagKeys(self, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_TAG_KEYS
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name'])
    def CreateTagKey(self, name):
        full_url = self.rest_prefix + NCSClient.URI_TAG_KEYS
        data = {"name": name}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['tag_key_id'])
    def GetTagKey(self, tag_key_id, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_TAG_KEYS + "/" + tag_key_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['tag_key_id'])
    def DeleteTagKey(self, tag_key_id):
        full_url = self.rest_prefix + NCSClient.URI_TAG_KEYS + "/" + tag_key_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Tags APIs

    def GetTags(self, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_TAGS
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['name', 'tag_key_uri'])
    def CreateTag(self, name, tag_key_uri):
        full_url = self.rest_prefix + NCSClient.URI_TAGS
        data = {"name": name, "tagKeyUri": tag_key_uri}
        r = requests.post(full_url, headers=NCSClient.HEADERS, json=data)
        return r.json()

    @stringnotempty(['tag_id'])
    def GetTag(self, tag_id, view="full"):
        full_url = self.rest_prefix + NCSClient.URI_TAGS + "/" + tag_id
        params = {"view": view}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

    @stringnotempty(['tag_id'])
    def DeleteTag(self, tag_id):
        full_url = self.rest_prefix + NCSClient.URI_TAGS + "/" + tag_id
        r = requests.delete(full_url, headers=NCSClient.HEADERS)
        return r.json()

    # Keypairs APIs

    @stringnotempty(['region_uri', 'workspace_uri'])
    def GetKeyPair(self, region_uri, workspace_uri):
        full_url = self.rest_prefix + NCSClient.URI_KEYPAIRS
        params = {"regionUri": region_uri, "workspaceUri": workspace_uri}
        r = requests.get(full_url, headers=NCSClient.HEADERS, params=params)
        return r.json()

