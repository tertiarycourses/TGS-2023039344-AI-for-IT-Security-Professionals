# Lab 7 - Manage Security Posture with Azure Policy and Defender for Cloud

In this lab you will use Azure Policy and Microsoft Defender for Cloud to assess compliance, secure score, and recommended remediation actions.

---

## Step 1 - Assign an Azure Policy

1. Search for **Policy**.
2. Select **Definitions**.
3. Find a built-in policy such as **Storage accounts should prevent shared key access** or **Secure transfer to storage accounts should be enabled**.
4. Assign it to `rg-az500-<initials>`.
5. Name the assignment `az500-storage-security-<initials>`.
6. Create the assignment.

Checkpoint: a security policy is assigned to the training scope.

---

## Step 2 - Review compliance

1. Open **Policy** > **Compliance**.
2. Find your policy assignment.
3. Review compliant and non-compliant resources.
4. Open a non-compliant resource if one exists.
5. Identify the remediation action.

Checkpoint: you can interpret policy compliance results.

---

## Step 3 - Open Defender for Cloud

1. Search for **Microsoft Defender for Cloud**.
2. Open **Overview**.
3. Review secure score.
4. Open **Recommendations**.
5. Filter by your resource group or subscription if possible.

Checkpoint: you can find security recommendations and affected resources.

---

## Step 4 - Review regulatory compliance

1. Open **Regulatory compliance**.
2. Review available standards.
3. Open Microsoft Cloud Security Benchmark if available.
4. Identify failed controls and affected resources.

Checkpoint: you can connect policy findings to compliance frameworks.

---

## Step 5 - Review Defender plans

1. Open **Environment settings**.
2. Select the subscription.
3. Review Defender plans for Servers, Storage, SQL, Containers, and other workloads.
4. Do not enable paid plans unless your instructor approves.

Checkpoint: you can explain how workload protection plans affect alerting and recommendations.

---

## What you learned

- How Azure Policy enforces governance.
- How Defender for Cloud calculates secure score.
- How recommendations support remediation.
- How compliance standards map technical controls to frameworks.

