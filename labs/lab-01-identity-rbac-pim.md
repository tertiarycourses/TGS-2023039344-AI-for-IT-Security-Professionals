# Lab 1 - Configure RBAC, Custom Roles, and Privileged Access Review

In this lab you will configure Azure role-based access control, create a scoped custom role, and review privileged access patterns with Microsoft Entra Privileged Identity Management.

---

## Step 1 - Create the training resource group

1. Open the Azure portal.
2. Search for **Resource groups**.
3. Select **Create**.
4. Name the resource group `rg-az500-<initials>`.
5. Choose the region assigned by your instructor.
6. Select **Review + create**, then **Create**.

Checkpoint: the resource group exists and is empty.

---

## Step 2 - Review inherited access

1. Open `rg-az500-<initials>`.
2. Select **Access control (IAM)**.
3. Select **View my access**.
4. Record your role assignments.
5. Open **Role assignments**.
6. Filter by your user account.

Checkpoint: you can identify whether your access is direct, group-based, or inherited from subscription scope.

---

## Step 3 - Assign a built-in role

1. In **Access control (IAM)**, select **Add role assignment**.
2. Choose **Reader**.
3. Select a classmate or instructor-provided test user.
4. Assign the role at the resource group scope.
5. Open **Role assignments** and confirm the assignment appears.

Checkpoint: the test user has read-only access to the training resource group.

---

## Step 4 - Create a custom role definition

1. In **Access control (IAM)**, select **Roles**.
2. Select **Create custom role**.
3. Name it `AZ500 Storage Key Reader <initials>`.
4. Start from scratch.
5. Add this permission:

```text
Microsoft.Storage/storageAccounts/listKeys/action
```

6. Set assignable scope to your training resource group.
7. Create the role.

Checkpoint: the custom role appears in the role list.

---

## Step 5 - Review privileged identity management

1. Search for **Microsoft Entra Privileged Identity Management**.
2. Open **Azure resources**.
3. Find your subscription or resource group if available.
4. Review eligible and active assignments.
5. If allowed, configure an eligible assignment for the Reader role.
6. Set activation to require justification.

If PIM is unavailable, record: `PIM requires Microsoft Entra ID P2 and sufficient role administration permissions.`

---

## What you learned

- How Azure RBAC scopes permissions.
- How built-in and custom roles differ.
- How PIM reduces standing privilege.
- How to document missing identity licensing or permissions during security reviews.

