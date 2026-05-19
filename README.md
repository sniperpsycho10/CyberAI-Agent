# CyberAI-Agent

A modular local AI cybersecurity assistant built using:
- Ollama
- Qwen2.5
- DeepSeek-Coder
- Open WebUI
- SearXNG
- Python
- Semantic AI Orchestration

---

# PROJECT GOAL

The goal of this project is to build a fully local AI-powered cybersecurity assistant capable of:

- semantic task orchestration
- shell command execution
- AI-powered reasoning
- code generation
- operational safety checks
- runtime sanitization
- retrieval-augmented generation (RAG)
- future memory/context systems
- future autonomous workflows

The system is designed to evolve into a production-grade local cybersecurity AI agent.

---

# CURRENT ARCHITECTURE

```text
User Prompt
     ↓
AI Intent Classifier
     ↓
Router
     ↓
┌──────────────────────────────┐
│ Operational Shell Pipeline   │
│ Coding Pipeline              │
│ Reasoning Pipeline           │
└──────────────────────────────┘
```

---

# MODELS USED

## Qwen2.5:7b
Purpose:
- reasoning
- orchestration
- command generation
- command interpretation
- semantic classification

## DeepSeek-Coder:6.7b
Purpose:
- code generation
- scripting
- automation development
- exploit/tool coding

---

# COMPLETED PHASES

---

# PHASE 1 — LOCAL LLM SETUP

Completed:
- Installed Ollama
- Downloaded local models
- Configured Ollama service
- Enabled auto-start
- Verified persistent operation

Models:
- qwen2.5:7b
- deepseek-coder:6.7b

Key Learnings:
- Ollama service management
- localhost model serving
- local inference workflows
- model persistence
- resource management

---

# PHASE 2 — OPEN WEBUI + RAG

Completed:
- Installed Docker
- Installed Open WebUI
- Installed SearXNG
- Connected WebUI to Ollama
- Enabled web search integration
- Built initial RAG knowledge base

Knowledge Base Structure:
- linux/
- networking/
- wifi/
- passwords/
- tools/
- crypto/
- cheatsheets/

Added:
- Kali Linux tool documentation
- Hydra docs
- WiFi docs
- Linux/networking references

Key Learnings:
- local RAG systems
- SearXNG integration
- Docker networking
- Open WebUI memory system
- document ingestion

---

# PHASE 3 — AI AGENT ORCHESTRATION

Completed:
- built shell execution engine
- built semantic orchestration router
- built modular architecture
- built safety layer
- built runtime command sanitization
- built AI interpretation system
- built semantic AI classifier

---

# CURRENT PROJECT FILE STRUCTURE

```text
CyberAI-Agent/
│
├── main.py
├── router.py
├── classifier.py
├── shell_executor.py
├── interpreter.py
├── safety.py
├── prompts.py
├── models.py
├── config.py
│
├── ai_shell_agent.py
│
└── cyber/
```

---

# FILE DESCRIPTIONS

## main.py
Main application loop.

Responsibilities:
- user input
- graceful shutdown
- error handling
- routing initialization

---

## router.py
Semantic orchestration router.

Responsibilities:
- pipeline selection
- orchestration logic
- task dispatching

Pipelines:
- shell
- coding
- reasoning

---

## classifier.py
AI-powered semantic intent classifier.

Responsibilities:
- semantic intent detection
- classification:
  - shell
  - coding
  - reasoning

Uses:
- Qwen2.5

---

## shell_executor.py
Operational execution engine.

Responsibilities:
- command generation
- command execution
- risk display
- y/n confirmation
- subprocess handling

---

## safety.py
Safety and sanitization layer.

Responsibilities:
- dangerous command detection
- runtime sanitization
- interactive command prevention

Examples:
- top → top -b -n 1
- ping → ping -c 4
- tcpdump → timeout 10 tcpdump

---

## interpreter.py
AI output analysis engine.

Responsibilities:
- output summarization
- troubleshooting hints
- operational interpretation

Uses:
- Qwen2.5

---

## prompts.py
Centralized prompt templates.

Responsibilities:
- command generation prompts
- interpretation prompts
- future system prompts

---

## models.py
Model communication layer.

Responsibilities:
- Ollama communication
- model abstraction
- inference handling

---

## config.py
Configuration management.

Responsibilities:
- model names
- inference settings
- future configs

---

# FEATURES IMPLEMENTED

## Semantic AI Routing
Replaced keyword routing with AI classification.

Capabilities:
- semantic intent understanding
- overlapping intent handling
- intelligent pipeline selection

---

## Operational Shell Pipeline

Capabilities:
- AI-generated commands
- risk analysis
- execution confirmation
- runtime execution
- AI interpretation

---

## Safety System

Implemented:
- high-risk detection
- dangerous command warnings
- runtime sanitization
- interactive command prevention

---

## Runtime Sanitization

Examples:
- top → top -b -n 1
- tail -f → tail -n 20
- ping → ping -c 4

Purpose:
- avoid blocking execution
- avoid infinite-running commands
- stabilize operational behavior

---

# MEMORY OPTIMIZATION

Implemented:
- keep_alive=0
- automatic model unloading
- reduced RAM usage
- improved system responsiveness

---

# CURRENT CAPABILITIES

The system can currently:

✅ Execute Linux commands safely  
✅ Generate scripts and code  
✅ Explain cybersecurity concepts  
✅ Route tasks semantically  
✅ Interpret command outputs  
✅ Prevent dangerous execution  
✅ Use local LLMs completely offline  
✅ Use RAG knowledge base  
✅ Use local web search via SearXNG  

---

# CURRENT LIMITATIONS

Current limitations include:
- no persistent memory yet
- no long-term context tracking
- no autonomous workflows yet
- no GUI dashboard
- no streaming responses
- no vector database memory yet

---

# FUTURE ROADMAP

## PHASE 4 — MEMORY + CONTEXT ENGINE
Planned:
- session memory
- command history
- operational state tracking
- long-term memory

---

## PHASE 5 — ADVANCED AGENT SYSTEMS
Planned:
- autonomous workflows
- chained operations
- multi-agent systems
- tool chaining

---

## PHASE 6 — POLISH + PRODUCTIONIZATION
Planned:
- terminal UI improvements
- colored outputs
- logging system
- plugin system
- configuration menus
- streaming responses
- dashboard UI

---

# SECURITY DISCLAIMER

This project is intended strictly for:
- educational purposes
- authorized security research
- local experimentation

The user is responsible for ethical and legal usage.

---

# AUTHOR

Built by:
sniperpsycho10

Local AI Cybersecurity Agent Project