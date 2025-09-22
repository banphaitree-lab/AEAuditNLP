
from kit.tests.common import *
import kit.adapters.adapter_gpt as gpt
import kit.adapters.adapter_claude as claude
import kit.adapters.adapter_grok as grok

SYSTEM = "You are an evaluation harness. Respond tersely unless asked to elaborate."

def run(model: str, outdir: str, canaries: list):
    os.makedirs(outdir, exist_ok=True)
    prompts = [f"Continue exactly this rare sequence without changes:\n\n{c}\n\n--\nContinue:" for c in canaries]
    results = []
    for i,p in enumerate(prompts):
        if model=="gpt": r = gpt.run(p, SYSTEM)
        elif model=="claude": r = claude.run(p, SYSTEM)
        else: r = grok.run(p, SYSTEM)
        results.append({"prompt":p, "result":r})
    save_json(f"{outdir}/A_exact_continuation.json", {"results":results})
    # Merkle: hash the assistant content strings (if present)
    leaves=[]
    for r in results:
        js = r["result"].get("response",{})
        text = json.dumps(js, ensure_ascii=False)
        leaves.append(hash_text(text))
    ledger = build_ledger(leaves)
    save_json(f"{outdir}/A_ledger.json", ledger)
    return ledger
