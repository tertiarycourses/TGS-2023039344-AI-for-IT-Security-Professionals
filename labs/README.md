# Microsoft Azure Security Engineer Associate AZ-500 - Lab Index

All labs run in the Azure portal using an instructor-provided subscription, training tenant, or sandbox environment. Some features require Microsoft Entra ID P2, Defender for Cloud plans, or Microsoft Sentinel permissions. If a feature is not available, complete the read-only review steps and record the missing license or permission.

---

## Domain 1 - Secure identity and access

| # | Lab | Azure services | AZ-500 focus |
|---|-----|----------------|--------------|
| 1 | [Configure RBAC, Custom Roles, and Privileged Access Review](lab-01-identity-rbac-pim.md) | Azure RBAC, custom roles, Microsoft Entra PIM | Role assignments, custom roles, privileged access |
| 2 | [Secure App Access with Conditional Access and Managed Identities](lab-02-conditional-access-managed-identities.md) | Conditional Access, app registrations, managed identities | MFA, app consent, service principals, managed identity |

## Domain 2 - Secure networking

| # | Lab | Azure services | AZ-500 focus |
|---|-----|----------------|--------------|
| 3 | [Secure Virtual Networks with NSGs, ASGs, Peering, and Network Watcher](lab-03-network-security-nsg-asg.md) | VNet, NSG, ASG, Network Watcher | Network segmentation, flow verification, diagnostics |
| 4 | [Protect Public and Private Access with Azure Firewall, WAF, and Private Endpoints](lab-04-firewall-waf-private-endpoints.md) | Azure Firewall, Application Gateway WAF, Private Endpoint | Public/private access protection |

## Domain 3 - Secure compute, storage, and databases

| # | Lab | Azure services | AZ-500 focus |
|---|-----|----------------|--------------|
| 5 | [Secure Virtual Machines, Bastion, JIT Access, and Disk Encryption](lab-05-compute-security-vm-bastion-jit.md) | VM, Azure Bastion, Defender JIT, disk encryption | Remote access, VM hardening, encryption |
| 6 | [Protect Storage, SQL Database, and Key Vault Secrets](lab-06-storage-sql-key-vault.md) | Storage, SQL Database, Key Vault | Data protection, keys, secrets, database security |

## Domain 4 - Defender for Cloud and Sentinel

| # | Lab | Azure services | AZ-500 focus |
|---|-----|----------------|--------------|
| 7 | [Manage Security Posture with Azure Policy and Defender for Cloud](lab-07-defender-policy-secure-score.md) | Azure Policy, Defender for Cloud | Governance, secure score, compliance |
| 8 | [Monitor, Investigate, and Automate with Microsoft Sentinel](lab-08-sentinel-monitor-investigate-automate.md) | Log Analytics, Sentinel, analytics rules, playbooks | SIEM, alerts, incidents, automation |

---

## Suggested schedule

| Time | Activity |
|------|----------|
| Morning | Labs 1-2 |
| Midday | Labs 3-4 |
| Afternoon | Labs 5-6 |
| Final block | Labs 7-8, cleanup, and AZ-500 revision |

---

## Cleanup rule

Delete the training resource group after the course unless your instructor asks you to preserve it for assessment or review.

