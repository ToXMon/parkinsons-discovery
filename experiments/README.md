# experiments/

One folder per drylab experiment: `experiments/<hypothesis-id>-<slug>/README.md`.
Copy the template below. Write the card before the brev.dev instance starts;
update the results section when it finishes.

## Template

```
# <hypothesis-id>: <short title>

- Date started / finished:
- Registry hypothesis: H-XXX (status before / after)
- Question: what would this experiment change about the hypothesis?
- Decision rule: result X parks it, result Y promotes it, decided before running.
- Data: source, version/access date, terms (see data/README.md rules).
- Method: brief; note anything pre-specified (splits, thresholds).
- Compute: brev.dev instance type, hours, cost ceiling and actual.
- Environment: image, key package versions.
- Results: observed numbers only, separated from interpretation.
- Interpretation: what this means for the hypothesis.
- Registry action: status change + citation (the experiment card is the source).
- Tear-down: instance destroyed (yes/no).
```

Cheapest test first (see docs/WORKFLOW.md for the ranked menu). If the
bottleneck is manufacturing or delivery rather than biology, write that down;
it is a legitimate kill reason.
