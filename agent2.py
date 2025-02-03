# uAgents + Together ai ( on together ai deepseek r-1 running on cloud)
from uagents import Agent, Model, Context
from uagents.setup import fund_agent_if_low
import re,os
from together import Together

from dotenv import load_dotenv

load_dotenv()

os.environ["TOGETHER_API_KEY"]=os.getenv("TOGETHER_API_KEY")

client = Together()

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

@DeepseekAgent.on_message(model=DeepSeekRequest)
async def reply(ctx:Context, sender: str, msg:DeepSeekRequest):
    context = msg.context
    ctx.logger.info(f"{context}\n")
    response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[{"role": "user", "content": context}],
    )
    output = response.choices[0].message.content
    cleaned_response = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL)

    ctx.logger.info(cleaned_response)
    await ctx.send(sender,DeepSeekResponse(response=cleaned_response))

if __name__ == "__main__":
    DeepseekAgent.run()