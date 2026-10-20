<!--
Sync Impact Report
- Version change: unversioned scaffold -> 1.0.0
- Modified principles: none; initial principles established
- Added sections: Security and Reliability; Development Workflow and Quality Gates
- Removed sections: none
- Follow-up TODOs: Confirm the original ratification date.
-->

# Taskify Constitution

## Core Principles

### I. User-Centered Task Management
Taskify MUST model task creation, organization, status changes, and completion around clear
user goals. Features MUST preserve understandable task state and MUST avoid hidden mutations
that make a user's work difficult to recover or explain. This keeps the product predictable
and useful for day-to-day planning.

### II. Explicit and Consistent Data Contracts
User-facing behavior and integrations MUST use explicit, documented data contracts. Input
validation MUST happen at system boundaries, persisted data MUST have defined ownership and
lifecycle rules, and changes to shared contracts MUST include a migration or compatibility
plan. This prevents inconsistent task state across the application.

### III. Testable Correctness
Every behavior change MUST include automated tests at the narrowest appropriate level.
Critical task lifecycle, persistence, authorization, and integration paths MUST have
integration coverage where unit tests cannot establish the contract. Tests MUST cover
success, validation failure, and relevant recovery or empty-state behavior.

### IV. Secure and Resilient Defaults
The application MUST enforce least-privilege access to user data, MUST treat external and
user-provided values as untrusted, and MUST fail explicitly rather than silently discarding
work. Sensitive information MUST NOT be written to logs or committed to the repository.
Operations that can lose or overwrite user work MUST be deliberate and recoverable.

### V. Simple, Observable Evolution
Taskify MUST prefer the simplest design that satisfies the requirement and MUST avoid
speculative abstractions. User-visible and operationally significant failures MUST provide
actionable diagnostics without exposing sensitive data. Breaking changes MUST be documented,
reviewed, and accompanied by an upgrade or migration path.

## Security and Reliability

Authentication and authorization checks MUST be applied at every protected boundary, not only
in the user interface. Database changes MUST preserve data integrity and MUST be reviewed for
rollback or migration safety. Network and storage failures MUST surface as errors with
context-appropriate recovery guidance. Dependencies MUST be kept current within the project's
supported runtime and license requirements.

## Development Workflow and Quality Gates

Each change MUST state its user or operational purpose, identify affected contracts, and
include focused tests. Code review MUST verify constitution compliance, data-access controls,
error handling, and migration impact. A change MUST NOT be considered complete until its
automated checks pass and any intentionally deferred risk is recorded. Documentation MUST be
updated when behavior, configuration, or public contracts change.

## Governance

This constitution supersedes conflicting project practices. Amendments MUST include a
written rationale, an updated Sync Impact Report, and a review of affected templates,
workflows, and documentation. Amendments MUST update the semantic version: MAJOR for
backward-incompatible governance changes, MINOR for new or materially expanded principles or
sections, and PATCH for clarifications or non-semantic wording changes.

Every pull request or equivalent review MUST verify compliance with the current constitution.
The reviewer MUST record any justified exception and its follow-up owner or expiry. The
constitution MUST be revisited when the architecture, data model, security posture, or
delivery workflow materially changes.

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): confirm original adoption date | **Last Amended**: 2026-10-20
