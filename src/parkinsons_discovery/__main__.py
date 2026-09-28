"""List and check the hypothesis registry."""

import argparse
import sys

from parkinsons_discovery.registry import get, hypotheses, validate


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="parkinsons_discovery",
        description=("List Parkinson's therapy hypotheses tracked in this repo. "
                     "Not a treatment recommendation."),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    list_cmd = sub.add_parser("list", help="List hypothesis ids and status")
    list_cmd.add_argument("--status", default=None)
    list_cmd.add_argument("--modality", default=None)

    show = sub.add_parser("show", help="Print one hypothesis")
    show.add_argument("hypothesis_id")

    sub.add_parser("check", help="Validate the registry")

    args = parser.parse_args(argv)

    if args.command == "check":
        problems = validate()
        if problems:
            for problem in problems:
                print(problem, file=sys.stderr)
            return 1
        print(f"ok: {len(hypotheses())} hypotheses")
        return 0

    if args.command == "list":
        rows = list(hypotheses())
        if args.status:
            rows = [i for i in rows if i.status.value == args.status]
        if args.modality:
            rows = [i for i in rows if i.modality.value == args.modality]
        if not rows:
            print("no matches", file=sys.stderr)
            return 1
        for item in rows:
            print(" | ".join([item.id, item.status.value, item.modality.value, item.claim.value]))
        return 0

    item = get(args.hypothesis_id)
    if item is None:
        print(f"unknown hypothesis: {args.hypothesis_id}", file=sys.stderr)
        return 1
    print(item.format(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
