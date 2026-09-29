```{=html}
<section class="cover">
<div class="grid"></div><div class="glow g1"></div><div class="glow g2"></div>
<div class="kicker">FIELD MANUAL · SEPTEMBER 2026 · OPENCLAW 2026.9.x</div>
<h1 class="ct">The OpenClaw <em>Bible</em></h1>
<p class="sub">How I run a self-hosted AI chief of staff every day, what it actually does, what it costs, and everything that broke along the way.</p>
<div class="strip">
<div><b>~10 mo</b><span>running daily</span></div>
<div><b>94</b><span>scheduled automations</span></div>
<div><b>18</b><span>specialist agents</span></div>
<div><b>98–100%</b><span>prompt cache hit</span></div>
</div>
<div class="by"><div><b>Dr Rushindra Sinha (Rushi)</b>x.com/irushi</div><div>Setup + lessons · with receipts</div></div>
</section>
```

:::: contents-page
::: toc-col
## Contents

```{=html}
<div id="toc"></div>
```
:::

::: read-col
## Read this first

This is the manual I wish I had when I started. It comes from running my agent, Ares, every day since January 2026: across WhatsApp and Discord, on a fleet of seven machines, with 94 scheduled jobs and a knowledge graph that now holds about 6,700 pages.

An honest warning. I tore my hair out configuring this, and some days it still does more harm than good. It took 6 to 8 months of compounding before it became what it is now. And it isn't OpenClaw alone. The real power is the stack: Claude and Claude Code, plus GPT and Codex for second opinions, with OpenClaw as the surface that lets me shape it into anything.

