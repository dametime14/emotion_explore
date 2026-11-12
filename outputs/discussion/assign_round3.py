#!/usr/bin/env python3
"""Stage 3 Round 3 reviewer assignment (prompts/stage3 2절 1번).

Each of the 10 research agents reviews exactly 3 proposals made by OTHER agents.
Each selected proposal gets 2 reviewers from different fields. Reviewers are
neither the sender nor a named receiver (the receiver already responds to it).
The 15 proposals are chosen by the Coordinator (SELECTED, with reasons in
outputs/discussion/round3_assignment.md); the reviewer draw is random with a fixed seed.

Usage: python3 -I outputs/discussion/assign_round3.py
"""
import csv
import os
import random

SEED = 20261114
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AGENTS = ["emotion-theory", "vision-decoding", "encoding-foundation", "multimodal-dynamics",
          "frontier-ai", "geometry-info", "systems-neuro", "generative-counterfactual",
          "llm-semantics", "brain-inspired"]
FIELD = {"emotion-theory": "theory", "vision-decoding": "brain-ml", "encoding-foundation": "brain-ml",
         "multimodal-dynamics": "multimodal", "frontier-ai": "ai", "geometry-info": "math",
         "systems-neuro": "systems", "generative-counterfactual": "generative",
         "llm-semantics": "language", "brain-inspired": "computation"}
SELECTED = os.environ.get("R3_SELECTED", "").split()


def main():
    idx = {r["proposal_id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "outputs/discussion/proposals_index.csv"), encoding="utf-8"))}
    props = [idx[p] for p in SELECTED]
    rng = random.Random(SEED)
    for attempt in range(200000):
        load = {a: 0 for a in AGENTS}
        out = []
        ok = True
        order = props[:]
        rng.shuffle(order)
        for p in order:
            banned = {p["from"]} | set(filter(None, p["to"].split("; ")))
            cands = [a for a in AGENTS if a not in banned and load[a] < 3]
            rng.shuffle(cands)
            cands.sort(key=lambda a: load[a])
            pair = None
            for i in range(len(cands)):
                for j in range(i + 1, len(cands)):
                    if FIELD[cands[i]] != FIELD[cands[j]]:
                        pair = (cands[i], cands[j])
                        break
                if pair:
                    break
            if not pair:
                ok = False
                break
            for a in pair:
                load[a] += 1
            out.append((p["proposal_id"], p["from"], p["to"], pair))
        if ok and all(v == 3 for v in load.values()):
            break
    else:
        raise SystemExit("no valid assignment")
    out.sort(key=lambda x: SELECTED.index(x[0]))
    with open(os.path.join(ROOT, "outputs/discussion/round3_assignment.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["proposal_id", "from", "to", "reviewer_1", "reviewer_2"])
        for pid, frm, to, (r1, r2) in out:
            w.writerow([pid, frm, to, r1, r2])
    print(f"seed={SEED} attempts={attempt + 1}")
    by_agent = {a: [] for a in AGENTS}
    for pid, frm, to, pair in out:
        print(pid, frm, "->", to, "| reviewers:", pair)
        for a in pair:
            by_agent[a].append(pid)
    for a, ps in by_agent.items():
        print(a, ps)


if __name__ == "__main__":
    main()
