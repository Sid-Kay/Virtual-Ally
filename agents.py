# agents.py
# Defines the small agents used in the Virtual-Ally system.
# Each agent is intentionally simple and can be replaced with a real LLM call.

import asyncio
from config import OPENAI_API_KEY
from tools import create_placeholder_image, extract_palette_from_text

class SimulatedLLM:
    def __init__(self):
        self.real = bool(OPENAI_API_KEY)

    async def generate(self, prompt: str):
        # If a real key is present, user can implement a real API call here.
        # For safety this repo uses a simulated response by default.
        if self.real:
            return "[REAL LLM] Replace this stub with your own API call using OPENAI_API_KEY from env."
        # Simulated short response to keep outputs readable
        return f"[SIM] Response for prompt (truncated): {prompt[:200]}"

class StyleAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, ctx):
        prompt = f"Style prompt for: {ctx.get('occasion', 'casual')}"
        out = await self.llm.generate(prompt)
        return {'style_text': out}

class ArchAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, ctx):
        prompt = f"Architecture prompt for: {ctx.get('occasion', 'casual')}"
        out = await self.llm.generate(prompt)
        images = [create_placeholder_image('mood1'), create_placeholder_image('mood2')]
        palette = extract_palette_from_text(out)
        return {'arch_text': out, 'images': images, 'palette': palette}

class GameAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, ctx):
        prompt = f"Game prompt for mood: {ctx.get('mood','playful')}"
        out = await self.llm.generate(prompt)
        return {'game_text': out}

class WorkoutAgent:
    def __init__(self, llm):
        self.llm = llm

    async def run(self, ctx):
        # Simple canned workout based on intensity
        intensity = ctx.get('intensity','low')
        if intensity == 'low':
            plan = ['5 min warmup', '3x 30s jumping jacks', '3x 10 squats', '5 min cool down']
        else:
            plan = ['5 min warmup', '4x 45s burpees', '4x 15 lunges', '5 min cool down']
        return {'workout_plan': plan}
