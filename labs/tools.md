# Tools and Prerequisites - AZ-500 Labs

These labs are designed for Azure portal-first delivery, with Cloud Shell as the optional command-line environment.

---

## Required

| Requirement | Purpose |
|-------------|---------|
| Azure subscription or training sandbox | Create and secure Azure resources |
| Microsoft Entra ID tenant | Identity, access, app registration, Conditional Access |
| Contributor or Owner on a training resource group | Create lab resources |
| User Access Administrator or Owner | Assign RBAC roles in Lab 1 |
| Security Admin or Security Reader | Review Defender for Cloud and Sentinel settings |
| Modern browser | Azure portal access |

---

## Optional but useful

| Tool | Purpose |
|------|---------|
| Azure Cloud Shell | Run Azure CLI and PowerShell without local install |
| Azure CLI | Optional local command-line work |
| VS Code | Edit JSON, KQL, and lab notes |
| Microsoft Learn | Official AZ-500 reference |

---

## Licensing notes

Some security features depend on tenant licensing or subscription configuration.

| Feature | Possible requirement |
|---------|----------------------|
| Microsoft Entra Privileged Identity Management | Microsoft Entra ID P2 |
| Conditional Access | Microsoft Entra ID P1 or P2 |
| Defender for Cloud workload protection | Defender plan enabled for workload |
| Microsoft Sentinel | Log Analytics workspace and Sentinel enabled |
| Automation playbooks | Logic Apps permissions |

If your tenant blocks a step, record the feature name, missing permission, and what you would configure in production.

---

## Naming convention

Use your initials in all resources.

| Resource | Example |
|----------|---------|
| Resource group | `rg-az500-al` |
| Virtual network | `vnet-az500-al` |
| Storage account | `staz500al001` |
| Key Vault | `kv-az500-al-001` |
| Log Analytics workspace | `law-az500-al` |
| Sentinel analytics rule | `az500-al-suspicious-signin` |

