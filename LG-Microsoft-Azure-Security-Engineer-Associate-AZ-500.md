# Learner Guide - Microsoft Azure Security Engineer Associate (AZ-500)

> **Course Code:** TGS-2023039344  
> **Course:** WSQ - Microsoft Azure Security Engineer Associate (AZ-500)  
> **Provider:** Tertiary Infotech Academy Pte Ltd  
> **Registration:** https://www.tertiarycourses.com.sg/wsq-microsoft-azure-security-engineer-associate-az-500.html

This learner guide contains the hands-on exercises for the AZ-500 course. The labs follow the Microsoft AZ-500 study guide domains: secure identity and access, secure networking, secure compute/storage/databases, and secure Azure with Microsoft Defender for Cloud and Microsoft Sentinel.

---

## Important exam note

Microsoft states that Exam AZ-500 retires on **August 31, 2026, at 11:59 PM Central Standard Time**. Use the current Microsoft study guide for the latest retirement and replacement guidance before booking the exam.

---

## Before you begin

You need:

1. An Azure subscription or training sandbox.
2. A Microsoft Entra tenant.
3. Permission to create resources in a training resource group.
4. Permission to assign RBAC roles for identity labs.
5. Security Reader or Security Admin-style access for Defender for Cloud and Sentinel review.

Some labs involve features that may require Microsoft Entra ID P1/P2, Defender for Cloud plans, or Microsoft Sentinel permissions. If a feature is unavailable, complete the review steps and write down the missing license or role.

---

## Naming convention

Use your initials in every object name.

| Resource | Example |
|----------|---------|
| Resource group | `rg-az500-al` |
| Virtual network | `vnet-az500-al` |
| Storage account | `staz500al001` |
| Key Vault | `kv-az500-al-001` |
| Log Analytics workspace | `law-az500-al` |
| Sentinel rule | `AZ500 Suspicious Resource Changes AL` |

---

## Lab 1 - Configure RBAC, Custom Roles, and Privileged Access Review

### Objective

Configure Azure RBAC, create a scoped custom role, and review privileged access management.

### Steps

1. Open the Azure portal.
2. Search for **Resource groups**.
3. Create a resource group named `rg-az500-<initials>`.
4. Choose the instructor-approved region.
5. Open the resource group.
6. Select **Access control (IAM)**.
7. Select **View my access**.
8. Record your current access and whether it is direct, group-based, or inherited.
9. Open **Role assignments**.
10. Filter by your user account.
11. Select **Add role assignment**.
12. Choose **Reader**.
13. Select an instructor-provided test user or classmate.
14. Assign the role at the resource group scope.
15. Confirm the Reader role assignment appears.
16. Select **Roles**.
17. Select **Create custom role**.
18. Name it `AZ500 Storage Key Reader <initials>`.
19. Start from scratch.
20. Add this permission:

```text
Microsoft.Storage/storageAccounts/listKeys/action
```

21. Set assignable scope to your resource group.
22. Create the custom role.
23. Search for **Microsoft Entra Privileged Identity Management**.
24. Open **Azure resources**.
25. Review eligible and active assignments.
26. If allowed, configure an eligible Reader assignment requiring justification.
27. If unavailable, record: `PIM requires Microsoft Entra ID P2 and sufficient role administration permissions.`

### Checkpoint

You should be able to explain RBAC scope, role assignments, custom roles, and why PIM reduces standing privilege.

### Review questions

1. What is the difference between Owner and User Access Administrator?
2. Why should custom roles have narrow assignable scopes?
3. Why is eligible access safer than permanent active access?

---

## Lab 2 - Secure App Access with Conditional Access and Managed Identities

### Objective

Review Conditional Access, app registration permissions, service principals, and managed identities.

### Steps

