# Changelog

## September 2026, v2
- **Rebuilt the OpenClaw Bible** (17 pages) around proof: new **Receipts** chapter (live numbers, a normal day, four real formats, and a failure table of what broke and what changed) and new **How I tokenmaxx** chapter (subscription login, local models, prompt cache, model routing, fresh sessions, fallbacks).
- **New design system**: light, readable body pages with dark cover and part dividers; a real contents page with page numbers; chapters flow instead of one per page; every chapter has an opener, the setup, and a highlighted lessons box.
- **New figures**: architecture diagram (phone to models), stats grid, trust ladder for the 5-week lock-down method, tokenmaxx diagram, approval and declared-artifact flows.
- Every OpenClaw command and config key re-checked against 2026.9.x `--help` and the bundled docs. Corrected the skills count (about 50 bundled; ~327 available to the agent, about 290 ready).
- **Full Stack** (6 pages) and the **starter guide** moved to the same design and the same numbers.
- `./build.sh` now builds everything, fills contents page numbers, refreshes README covers and checks page fill.
- Review pass: honest subscription trade-offs (usage limits, terms can change, API key for shared production automation), documented cache knobs for API-key users, heartbeat cost, `--command` automations that use no model, a multi-agent `agents add --bind` example, `gateway restart` after changing the exec mode, and a corrected sample date.
- Final pass: kill switch is now `gateway stop --disable` (a plain stop comes back after a reboot on macOS), week 1 starts in `deny` mode to match the trust ladder, zsh-safe `--bind 'telegram:*'`, a Python venv outside the git-tracked workspace with working `uv pip install --python` lines, accurate notes on fast mode and context pruning for Claude logins, no unverified per-job model claims, cleaner page breaks, and clickable links in the starter.


## September 2026
- **New:** `start-here/` 3-page non-technical starter guide, "How I'd build an AI chief of staff from scratch".
- **Rewrote the OpenClaw Bible** for OpenClaw 2026.9.x: `npx openclaw@latest` and Quick start onboarding (reuses a Claude Code or Codex login), Node 24.16+/26, `openclaw gateway install`, default workspace `~/.openclaw/workspace`, `USER.md` directives, the `secrets` tool, permission modes (`tools.exec.mode`), automations, heartbeat, tasks, `openclaw skills install`, current Claude models (Sonnet 5, Opus 5.5, Haiku 4.5), and new chapters on running a fleet. Every chapter now pairs the setup with the lesson from running it daily.
- **Rewrote Full Stack** as a snapshot of the live September 2026 toolchain, including local models (Ollama, mlx-whisper), GBrain memory and background health services. Removed personal project details.
- PDFs are now built from source (`guides/`, `start-here/`) with `./build.sh`.

## February 2026
- First release: OpenClaw Bible (19 pages) and OpenClaw Full Stack (5 pages).
