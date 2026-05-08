#!/usr/bin/env python3
"""Demo output for AI Meeting Prep Agent — matches real prep.py output format."""
import time

lines = [
    ("Researching Jordan Kim @ Crestline Systems...\n\n", 0.5),
    ("## Company Snapshot\n", 0.2),
    ("Crestline Systems is a B2B SaaS platform for mid-market ops teams —\n", 0.04),
    ("workflow automation, reporting, and team performance tooling.\n", 0.04),
    ("- **Model:** B2B SaaS · ~$80M ARR · Series D ($120M raised)\n", 0.04),
    ("- **Size:** ~500 employees, growth-to-profitability phase\n\n", 0.1),
    ("## Recent News & Signals\n", 0.2),
    ("- Launched AI-powered workflow summaries (Q4 2024)\n", 0.04),
    ("- 3 open RevOps analyst JDs in last 30 days — scaling ops team\n", 0.04),
    ("- No new funding; focused on profitability post-Series D\n", 0.04),
    ("- *Note: based on AI training data — re-run closer to call date for freshest signals*\n\n", 0.1),
    ("## Tech Stack (Likely)\n", 0.2),
    ("- CRM: Salesforce | Marketing: HubSpot | BI: Looker\n", 0.04),
    ("- Sales Engagement: Outreach | Data: Segment, Fivetran\n\n", 0.1),
    ("## CRM Context\n", 0.2),
    ("- No prior CRM data provided.\n\n", 0.1),
    ("## Pain Points to Probe\n", 0.2),
    ('- "Are you connecting CRM data to comp planning automatically, or still manual?"\n', 0.04),
    ('- "How long does it take your team to produce the weekly revenue narrative?"\n', 0.04),
    ('- "With your AI push, are you worried about data quality feeding those models?"\n\n', 0.1),
    ("## Talking Points\n", 0.2),
    ("- Their AI initiative signals they want to move fast — position as the ops layer that makes AI reliable\n", 0.04),
    ("- 3 open RevOps JDs = scaling pains. Offer to reduce time-to-ramp\n", 0.04),
    ("- Series D + profitability focus = they need efficiency, not headcount\n\n", 0.1),
    ("## Red Flags\n", 0.2),
    ("- Already deep in a post-Series D cost review — budget scrutiny likely\n", 0.04),
    ("- Internal RevOps team build-out may overlap with your use case\n\n", 0.1),
    ("## Suggested Opening\n", 0.2),
    ('"Jordan — saw you\'re scaling the RevOps team at Crestline. We help Series D SaaS ops leaders\n', 0.04),
    ('cut reporting time in half without adding headcount. Worth 15 minutes?"\n\n', 0.04),
    ("\n---\n", 0.3),
    ("Brief saved to: brief_crestline_jordan.md\n", 0.3),
]

for text, delay in lines:
    print(text, end="", flush=True)
    time.sleep(delay)