1. Open the Microsoft Entra admin center.
2. Go to **Protection** > **Conditional Access**.
3. Open **Policies**.
4. Create a report-only policy named `AZ500 Require MFA for Azure Portal <initials>`.
5. Target your test group or your own account.
6. Target **Microsoft Azure Management**.
7. Under Grant, choose **Require multifactor authentication**.
8. Set policy mode to **Report-only**.
9. Save the policy.
10. Open **Sign-in logs**.
11. Filter to your account.
12. Open a recent Azure portal sign-in.
13. Review the Conditional Access tab.
14. Confirm whether the report-only policy would have applied.
15. Go to **Microsoft Entra ID** > **App registrations**.
16. Create an app registration named `app-az500-<initials>`.
17. Use single tenant access.
18. Record the Application client ID and Directory tenant ID.
19. Open **API permissions**.
20. Add delegated Microsoft Graph permission `User.Read`.
21. Review whether admin consent is required.
22. Do not grant admin consent unless instructed.
23. Open a training VM, app service, or automation account.
24. Open **Identity**.
25. Enable the system-assigned managed identity.
26. Return to your resource group IAM page.
27. Assign the managed identity the Reader role.

### Checkpoint

You should understand report-only Conditional Access, app consent, service principals, and credential-free managed identities.

### Review questions

1. Why should Conditional Access policies be tested in report-only mode first?
2. What is the risk of broad admin consent?
3. Why are managed identities safer than stored client secrets?

---

## Lab 3 - Secure Virtual Networks with NSGs, ASGs, and Network Watcher

### Objective

Build a segmented virtual network and validate traffic rules.

### Steps

1. Create virtual network `vnet-az500-<initials>`.
2. Use address space `10.50.0.0/16`.
3. Create subnet `snet-web` with `10.50.1.0/24`.
4. Create subnet `snet-app` with `10.50.2.0/24`.
5. Create subnet `snet-data` with `10.50.3.0/24`.
6. Create ASG `asg-web-<initials>`.
7. Create ASG `asg-app-<initials>`.
8. Create ASG `asg-data-<initials>`.
9. Create NSG `nsg-web-<initials>`.
10. Add a rule allowing inbound HTTPS from Internet to the web ASG.
11. Create NSG `nsg-app-<initials>`.
12. Add a rule allowing app traffic only from the web ASG to the app ASG.
13. Create NSG `nsg-data-<initials>`.
14. Add a rule allowing database traffic only from the app ASG to the data ASG.
15. Associate each NSG to the matching subnet.
16. Open **Network Watcher**.
17. Select **IP flow verify**.
18. Choose an instructor-provided VM NIC if available.
19. Test one allowed flow and one denied flow.
20. Record which NSG rule explains the result.

### Checkpoint

You should be able to design and validate tier-based network segmentation.

### Review questions

1. Why are ASGs easier to manage than hard-coded IP rules?
2. Which tool helps identify the NSG rule that allowed or denied a flow?
3. What is the risk of allowing broad inbound management traffic?

---

## Lab 4 - Protect Public and Private Access with Azure Firewall, WAF, and Private Endpoints

### Objective

Review and configure controls for public and private access to Azure resources.

### Steps

1. Open the VNet from Lab 3.
2. Add `AzureFirewallSubnet` with address range `10.50.10.0/26`.
3. Review the Azure Firewall creation workflow.
4. Name the planned firewall `afw-az500-<initials>`.
5. If allowed, create Azure Firewall with a firewall policy.
6. If deployment is not allowed, document the subnet, public IP, and policy requirements.
7. Open the firewall policy.
8. Create a rule collection group named `rcg-az500-training`.
9. Add an application rule allowing outbound HTTPS to `learn.microsoft.com`.
10. Add a network rule allowing DNS to an approved DNS server.
11. Review threat intelligence mode.
12. Search for **Application Gateway**.
13. Review the WAF v2 tier.
14. Open **Web application firewall policies**.
15. Create policy `waf-az500-<initials>` if permitted.
16. Review managed OWASP rules.
17. Keep prevention mode disabled unless instructed.
18. Create storage account `staz500<initials>001`.
19. Disable public blob access.
20. Open **Networking**.
21. Create a private endpoint for the Blob service.
22. Place it in `snet-data`.
23. Enable private DNS integration if available.
24. Review public network access settings.

