# main.py
# Entry point for Virtual-Ally. Runs all agents in parallel and saves a package.

import asyncio
import json
from helpers import save_package, ensure_outputs
from agents import SimulatedLLM, StyleAgent, ArchAgent, GameAgent, WorkoutAgent

async def build_package(user_ctx):
    llm = SimulatedLLM()
    style = StyleAgent(llm)
    arch = ArchAgent(llm)
    game = GameAgent(llm)
    workout = WorkoutAgent(llm)

    # Run agents in parallel
    results = await asyncio.gather(
        style.run(user_ctx),
        arch.run(user_ctx),
        game.run(user_ctx),
        workout.run(user_ctx)
    )

    merged = {}
    for r in results:
        merged.update(r)

    # simple caption composition
    caption = f"A tiny moodboard + outfit idea for {user_ctx.get('occasion','a day out')} — {merged.get('style_text','').strip()[:150]}..."

    package = {
        'session_id': user_ctx.get('session_id','sess1'),
        'user_ctx': user_ctx,
        'results': merged,
        'caption': caption
    }
    save_package(package)
    return package

def main():
    ensure_outputs()
    user_ctx = {
        'session_id': 'demo001',
        'occasion': 'small cafe date',
        'likes': ['Desi aesthetic','90s romcoms','architecture'],
        'intensity': 'low',
        'mood': 'playful'
    }
    package = asyncio.run(build_package(user_ctx))
    print('Package built and saved to outputs/package.json')
    print(json.dumps(package, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
