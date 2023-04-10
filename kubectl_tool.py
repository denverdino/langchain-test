# kubectl_tool.py
# A langchain tool that use kubectl
#
from langchain.agents import Tool
from langchain.utilities import BashProcess
import json


def kubectl_tool(command) -> str:
    bash = BashProcess()
    result = bash.run(command)
    return result


name = "kubectl_tool"
description = "This is a tool for kubernetes cluster. The input is the kubectl command with jsonpath-as-json format, e.g. kubectl get pod --output=jsonpath-as-json={{.items..metadata.name}}  The output will be a JSON data structure."

# create an instance of the custom langchain tool
Kubectl = Tool(
    name=name,
    func=kubectl_tool,
    description=description,
    return_direct=False
)


if __name__ == '__main__':
    print(kubectl_tool("kubectl get pod"))
