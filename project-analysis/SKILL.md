---
name: project-analysis
description: Analyze any project (website, app, backend service, ML system, command-line tool, or similar) and produce a full written report covering purpose, technologies used, architecture, features, security, internal organization, dependencies, APIs, data handling, build and deployment process, quality scoring, and an honest evaluation of strengths and weaknesses. Use whenever asked to analyze, review, audit, or explain a project or codebase.
---

# Project Analysis Skill

Produce a deep, well-organized, and honest written report analyzing any project, regardless of what kind of project it is or what technology it's built with. The final report should read like a professional consulting audit — scannable, evidence-based, and visually organized — not a wall of prose.

## Core principle

Investigate before writing. Never guess or invent details. Every claim in the report should be based on something actually found while examining the project. If something cannot be determined, say so plainly rather than making it up — "not present" or "not determined" is a valid and useful finding, not a gap to paper over. Where a claim is inferred rather than confirmed, mark it inline with `⚠️ Inferred` so uncertain claims are visually distinct from confirmed ones.

## Step 0: Report header and executive summary

Open the report with a short metadata block: project name, analysis date, and a rough scope note (e.g. number of files/modules scanned). Follow it with a table of contents if the report will be long.

Then write a 3–5 sentence executive summary covering: what the project is, how mature/production-ready it appears to be, and the single biggest strength and the single biggest risk. This goes before any detailed section — a reader should get the verdict before the evidence.

## Step 1: Understand what the project is

Work out what kind of project this is — a website, a mobile app, a backend service, a data or machine learning system, a command-line tool, or a combination of several. Identify the general category and the technology it's built with. This first impression shapes everything that follows and should never be skipped.

## Step 2: Understand its purpose

Work out what the project actually does, who it's meant for, and why it exists. This becomes the foundation the rest of the report builds on.

## Step 3: Identify the technologies used

Identify the frameworks, tools, and technologies that power the project, and explain the role each one plays. Note anything that seems referenced but unused, or used but not properly accounted for.

## Step 4: Study the architecture

Examine how the project is structured at a high level — how its different parts relate to one another, how information flows through it, and how its components communicate and work together. Where the structure is non-trivial, include a simple diagram (Mermaid syntax or clean ASCII) showing the major components and how they connect. A diagram here is strongly preferred over prose alone.

## Step 5: List the features and functionality

Describe, in concrete and specific terms, everything the project can actually do — what a user or another system could interact with or accomplish through it.

## Step 6: Examine security

Assess how access is controlled, how sensitive information is protected, how input is handled safely, and whether encryption or other protections are in place. Call out anything risky clearly and specifically rather than vaguely.

## Step 7: Review the internal organization

Look at how the project is organized internally, what conventions and patterns are followed, and how consistent, clean, and well thought-out the overall design is. Note anything messy, duplicated, or inconsistent. Where relevant, note whether the project follows common conventions for its language/framework (e.g. PEP8, standard REST resource naming) or deviates from them.

## Step 8: List what it depends on

Identify everything the project relies on to function. Distinguish between what's essential to run it versus what's only used during development, and flag anything outdated or notably important. Note the project's license if one is present, and flag any dependency whose license could conflict with it (e.g. a copyleft dependency inside a project intended for closed/commercial use).

## Step 9: Analyze any APIs, if present

If the project exposes a way for other systems to interact with it, describe what's available, how it's accessed, what it requires to be used, and how well protected it is. If there's no such interface, say so plainly.

## Step 10: Examine data storage, if present

If the project stores or manages data, describe how that data is structured, organized, and handled. If there's no data storage involved, say so plainly.

## Step 11: Understand how it's built, tested, and deployed

Describe the process by which the project gets assembled, tested, and put into real use, including any automation involved. If automated tests exist, note what's covered and, if determinable, pass/fail status or coverage. If no tests exist, state that plainly as a finding rather than skipping the topic.

## Step 12: Score the project

Produce a scorecard table rating the project across key dimensions — at minimum: Security, Code Quality, Documentation, Test Coverage, and Architecture/Scalability. Use a simple scale (e.g. Low / Medium / High, or 1–5) with one sentence of justification per rating, tied to something specific found during the analysis. Never assign a score without a reason attached to it.

## Step 13: Give an honest evaluation and prioritized recommendations

Summarize what the project does well and what issues exist. Then produce a prioritized recommendations table with columns: Issue | Severity (Critical / High / Medium / Low) | Effort to Fix | Suggested Action. Order it with the most important issues first, especially anything related to security or correctness. Be balanced — don't pad with empty praise or vague criticism, and tie every point to something actually found.

## Step 14: Appendix and glossary (as needed)

If the project uses domain-specific or unusual terminology, include a short glossary. Include an appendix with raw supporting data that would clutter the main body — full dependency lists, file/line counts per module, etc. — so the main report stays readable while nothing is hidden.

## Quality bar

Every section should be specific and grounded in what was actually found, not generic or templated language. Where something is inferred rather than confirmed outright, mark it with `⚠️ Inferred` and use language like "appears to" or "likely" rather than stating it as settled fact. Never invent specific figures, measurements, or scores that weren't actually determined — if such information genuinely isn't available, say so rather than guessing. The scorecard and recommendations table are required whenever a full report is produced; do not omit them even for small or simple projects.