# OpenClaw Guide

The complete setup guide for self-hosted AI agents using OpenClaw.

Built and battle-tested by [@irushi](https://x.com/irushi) running agents Ares and Sam on a Mac Mini (Apple Silicon) since 2025.

## What's Inside

**OpenClaw Bible** (19 pages) — Everything you need to go from zero to a working AI agent. Covers installation, the Soul Stack (the most important part), channel setup, security, memory systems, multi-agent coordination, prompt engineering, cost estimates, and a quick reference card.

**OpenClaw Full Stack** (5 pages) — The exact package list to replicate my setup. Every npm package, brew formula, pip install, ClawHub skill, API key, and LaunchD agent. Copy-paste ready.

## Quick Start

1. Read the Bible first. Seriously, read it.
2. Install OpenClaw: `curl -fsSL https://openclaw.ai/install.sh | bash`
3. Run `openclaw onboard --install-daemon`
4. Write your `SOUL.md` — this is the most important step
5. Use the Full Stack doc to install everything else

## The One Thing You Need to Know

> "The secret is not in the skills.md file — it's in the soul.md file."

Skills define HOW to use a tool. The Soul defines WHO the agent is, WHEN it acts, and WHY. A well-written SOUL.md with no skills is more useful than 50 skills with a bad soul.

## Cost

Runs on Anthropic API (Claude). Expect $30-80/month for a full dual-agent setup on Sonnet. Haiku for simple tasks, Opus for deep reasoning.

## Links

- [OpenClaw Docs](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
- [My X](https://x.com/irushi)

## About

I'm Rushi. I run Global Esports (VCT Pacific franchise) and build consumer products at Gesports Pvt Ltd. OpenClaw is the infrastructure layer underneath everything I ship. If you set this up and build something cool, tag me.
