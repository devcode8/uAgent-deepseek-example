### deepseek-r1 Agent
---

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

This agent is a simple wrapper around `deepseek-r1` Large Language Model.

### Example input
---

```
DeepSeekRequest(
    context="What is API?",
)
```

### Example output
---

```
Response(
    response="An API (Application Programming Interface) is a set of rules, protocols, and tools that enables different software applications to communicate with each other. It defines how software components should interact, allowing developers to access specific features or data from a service, library, or operating system without needing to understand its internal workings."
)
```

### Usage Example
---

Copy and paste the following code into a new Blank agent for an example of how to interact with this agent.

```
from uagents import Agent, Context, Model

class DeepSeekRequest(Model):
    context:str

class DeepSeekResponse(Model):
    response:str

agent = Agent()

AI_AGENT_ADDRESS = "<deployed_agent_address>"


prompt = DeepSeekRequest(
    context="What is API?"
)

@agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(AI_AGENT_ADDRESS, prompt)

@agent.on_message(DeepSeekResponse)
async def handle_response(ctx: Context, sender: str, msg: DeepSeekResponse):
    ctx.logger.info(f"Received response from {sender}: {msg.response}")

if __name__ == "__main__":
agent.run()
```

### Local Agent
---


1. Install the necessary packages:

```
pip install requests uagents
```

2. To interact with this agent from a local agent instead, replace `agent = Agent()` in the above with:

```
agent = Agent(
name="user",
endpoint="http://localhost:8000/submit",
)
```

3. Run the agent:

```
python agent.py
```

### Usage Allowance
---

Each agent is allowed to make up to 6 requests per hour from this agent.
