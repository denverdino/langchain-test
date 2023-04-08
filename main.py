from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.tools import BaseTool
from langchain.llms import OpenAI
from langchain import LLMMathChain
from datetime_tool import Datetime
from aliyun_tool import AliyunCli
from kubectl_tool import Kubectl



llm = OpenAI(temperature=0.5)
llm_math_chain = LLMMathChain(llm=llm, verbose=True)
tools = [
    Datetime,
    AliyunCli,
    Kubectl
]

# Construct the react agent type.
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

#agent.run("What is tomorrow's date?")
#agent.run("What will be time one day after?")
#agent.run("What date will be coming Friday?")
#agent.run("Do I have some ECS instances in cn-hongkong region of Alibaba Cloud?")
#agent.run("Return ip address in hongkong region of Alibaba Cloud if there is any ECS instance")
#agent.run("如果阿里云香港地域有ECS返回其IP地址")
#agent.run("List all pods in the default namespace from kubernetes cluster")
agent.run("返回kubernetes cluster集群中kube-system命名空间下的所有Service")
