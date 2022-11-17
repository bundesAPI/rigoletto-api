# rigoletto.DefaultApi

All URIs are relative to *https://rigoletto.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_tabelle_export_tabelle_get**](DefaultApi.md#export_tabelle_export_tabelle_get) | **GET** /Export_Tabelle | Export Tabelle


# **export_tabelle_export_tabelle_get**
> bool, date, datetime, dict, float, int, list, str, none_type export_tabelle_export_tabelle_get()

Export Tabelle

### Example


```python
import time
from deutschland import rigoletto
from deutschland.rigoletto.api import default_api
from deutschland.rigoletto.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://rigoletto.herokuapp.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rigoletto.Configuration(
    host = "https://rigoletto.herokuapp.com"
)


# Enter a context with an instance of the API client
with rigoletto.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    kennnummer = 1 # int |  (optional)
    kennnummer_greater_than = 1 # int |  (optional)
    kennnummer_greater_than_equal = 1 # int |  (optional)
    kennnummer_less_than = 1 # int |  (optional)
    kennnummer_less_than_equal = 1 # int |  (optional)
    einstufungsbezeichnung = "Einstufungsbezeichnung_example" # str |  (optional)
    einstufungsbezeichnung_contains = "Einstufungsbezeichnung_contains_example" # str |  (optional)
    einstufungsbezeichnung_englisch = "EinstufungsbezeichnungEnglisch_example" # str |  (optional)
    einstufungsbezeichnung_englisch_contains = "EinstufungsbezeichnungEnglisch_contains_example" # str |  (optional)
    stoffname = "Stoffname_example" # str |  (optional)
    stoffname_contains = "Stoffname_contains_example" # str |  (optional)
    gruppenname = "Gruppenname_example" # str |  (optional)
    gruppenname_contains = "Gruppenname_contains_example" # str |  (optional)
    cas_nr = "CAS_Nr_example" # str |  (optional)
    cas_nr_contains = "CAS_Nr_contains_example" # str |  (optional)
    eg_nr = "EG_Nr_example" # str |  (optional)
    eg_nr_contains = "EG_Nr_contains_example" # str |  (optional)
    m_faktor = "MFaktor_example" # str |  (optional)
    m_faktor_contains = "MFaktor_contains_example" # str |  (optional)
    synonym = "Synonym_example" # str |  (optional)
    synonym_contains = "Synonym_contains_example" # str |  (optional)
    verffentlichungsdatum = "Veröffentlichungsdatum_example" # str |  (optional)
    verffentlichungsdatum_contains = "Veröffentlichungsdatum_contains_example" # str |  (optional)
    wgk = "WGK_example" # str |  (optional)
    wgk_contains = "WGK_contains_example" # str |  (optional)
    fussnoten = 3.14 # float |  (optional)
    fussnoten_greater_than = 3.14 # float |  (optional)
    fussnoten_greater_than_equal = 3.14 # float |  (optional)
    fussnoten_less_than = 3.14 # float |  (optional)
    fussnoten_less_than_equal = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Tabelle
        api_response = api_instance.export_tabelle_export_tabelle_get(kennnummer=kennnummer, kennnummer_greater_than=kennnummer_greater_than, kennnummer_greater_than_equal=kennnummer_greater_than_equal, kennnummer_less_than=kennnummer_less_than, kennnummer_less_than_equal=kennnummer_less_than_equal, einstufungsbezeichnung=einstufungsbezeichnung, einstufungsbezeichnung_contains=einstufungsbezeichnung_contains, einstufungsbezeichnung_englisch=einstufungsbezeichnung_englisch, einstufungsbezeichnung_englisch_contains=einstufungsbezeichnung_englisch_contains, stoffname=stoffname, stoffname_contains=stoffname_contains, gruppenname=gruppenname, gruppenname_contains=gruppenname_contains, cas_nr=cas_nr, cas_nr_contains=cas_nr_contains, eg_nr=eg_nr, eg_nr_contains=eg_nr_contains, m_faktor=m_faktor, m_faktor_contains=m_faktor_contains, synonym=synonym, synonym_contains=synonym_contains, verffentlichungsdatum=verffentlichungsdatum, verffentlichungsdatum_contains=verffentlichungsdatum_contains, wgk=wgk, wgk_contains=wgk_contains, fussnoten=fussnoten, fussnoten_greater_than=fussnoten_greater_than, fussnoten_greater_than_equal=fussnoten_greater_than_equal, fussnoten_less_than=fussnoten_less_than, fussnoten_less_than_equal=fussnoten_less_than_equal)
        pprint(api_response)
    except rigoletto.ApiException as e:
        print("Exception when calling DefaultApi->export_tabelle_export_tabelle_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kennnummer** | **int**|  | [optional]
 **kennnummer_greater_than** | **int**|  | [optional]
 **kennnummer_greater_than_equal** | **int**|  | [optional]
 **kennnummer_less_than** | **int**|  | [optional]
 **kennnummer_less_than_equal** | **int**|  | [optional]
 **einstufungsbezeichnung** | **str**|  | [optional]
 **einstufungsbezeichnung_contains** | **str**|  | [optional]
 **einstufungsbezeichnung_englisch** | **str**|  | [optional]
 **einstufungsbezeichnung_englisch_contains** | **str**|  | [optional]
 **stoffname** | **str**|  | [optional]
 **stoffname_contains** | **str**|  | [optional]
 **gruppenname** | **str**|  | [optional]
 **gruppenname_contains** | **str**|  | [optional]
 **cas_nr** | **str**|  | [optional]
 **cas_nr_contains** | **str**|  | [optional]
 **eg_nr** | **str**|  | [optional]
 **eg_nr_contains** | **str**|  | [optional]
 **m_faktor** | **str**|  | [optional]
 **m_faktor_contains** | **str**|  | [optional]
 **synonym** | **str**|  | [optional]
 **synonym_contains** | **str**|  | [optional]
 **verffentlichungsdatum** | **str**|  | [optional]
 **verffentlichungsdatum_contains** | **str**|  | [optional]
 **wgk** | **str**|  | [optional]
 **wgk_contains** | **str**|  | [optional]
 **fussnoten** | **float**|  | [optional]
 **fussnoten_greater_than** | **float**|  | [optional]
 **fussnoten_greater_than_equal** | **float**|  | [optional]
 **fussnoten_less_than** | **float**|  | [optional]
 **fussnoten_less_than_equal** | **float**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

