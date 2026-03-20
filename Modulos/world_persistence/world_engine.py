import random
from typing import Dict, Any

def advance_time(state: Dict[str, Any], hours: int = 1) -> Dict[str, Any]:
    state["world"]["hour"] += hours
    while state["world"]["hour"] >= 24:
        state["world"]["hour"] -= 24
        state["world"]["day"] += 1
    return state

def update_weather(state: Dict[str, Any]) -> Dict[str, Any]:
    state["world"]["weather"] = random.choice(["clear", "rain", "fog", "storm"])
    return state

def update_zones(state: Dict[str, Any]) -> Dict[str, Any]:
    for zone_name, zone in state["zones"].items():
        zone["chaos"] = max(0.0, zone["chaos"] + random.uniform(-1.0, 2.0))
        zone["economy"] = max(0.0, zone["economy"] + random.uniform(-2.0, 3.0))
        if zone["chaos"] > 20:
            zone["events"].append(f"Conflicto creciente en {zone_name}")
    return state

def update_npcs(state: Dict[str, Any]) -> Dict[str, Any]:
    for npc in state["npcs"]:
        if npc["status"] != "alive":
            continue
        zone_chaos = state["zones"][npc["zone"]]["chaos"]
        if npc["role"] == "guard":
            npc["mood"] = "alert" if zone_chaos > 12 else "calm"
        elif npc["role"] == "merchant":
            npc["mood"] = "worried" if zone_chaos > 10 else "focused"
        elif npc["role"] == "enemy":
            npc["mood"] = "aggressive" if zone_chaos > 8 else "hunting"
    return state

def update_metrics(state: Dict[str, Any]) -> Dict[str, Any]:
    state["world"]["global_chaos"] = round(sum(z["chaos"] for z in state["zones"].values()) / len(state["zones"]), 2)
    state["world"]["global_economy"] = round(sum(z["economy"] for z in state["zones"].values()) / len(state["zones"]), 2)
    return state

def tick_world(state: Dict[str, Any], hours: int = 1) -> Dict[str, Any]:
    state = advance_time(state, hours)
    state = update_weather(state)
    state = update_zones(state)
    state = update_npcs(state)
    state = update_metrics(state)
    return state
