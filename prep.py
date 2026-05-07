#!/usr/bin/env python3
"""
AI Meeting Prep Agent
Input a prospect's name + company. Get a research brief in seconds.
"""

import anthropic
import sys
from datetime import date


SYSTEM_PROMPT = """You are an elite sales intelligence researcher.
Given a prospect's name and company, produce a concise, actionable meeting prep brief.
Be specific, direct, and sales-oriented. Skip filler. Surface what an AE actually needs to walk in confident."""


def build_prompt(name: str, company: str, role: str = "") -> str:
    role_line = f"Role: {role}" if role else ""
    return f"""Research this prospect and produce a meeting prep brief.

Prospect: {name}
Company: {company}
{role_line}
Today's date: {date.today()}

Return a structured brief with these sections:

## Company Snapshot
- What they do (1-2 sentences, plain English)
- Business model (SaaS/services/marketplace/etc)
- Size & stage (employees, revenue range if known, funding)

## Recent News & Signals
- Last 3-6 months: funding, product launches, exec hires, layoffs, earnings, press
- What this signals about their priorities right now

## Tech Stack (Likely)
- CRM, marketing automation, sales tools they probably use
- Based on company profile, job postings, and known integrations

## Pain Points to Probe
- 3 specific challenges this type of company/buyer typically faces
- Frame as questions: "Are you running into X?"

## Talking Points
- 3 tailored value angles to open with
- Connect their recent signals to your solution

## Red Flags
- Reasons they might not be a fit or this might be a hard sell

## Suggested Opening
One sentence to open the call that references something specific about them.
"""


def generate_brief(name: str, company: str, role: str = "") -> str:
    client = anthropic.Anthropic()

    print(f"Researching {name} @ {company}...\n")

    with client.messages.stream(
        model="claude-sonnet-4-6",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": build_prompt(name, company, role)}],
    ) as stream:
        full_text = ""
        for text in stream.text_stream:
            print(text, end="", flush=True)
            full_text += text

    return full_text


def save_brief(name: str, company: str, content: str) -> str:
    filename = f"brief_{company.lower().replace(' ', '_')}_{name.split()[0].lower()}.md"
    with open(filename, "w") as f:
        f.write(f"# Meeting Prep: {name} @ {company}\n")
        f.write(f"*Generated {date.today()}*\n\n")
        f.write(content)
    return filename


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python prep.py \"Prospect Name\" \"Company Name\" [\"Title/Role\"]")
        print('Example: python prep.py "Sarah Chen" "Lattice" "VP of RevOps"')
        sys.exit(1)

    name = sys.argv[1]
    company = sys.argv[2]
    role = sys.argv[3] if len(sys.argv) > 3 else ""

    brief = generate_brief(name, company, role)

    print("\n\n---")
    saved = save_brief(name, company, brief)
    print(f"Brief saved to: {saved}")