### Checkpoint

You should be able to explain when to use Azure Firewall, WAF, and Private Endpoints.

### Review questions

1. What does Azure Firewall protect that WAF does not?
2. What does WAF protect that Azure Firewall does not?
3. Why do Private Endpoints reduce public attack surface?

---

## Lab 5 - Secure Virtual Machines, Bastion, JIT Access, and Disk Encryption

### Objective

Secure administrative access to VMs and review compute encryption controls.

### Steps

1. Create VM `vm-az500-<initials>`.
2. Place it in `snet-app`.
3. Use a small approved size.
4. Avoid public RDP or SSH exposure.
5. Add subnet `AzureBastionSubnet` with address range `10.50.20.0/26`.
6. Review or deploy Azure Bastion named `bas-az500-<initials>`.
7. Open the VM networking blade.
8. Remove direct inbound RDP or SSH rules from Internet.
9. Confirm no broad management rule remains in the NSG.
10. Open **Microsoft Defender for Cloud**.
11. Open **Workload protections**.
12. Open **Just-in-time VM access**.
13. Add the VM if Defender for Servers is available.
14. Configure approved ports, source IP ranges, and duration.
15. If unavailable, record the missing Defender plan or permission.
16. Open the VM **Disks** blade.
17. Review encryption settings.
18. Identify platform-managed key and customer-managed key options.
19. Review encryption at host if available.

### Checkpoint

You should understand secure VM administration, JIT access, and disk encryption options.

### Review questions

1. Why is Bastion safer than exposing RDP or SSH to the Internet?
2. How does JIT reduce management-port risk?
3. When would a customer-managed key be required?

---

## Lab 6 - Protect Storage, SQL Database, and Key Vault Secrets

### Objective

Configure storage protection, Key Vault secret management, and SQL security controls.

### Steps

1. Open the storage account from Lab 4.
2. Go to **Configuration**.
3. Require secure transfer.
4. Disable blob anonymous access.
5. Review minimum TLS version.
6. Open **Data protection**.
7. Enable blob soft delete.
8. Enable versioning if available.
9. Open **Access keys**.
10. Review key rotation.
11. Do not copy keys into your notes.
12. Open **Shared access signature**.
13. Review SAS expiry and scope.
14. Do not create a broad account SAS unless instructed.
15. Create Key Vault `kv-az500-<initials>-001`.
16. Use Azure RBAC permission model if instructed.
17. Enable soft delete.
18. Enable purge protection if allowed.
19. Review Key Vault networking.
20. Create secret `training-api-key`.
21. Use dummy value `not-a-real-secret`.
22. Set an expiration date.
23. Review secret version history.
24. Create or review an Azure SQL Database.
25. Enable Microsoft Entra authentication if available.
26. Enable auditing to storage or Log Analytics.
27. Review Dynamic Data Masking.
28. Review Transparent Data Encryption.
29. Review Always Encrypted documentation.

### Checkpoint

You should be able to secure storage, secrets, and SQL Database using identity, network, recovery, and encryption controls.

### Review questions

1. Why should shared keys be avoided when identity-based access is available?
2. Why should Key Vault secrets have expiry dates?
3. What is the difference between TDE and Always Encrypted?

---

## Lab 7 - Manage Security Posture with Azure Policy and Defender for Cloud

### Objective

Use Azure Policy and Defender for Cloud to assess security posture and compliance.

### Steps

