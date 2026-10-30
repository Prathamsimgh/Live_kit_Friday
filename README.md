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

## run it

coming soon — docker-compose setup is being ironed out.
