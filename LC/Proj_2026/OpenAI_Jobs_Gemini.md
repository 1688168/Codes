# Report 1: Software Engineering Roles at OpenAI and Anthropic

Both OpenAI and Anthropic are aggressively scaling their engineering teams, and their open positions reflect the massive compute, infrastructure, and productization demands of state-of-the-art Large Language Models (LLMs). Open software developer positions at both companies generally fall into five distinct categories:

### 1. Applied AI & Product Engineering
These roles focus on building user-facing products (like ChatGPT and Claude) and developer platforms (APIs, enterprise tools).
* **Typical Titles:** Full-Stack Engineer, Backend/Frontend Engineer, Mobile Engineer (iOS/Android), Desktop Engineer.
* **Focus:** Building robust API infrastructures, B2B enterprise integrations, subscription billing platforms, and consumer-facing chat interfaces. For example, OpenAI is heavily recruiting for its "Applied AI Engineering" division (focusing on Growth, ChatGPT ecosystem, and Edu platforms), while Anthropic has strong demand on its "Engineering & Design - Product" team for its Claude Code and UI platforms.

### 2. Infrastructure, Cloud & Distributed Systems
These are the backbone roles that support the massive scale required for model training and real-time inference.
* **Typical Titles:** Infrastructure Engineer, Distributed Systems Engineer, Kubernetes Platform Engineer, Cloud Inference Engineer.
* **Focus:** Optimizing cluster infrastructure, node deployment, caching, databases, and high-availability inference routing across cloud environments (like AWS for Anthropic or Azure for OpenAI). Both companies heavily hire for Site Reliability Engineering (SRE) to maintain near 100% uptime.

### 3. AI Research & Performance Engineering
These roles bridge the gap between traditional software engineering and machine learning science.
* **Typical Titles:** ML Systems Engineer, Performance Engineer, TPU/GPU Kernel Engineer, Compute Optimization Engineer.
* **Focus:** Writing low-level hardware kernels, scaling Reinforcement Learning (RL) velocity, optimizing model inference runtimes, and building internal research/evaluation tools. At OpenAI, this includes the "Accelerators" and "Runtime" teams; Anthropic heavily hires for "Inference Routing and Performance."

### 4. Security, Safety & Alignment
Engineers in these roles are dedicated to ensuring the models operate within safe bounds and protecting core intellectual property.
* **Typical Titles:** Privacy Research Engineer, Cybersecurity Software Engineer, ML Infrastructure Engineer (Safeguards), Sandboxing Engineer.
* **Focus:** Building automated evaluation frameworks, abuse detection systems, red-teaming infrastructure, and maintaining strict sandboxing environments to safely execute AI-generated code.

### 5. Hardware & Datacenter Compute
Software engineers who interface directly with physical scaling and networking operations.
* **Typical Titles:** Datacenter NetworkDeploy Lead, ASIC Firmware Engineer, Datacenter Server Lifecycle Engineer.
* **Focus:** Automating global datacenter scaling, fiber network engineering, power management, and hardware telemetry.

---

# Report 2: SDE Labor Market Analysis for Frontier AI Labs (OpenAI & Anthropic)

Frontier AI companies are currently operating in a hyper-growth phase where compute and scale are their primary bottlenecks. They do not just need engineers who know how to call an LLM API; they desperately need hardcore systems engineers who can build the infrastructure to train, serve, and productize those models at global scale.

Here is a breakdown of what OpenAI and Anthropic are looking for, what they pay, and how experience in high-scale environments translates to their tech stacks.

### 1. The Desired SDE Archetypes
While they occasionally hire pure ML researchers, the bulk of their open software engineering roles fall into two buckets that are highly relevant to traditional big-tech experience:

* **Inference & Distributed Systems Engineers:** The core challenge right now is serving massive models efficiently. They need engineers who can build highly available, fault-tolerant distributed systems that route traffic, manage GPU memory allocation, and handle massive concurrency without dropping requests.
* **Applied / Product Engineers:** These teams build the enterprise APIs, consumer apps (ChatGPT / Claude), and the surrounding infrastructure (billing, rate-limiting, authentication, data pipelines). 

### 2. Required Skills & Tech Stack
To pass their technical loops, the skill expectations are rigorous and lean heavily into systems design and low-level optimization.

* **Core Languages:** Python is mandatory for interfacing with the ML stack (PyTorch), but there is a massive shift toward **Rust, Go, and C++** for performance-critical backend services and infrastructure.
* **Systems Architecture:** Deep expertise in microservices, Kubernetes, gRPC, Kafka, and asynchronous programming. 
* **Performance Optimization:** You need to understand how to squeeze every ounce of performance out of a system. Concepts like caching strategies, load balancing, low-latency network routing, and memory profiling are critical.
* **AI Context (Nice to Have):** You do not need a PhD in Machine Learning to be an SDE here. However, understanding the fundamentals of how transformers work, GPU memory constraints (VRAM), and concepts like batching and quantization will heavily differentiate you in the interview process.

### 3. The AdTech Advantage (Transferable Skills)
Building highly available, low-latency distributed systems for ad bidding and delivery translates remarkably well to scaling LLM inference. 

Handling millions of queries per second (QPS) with strict, sub-millisecond Service Level Agreements (SLAs) is exactly the kind of engineering rigor required to manage API gateways and inference routing for large models. The architecture used to predict, retrieve, and serve an ad payload at massive scale is structurally similar to managing the distributed infrastructure that serves a language model's output to enterprise clients. 

### 4. Compensation Expectations (2026 Market Data)
Compensation at OpenAI and Anthropic is highly competitive and aggressively structured around equity to compete with Big Tech. An SDE II maps roughly to an L4 (Mid-Level) or L5 (Senior) depending on interview performance. 

* **Base Salary:** Typically ranges from **$200,000 to $350,000** depending on the specific team and level. 
* **Equity / Profit Participation Units (PPUs):** This is where the numbers explode. Instead of standard Restricted Stock Units (RSUs), OpenAI uses PPUs, and Anthropic offers highly lucrative equity packages based on recent multi-billion dollar valuations.
* **Total Compensation (TC):** For a mid-level to senior engineer, TC generally ranges from **$450,000 to $800,000+** per year. Keep in mind that this equity is highly illiquid compared to public stock, though secondary tender offers happen occasionally.