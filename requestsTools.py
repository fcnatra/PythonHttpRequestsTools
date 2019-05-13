import requests, json
import urllib3

#pip install requests  --trusted-host pypi.org --trusted-host files.pythonhosted.org

accessToken = ''

def setupAuthentication():
    disableWarningForInsecureHttpRequests()

def disableWarningForInsecureHttpRequests():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getResponseFromUrl(url):
    parameterConcatenator = '&' if ('?' in url) else '?'    
    return requests.get(url + parameterConcatenator + accessToken, verify=False)

def getContentFromUrl(url):
    response = getResponseFromUrl(url)
    return response.content

def getJsonFromUrl(url):
    content = getContentFromUrl(url)
    return json.loads(content)

def getNodesFromJson(jsonContent, nodeNamesCsv):
    values = []
    for mainNode in jsonContent:
        if (type(mainNode) is not str):
            nodes = []
            for childNode in nodeNamesCsv.split(','):
                if (mainNode.__contains__(childNode)):
                    nodes.append(mainNode[childNode])
            values.append(nodes)

    return values