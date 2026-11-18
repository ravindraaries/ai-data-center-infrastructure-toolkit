# AI Data Center Infrastructure Evaluation Toolkit

A practical, vendor-neutral starting point for evaluating **optical interconnects, co-packaged optics testing, liquid-cooled optical transceivers, and in-chip microfluidic cooling** in AI infrastructure projects.

> **Scope:** Educational decision support. This toolkit does not certify equipment, predict performance, or replace qualified engineering, safety, and supplier testing.

## What's inside

| Resource | Purpose |
| --- | --- |
| [`docs/architecture-guide.md`](docs/architecture-guide.md) | Five architecture decisions and integration trade-offs |
| [`docs/qualification-checklists.md`](docs/qualification-checklists.md) | Test and deployment questions for four technology areas |
| [`templates/decision-matrix.csv`](templates/decision-matrix.csv) | Editable weighted decision inputs |
| [`tools/score_options.py`](tools/score_options.py) | Standard-library Python scoring and validation |
| [`examples/sample-options.csv`](examples/sample-options.csv) | **Illustrative fictional** options to test the tool |

## Quick start

Requires Python 3.9+; no external packages.

```bash
python tools/score_options.py examples/sample-options.csv
python tools/score_options.py templates/decision-matrix.csv
```

Scores are **illustrative**, not market benchmarks. Ratings use a 1–5 scale, where 5 is better; for cost, 5 means more favorable lifecycle economics, not higher expenditure. Weights are nonnegative and must sum to 100 per option. Missing ratings are rejected instead of silently treated as zero.

## Workflow

1. Define the AI workload and identify measured bottlenecks.
2. Select feasible candidate technologies and the baseline alternative.
3. Establish acceptance criteria, safety requirements, and operating constraints.
4. Populate the decision matrix with documented measurements or explicitly labeled assumptions.
5. Run the scorer; review the detailed contributions and any uncertainties.
6. Complete qualification checklists and pilot tests before procurement.

## Technology context and market reading

- **Optical compute interconnects:** Where does optical communication offer meaningful system-level benefits over electrical links? [KBV Research: Optical Compute Interconnect Market](https://www.kbvresearch.com/optical-compute-interconnect-market/)
- **Co-packaged optics testing:** How will integrated photonic assemblies be validated and diagnosed? [KBV Research: Co-Packaged Optics Testing Equipment Market](https://www.kbvresearch.com/co-packaged-optics-testing-equipment-market/)
- **Liquid-cooled optical transceivers:** When is dedicated liquid cooling justified for networking modules? [KBV Research: Liquid-Cooled Optical Transceiver Market](https://www.kbvresearch.com/liquid-cooled-optical-transceiver-market/)
- **In-chip microfluidic cooling:** What additional value does integrated chip-level cooling provide compared with qualified conventional approaches? [KBV Research: In-Chip Microfluidic Cooling Market](https://www.kbvresearch.com/in-chip-microfluidic-cooling-market/)

These links provide market context, not engineering certification or validation of any scoring result.

## Independent technical resources

- [Open Compute Project](https://www.opencompute.org/)
- [IEEE Photonics Society](https://www.photonicssociety.org/)
- [Uptime Institute](https://uptimeinstitute.com/)

## Important limitations

- Candidate ratings must be supported by actual supplier documentation, lab results, or explicitly identified estimates.
- A weighted score cannot override mandatory safety, compliance, interoperability, or reliability requirements.
- Technologies are at different levels of maturity and should not be assumed ready for universal deployment.
- Do not compare options across fundamentally different workloads without revisiting criteria and weights.

## License

MIT License. See [`LICENSE`](LICENSE).
