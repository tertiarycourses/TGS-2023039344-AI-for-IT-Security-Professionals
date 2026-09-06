# Lab 11 Access rights troubleshooting

AI for IT Security Professionals | TGS-2023039344 | v6.0

## Purpose and output

Create a access diagnosis and review decisions. This lab supports LO3. It uses a simplified deterministic teaching model, not a trained AI system or full Azure emulator. The AI review is a separate exercise using the included prompt.

## Requirements

Python 3.10 or later, a text editor and this entire folder. No packages, network access or API key are required for the baseline. On Windows use `py -3` if `python3` is unavailable. An approved AI tool is optional; the trainer can provide a review response for critique. Azure exercises require the trainer-assigned subscription, permission and feature entitlement. Record an exact blocker where unavailable; never describe an unperformed test as passed.

## Folder contents

- `mock-data.json`: synthetic input with no real personal data or credentials.
- `analyse.py`: runnable analysis for this lab only.
- `expected-results.json`: expected baseline and source checksum.
- `ai-review-prompt.txt`: evidence-constrained AI review prompt.
- `evidence-template.md`: your deliverable template.
- `INSTRUCTIONS.md` and `INSTRUCTIONS.pdf`: the same procedure in two formats.

## 1 Prepare a working copy

Copy this whole folder to a location you can edit. Open a terminal in the copied folder. Confirm Python and inspect the data before running code.

```text
python3 --version
python3 -m json.tool mock-data.json
```

Identify the record IDs and explain the meaning of each field. All values are invented classroom fixtures. Open `analyse.py` in the editor and locate the decision rule. It reads a local JSON file and writes a local report.

## 2 Run the baseline

```text
python3 analyse.py --input mock-data.json --output results.json
```

Open `results.json`. The expected decisions in output order are: ALLOW, MISSING_ACTION, SELF_APPROVAL. The `source_sha256` binds the report to the exact input bytes. Compare against the supplied baseline:

```text
python3 -c "import json; a=json.load(open('results.json')); b=json.load(open('expected-results.json')); assert a==b; print('BASELINE PASS')"
```

A pass proves this fixture was processed as specified; it does not prove an Azure control was deployed. Copy the input checksum and decision rows into your evidence template.

## 3 Trace the mechanism

### Least privilege troubleshooting

Diagnose actor, scope, action and policy before granting broader access.

Contract: `actor_id, target_scope, attempted_action, error_code`

Accepted case: The failing action is absent at the intended resource scope.

Counterexample: Owner is granted without identifying the failing action.

Diagnosis: Add only a justified permission through approval and repeat a negative test outside scope.

Evidence: Keep the original error, policy evaluation and post-fix result.

### Access review decisions

Compare actual grants to job need and make an accountable retain/revoke decision.

Contract: `principal, grant, business_need, reviewer, decision`

Accepted case: An inactive contractor's unneeded grant is revoked.

Counterexample: A reviewer approves every grant without evidence of need.

Diagnosis: Investigate stale accounts and verify revocation across group and direct assignments.

Evidence: Record reviewer reasoning and a subsequent denied access attempt.

### Separation of duties

A requester cannot approve their own privileged change when the process requires independent review.

Contract: `requester_id, approver_id, requested_action`

Accepted case: user_004 requests and owner_002 approves.

Counterexample: The requester and approver are the same principal.

Diagnosis: Reject self-approval and route to an authorised independent owner.

Evidence: Capture both identities and the immutable request identifier.

## 4 Change one input and test the consequence

Save a copy of `mock-data.json` as `changed-data.json` using the editor. Add write to req-b grants and leave req-c unchanged. Only req-b should become ALLOW. Explain why role permission does not replace independent approval.

```text
python3 analyse.py --input changed-data.json --output changed-results.json
```

Compare decisions and source hashes with the baseline. Identify the exact expression in `analyse.py` responsible for the changed behaviour. Do not overwrite `expected-results.json` to make a failing baseline pass. Restore the original fixture if you edited it accidentally.

## 5 Review AI claims against evidence

Open `ai-review-prompt.txt`. In an organisation-approved AI tool, submit the prompt with the synthetic input and result only. Record the tool/model name, date and prompt version if available. If no approved AI tool is available, manually draft a tentative analyst summary and label it as a human exercise.

For each returned claim, record its cited ID, the actual field value, whether the claim follows, and any correction. Reject conclusions unsupported by the records even when the model is confident. Include one alternative explanation. The AI response is a proposal; it has no authority to approve or execute a security action.

## 6 Verify the corresponding operational control

On the assigned resource, use IAM > Check access for the test principal and capture the failing operation from the Activity log. Compare the action to the role definition and scope. Propose the smallest grant that resolves the duty. Re-test an allowed operation and an operation outside scope after a trainer-approved change.

For every screenshot or export, record resource scope, UTC time and expected versus observed result. Redact personal data and secrets. If blocked, record the exact error, missing permission/licence, what could be inspected, and the unverified outcome. Ask the trainer to provide an authorised sandbox demonstration where the assessed ability cannot otherwise be evidenced.

## 7 Submit evidence and clean up

Complete `evidence-template.md` with baseline, changed result, AI claim review and Azure evidence or clearly labelled limitations. Keep `results.json` and `changed-results.json` with your submission. Check that your conclusion distinguishes an observed fact from a hypothesis. Remove only resources or assignments you created with trainer approval; do not delete shared training infrastructure.

## Acceptance checks

- The unchanged fixture produces the exact expected report.
- The changed fixture produces the explained result and a different input hash.
- At least one AI or analyst claim is checked against a specific record and field.
- The report states simulation, Azure verified or blocked for each relevant claim.
- The output is a access diagnosis and review decisions with an owner, evidence and remaining uncertainty.

## Troubleshooting

- Python not found: install the trainer-approved Python distribution or use `py -3` on Windows.
- File not found: open the terminal in this lab folder; check the input filename.
- JSON parse error: validate with `python3 -m json.tool changed-data.json`; use lowercase `true` and `false` in JSON.
- Baseline mismatch: restore the supplied fixture and inspect the first differing decision; never edit the expected file.
- Azure denial or missing feature: capture the exact error and scope. A blocker is a limitation, not proof of competence or deployment.
- AI invents evidence: reject the claim, cite the missing ID, and request an evidence-limited revision.

## References

The Learner Guide contains the complete source register and the lecture explanations for this lab. Original examples are adapted from the supplied Azure and AI-security references. Product behaviour should be checked against current Microsoft Learn documentation before a real deployment.
