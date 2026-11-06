"""Fill plan.sfx from a sound cue sheet. Idempotent: plan.sfx is always rebuilt from the cues.

Usage: python cues_to_plan.py --project <kallaway dir> [--cues cues_yield.json]
Cue format: references/audio.md.
"""
import argparse
import json
import pathlib
import sys


def to_plan_item(cue: dict) -> dict:
    start = cue["t"] - cue["anchor_s"]
    if start < 0:
        sys.exit(f'cue at {cue["t"]} starts before the video: anchor_s {cue["anchor_s"]} is too large for {cue["file"]}')
    item = {
        "src": cue["file"],
        "at": round(start, 3),
        "volume": round(10 ** ((cue["target_db"] - cue["file_peak_db"]) / 20), 4),
        "rule": cue.get("rule", ""),
    }
    if cue.get("trim_end_s"):
        item["dur"] = cue["trim_end_s"]
    return item


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", required=True)
    ap.add_argument("--cues", default="cues_yield.json")
    a = ap.parse_args()
    public = pathlib.Path(a.project) / "public"
    cues = json.loads((public / a.cues).read_text(encoding="utf8"))
    missing = sorted({c["file"] for c in cues if not (public / c["file"]).exists()})
    if missing:
        sys.exit(f"missing sound files under public/: {missing}")
    plan_path = public / "plan.json"
    plan = json.loads(plan_path.read_text(encoding="utf8"))
    plan["sfx"] = sorted((to_plan_item(c) for c in cues), key=lambda s: s["at"])
    plan_path.write_text(json.dumps(plan, ensure_ascii=False, indent=1), encoding="utf8")
    print(f"plan.sfx: {len(plan['sfx'])} cues written to {plan_path}")


if __name__ == "__main__":
    main()
