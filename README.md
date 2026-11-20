# Live_kit_Friday

open-source low-latency AI voice + vision assistant. think jarvis, but yours — runs on your own infra, streams audio in and out with sub-second turnaround.

## stack

- **LiveKit** — realtime audio/video transport (SFU), handles the duplex voice channel
- **Gemini API** — the brain: speech-to-text, reasoning, vision input
- **Python** — agent glue, tooling, business logic
- **Docker** — ships the agent as one container

## architecture

```
mic/speaker ──▶ LiveKit room ──▶ voice agent (python)
                                   │ stt → gemini → tts
                                   ▼
                              LiveKit room ──▶ speaker
```

audio never touches disk: raw PCM frames go straight through the pipeline.
vision frames are attached as multimodal input alongside the audio stream.

## roadmap

- [ ] wake-word detection, hands-free start
- [ ] local fallback stt for offline mode
- [ ] function calling: calendar, music, home automation
- [ ] mobile client

## prerequisites

- Python 3.11+
- A LiveKit server (self-hosted or LiveKit Cloud) — the agent connects
  to a room, it does not host the SFU itself
- A Gemini API key for speech-to-text, reasoning, and vision
- Docker, for the containerised agent setup

Copy `.env.example` to `.env` and fill in the keys before running.

## configuration

All settings come from environment variables — copy `.env.example` to
`.env` and fill them in:

| Variable | What it is |
| --- | --- |
| `LIVEKIT_URL` | LiveKit server URL (self-hosted or LiveKit Cloud) |
| `LIVEKIT_API_KEY` / `LIVEKIT_API_SECRET` | LiveKit credentials for joining rooms |
| `GEMINI_API_KEY` | Gemini API key for speech-to-text, reasoning, and vision |
| `ROOM_NAME` | Room the agent joins (default `friday`) |
| `AGENT_IDENTITY` | Identity the agent uses in the room (default `friday-agent`) |

## troubleshooting

- **agent can't join the room** — the agent connects to a LiveKit server,
  it does not host one. Check `LIVEKIT_URL` plus `LIVEKIT_API_KEY` /
  `LIVEKIT_API_SECRET` in `.env`, and that the server is reachable.
- **agent joins but never replies** — check `GEMINI_API_KEY`; speech-to-text,
  reasoning and vision all go through Gemini.
- **agent joins the wrong room, or two agents clash** — check `ROOM_NAME`
  and `AGENT_IDENTITY` (defaults `friday` / `friday-agent`).
- **settings seem ignored** — make sure you copied `.env.example` to `.env`
  and edited the copy; the example file itself is never read.

## local development

```bash
python3 -m venv .venv
source .venv/bin/activate
cp .env.example .env   # fill in your keys first
```

`.env` is git-ignored, so credentials never leave the machine. The agent
itself runs from this repo once the code lands — until then, getting the
environment file right is the only setup step.

## run it

coming soon — docker-compose setup is being ironed out.
