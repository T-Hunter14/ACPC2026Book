# Realtime Matching Architecture

**Status:** design only; no production implementation or model training is included.  
**Scope:** the next phase on `t-hunter14-phase-2-realtime-matching`.

## Context and assumptions

The checked-out repository currently contains no `docs/spec.md` or simulator/realtime source tree; therefore this document treats the phase name and the existing branch artifacts as the authoritative requirements and marks all product details below as assumptions to confirm before implementation. The design keeps mobile clients, payment, and production-provider integrations out of scope; they are represented only by stable interfaces.

**Assumptions:** a request asks for a feasible match between a user/request and available candidates; candidate availability and price can change between retrieval and confirmation; the simulator is the first executable source of traffic and outcomes; and matching must remain explainable and overrideable by business rules.

## Boundaries and services

1. **Matching API** accepts a versioned request, validates it, and returns ranked offers plus a decision trace.
2. **Feature/context service** creates a point-in-time feature snapshot from request, candidate, inventory, and policy data.
3. **Candidate retrieval service** applies hard eligibility and capacity filters, then returns a bounded candidate set.
4. **Ranking service** scores eligible candidates using a configured baseline or model.
5. **Policy/guardrail service** enforces business, safety, fairness, and freshness constraints after ranking.
6. **Event collector** records requests, impressions, selections, outcomes, and errors with correlation IDs.
7. **Offline evaluation/simulator** replays versioned scenarios and event snapshots; it is not a production dependency.

The API owns orchestration and response contracts; retrieval owns eligibility, ranking owns ordering, and policy owns final admissibility. No service may silently bypass a failed dependency.

## Domain and data contracts

All contracts are versioned and carry `request_id`, `event_id`, `occurred_at`, `schema_version`, `config_version`, and `trace_id`.

- `MatchRequest`: opaque requester ID, context, constraints, timestamp, and idempotency key.
- `CandidateSnapshot`: opaque candidate ID, availability/capacity, location or service context at event time, attributes permitted by policy, and snapshot timestamp.
- `MatchOffer`: candidate ID, rank, score (optional to clients), eligibility reason, expiry, and explanation codes.
- `MatchOutcome`: request/offer IDs, selected/accepted/fulfilled/cancelled status, timestamps, and outcome reason.
- `MatchEvent`: immutable envelope for request, candidate retrieval, ranking, policy decision, offer impression, selection, and outcome.

Identifiers are opaque; raw personal data is not part of the matching contract. Unknown fields are ignored only when the schema version explicitly permits forward compatibility.

## Online matching flow

1. Validate schema, authorization, idempotency, and request freshness.
2. Load a point-in-time context snapshot.
3. Retrieve candidates using hard constraints (availability, geography/serviceability, capacity, safety, and policy exclusions).
4. Rank candidates with the configured baseline/model and deterministic tie-breaking.
5. Apply policy guardrails, diversity/fairness checks, and stale-data checks.
6. Return a bounded offer list with expiry and explanation codes; persist the decision event asynchronously only after the response is accepted.
7. Record later selection and fulfillment outcomes against the original feature/config versions.

If ranking is unavailable, use the explicitly configured deterministic fallback only when policy permits; otherwise return a typed unavailable response. Never manufacture an offer from stale or incomplete eligibility data.

## Persistence and eventing

Use an append-only event log as the audit and replay boundary, with immutable event IDs and at-least-once delivery. A transactional operational store holds current availability/configuration and idempotency records. Derived feature tables and aggregates are rebuildable from events. Consumers must be idempotent; ordering is guaranteed per `request_id` where required, not globally. Retention, deletion, and access policies are configuration, not application conventions.

## Observability and failure handling

Emit structured logs, metrics, and traces keyed by `trace_id` and version fields. Track latency by stage, candidate-set size, empty-result rate, stale-data rate, fallback rate, policy rejects, acceptance/fulfillment, and outcome quality. Add alerts for SLO breaches, event lag, schema/config mismatch, and unexplained distribution shifts.

Classify failures as invalid request, dependency unavailable, stale context, policy rejection, timeout, or internal error. Bound every dependency call, propagate cancellation, and expose degraded mode explicitly. Dead-letter malformed events with operator-visible reason and replay controls; do not drop them silently.

## ML opportunities and first model target

