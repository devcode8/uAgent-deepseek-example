# Running Deepseek r-1 locally using ollama (Langchain + uAgents)

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from uagents import Agent, Model, Context
from uagents.setup import fund_agent_if_low
import re

class DeepSeekRequest(Model):
    context:str

class DeepSeekResponse(Model):
    response:str
    
DeepseekAgent = Agent(
    name="deepseek Agent",
    seed="This is a deepseek r-1 Agent",
    mailbox=True,
    readme_path="readme.md",
    publish_agent_details=True
)

fund_agent_if_low(DeepseekAgent.wallet.address())

prompt = ChatPromptTemplate.from_messages([
    ("user", "{context}")
    ])

llm = Ollama(model="deepseek-r1:8b")

@DeepseekAgent.on_message(model=DeepSeekRequest)
async def reply(ctx:Context, sender: str, msg:DeepSeekRequest):
    context = msg.context
    ctx.logger.info(f"{context}")
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({'context':context})
    cleaned_response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
    ctx.logger.info(cleaned_response)
    await ctx.send(sender,DeepSeekResponse(response=cleaned_response))

if __name__ == "__main__":
    DeepseekAgent.run()