1. Search for **Policy**.
2. Open **Definitions**.
3. Find a built-in storage security policy.
4. Assign it to `rg-az500-<initials>`.
5. Name the assignment `az500-storage-security-<initials>`.
6. Open **Policy** > **Compliance**.
7. Find your assignment.
8. Review compliant and non-compliant resources.
9. Open a non-compliant resource if one exists.
10. Identify the remediation action.
11. Search for **Microsoft Defender for Cloud**.
12. Open **Overview**.
13. Review secure score.
14. Open **Recommendations**.
15. Filter to your subscription or resource group if possible.
16. Open **Regulatory compliance**.
17. Review available standards.
18. Open Microsoft Cloud Security Benchmark if available.
19. Review failed controls and affected resources.
20. Open **Environment settings**.
21. Review Defender plans for Servers, Storage, SQL, and Containers.
22. Do not enable paid plans unless instructed.

### Checkpoint

You should understand how policy, secure score, recommendations, and compliance standards work together.

### Review questions

1. What is the difference between Azure Policy and Defender for Cloud recommendations?
2. How does secure score help prioritize remediation?
3. Why should paid Defender plans be intentionally enabled rather than casually toggled on?

---

## Lab 8 - Monitor, Investigate, and Automate with Microsoft Sentinel

### Objective

Configure Sentinel, connect Azure telemetry, investigate with KQL, and review automation.

### Steps

1. Create Log Analytics workspace `law-az500-<initials>`.
2. Search for **Microsoft Sentinel**.
3. Select **Create**.
4. Choose your Log Analytics workspace.
5. Add Sentinel.
6. Open **Content hub** or **Data connectors**.
7. Find **Azure Activity**.
8. Open the connector page.
9. Connect subscription activity logs if permitted.
10. If blocked, record the missing permission.
11. Open **Logs**.
12. Run:

```kusto
AzureActivity
| take 10
```

13. Run:

```kusto
AzureActivity
| summarize Events=count() by OperationNameValue
| order by Events desc
```

14. Open **Analytics**.
15. Select **Create** > **Scheduled query rule**.
16. Name it `AZ500 Suspicious Resource Changes <initials>`.
17. Use a query based on AzureActivity.
18. Set severity to Medium.
19. Configure entity mapping if available.
20. Set the rule to create incidents.
21. Save the rule.
22. Open **Automation**.
23. Review automation rules.
24. Review playbook creation options.
25. If allowed, create a simple automation rule that tags incidents from your lab rule.
26. Avoid external notifications or remediation playbooks unless instructed.

### Checkpoint

You should be able to explain how data connectors, KQL, analytics rules, incidents, and automation support security operations.

### Review questions

1. Why does Sentinel use a Log Analytics workspace?
2. What makes a KQL query useful for an analytics rule?
3. When should incident response be automated, and when should it require analyst approval?

---

## Final AZ-500 revision checklist

| Skill | Can you do it? |
|-------|----------------|
| Assign Azure built-in roles | Yes / No |
| Create a custom role | Yes / No |
| Explain PIM eligible access | Yes / No |
| Create a report-only Conditional Access policy | Yes / No |
| Review app permissions and consent | Yes / No |
| Enable and assign a managed identity | Yes / No |
| Design NSG and ASG segmentation | Yes / No |
| Explain Azure Firewall, WAF, and Private Endpoints | Yes / No |
| Secure VM management access | Yes / No |
| Explain Bastion and JIT | Yes / No |
| Harden storage accounts | Yes / No |
| Configure Key Vault secret controls | Yes / No |
| Review SQL auditing, masking, and encryption | Yes / No |
| Assign Azure Policy | Yes / No |
| Interpret Defender for Cloud secure score | Yes / No |
| Configure Sentinel and run KQL | Yes / No |
| Create a Sentinel analytics rule | Yes / No |

---

## Cleanup

At the end of the course:

1. Disable test Conditional Access policies unless the instructor asks you to keep them.
2. Remove temporary role assignments.
3. Delete the training resource group.
4. Delete Sentinel and Log Analytics resources if they were created only for class.
5. Confirm no paid Defender plans or scheduled automation remain enabled unintentionally.
6. Sign out of Azure on shared computers.

