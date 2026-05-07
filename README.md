# AI Meeting Prep Agent

> One command. Thirty seconds. Walk into every discovery call knowing exactly what to say.

Built for Account Executives and founders who do their own selling — and don't have 45 minutes to research every prospect before a call.

---

## What It Does

Input a prospect's name and company. Get back a structured brief covering:

- **Company snapshot** — what they do, size, stage, business model
- **Recent signals** — funding, hires, product launches, layoffs in the last 6 months
- **Likely tech stack** — CRM, automation tools, sales infrastructure
- **Pain points to probe** — framed as questions to ask on the call
- **Tailored talking points** — 3 value angles tied to their situation
- **Red flags** — reasons this might be a hard sell
- **Suggested call opener** — one specific sentence to start strong

---

## Demo

```bash
$ python prep.py "Sarah Chen" "Lattice" "VP of RevOps"

Researching Sarah Chen @ Lattice...

## Company Snapshot
Lattice is a people management platform helping HR and people ops teams run
performance reviews, engagement surveys, and career development programs...

## Recent News & Signals
- Raised $175M Series F in 2021, now focused on profitability
- Launched AI-powered performance summaries (Q4 2024)
- Actively hiring RevOps roles (3 open JDs)...

## Pain Points to Probe
- "Are you running attribution manually across multiple systems?"
- "How are you currently connecting CRM data to your comp planning?"...

---
Brief saved to: brief_lattice_sarah.md
```

---

## Setup

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
```

---

## Usage

```bash
# Basic
python prep.py "Prospect Name" "Company"

# With role for better targeting
python prep.py "Marcus Webb" "Rippling" "Director of Sales"
```

Brief is streamed live to terminal and saved as a `.md` file.

---

## Stack

- Python 3.10+
- [Anthropic Claude API](https://docs.anthropic.com) (`claude-sonnet-4-6`) with streaming

---

## Why This Matters

The average AE spends 20–30 minutes on pre-call research — most of it scattered across LinkedIn, Google News, and Crunchbase. This agent does it in under 30 seconds and surfaces only what matters for the conversation.

*Built by [Henry Tran](https://linkedin.com/in/get-henry) — AI automation for Revenue teams.*
