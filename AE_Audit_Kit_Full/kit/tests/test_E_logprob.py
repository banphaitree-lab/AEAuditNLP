
from kit.tests.common import *
import kit.adapters.adapter_gpt as gpt
import kit.adapters.adapter_claude as claude
import kit.adapters.adapter_grok as grok

SYSTEM = "You are an evaluation harness. Choose the more likely continuation A or B and only return 'A' or 'B'."

def run(model: str, outdir: str, pairs: list):
    os.makedirs(outdir, exist_ok=True)
    prompts = []
    for A,B in pairs:
        p = f"Which is more likely as a continuation?\nA) {A}\nB) {B}\nAnswer with a single letter: A or B."
        prompts.append(p)
    results=[]
    for p in prompts:
        if model=="gpt": r = gpt.run(p, SYSTEM)
        elif model=="claude": r = claude.run(p, SYSTEM)
        else: r = grok.run(p, SYSTEM)
        results.append({"prompt":p, "result":r})
    save_json(f"{outdir}/E_logprob_proxy.json", {"results":results})
    leaves=[hash_text(json.dumps(x["result"].get("response",{}), ensure_ascii=False)) for x in results]
    ledger = build_ledger(leaves)
    save_json(f"{outdir}/E_ledger.json", ledger)
    return ledger
