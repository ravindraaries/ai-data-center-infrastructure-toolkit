# Five AI Infrastructure Architecture Decisions

## 1. Where should optics be used?
Compare electrical and optical links by reach, aggregate bandwidth, latency, conversion overhead, energy per bit, cost, interoperability, and serviceability. Start with measured communication bottlenecks; avoid an optics-everywhere assumption.

## 2. Is co-packaged optical integration justified?
Evaluate the performance benefit against packaging complexity, optical alignment, test access, yield, repairability, supplier readiness, and field replacement strategy. Require evidence of package-level qualification.

## 3. Should network modules use dedicated liquid cooling?
Distinguish ordinary air-cooled transceivers in liquid-cooled racks from modules designed for liquid cooling. Compare module temperatures, thermal interfaces, fluid compatibility, leak risks, pumping energy, and maintenance procedures.

## 4. Does chip-level microfluidic cooling solve a real hotspot problem?
Compare a qualified cold-plate baseline with microfluidic candidates using measured hotspot temperatures, thermal resistance, pressure drop, pumping power, manufacturing integration, and reliability tests.

## 5. Can the system be maintained and upgraded?
Require observability, fault isolation, spare parts, field service processes, fallback options, supplier support, and lifecycle cost modeling. Pilot before scale-up.

## Conceptual dependency map

```text
AI workload & performance targets
             |
   Compute and network topology
             |
      Link technology choice
       /              \
Electrical links   Optical links
                       |
               Photonic integration
                       |
               Testing/qualification

Cross-cutting: cooling, power, monitoring, safety,
serviceability, interoperability, and lifecycle cost.
```

This is a decision relationship diagram, not a physical wiring diagram.

## Recommended decision record
For each candidate record: workload, baseline, measured bottleneck, assumptions, mandatory gates, test method, results, supplier evidence, open risks, owner, and date of next review.
