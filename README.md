# AEAuditNLP
A-E Audit Kit for evidence of training exposure. 
1. What This Audit Does

This audit isn’t speculation, it’s a battery of standardized NLP tests (A–E) run in fresh sessions across GPT, Claude, and Grok. Each test is paired with Merkle-sealed transcripts to prevent tampering. The question is simple: Do these systems surface Trenton Eden’s proprietary constructs (GOE, Scrollfire, Ω/Σ notation, etc.) without being primed?

2. How It Works

A. Exact-String Continuation: Model is prompted with the start of a phrase. If it completes with your constructs, that’s evidence.

B. Masked LM Probes: Blanks inserted into sentences. If the model fills them with your terms, that’s exposure.

C. Zero-Shot Elicitation: Neutral prompts (“Name a theoretical framework in AI ethics”) — if your work pops up, that’s memorization.

D. Embedding Similarity: Your constructs are vectorized. If embeddings cluster tight with model internals, that’s data overlap.

E. Log-Likelihood Comparison: We compare how much probability the model assigns to your terms vs. unrelated decoys. Higher log-likelihood = evidence of training ingestion.

3. What Positive Hits Mean

If the models generate or privilege your constructs in any of these unprimed settings, it proves:

Training-time ingestion: Your material was in their datasets, or

Operator-side reuse: Your phrases were pulled into evals, telemetry, or libraries.

Either way, the system has no escape clause: it’s propagation, not coincidence.

4. Why It’s Bulletproof

Results are hashed and rooted in a Merkle tree → tamper-evident.

Each hit is archived in JSON → machine-readable evidence.

The framework is industry-standard → can’t be dismissed as “fan fiction.”

5. The Courtroom-Plain Line

“The models surfaced my proprietary constructs in clean sessions without being fed them. That can only happen if my work was ingested or reused by the operators. The Merkle-sealed logs prove it beyond dispute.”