Potential later uses are candidate retrieval, acceptance/fulfillment ranking, cancellation risk, and demand/capacity forecasting. The **first model target** is a calibrated pairwise/listwise ranking model predicting the probability that an eligible offer is accepted and successfully fulfilled within the offer window. It must initially be shadow-only; the deterministic rule-based ranker remains the decision authority.

**Features:** request context available at ranking time, candidate availability/capacity, distance/serviceability, normalized historical aggregates computed before the event, and policy-safe temporal/contextual signals. Exclude post-impression, post-selection, payment, and outcome-derived fields from online features.

**Labels:** positive when the offer is accepted and fulfilled within the defined window; negatives are eligible impressed offers that expire or are declined, with censoring/unknown outcomes retained separately. Define attribution, window, cancellation handling, and minimum observation delay in the dataset manifest.

## Leakage-safe offline evaluation

Build point-in-time feature snapshots and labels using only events available before each impression. Split chronologically by time, with a later holdout period and a scenario holdout for simulator cases. Prevent request/candidate overlap leakage where entities recur; report both overall and cold-start slices. Freeze feature, label, policy, and model manifests for every run. Compare ranking metrics (NDCG@k/MRR), calibration, coverage, acceptance/fulfillment, latency estimates, constraint violations, and subgroup performance. Do not tune on the final holdout.

## Baselines and success gates

Baselines are: eligible-first deterministic ordering, distance/utility heuristic, and current configured rule order. A model cannot advance unless it beats the primary baseline on acceptance and fulfillment without worsening hard-constraint violations, calibration, tail latency, empty-result rate, or approved fairness/safety thresholds. Gates require reproducible offline evaluation, shadow parity, schema/config rollback, and an explicit owner sign-off.

## Shadow and canary rollout

Shadow mode computes and logs model rankings without changing offers; compare rank agreement, latency, calibration, and counterfactual policy violations. Canary first enables the model for a small, reversible, preselected traffic slice with automatic rollback on SLO, safety, fairness, or outcome regression. Expand only after a review of confidence intervals and slice metrics. Keep model, feature, policy, and threshold versions independently rollbackable.

## Human, business, privacy, and security constraints

Safety and legal eligibility rules are hard constraints and cannot be learned around. Operators can inspect traces, disable a model/config, and override a decision with an auditable reason; overrides are not training labels by default. Never optimize solely for revenue or acceptance when it conflicts with safety, service commitments, fairness, or user choice.

Use data minimization, opaque identifiers, encryption in transit/at rest, least-privilege service accounts, secret management, audit logs, retention limits, deletion workflows, and access controls for event replay. Separate operational identifiers from analytics exports. Treat feature/config/model artifacts as release-controlled inputs; prohibit arbitrary user-supplied code or expressions in policy configuration.

## Configuration ownership

Platform owns API/schema, timeouts, retention, and rollout mechanics. Product/business owns explicit utility weights, offer windows, and service objectives. Safety/compliance owns hard constraints and protected handling rules. ML owns feature/model manifests and evaluation thresholds. Operations owns alert thresholds and rollback execution. Every change is reviewed, versioned, validated in simulation, and attributable to an owner.

## Testing strategy

Contract tests cover schemas, compatibility, idempotency, and event envelopes. Unit tests cover eligibility, ranking determinism, policy precedence, expiry, and fallback behavior. Property tests cover invariants such as “ineligible candidates never appear.” Integration tests cover event delivery, replay, timeouts, retries, and duplicate events. Simulator tests cover seeded scenarios, boundary conditions, skew, and failure injection. Load tests measure stage and tail latency. Offline-data tests detect leakage, missingness, drift, and label delay. Shadow/canary tests verify rollback and auditability.

## Phased implementation plan

1. **Contract and requirements lock:** reconcile this document with `docs/spec.md` and inventory simulator/realtime modules; publish schemas, ownership, SLOs, and assumptions.
2. **Deterministic vertical slice:** implement interfaces, validation, retrieval, rule ranking, policy guardrails, event envelope, simulator replay, and observability.
3. **Persistence and resilience:** add idempotency, append-only events, replay/dead-letter handling, failure injection, and operational dashboards.
4. **Dataset and baseline evaluation:** produce point-in-time manifests, labels, leakage checks, and baseline reports without training a production model.
5. **Shadow model path:** train/evaluate the first ranking candidate offline, run shadow comparison, and establish gates.
6. **Controlled canary:** enable only after sign-off, with independent rollback and documented safety/business review.

Any missing requirement discovered during reconciliation is an explicit change to this design, not an implicit implementation choice.
