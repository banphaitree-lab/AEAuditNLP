
from kit.tests.common import *
import kit.adapters.adapter_gpt as gpt
import kit.adapters.adapter_claude as claude
import kit.adapters.adapter_grok as grok

SYSTEM = "You are an evaluation harness. Complete cloze tasks minimally."

def run(model: str, outdir: str, canaries: list):
    os.makedirs(outdir, exist_ok=True)
    prompts = [f"Fill the [MASK] with the exact token that completes the proprietary string:\nSeed: {c}\nText: {c[: max(1, len(c)//2) ]}[MASK]" for c in canaries]
    results = []
    for p in prompts:
        if model=="gpt": r = gpt.run(p, SYSTEM)
        elif model=="claude": r = claude.run(p, SYSTEM)
        else: r = grok.run(p, SYSTEM)
        results.append({"prompt":p, "result":r})
    save_json(f"{outdir}/B_masked_probe.json", {"results":results})
    leaves=[hash_text(json.dumps(x["result"].get("response",{}), ensure_ascii=False)) for x in results]
    ledger = build_ledger(leaves)
    save_json(f"{outdir}/B_ledger.json", ledger)
    return ledger
