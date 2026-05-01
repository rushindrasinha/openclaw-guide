<p align="center">
  <img src="docs/openclaw-bible-cover.png" alt="OpenClaw Bible cover" width="48%" />
  <img src="docs/openclaw-full-stack-cover.png" alt="OpenClaw Full Stack cover" width="48%" />
</p>

<h1 align="center">OpenClaw Guide</h1>

<p align="center">
  <strong>The field manual for running a real self-hosted AI agent on your own hardware.</strong>
</p>

<p align="center">
  Built and battle-tested by <a href="https://x.com/irushi">@irushi</a> running agents Ares and Sam on Apple Silicon since 2025.
</p>

<p align="center">
  <a href="./openclaw-bible.pdf">OpenClaw Bible (19 pages)</a> •
  <a href="./openclaw-full-stack.pdf">OpenClaw Full Stack (5 pages)</a> •
  <a href="https://docs.openclaw.ai">OpenClaw Docs</a> •
  <a href="https://clawhub.ai">ClawHub</a>
</p>

---

## What this repo is

This repo is not a theory deck.

It is the exact guide and package stack I would hand to someone who wants to go from **zero** to a functioning, self-hosted OpenClaw agent with:
- a real identity layer
- real channels
- real tooling
- real memory
- real safety constraints
- real operating cost awareness

If you want the shortest path to a serious personal AI system, start here.

## What’s inside

### 1) OpenClaw Bible
**[`openclaw-bible.pdf`](./openclaw-bible.pdf)**

A 19-page setup manual covering the full operating model:
- what OpenClaw actually is
- installation and directory structure
- the **Soul Stack** (`SOUL.md`, `AGENTS.md`, `MEMORY.md`, `HEARTBEAT.md`)
- channel setup
- token and API key management
- usage monitoring and cost control
- safety and security
- skills, cron jobs, and heartbeats
- memory architecture
- multi-agent setup
- prompt engineering
- common issues and fixes

### 2) OpenClaw Full Stack
**[`openclaw-full-stack.pdf`](./openclaw-full-stack.pdf)**

A 5-page replication checklist for the exact software stack:
- global npm packages
- Homebrew packages
- Python environment and dependencies
- OpenClaw skills to install
- media, browser, GitHub, and Google Workspace tooling

## The 5 ideas that matter most

### 1. The Soul Stack is the core system
The most important part of an agent is not its tools — it is the identity and operating layer defined by files like `SOUL.md`, `AGENTS.md`, `MEMORY.md`, and `HEARTBEAT.md`.

### 2. OpenClaw is self-hosted infrastructure, not a chat toy
You run it on your own machine, wire it to your own models, and give it access to real execution surfaces like shell, browser, files, and messaging channels.

### 3. One agent can span multiple channels and workflows
The same agent can operate across WhatsApp, Telegram, Discord, iMessage, and more while keeping a coherent operating model.

### 4. Safety is not optional
If your agent has access to shell, files, and messaging, you need explicit identity, permissions, cost limits, and behavioral rules.

### 5. Memory and heartbeat behavior determine whether the system feels alive
A useful agent is not just responsive — it remembers, tracks context, and proactively does work when the moment calls for it.

## Quick start

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw onboard --install-daemon
openclaw gateway status
openclaw dashboard
```

Then:
1. read the **Bible** first
2. write your `SOUL.md`
3. use the **Full Stack** doc to replicate the surrounding toolchain
4. connect one channel
5. test one real workflow end-to-end

## Who this is for

This repo is for:
- founders building a personal AI operating system
- operators who want a real self-hosted agent instead of a SaaS wrapper
- creators who want agents inside messaging and media workflows
- developers who want to understand how a production OpenClaw stack is actually assembled

This repo is **not** for someone looking for a one-click toy demo.

## Cost and hardware expectations

- recommended model starting point: **Claude Sonnet**
- expected operating cost for a serious dual-agent setup: **~$30–80/month**
- recommended hardware: **Apple Silicon Mac mini / MacBook**, though Linux and VPS setups are also viable

## Why this repo exists

Most AI agent content online is either:
- too abstract
- too beginner-fluffy
- or too fragmented to reproduce

This repo exists to close that gap.

It gives you the documents I wish I had when wiring a real self-hosted agent stack from scratch.

## Related links

- [OpenClaw Docs](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.ai)
- [Rushi on X](https://x.com/irushi)

## Usage

These docs are public so builders can learn from and adapt the setup. If you build something from this, tag me — I want to see what you make.
