Learning this course for landing job interviews in AI engineer role

Reverse-engineered from real job descriptions. Every module maps to skills that appeared in 30%+ of AI Engineer JDs sampled from Indian and global product companies.
Open-source first. Zero API cost required to complete the course. Groq's free tier + Ollama + HuggingFace = you can finish this on a laptop with no credit card.
Evaluation-first mindset. "Red flag if candidate doesn't start with evals" is the #1 senior interviewer complaint. Most courses skip this. This one leads with it from Week 4.
Interview + resume module. No other free course does this. You'll get 30 real interview questions with model answers, a system design framework, and a resume template that matches the roles you're targeting.


WEEK 1 — LLM Fundamentals + API Mastery
Objective: Student can call any major LLM API, handle streaming, structured output, errors, and retries. Understand what an LLM actually is at a working-engineer level.

Interview questions this week prepares for: "What is temperature?", "What is a token?", "Explain context window", "OpenAI vs Anthropic vs Gemini — when to pick what?", "How do you handle rate limits?"

Episode 1.1 — What an LLM Actually Is (No BS Version)
Runtime: 12-15 min
Cover: Tokens, context window, temperature, top_p, system/user/assistant roles, why hallucinations happen, what "GPT-4o", "Claude Sonnet 4.5", "Gemini 2.5 Pro" mean
Skip: Transformer architecture math, attention mechanism, backprop
Assignment: Explain to a friend in Hinglish what an LLM is in under 60 seconds
Episode 1.2 — Your First LLM Call (Multi-Provider)
Runtime: 15-18 min
Cover: Setup, API keys, first call with OpenAI, Anthropic, Groq (free), and Gemini in one notebook
Tools: openai, anthropic, google-genai, groq SDKs
Assignment: Write a script that asks the same question to 3 providers and prints all responses
Episode 1.3 — Streaming, Async, and Production Basics
Runtime: 15 min
Cover: Streaming responses, async calls, retries with tenacity, timeout handling, rate limit backoff
Assignment: Build a streaming CLI chatbot with retry logic
Episode 1.4 — Structured Output with Pydantic
Runtime: 12-15 min
Cover: JSON mode, Pydantic models, response_format parameter, why this is 80% of production LLM code
Interview relevance: "How do you get reliable structured output from an LLM?"
Assignment: Extract structured data (name, email, intent) from customer support messages
Episode 1.5 — Model Selection & Cost Math
Runtime: 12 min
Cover: Frontier vs open-source, cost per 1M tokens, latency benchmarks, when to use Groq vs OpenAI vs local Ollama, quick model-routing pattern
Deliverable this week: Multi-provider chatbot with streaming, structured output, and error handling. Push to GitHub.
Resume line unlocked: "Built a multi-provider LLM abstraction layer supporting streaming, structured output (Pydantic), and automatic failover across OpenAI, Anthropic, and Groq."
