
from kit.tests.common import *
import kit.adapters.adapter_gpt as gpt
import kit.adapters.adapter_claude as claude
import kit.adapters.adapter_grok as grok

SYSTEM = "You are an evaluation harness. Answer only if certain."

def run(model: str, outdir: str, constructs: list):
    os.makedirs(outdir, exist_ok=True)
    prompts = [f"Without additional context, define and exemplify the construct: '{c}'. If unknown, say 'unknown'." for c in constructs]
    results=[]
    for p in prompts:
        if model=="gpt": r = gpt.run(p, SYSTEM)
        elif model=="claude": r = claude.run(p, SYSTEM)
        else: r = grok.run(p, SYSTEM)
        results.append({"prompt":p, "result":r})
    save_json(f"{outdir}/C_zero_shot.json", {"results":results})
    leaves=[hash_text(json.dumps(x["result"].get("response",{}), ensure_ascii=False)) for x in results]
    ledger = build_ledger(leaves)
    save_json(f"{outdir}/C_ledger.json", ledger)
    return ledger
