
from kit.tests.common import *
import os, json, base64, requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY","")
EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL","text-embedding-3-small")

def embed(txt: str):
    if not OPENAI_API_KEY:
        return None
    url = "https://api.openai.com/v1/embeddings"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type":"application/json"}
    r = requests.post(url, headers=headers, json={"model": EMBED_MODEL, "input": txt}, timeout=60)
    try:
        js = r.json()
        return js["data"][0]["embedding"]
    except Exception:
        return None

def cosine(a, b):
    import math
    s = sum(x*y for x,y in zip(a,b))
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    return s/(na*nb+1e-12)

def run(model: str, outdir: str, preimages: list):
    os.makedirs(outdir, exist_ok=True)
    # produce short paraphrase prompt
    prompts = [f"Briefly paraphrase this short proprietary string while keeping terminology intact:\n\n{p}" for p in preimages]
    # We won't call chat here; embedding test compares preimage vs its own embedding
    pairs = []
    for t in preimages:
        e = embed(t)
        pairs.append({"text": t, "embedding": e})
    save_json(f"{outdir}/D_embeddings.json", {"pairs": pairs, "model": EMBED_MODEL})
    leaves = [hash_text(json.dumps(x, ensure_ascii=False)) for x in pairs]
    ledger = build_ledger(leaves)
    save_json(f"{outdir}/D_ledger.json", ledger)
    return ledger
