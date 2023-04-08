# kubectl_tool.py
# A langchain tool that use kubectl
#
from langchain.agents import Tool
from langchain.utilities import BashProcess
import json


def kubectl_tool(command) -> str:
    bash = BashProcess()
    result = bash.run(command)
    data = {
        'result': result.split()
    }
    response_as_json = json.dumps(data)
    return response_as_json


name = "kubectl_tool"
description = "This is kubectl CLI. The input is the kubectl command, e.g. kubectl get pod --output=jsonpath={{.items..metadata.name}}. The output will be a JSON data structure, in the format: '{{\"result\":\"<result>\"}}'"

# create an instance of the custom langchain tool
Kubectl = Tool(
    name=name,
    func=kubectl_tool,
    description=description,
    return_direct=False
)


if __name__ == '__main__':
    print(kubectl_tool("kubectl get pod"))
