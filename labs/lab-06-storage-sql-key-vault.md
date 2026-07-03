# Lab 6 - Protect Storage, SQL Database, and Key Vault Secrets

In this lab you will configure security controls for Azure Storage, Azure SQL Database, and Azure Key Vault.

---

## Step 1 - Harden storage account access

1. Open the storage account from Lab 4.
2. Go to **Configuration**.
3. Require secure transfer.
4. Disable blob anonymous access.
5. Review minimum TLS version.
6. Go to **Data protection**.
7. Enable soft delete for blobs.
8. Enable versioning if available.

Checkpoint: storage data protection settings are enabled.

---

## Step 2 - Review storage keys and shared access

1. Open **Access keys**.
2. Review key rotation options.
3. Do not copy keys into lab notes.
4. Open **Shared access signature**.
5. Review how SAS scope and expiry reduce risk.
6. Do not generate a broad account SAS unless instructed.

Checkpoint: you can explain why identity-based access is preferred over long-lived keys.

---

## Step 3 - Create a Key Vault

1. Create Key Vault `kv-az500-<initials>-001`.
2. Use Azure RBAC permission model if instructed.
3. Enable purge protection if allowed.
4. Enable soft delete.
5. Open **Networking** and review public access options.

Checkpoint: Key Vault has recovery protections enabled.

---

## Step 4 - Add and protect a secret

1. Open **Secrets**.
2. Create a secret named `training-api-key`.
3. Use a dummy value such as `not-a-real-secret`.
4. Set an expiration date.
5. Review secret version history.

Checkpoint: secret lifecycle and expiry are visible.

---

## Step 5 - Create or review Azure SQL Database security

1. Create a small Azure SQL Database if class budget allows, or review an instructor-provided database.
2. Enable Microsoft Entra authentication if available.
3. Open **Auditing** and enable audit logs to a storage account or Log Analytics workspace.
4. Review **Dynamic data masking**.
5. Review **Transparent Data Encryption**.
6. Review **Always Encrypted** documentation from the SQL security blade.

Checkpoint: you can identify SQL controls for authentication, auditing, masking, and encryption.

---

## What you learned

- How to harden storage access and recovery settings.
- How Key Vault protects keys, secrets, and certificates.
- How Azure SQL Database security features map to confidentiality and audit requirements.
- Why secret values should not be copied into lab submissions.

