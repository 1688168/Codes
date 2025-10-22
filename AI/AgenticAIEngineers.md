# <center><b><span style="color:orange">Agentic AI Engineer</span></b></center>
> # <b><span style="color:purple">Lab1</span></b>
> ### <b><span style="color:green">Env Keys</span></b>

```
.env file

* setup OPENAI_API_KEY
```

```python
# The imports

from dotenv import load_dotenv
from agents import Agent, Runner, trace
# The usual starting point

load_dotenv(override=True) #set override as True
```

> ### <b><span style="color:green">Communicating with LLM</span></b>
* system prompt
* user prompt

> ### <b><span style="color:green">construct the msg and get response</span></b>

```python
messages = [{"role": "user", "content": "What is 2+2?"}]

response = openai.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

print(response.choices[0].message.content)

```
> another example to raise a question to LLM
```python
openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
)
question = response.choices[0].message.content
print(question)
```


```python
# Make an agent with name, instructions, model

agent = Agent(name="Jokester", instructions="You are a joke teller", model="gpt-4o-mini")

# Run the joke with Runner.run(agent, prompt) then print final_output

# start a conversation with trace with LLM
with trace("Telling a joke"):
    result = await Runner.run(agent, "Tell a joke about Autonomous AI Agents")
    print(result.final_output)
```
* in lab1, we only ask and does not processing the response
* where to check the trace: https://platform.openai.com/traces

> # <b><span style="color:purple">Lab 2</span></b>
> ### <b><span style="color:green">use openAI interface to call with different LLM model</span></b>

```python
model_name = "gpt-4o-mini"

response = openai.chat.completions.create(model=model_name, messages=messages) # call with different model

answer = response.choices[0].message.content

display(Markdown(answer)) #how to print markdown
competitors.append(model_name)
answers.append(answer)
```
> # <b><span style="color:purple">role content</span></b>

  
```python
# Judgement time!
judge_messages = [{"role": "user", "content": judge}]
openai = OpenAI()
response = openai.chat.completions.create(
    model="o3-mini",
    messages=judge_messages,
)
results = response.choices[0].message.content
print(results)
```

> # <b><span style="color:purple">Lab 3</span></b>

* Resources
  - PDF.pdf
  - summary.txt

* pdfReader: read the pdf
* read the summary
* define system prompt and provide context from pdf+summary.  So this will define the perspective of LLM for the overall conversation.   We, therefore, do not need to redefine the system role in each msg.

> ### <b><span style="color:green">a query with system prompt</span></b>
```python
def chat(message, history):
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=messages)
    return response.choices[0].message.content
```

> # <b><span style="color:purple">---</span></b>
> ### <b><span style="color:green">---</span></b>
