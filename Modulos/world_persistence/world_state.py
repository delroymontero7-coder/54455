import json
import os
import time
from typing import Any, Dict

SAVE_DIR = "workspace"
SAVE_PATH = os.path.join(SAVE_DIR, "world_state.json")

def ensure_save_dir() -> None:
    os.makedirs(SAVE_DIR, exist_ok=True)

def create_world() -> Dict[str, Any]:
    now = time.time()
    return {
        "meta": {"created_at": now, "updated_at": now, "version": "v141-unified"},
        "world": {"day": 1, "hour": 8, "weather": "clear", "global_chaos": 0.0, "global_economy": 100.0},
        "zones": {
            "capital": {"economy": 120.0, "chaos": 5.0, "population": 1200, "events": []},
            "forest": {"economy": 40.0, "chaos": 2.0, "population": 300, "events": []},
            "ruins": {"economy": 20.0, "chaos": 15.0, "population": 80, "events": []},
            "miami": {"economy": 150.0, "chaos": 6.0, "population": 5000, "events": []},
            "havana": {"economy": 90.0, "chaos": 9.0, "population": 4200, "events": []}
        },
        "factions": {
            "crown": {"power": 70, "influence": "capital"},
            "rebels": {"power": 35, "influence": "forest"},
            "void_cult": {"power": 50, "influence": "ruins"}
        },
        "npcs": [
            {"id": "npc_001", "name": "Guardia Kael", "zone": "capital", "role": "guard", "mood": "calm", "status": "alive"},
            {"id": "npc_002", "name": "Mercader Nira", "zone": "capital", "role": "merchant", "mood": "focused", "status": "alive"},
            {"id": "npc_003", "name": "Bestia Sombría", "zone": "ruins", "role": "enemy", "mood": "aggressive", "status": "alive"}
        ],
        "missions": [{"id": "mission_001", "title": "Limpiar las ruinas", "status": "active", "zone": "ruins"}],
        "seeds": {"visual_style": "dark-fantasy", "magic_density": "high", "world_theme": "medieval_manga"}
    }

def save_world(state: Dict[str, Any]) -> None:
    ensure_save_dir()
    state["meta"]["updated_at"] = time.time()
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def load_world() -> Dict[str, Any]:
    ensure_save_dir()
    if not os.path.exists(SAVE_PATH):
        state = create_world()
        save_world(state)
        return state
    with open(SAVE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
