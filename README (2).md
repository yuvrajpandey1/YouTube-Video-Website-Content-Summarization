
# Content Summarization

By using Groq API Key specifically using open source model, There is option Summarize URL in that field paste any URL whether YouTube or any external URL as soon as click on Summarize button model will extract content from that particular URL and give Summarize content as Output.


# Documentation 

[Groq](https://groq.com/wp-content/uploads/2024/07/GroqThoughts_WhatIsALPU-vF.pdf?_gl=1*vbjuvi*_ga*MTc0NTUwMDIyLjE3MzAxMzI2MzE.*_ga_SHN3NF0K22*MTczMDUzNzU5Ny4yLjAuMTczMDUzNzU5Ny4wLjAuMA..)

Groq is Fast AI Inference,Groq Powers Leading
Openly-available AI Models such as LLAMA,MIXTRAL,GEMMA,WHISPER.

Groq solutions are based on the Language Processing Unit (LPU), a new
category of processor. Groq is the creator of the LPU and built it from the
ground up to meet the unique characteristics and needs of AI. LPUs run Large
Language Models (LLMs) at substantially faster speeds and, on an architectural
level, up to 10x better energy efficiency compared to GPUs.

So Groq built the LPU. Its four core design principles deliver
performance advantages today and tomorrow.


1.** Software-first (LPU Design Principle 1) :
  The Groq LPU architecture started with the principle of
software-first. The objective was to make the software
developer’s job of maximizing hardware utilization easier and
put as much control as possible in the developer’s hands

GPUs are versatile and powerful; they can handle many
different compute tasks. But they are also complex, putting
extra burden on the software. It must account for variability
in how a workload executes, within and across multiple chips,
making scheduling runtime execution and maximizing
hardware utilization much more challenging. To maximize
hardware utilization on GPUs, every new AI model requires
coding of model-specific kernels. This is where our softwarefirst principle is so important – with GPUs, the software is
always secondary to the hardware. 

The Groq LPU was designed from the outset for linear algebra
calculations – the primary requirement for AI inference. By
limiting the focus to linear algebra compute and simplifying
the multi-chip computation paradigm, Groq took a different
approach to AI inference and chip design. The LPU employs a
programmable assembly line architecture, which enables the
AI inference technology to use a generic, model-independent
compiler and stay true to its software-first principle. The
software is always primary, in complete control of every step
of inference.

2.** Programmable assembly line architecture (LPU Design Principle 2) :


 The primary defining characteristic of the Groq  LPU is its programmable assembly line architecture.

 The LPU features data “conveyor belts” which move instructions and data between the chip’s SIMD (single instruction/multiple
data) function units. At each step of the assembly process, the function unit receives instructions via the conveyor belt. The
instructions inform the function unit where it should go to get the input data (which conveyor belt), which function it should
perform with that data, and where it should place the output data. This process is all software-controlled; no synchronization is
required within the hardware.

The LPU programmable streaming architecture supports an assembly line process within a chip as well as between chips. There
is ample chip-to-chip bandwidth, which enables the data conveyor belts to flow between chips as easily as within a chip. There
is no need for routers or controllers for inter-chip connectivity, even at maximum capacity

The assembly line process within and across chips eliminates bottlenecks. There is no waiting for compute or memory resources
to complete a task. There is no need for additional controllers on the chip given there are no bottlenecks to manage. The
assembly line moves smoothly and efficiently, perfectly in sync.

This is a big improvement compared to how GPUs work. GPUs operate in a multi-core “hub and spoke” model, where an
inefficient data paging approach requires significant overhead to shuttle data back and forth between the compute and
memory units within and across chips. GPUs also utilize multiple hierarchies of external switches and networking chips, both
within and across racks, to communicate among themselves, further exacerbating the software’s scheduling complexity. The
result is a hard-to-program, multi-core approach. 

3.** Deterministic Compute & Networking (LPU Design Principle 3) :


For an assembly line to operate efficiently, there needs to be a high degree of certainty about exactly how long each step will
take. If there is excessive variability in how long a particular task takes to execute, that variability manifests across the entire
assembly line. An efficient assembly line requires highly precise determinism. 

The LPU architecture is deterministic, meaning every execution step is completely predictable to the smallest execution period
(also known as clock cycle). The software-controlled hardware knows with a high degree of precision exactly when and where
an operation will occur and how long it will take.

The Groq LPU achieves its high degree of determinism by eliminating contention for critical resources, namely data bandwidth
and compute. There is ample capacity for routing data around the chip (the conveyor belts) and plenty of compute in the
chip’s functional units. There is no issue with different tasks using the same resource, so there are no execution delays due to
resource bottlenecks.

The same is true for routing data between chips. The LPU data conveyor belts also operate between chips, so connecting
chips results in a larger programmable assembly line. Data flow is statically scheduled by the software during compilation, and
executes the same way every time the program runs. 


4.** On-chip Memory (LPU Design Principle 4) :

LPUs include both memory and compute on-chip, vastly improving the speed of storing and retrieving data while eliminating
timing variation. While determinism ensures the assembly line runs efficiently and eliminates the variability of each compute
stage, on-chip memory enables it to run much faster. 

GPUs utilize separate high-bandwidth memory chips, introducing complexity – multiple layers of memory cache, switches,
and routers to move the data back and forth – while also consuming significant energy. Having the memory on the same chip
improves the efficiency and speed of each I/O action and removes complexity and uncertainty. 

Groq on-chip SRAM has memory bandwidth upwards of 80 terabytes/second, while GPU off-chip HBM clocks in at about eight
terabytes/second. That difference alone gives LPUs up to a 10X speed advantage, on top of the boost LPUs get from not having
to go back and forth to a separate memory chip to retrieve data. 








## Important Libraries Used

 - [Document loaders](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/)
 - [Prompt Template](https://python.langchain.com/v0.1/docs/integrations/llms/deepinfra/#create-a-prompt-template)
 - [YouTube transcripts](https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/)
  - [UnstructuredURLLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url.UnstructuredURLLoader.html#unstructuredurlloader)

- [ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)





## Plateform or Providers

 - [LangChain-ChatGroq](https://python.langchain.com/docs/integrations/chat/groq/)
 - [Streamlit](https://docs.streamlit.io/)

## Model

 - LLM - Gemma-7b-It


## Installation

Install below libraries

```bash
  pip install langchain
  pip install langchain_community
  pip install streamlit
  pip install langchain-groq
  pip install numexpr
  pip install validators
  pip install youtube_transcript_api

```
    
## Tech Stack

**Client:** Python, LangChain PromptTemplate, ChatGroq

**Server:** Streamlit, LangChain,Groq


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`GROQ_API_KEY`


## Examples

```javascript
from langchain_groq import ChatGroq'

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
```

## Chaining


```javascript
from langchain_core.prompts import ChatPromptTemplate'

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

```

