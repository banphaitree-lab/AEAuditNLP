
import os, json, time, hashlib, numpy as np
from typing import List, Dict
from kit.utils.merkle import pairwise_merkle, sorted_concat_merkle

def hash_text(txt: str) -> str:
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()

def load_canaries(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(path: str, obj: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)

def build_ledger(leaves: List[str]) -> Dict:
    return {
        "pairwise_root": pairwise_merkle(leaves),
        "sorted_concat_root": sorted_concat_merkle(leaves),
        "leaf_count": len(leaves),
    }
