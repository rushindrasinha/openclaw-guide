---
title: "OpenClaw Full Stack"
subtitle: "The exact toolchain behind a working personal agent"
author: "Dr Rushindra Sinha (Rushi)"
date: "September 2026 · snapshot of a live Apple-silicon setup"
---

# What this is

A snapshot of the software my agent actually runs on, taken from the live machine in September 2026. Use it as a shopping list, not a script: install the core, then add pieces only when a real task needs them.

> Install the minimum. Add a tool the second time you need it, not the first time you imagine it.

# 1. The core (install these first)

| Piece | Why |
|---|---|
| **OpenClaw** 2026.9.x | The agent gateway: channels, sessions, tools, automations, memory |
| **Node.js 26** | OpenClaw's runtime (24.16+ also works) |
| **Claude Code** | The Claude login OpenClaw reuses, and a coding agent in its own right |
| **Tailscale** | Private network between your machines; nothing exposed to the internet |
| **git + gh** | Version your workspace; GitHub from the command line |

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw gateway install
brew install gh jq tailscale
```

# 2. Models

| Role | What we run |
|---|---|
| Main reasoning | Claude (Sonnet 5 daily, Opus 5.5 for hard problems) through a Claude subscription login |
| Fallbacks | A second Claude model, configured so an outage doesn't stop the agent |
| Local bulk work | **Ollama** with Qwen 3.5 35B: summarising and extracting from meeting recordings |
| Transcription | **mlx-whisper** with `large-v3-turbo` on Apple silicon: voice notes and recordings |
| Memory search | Small local embedding models (nomic-embed-text, EmbeddingGemma) |

```bash
brew install ollama
ollama pull qwen3.5:35b          # ~23 GB; needs a high-RAM Mac
pip install mlx-whisper          # Apple silicon only
```

Local models are free per call and keep private data on the machine. Only pull the ones you'll actually use: we once found about 150 GB of models nothing had touched in weeks.

# 3. Command-line tools (Homebrew)

```bash
brew install ffmpeg        # video and audio processing
brew install yt-dlp        # video downloading
brew install pandoc        # document conversion (Markdown → HTML/PDF/DOCX)
brew install uv            # fast Python environments
brew install himalaya      # email over IMAP/SMTP
brew install ollama        # local models
```

Plus **gog** (Google Workspace: Gmail, Calendar, Drive, Sheets, Docs), which the bundled `gog` skill sets up.

# 4. Node global packages

What's installed globally on our main machine, grouped by job:

| Package | Job |
|---|---|
| `openclaw` | The gateway |
| `@anthropic-ai/claude-code` | Claude Code CLI |
| `@openai/codex`, `@google/gemini-cli` | Second-opinion coding agents |
| `mcporter` | Manage MCP servers from the command line |
| `agent-browser` | Headless browser automation |
| `firecrawl-cli` | Scraping and crawling public sites |
| `vercel`, `@railway/cli` | Deploying sites and services |
| `docx`, `pptxgenjs`, `sharp` | Generating documents, slides and images |

# 5. Python

Keep one virtual environment for the agent's scripts and always call its Python, never the system one.

```bash
uv venv ~/.openclaw/workspace/.venv
uv pip install anthropic google-api-python-client google-auth-oauthlib \
  requests beautifulsoup4 pillow pypdf python-pptx playwright
```

# 6. Memory

| Layer | Tool |
|---|---|
| Built-in | OpenClaw's Markdown memory: `USER.md`, `MEMORY.md`, daily notes, memory search |
| Knowledge graph | **GBrain** (open source): thousands of linked pages about people, projects and decisions, on Postgres + pgvector |
| Verbatim recall | A searchable index of past conversations, for exact quotes and dates |

If you run GBrain alongside many agent sessions, raise Postgres `max_connections`: every session opens its own connection pool.

# 7. Skills

OpenClaw now ships with hundreds of bundled skills (`openclaw skills list`; about 290 are ready on our machine). The ones that earn their keep for us:

| Skill | Job |
|---|---|
| `gog` | Gmail, Calendar, Drive, Sheets, Docs |
| `himalaya` | Any IMAP/SMTP mailbox |
| `github`, `gh-issues` | Repos, issues, pull requests |
| `1password` | Secrets from 1Password |
| `apple-notes`, `apple-reminders` | Apple's notes and reminders |
| `firecrawl-*` | Web scraping and search |
| `browser-automation` | Multi-step browser work |
| `healthcheck` | Security and hardening audit of the host |
| `deep-research` | Multi-source research with citations |

Install community skills with `openclaw skills install @owner/<slug>` from [ClawHub](https://clawhub.ai). Our own public skills: [ares-skills](https://github.com/rushindrasinha/ares-skills).

# 8. Background services

| Service | Job |
|---|---|
| OpenClaw gateway | Always-on agent (installed by `openclaw gateway install`) |
| Liveness guard | Every 2 minutes: is the config valid, is the gateway answering? |
| Health report | Every 6 hours: full check, alerts only on failure |
| Build health | Daily: every shipped build runs its own health command |
| Job verifier | Every 15 minutes: did scheduled jobs actually produce their outputs? |
| Session cleanup | Daily: prunes orphaned sessions and archives old transcripts |

Every alert goes through a gate that suppresses repeats unless something gets worse.

# 9. The fleet

| Machine | Role |
|---|---|
| Mac mini (main) | The brain: main agent, memory, automations, local models, fleet admin |
| Mac mini (business) | A separate agent and WhatsApp number for our esports org |
| iMac | A separate agent for a family business |
| MacBook Pro | Compute and coding |
| Cloud server | Backend for a customer-facing product |
| Windows PC | Gaming and streaming; the agent can drive it for game work |

Everything connects over Tailscale and SSH from the main Mac mini.

# 10. Fresh install, in order

1. Install OpenClaw and finish onboarding (Quick start reuses your Claude login).
2. `openclaw gateway install`, then message the agent from your phone and get a reply.
3. Write `SOUL.md`, `USER.md` and the first rules in `AGENTS.md`. **This is the most important step.**
4. Set `tools.exec.mode` to `ask` and run `openclaw security audit`.
5. Connect one channel: your own WhatsApp or Telegram chat.
6. Add Google (gog) read-only: calendar first, then email.
7. Turn on a morning brief automation.
8. Put the workspace under git and take a backup (`openclaw backup create`).
9. Only now add local models, more channels, more skills and more machines, one at a time.

*Companion to [The OpenClaw Bible](openclaw-bible.pdf). Updates at [github.com/rushindrasinha/openclaw-guide](https://github.com/rushindrasinha/openclaw-guide).*
