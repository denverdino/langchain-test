# aliyun_tool.py
# A langchain tool that use aliyun-cli
#
from langchain.agents import Tool
from langchain.utilities import BashProcess


def aliyun_cli_tool(command) -> str:
    bash = BashProcess()
    return bash.run(command)


name = "aliyun_cli_tool"
description = "This is an Alibaba Cloud CLI tool. You can use it like, aliyun ecs DescribeInstances --region cn-hangzhou , or you can use it with jq filter, e.g. aliyun ecs DescribeInstances --region cn-hongkong | jq '.Instances.Instance[].InstanceName'"

# create an instance of the custom langchain tool
AliyunCli = Tool(
    name=name,
    func=aliyun_cli_tool,
    description=description,
    return_direct=False
)


if __name__ == '__main__':
    print(aliyun_cli_tool("aliyun ecs DescribeInstances"))