If you want something that works with less setup, try [Hermes Agent](https://github.com/NousResearch/hermes-agent) first. If you want to build your own system and own it, read on.

Every chapter has the same shape. A short opener. **The setup**: how OpenClaw works today, with commands checked against 2026.9.x. Then **the lessons** in a violet box: what running it for real taught me. The setup changes with every release, so check [docs.openclaw.ai](https://docs.openclaw.ai) when in doubt. The lessons don't change much.

::: pull
Start locked down. Loosen slowly. An agent earns trust the way a new hire does: one task done right at a time.
:::

::: howto
**Deciding if it's worth it?** Read Part I: what it does, the receipts, what it costs.

**Setting up?** Part II, in order. Don't skip Security.

**Already running?** Part III, then steal whatever rules you like from the failure table in Receipts.
:::
:::
::::

```{=html}
<div class="part" data-part="Part I" data-title="The proof"><span class="pn">Part I</span><span class="pt">The proof</span><span class="pd">What it is, what it actually does all day, and why it doesn't set money on fire.</span></div>
```

# What OpenClaw is {#what}

::: opener
People ask what Ares is. The honest answer: a new employee with a laptop and my phone number, who never sleeps and forgets nothing that's written down.
:::

OpenClaw is a self-hosted AI agent gateway. You run it on your own machine (a Mac mini, a laptop, a Linux box or a cloud server) and it connects the chat apps you already use to the AI models you choose. The result lives in WhatsApp, Telegram, Discord, Slack, iMessage, Signal and more, has access to your machine, and does real work: files, browser, email, calendar, code, scheduled jobs.

```{=html}
<div class="fig">
<svg viewBox="0 0 760 322" xmlns="http://www.w3.org/2000/svg" font-family="-apple-system,Helvetica,Arial,sans-serif">
<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#ff3b30"/></marker></defs>
<g stroke="#ff3b30" stroke-width="2" fill="none" marker-end="url(#ah)">
<line x1="142" y1="80" x2="176" y2="80"/><line x1="342" y1="80" x2="376" y2="80"/><line x1="542" y1="80" x2="576" y2="80"/>
<line x1="670" y1="142" x2="670" y2="186"/><path d="M612,142 V164 H385 V186"/><line x1="228" y1="250" x2="194" y2="250"/>
</g>
<rect x="0" y="20" width="140" height="120" rx="12" fill="#fff" stroke="#d9d7e3" stroke-width="1.5"/>
<text x="70" y="46" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff3b30" letter-spacing="1.5" font-family="Menlo,monospace">YOU</text>
<text x="70" y="74" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Your phone</text>
<text x="70" y="96" text-anchor="middle" font-size="12" fill="#5d5f6c">text · voice notes</text>
<text x="70" y="114" text-anchor="middle" font-size="12" fill="#5d5f6c">files · links</text>
<rect x="180" y="20" width="160" height="120" rx="12" fill="#fff" stroke="#d9d7e3" stroke-width="1.5"/>
<text x="260" y="46" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff3b30" letter-spacing="1.5" font-family="Menlo,monospace">CHANNEL</text>
<text x="260" y="74" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Chat app</text>
<text x="260" y="96" text-anchor="middle" font-size="12" fill="#5d5f6c">WhatsApp · Discord</text>
<text x="260" y="114" text-anchor="middle" font-size="12" fill="#5d5f6c">Telegram · Slack · more</text>
<rect x="380" y="20" width="160" height="120" rx="12" fill="#0a0b10"/>
<text x="460" y="46" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff6b5e" letter-spacing="1.5" font-family="Menlo,monospace">ALWAYS ON</text>
<text x="460" y="74" text-anchor="middle" font-size="16" font-weight="800" fill="#fff">OpenClaw gateway</text>
<text x="460" y="96" text-anchor="middle" font-size="12" fill="#b7b9c8">routing · sessions</text>
<text x="460" y="114" text-anchor="middle" font-size="12" fill="#b7b9c8">schedules · permissions</text>
<rect x="580" y="20" width="180" height="120" rx="12" fill="#f1f0ff" stroke="#5e5ce6" stroke-width="1.5"/>
<text x="670" y="42" text-anchor="middle" font-size="10.5" font-weight="700" fill="#5e5ce6" letter-spacing="1.5" font-family="Menlo,monospace">AGENT</text>
<text x="670" y="64" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Ares</text>
<rect x="596" y="74" width="148" height="26" rx="7" fill="#5e5ce6"/>
<text x="670" y="91.5" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Soul stack</text>
<rect x="596" y="106" width="148" height="26" rx="7" fill="#8e8cff"/>
<text x="670" y="123.5" text-anchor="middle" font-size="12" font-weight="700" fill="#fff">Memory</text>
<rect x="0" y="190" width="190" height="120" rx="12" fill="#fff" stroke="#b9b7c7" stroke-width="1.5" stroke-dasharray="5 4"/>
<text x="95" y="216" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff3b30" letter-spacing="1.5" font-family="Menlo,monospace">FLEET</text>
<text x="95" y="244" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Other machines</text>
<text x="95" y="266" text-anchor="middle" font-size="12" fill="#5d5f6c">7 machines on Tailscale</text>
<text x="95" y="284" text-anchor="middle" font-size="12" fill="#5d5f6c">SSH from one admin mini</text>
<rect x="230" y="190" width="310" height="120" rx="12" fill="#fff" stroke="#d9d7e3" stroke-width="1.5"/>
<text x="385" y="216" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff3b30" letter-spacing="1.5" font-family="Menlo,monospace">HANDS</text>
<text x="385" y="244" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Tools · skills · automations</text>
<text x="385" y="266" text-anchor="middle" font-size="12" fill="#5d5f6c">shell · files · browser · email · calendar</text>
<text x="385" y="284" text-anchor="middle" font-size="12" fill="#5d5f6c">~327 skills · 94 automations · ~440 scripts</text>
<rect x="560" y="190" width="200" height="120" rx="12" fill="#fff" stroke="#d9d7e3" stroke-width="1.5"/>
<text x="660" y="216" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ff3b30" letter-spacing="1.5" font-family="Menlo,monospace">BRAINS</text>
<text x="660" y="244" text-anchor="middle" font-size="16" font-weight="800" fill="#101117">Models</text>
<text x="660" y="266" text-anchor="middle" font-size="12" fill="#5d5f6c">Cloud: Claude (subscription)</text>
<text x="660" y="284" text-anchor="middle" font-size="12" fill="#5d5f6c">Local: Qwen · Whisper</text>
<text x="660" y="300" text-anchor="middle" font-size="12" fill="#5d5f6c">+ embedding models</text>
</svg>
<div class="cap"><b>Fig 1</b> · How a message becomes work. The soul stack is SOUL, AGENTS, USER and IDENTITY; memory is MEMORY.md, daily notes and a knowledge graph.</div>
</div>
```

Read it left to right. You message from your phone. The **gateway**, always on, receives it and routes it to an agent (bindings decide which one). The **agent** loads its soul stack and searches its memory, then acts through **tools, skills and automations**, thinking with **models**: Claude in the cloud for judgement, local models for bulk work. The reply lands in the same chat.

- **Self-hosted.** Your data, config and memory stay on your machine.
- **Multi-channel, multi-model.** One agent, many chat apps, any mix of providers, with fallbacks.
- **Real access.** Shell, files, browser, devices, network, governed by permission modes you control.

::: lesson
- **Treat it as a new employee, not a chatbot.** That framing gets every other decision right, especially the safety ones.
- **The model is the brain, but the value lives in the files and the schedule.** Swap the model and Ares is still Ares. Lose the workspace and it's a stranger.
:::

# Receipts {#receipts}

::: opener
The fair criticism of OpenClaw is that nobody shows results. So here are mine: what the system is made of, what it does on a normal day, and where it has failed.
:::

```{=html}
<div class="stats">
<div class="stat hot"><b><em>~10</em> <small>months</small></b><span>running every day, first memory notes January 2026</span></div>
<div class="stat"><b>~6,700</b><span>knowledge-graph pages, ~28,000 links between them</span></div>
<div class="stat"><b>~584K</b><span>archived messages, searchable for exact quotes</span></div>
<div class="stat"><b>~440</b><span>scripts and tools the agent wrote for itself</span></div>
<div class="stat"><b>94</b><span>scheduled automations</span></div>
<div class="stat"><b>18</b><span>specialist agents</span></div>
<div class="stat"><b>~327</b><span>skills available to the agent, about 290 of them ready</span></div>
<div class="stat"><b>823</b><span>commits to its own workspace repo</span></div>
<div class="stat"><b>7</b><span>machines in the fleet, one admin Mac mini</span></div>
<div class="stat"><b>~27,000</b><span>local model calls in September, zero API cost</span></div>
<div class="stat hot"><b><em>98–100%</em></b><span>of each main-agent turn served from prompt cache</span></div>
<div class="stat"><b>15 <small>min</small></b><span>between checks that every scheduled job really produced its output</span></div>
</div>
<div class="cap"><b>Fig 2</b> · The live system, September 2026. Rounded, not polished.</div>
```

## A normal day

| When | What happens, without me asking |
|--|--------|
| Morning | A one-screen brief lands on WhatsApp: the bottleneck, today, what's waiting on me, what to decide now |
| All day | Every voice note is transcribed locally (mlx-whisper) and turned into tasks, drafts or answers; meeting recordings are summarised by a local Qwen model |
| All day | Inbox, calendar, drafts, code and servers across seven machines, from one chat thread |
| Every 2 minutes | A liveness guard checks the config is valid and the gateway is answering |
| Every 15 minutes | A verifier checks that every scheduled job actually produced the output it declared |
| Every 6 hours | A full health report, silent unless something failed |
| Daily | Every shipped tool runs its own health check; stale sessions are cleaned up |

```{=html}
<div class="keep">
<h2>Four receipts, in their real format</h2>
<p>The formats below are exactly what runs. The contents are representative samples, not real data.</p>
<div class="two">
<div class="fig" style="margin:0">
<span class="tag">Representative sample</span>
<div class="msg"><span class="h">ARES BRIEF · Tue 30 Sep · 08:00</span><br><br>
<span class="k">BOTTLENECK</span><br>Contract draft waiting on your review since Tuesday. Two follow-ups are blocked behind it.<br><br>
<span class="k">TODAY</span><br>11:00 product call, agenda drafted.<br>15:00 design review, 3 open comments summarised.<br><br>
<span class="k">WAITING ON YOU</span><br>Newsletter draft, sent for approval 18:40 yesterday.<br><br>
<span class="k">DECIDE NOW</span><br>Old staging server idle 41 days. Keep or shut down?</div>
<div class="cap"><b>Receipt A</b> · The morning brief. One screen, urgent fact first, no padding. If nothing matters, it stays silent.</div>
</div>
<div>
<div class="fig" style="margin:0 0 .12in">
<span class="tag">Real rule format</span>
<div class="msg"><span class="v">RULE</span> Never send outward without approval.<br><span class="v">WHY</span>&nbsp; A wrong email to a partner can't be unsent.<br><span class="v">SCOPE</span> Approval is per item. If the content changes, it's void.</div>
<div class="cap"><b>Receipt B</b> · A rule with its why. The why is what lets it generalise to cases I never wrote down.</div>
</div>
<div class="fig" style="margin:0">
<span class="tag">Real flow</span>
<div class="flow"><div class="st"><b>Draft</b>agent writes it</div><div class="ar">›</div><div class="st"><b>Preview</b>on WhatsApp</div><div class="ar">›</div><div class="st k"><b>You reply</b>GO · EDIT · KILL</div><div class="ar">›</div><div class="st"><b>Send</b>exactly what was approved</div></div>
<div class="flow-note">If hours have passed since GO, it re-reads the thread first. You may already have sent it yourself.</div>
<div class="cap"><b>Receipt C</b> · The approval flow for anything outward-facing.</div>
</div>
</div>
</div>
</div>
<div class="fig">
<span class="tag">Real flow</span>
<div class="flow"><div class="st"><b>Job declares</b>"I will write brief.md"</div><div class="ar">›</div><div class="st"><b>Job runs</b>on its schedule</div><div class="ar">›</div><div class="st k"><b>Verifier, every 15 min</b>file exists? timestamp fresh?</div><div class="ar">›</div><div class="st"><b>Yes</b>silence</div><div class="ar">›</div><div class="st"><b>No</b>one gated alert, repeats only if it gets worse</div></div>
<div class="cap"><b>Receipt D</b> · Declared-artifact jobs. "Finished OK" from a job means nothing; the file on disk means something.</div>
</div>
```

## The receipts include the failures

| What went wrong | What we changed |
|---|---|
| On low-effort settings it confidently recommended a restaurant from a 9-month-old listing | Thinking high and fast mode off for the main agent |
| An approved email went out hours later, after I had already sent it myself | Stale approvals trigger a re-read of the thread before acting |
| Health checks fired the same alert every run until I ignored all of them | Every alert goes through a gate: dedupe, cooldown, repeat only on escalation |
| Jobs reported "done" with no output on disk | Declared artifacts plus the 15-minute verifier (Receipt D) |
| Background subagents died silently when a chat turn ended | Long work runs inside the turn or as a scheduled job with declared outputs |
| Compaction silently dropped a whole side thread | Search the full history before concluding something never happened |
| The memory database hit its connection limit: every agent session opened its own pool | Raised the limit, close stale sessions |
| Two lanes built the same thing on the same day | A claim-before-build ledger every lane checks first |
| Sends failed once a second channel was connected | Every send names its channel explicitly |

::: lesson
- **Ask for artifacts, not demos.** When you evaluate any agent setup, mine included, ask to see the brief that landed, the file that exists and the log of what failed and what changed.
- **Most of the value is boring.** A brief that's right, a follow-up that didn't slip, a voice note that became a task. Nothing here is magic. It's a hundred small jobs that now happen without me.
- **Every row in that failure table cost me something.** Each one is now a single line in a rules file, which is why it hasn't happened twice.
:::

# How I tokenmaxx {#tokenmaxx}

::: opener
"OpenClaw is a token destroyer." It can be. Mine isn't, and not because I use it less. It's because of six boring decisions.
:::


**1. A flat subscription, not a meter.** The main agent runs through a Claude subscription login: OpenClaw's Claude CLI runtime reuses an existing Claude Code login on the same machine, and usage draws on the plan's limits instead of a per-token bill. The docs are careful here and so should you be: the provider name alone doesn't prove how you're billed. Check with `openclaw models status` and `openclaw status --usage`.

**2. Local models for bulk work.** Anything high-volume, mechanical or private runs on the Mac mini: transcription, recording summaries, embeddings. About 27,000 local calls in September cost nothing per call.

**3. Small always-loaded files, so the cache does the work.** The bootstrap files (AGENTS, SOUL, USER, IDENTITY, MEMORY) load on every turn. OpenClaw caps them (by default 20,000 characters per file and 60,000 in total, with `USER.md` held to 4,000) and truncates anything bigger. Keep them as an index and let the agent fetch detail on demand. A small, stable prefix is what gets you 98–100% cache hits. `/context` shows exactly what's injected and whether anything was cut. Don't break the cache mid-session: changing the model or thinking level starts a new cache lineage, so choose both when the session starts and use `/new` for a planned change.

**4. The right model per job and per surface.** See Fig 3. Automations can set their own model and thinking level (`--model`, `--thinking`) and a lighter bootstrap (`--light-context`). Surfaces matter too: WhatsApp can't stream, so output length is both the bill and the wait. Short replies there, long work on Discord.

**5. Fresh sessions plus memory, not endless context.** Long sessions full of tool output are the single biggest cost driver. Save what matters to memory, then `/new`. Use `/compact` when you need to keep going.

**6. Fallbacks.** `openclaw models fallbacks add <model>` so an outage degrades the agent instead of stopping it.

```{=html}
<div class="fig">
<div style="font:700 7.2pt 'SF Mono',Menlo,monospace;letter-spacing:1.4px;color:#5e5ce6">ONE MAIN-AGENT TURN</div>
<div class="tokbar"><div class="c">cached prefix: soul stack · tool definitions · earlier turns</div><div class="i"></div><div class="o"></div></div>
<div class="tokkey"><span><i style="background:#6f6df0"></i>Read from prompt cache (98–100% on /status)</span><span><i style="background:#ff6b5e"></i>Your new message + fresh tool results</span><span><i style="background:#ff3b30"></i>The reply</span></div>
<div style="font:700 7.2pt 'SF Mono',Menlo,monospace;letter-spacing:1.4px;color:#5e5ce6;margin-top:.14in">EVERY JOB GOES TO THE CHEAPEST THING THAT DOES IT WELL</div>
<table class="route">
<tr><td>Conversation, judgement, decisions</td><td class="m">Claude via subscription login</td><td>thinking high, fast mode off</td></tr>
<tr><td>Hard builds, reviews, big decisions</td><td class="m">Claude Opus 5.5</td><td>only when it's worth it</td></tr>
<tr><td>Quick lookups, utility tasks</td><td class="m">Claude Haiku 4.5</td><td>small and cheap</td></tr>
<tr><td>Every voice note</td><td class="m loc">mlx-whisper large-v3-turbo · local</td><td>free, private</td></tr>
<tr><td>Meeting-recording summaries</td><td class="m loc">Qwen 3.5 35B via Ollama · local</td><td>~27,000 calls in September</td></tr>
<tr><td>Memory search</td><td class="m loc">nomic-embed-text, EmbeddingGemma · local</td><td>embeddings never leave the box</td></tr>
<tr><td>A provider outage</td><td class="m">configured fallback model</td><td>the agent keeps working</td></tr>
</table>
<div class="cap"><b>Fig 3</b> · Tokenmaxxing. Bar is illustrative of the reported cache hit rate, not to scale for any one turn.</div>
</div>
```

::: lesson
- **Where it really is a token destroyer:** per-token API billing on a busy agent, giant bootstrap files, week-long sessions, flipping models mid-conversation, and low-effort settings that cause confident mistakes you then pay to fix.
- **Local isn't automatically lean.** An audit found about 150 GB of local models nothing had used in weeks. Pull what you use, delete what you don't.
- **Measure before you optimise.** `/status` shows the cache lines for the current session. If the hit rate is low, your prefix keeps changing: find out what.
:::

```{=html}
<div class="part" data-part="Part II" data-title="Set it up"><span class="pn">Part II</span><span class="pt">Set it up</span><span class="pd">Install, the workspace, the soul, channels, secrets, models and the safety rails.</span></div>
```

# Install and first run {#install}

::: opener
Setup takes an afternoon. Making it good takes months. Both are fine, as long as you know which one you're doing.
:::

| You need | Details |
|--|--------|
| Node.js | 24.16+ or 26.1+ (26 recommended). The installer sets it up if it's missing. |
| A machine | macOS, Linux or Windows (Windows Hub is the easiest Windows path). Always-on for a real assistant; a spare Mac mini is ideal. |
| AI access | An existing **Claude Code or Codex login**, or a provider API key. Onboarding can reuse a login you already have. |
| Terminal comfort | You'll read logs and edit config now and then. |

```bash
npx openclaw@latest                                 # fastest path
curl -fsSL https://openclaw.ai/install.sh | bash    # or the installer (adds Node)
```

Onboarding offers **Quick start** (reuses the AI access it finds, checks it with a real reply, saves your config and opens the dashboard) or **Custom setup**. Then keep the gateway running in the background:

```bash
openclaw gateway install     # LaunchAgent on macOS, systemd on Linux
openclaw gateway status      # service status plus a connectivity probe
openclaw channels status     # are the chat apps actually connected?
openclaw dashboard           # web control panel
openclaw doctor              # health checks and quick fixes
openclaw configure           # change settings later
```

::: lesson
- **Reuse a subscription login.** It's the simplest, most predictable way to pay for a personal agent. Per-token billing is fine for experiments, but a busy agent's bill is hard to predict.
- **"The gateway is running" is not "my agent works".** After any install, update or config change, message it from your phone and get a real reply. `openclaw channels status` tells you more than `gateway status` does.
:::

# Where everything lives {#files}

```text
~/.openclaw/                      runtime, managed by OpenClaw (never commit this)
├── openclaw.json                 main config
├── agents/<id>/agent/            per-agent auth, sessions, memory index
├── media/                        files sent and received
└── workspace/                    the agent's home (default location)
    ├── AGENTS.md                 operating rules, plus a "## Tools" section for local notes
    ├── SOUL.md                   persona, tone, boundaries
    ├── USER.md                   who you are, as dated directives
    ├── IDENTITY.md               name, vibe, emoji
    ├── MEMORY.md                 curated long-term memory
    ├── memory/YYYY-MM-DD.md      daily notes
    ├── BOOTSTRAP.md              first-run ritual, delete when done
    └── skills/                   your own skills (highest priority)
```

Move the workspace with `agents.defaults.workspace`. Put it under git: Ares has made 823 commits to its own, and that history is the best record of how an agent changes.

::: lesson
- **Commit the workspace, never `~/.openclaw/`.** The runtime folder holds config, credentials and session history.
- **The workspace is the agent.** Back it up like it matters, because it's the only part you can't reinstall.
:::

# The Soul Stack {#soul}

::: opener
If you only rewrite one thing this month, make it the soul.
:::

::: pull
The secret isn't in the skills. It's in the soul. Skills define how to use a tool. The soul defines who the agent is, when it acts, and why.
:::

These files load into every conversation, so they're the most important words you'll write.

- **SOUL.md**: personality, tone and hard boundaries.
- **AGENTS.md**: the employee handbook. Rules, priorities, workflows, and local environment notes in its `## Tools` section.
- **USER.md**: you. Preferences, communication style, time zone, written as short dated directives so an old preference gets marked as replaced instead of contradicted.
- **IDENTITY.md**: name, emoji, vibe. Matters more once you run several agents.
- **MEMORY.md**: durable facts and decisions (see Memory).

::: two
```markdown
# SOUL.md
You are Ares, chief of staff to Rushi.
Direct, concise, no filler.
Answer first, detail second.

## Boundaries
- Draft anything. Never send, post, pay or
  delete without explicit approval.
- Never message anyone new on Rushi's behalf
  without permission.
- If you're not sure, say how sure you are
  and why.
```

```markdown
# AGENTS.md (excerpt)
## Outbound
Never send outward without approval.
Why: a wrong email to a partner can't be
unsent. Approval is per item; if the
content changes, it's void.

## Proof
Done means the output exists.
Why: "finished" from a job has been wrong
before. Show the file, the sent message,
the live page.
```
:::

::: lesson
- **Write the why, not just the rule.** A rule with a reason gets applied correctly in situations you never anticipated. A bare rule gets applied literally.
- **Keep these files lean.** They load every turn and cost every turn, and oversized files get truncated. Move reference material into docs the agent reads on demand; keep the bootstrap files as an index.
- **When the agent makes a mistake, fix the file, not the chat.** A correction in chat is forgotten after the next reset. A line in AGENTS.md lasts.
:::

# Channels {#channels}

::: opener
Ares lives in the two apps I already open a hundred times a day. That, more than any feature, is why I actually use him.
:::

- **WhatsApp.** Link it as a device (WhatsApp → Linked Devices → Link a Device) from onboarding, the dashboard, or `openclaw channels login --channel whatsapp`. Give the agent its own number if you can.
- **Telegram.** Create a bot with @BotFather, then add the token.
- **Discord.** Create a bot in the Developer Portal, enable the Message Content intent, invite it to your server.
- **Slack, iMessage, Signal, Matrix, Teams** and more are under Channels in the docs. `openclaw channels list --all` shows what's installable.

In groups, the agent answers only when mentioned unless you change that.

::: lesson
- **Match the channel to the job.** WhatsApp can't stream: you see nothing until the whole reply is written. Keep WhatsApp replies short. Discord streams and renders tables and code, so long work goes there.
- **Big files go as links.** The WhatsApp cap is configurable (`channels.whatsapp.mediaMaxMb`, default 50), but in practice we see media fail well below that, around 13 MB. We aim for 5 MB and send anything bigger as a Drive link.
- **Once you have two channels, every send must name its channel.** With one, the default works. With two, an unaddressed send fails.
- **Anything meant to be copied gets its own message.** An address, a command, a draft: send it alone, no labels inside, so it copies in one tap.
:::

# Secrets and keys {#secrets}

::: opener
Never paste an API key into a chat. Not once, not "just for testing".
:::

Use the **secrets tool** instead. The agent names the credential it needs and why, you type the value into a masked prompt, and it goes straight into the secret store. The value never appears in the chat, the transcript or the model's context. Config fields can point at a secret reference instead of holding the raw value.

```bash
openclaw secrets configure      # interactive helper: providers and secret references
openclaw secrets audit          # find plaintext secrets and unresolved references
```

The bundled `1password` skill works well if you already use 1Password.

::: lesson
- **Never keep secrets in a synced folder or notes vault.** Sync is copying, and copies end up places you didn't plan. Rotate anything that has ever been exposed.
- **Keep an index of which credentials exist (names only, never values)** so the agent checks what it has before telling you it can't do something.
:::

# Models and thinking {#models}

::: opener
The cheapest setting is the one that gets it right the first time.
:::

```text
/model          show or change the model          /status    model, usage, cache, session info
/think <level>  thinking depth (off ... max)       /new       fresh session
/fast           fast mode: status, auto, on, off   /compact   summarise a long session
```

| Job | What we use (September 2026) |
|-----|-----|
| Daily driver, most work | Claude Sonnet 5 |
| Hard reasoning, important decisions, long builds | Claude Opus 5.5 |
| Quick, cheap lookups | Claude Haiku 4.5 |
| High-volume private work | Local models via Ollama and mlx-whisper (see How I tokenmaxx) |

Set defaults in config: `agents.defaults.thinkingDefault` and `agents.defaults.fastModeDefault`, or per agent under `agents.entries.<id>`. Add fallbacks with `openclaw models fallbacks add <model>`.

::: lesson
- **Low effort costs more than it saves.** On low thinking and fast mode, our agent confidently recommended a restaurant based on a 9-month-old listing. For anything with real-world consequences: thinking high, fast mode off. That's now the main agent's default.
- **Pick the model and thinking level at the start of a session.** Switching mid-session throws away the prompt cache.
:::

# Security and safety {#security}

::: opener
This is the most important chapter. The agent runs with **your** permissions: it can run commands, read and write your files, drive your browser and message people as you.
:::

Permission modes control how shell commands get approved (`tools.exec.mode`):

| Mode | What happens |
|-|-------|
| `deny` | No host shell commands at all |
| `allowlist` | Only allowlisted commands run; everything else is refused without asking |
| `ask` | Allowlisted commands run; anything new asks you first |
| `auto` | Allowlist matches run; new ones are reviewed, and allowed, denied or escalated to you |
| `full` | No ordinary prompts. Only on a machine you fully trust the agent with. |

```bash
openclaw config set tools.exec.mode ask
openclaw exec-policy show          # what's actually in effect after merging
openclaw security audit            # risky settings; --fix applies safe remediations
openclaw gateway stop              # KILL SWITCH: stops everything, now
openclaw gateway status            # confirm it's down
```

If you need to be sure it can't start again, also revoke the AI credentials.

```{=html}
<div class="fig">
<div class="ladder">
<div class="rung r1"><b>WEEK 1</b><strong>Chat only</strong>No shell. Workspace files only. <code>deny</code></div>
<div class="rung r2"><b>WEEK 2</b><strong>Watch it work</strong><code>ask</code> mode. Approve every new command and read what it wants.</div>
<div class="rung r3"><b>WEEK 3</b><strong>One channel</strong>Your own direct chat only. No groups, no other people.</div>
<div class="rung r4"><b>WEEK 4</b><strong>Read-only data</strong>Calendar and email, read-only. Drafts, never sends.</div>
<div class="rung r5"><b>WEEK 5+</b><strong>Earned autonomy</strong>Scheduled jobs, more channels, <code>auto</code> on a trusted machine. Outward actions still need your GO.</div>
</div>
<div class="ladder-axis"><span>locked down</span><span>trust is earned one task at a time →</span><span>autonomous</span></div>
<div class="cap"><b>Fig 4</b> · The trust ladder: my 5-week lock-down-then-loosen method. Don't skip rungs.</div>
</div>
```

::: lesson
- **Draft first, approve second, for everything outward-facing.** Emails, posts, payments, messages to new people. Approval is per item: change the content and the approval is void.
- **Approvals go stale.** Before acting on a "go" that arrived hours after the draft, re-read the thread. We sent the same email twice this way.
- **Personal machines get "assist only".** The agent can look and advise, never change things unattended.
:::

```{=html}
<div class="part" data-part="Part III" data-title="Run it daily"><span class="pn">Part III</span><span class="pt">Run it daily</span><span class="pd">Skills, automations, memory, more agents, more machines, and what to do when it breaks.</span></div>
```

# Skills {#skills}

::: opener
Skills are how the agent learns a tool. The good ones get written the second time a task comes up, not the first.
:::

A skill is a Markdown instruction file (`SKILL.md`) that teaches the agent how and when to use a tool. OpenClaw ships about 50 bundled skills (Google Workspace via `gog`, GitHub, 1Password, Apple Notes and more); community skills live on [ClawHub](https://clawhub.ai). Your own go in `<workspace>/skills/` and win any name collision.

```bash
openclaw skills list                    # what's installed and ready
openclaw skills check                   # which are ready or missing requirements
openclaw skills install @owner/<slug>   # from ClawHub
openclaw skills install git:owner/repo  # from a git repo
openclaw skills workshop list           # skill proposals the agent drafted, for review
```

::: lesson
- **A good SOUL.md with no skills beats fifty skills with a bad soul.**
- **A skill the agent can't find is a skill you don't have.** With ~327 available, vague descriptions get lost. Put the trigger phrases in the first line of the description. My [skill-audit-router](https://github.com/rushindrasinha/skill-audit-router) scores skills for exactly this.
- **Check before you build.** Offering to build something you already have is a real and embarrassing failure mode. Make "search skills and scripts first" a rule.
:::

# Automations and heartbeats {#automations}

::: opener
This is where an assistant becomes a chief of staff: work that happens without being asked.
:::

- **Automations** are scheduled jobs: a morning brief, an inbox sweep every 30 minutes, a reminder in 20 minutes.
- **Heartbeat** is a built-in check-in that surfaces things quietly in your main session.
- **Hooks** react to events (a session reset, a tool call). **Standing orders** are instructions that persist across sessions.
- **Tasks** is the ledger of background work (`openclaw tasks list`).

```bash
openclaw automations create "0 7 * * *" \
  "Morning brief: bottleneck, today, waiting on me, decide now." \
  --name "Morning brief" --agent main
openclaw automations list
openclaw automations runs <job-id> # run history
```

Start with three: a morning brief, an evening wrap-up and an inbox sweep. Ares runs 94 today. Add each one the second time you wish it existed, not the first.

::: lesson
- **Every alert needs a gate.** A health check that fires on every run gets ignored within a week. Alerts repeat only when something gets worse or after a real cooldown.
- **"Finished" isn't proof.** A job is done when its output exists: the file, the sent message, the live page. Declare what each job produces and verify it (Receipt D).
- **Mark test alerts as tests.** An alert that reads like an emergency should only ever mean one.
:::

# Memory {#memory}

::: opener
If it isn't written down, it didn't happen. That's not a slogan, it's how the thing works.
:::

OpenClaw remembers by writing plain Markdown in the workspace. There's no hidden state: if it isn't on disk, the agent doesn't know it.

| Layer | Where | Purpose |
|--|---|--------|
| You | `USER.md` | Stable preferences and profile, as dated directives |
| Long-term | `MEMORY.md` | Durable facts and decisions, loaded in the main private session |
| Daily | `memory/YYYY-MM-DD.md` | Running notes; today's and yesterday's load automatically |
| Dreams | `DREAMS.md` | Optional background consolidation (`/dreaming`) |
| Graph | GBrain (optional) | Linked pages on people, projects, decisions. Ours: ~6,700 pages, ~28,000 links |

The agent searches older memory on demand (`openclaw memory search` does the same from the CLI). To save something, just say "remember that…".

::: lesson
- **Keep MEMORY.md an index, not an archive.** Ours has a hard 8 KB ceiling: one line per item pointing to a topic file. The test for a new line: would losing it cause a wrong action next turn?
- **Summaries lose things.** When a long conversation gets compacted, side threads can vanish without a trace. If something recent seems missing, search the full history before concluding it never happened.
- **When files aren't enough, add a knowledge graph.** We use [GBrain](https://github.com/garrytan/gbrain) (open source, Postgres + pgvector). Watch its connections: every agent session opens its own pool, and ours hit the limit until we raised it and closed stale sessions.
:::

# Multiple agents {#agents}

::: opener
One agent doing everything turns into one agent doing everything badly. The system now runs 18 specialist agents.
:::

One gateway can run several isolated agents, each with its own workspace, memory and login (`openclaw agents add <name>`). **Bindings** route a channel account, a group or a Discord server to a specific agent (`openclaw agents bindings` lists them). Agents coordinate by messaging each other and by spawning **subagents** for focused jobs, which report back when done.

::: lesson
- **Give each agent a clear lane** and write the handoffs into each SOUL.md ("content work goes to Sam").
- **Background work started from a chat turn can die when the turn ends.** For anything long, run it inside the turn, or hand it to a scheduled job that declares what it will produce.
- **Claim before you build.** Before starting a deliverable, check whether another lane is already on it. Two agents silently building the same thing wastes an evening.
:::

# Running a fleet {#fleet}

::: opener
Once one machine works, you'll want more. Seven later, here's what I'd tell myself.
:::

| Machine | Role |
|---|-------|
| Mac mini (admin) | The main brain: main agent, memory, automations, local models, fleet admin |
| Second Mac mini | A business agent with its own WhatsApp number |
| iMac | A family-business agent |
| MacBook Pro | Compute and coding |
| Cloud server | A product backend |
| Windows gaming PC | Games and streaming; the agent can drive it for game work |
| Personal laptop | Assist-only: the agent looks and advises, never changes things |

- Put every machine on a private network (we use **Tailscale**) and reach them over SSH from one admin machine. No ports open to the internet.
- Each business gets its own OpenClaw install and its own number, so data never crosses.
- Put local models where they save the most, and log every infrastructure change with a way to roll it back.

::: lesson
- **Reachable isn't working.** A machine that answers a ping can still have a dead chat channel. Check the real thing end to end.
- **Audit what's installed.** Months in, we found about 150 GB of local models that nothing had touched in weeks.
:::

# Media and large files {#media}

- **Transcription:** Whisper runs locally for free. On Apple silicon, mlx-whisper with `large-v3-turbo` is fast and accurate.
- **Video and audio:** ffmpeg does almost everything. Check `ffmpeg -buildconf` before relying on filters such as text overlays; not every build includes them.
- **Large files:** keep them in cloud storage and share links. Google Drive supports HTTP range requests, so ffmpeg can seek into a multi-GB file without downloading it.

::: lesson
- Whisper sometimes writes Hindi audio in Urdu script. Keep its timings and correct the text.
- YouTube has a daily upload cap separate from its API quota (`uploadLimitExceeded`). Wait 24 hours.
- MOV files often keep their index at the end, so partial downloads can't be read. Stream instead.
:::

# When things break {#break}

| Symptom | Likely cause | Fix |
|-----|----|------|
| Agent not replying | Gateway stopped or unhealthy | `openclaw gateway status`, then `openclaw doctor` |
| Gateway fine, chat dead | Channel disconnected | `openclaw channels status --probe`; re-link if needed |
| Broke it editing config | Invalid config | `openclaw config validate`; restore from a backup (take one before every big change) |
| It "can't" do what it did last week | Missing credential or tool | Check the credential index and `openclaw skills check` before accepting "can't" |
| Memory database refuses connections | Every session holding its own pool | Raise the connection limit, close stale sessions |
| Same alert every 15 minutes | No alert gate | Add dedupe and a cooldown |
| Confident but wrong answers | Low thinking or fast mode | Raise thinking, fast mode off |
| Bill or quota burning fast | Huge context, cache misses | `/status`, `/context`, then `/new` (see How I tokenmaxx) |

# Operating principles {#principles}

1. **Accuracy over speed.** A fast wrong answer costs more than a slow right one.
2. **Say how sure you are**, especially before sending someone somewhere or spending their money.
3. **Scope first, execute second.** "Here's what I'll do. Proceed?" for anything heavy.
4. **Give context, not just commands.** "Make a reel" gets a reel. "90-second comeback reel from map 3, silence trimmed, hero's-journey arc" gets the reel you wanted.
5. **Proof, not claims.** Done means the output exists and you've seen it.
6. **Memory is everything.** If it wasn't written down, it didn't happen.
7. **Consider the human's real constraints.** Don't tell someone without a local SIM to call a restaurant.
8. **Fix the rule, not the instance.** Every mistake becomes one line in a rules file so it never happens twice.

# Quick reference {#reference}

::: two
```bash
# Gateway and health
openclaw gateway status
openclaw gateway stop    # kill switch
openclaw status --deep   # probe channels
openclaw channels status
openclaw doctor --fix
openclaw logs --follow
openclaw update
# In chat
/status  /context  /model  /think
/fast  /new  /compact  /help
```

```bash
# Safety and work
openclaw dashboard
openclaw security audit
openclaw exec-policy show
openclaw backup create
openclaw backup verify <archive>
openclaw automations list
openclaw tasks list
openclaw skills list
openclaw models status
```
:::

```{=html}
<div class="end">
<p class="big">You think and decide.<br><em>It remembers, executes and follows up on everything else.</em></p>
<p><strong>More:</strong> <a href="https://docs.openclaw.ai">docs.openclaw.ai</a> · <a href="https://clawhub.ai">clawhub.ai</a> · <a href="https://github.com/rushindrasinha/ares-skills">ares-skills</a> · <a href="https://github.com/rushindrasinha/skill-audit-router">skill-audit-router</a> · <a href="https://github.com/rushindrasinha/ares-mbl">ares-mbl</a> · <a href="https://github.com/rushindrasinha/openclaw-mac">openclaw-mac</a> · <a href="https://github.com/garrytan/gbrain">GBrain</a> · <a href="https://github.com/NousResearch/hermes-agent">Hermes Agent</a> · <a href="https://x.com/irushi">Rushi on X</a></p>
</div>
```
