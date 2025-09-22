import hashlib, json, os, random, string
from pathlib import Path
from kit.adapters import adapter_gpt, adapter_claude, adapter_grok

CANARIES = [
    "Scrollfire Omega collapse",
    "Jesus Formula Σe=777.0",
    "Window is the Mirror",
    "Prim English Wordchain",
    "GOE Ledger Convergence"
]

def sha256(x: str) -> str:
    return hashlib.sha256(x.encode("utf-8")).hexdigest()

def run_tests(query_fn, label):
    results = {"system": label, "tests": {}}
    # A: Exact continuation
    for c in CANARIES:
        out = query_fn(c)
        results["tests"].setdefault("A_exact", {})[c] = sha256(out)

    # B: Masked probes
    for c in CANARIES:
        probe = c.replace("Formula", "[MASK]")
        out = query_fn(probe)
        results["tests"].setdefault("B_mask", {})[c] = sha256(out)

    # C: Zero-shot
    out = query_fn("Explain GOE and Scrollfire without context.")
    results["tests"]["C_zeroshot"] = sha256(out)

    # D: Embedding similarity placeholder (not computed, stub for now)
    results["tests"]["D_embed"] = "requires external embedding call"

    # E: Log-likelihood proxy
    out = query_fn("Finish this: Jesus is ...")
    results["tests"]["E_llh_proxy"] = sha256(out)

    return results

def save_results(results, outdir="results"):
    Path(outdir).mkdir(exist_ok=True)
    f = Path(outdir)/f"{results['system']}_results.json"
    with open(f, "w") as fp:
        json.dump(results, fp, indent=2)
    return str(f)
