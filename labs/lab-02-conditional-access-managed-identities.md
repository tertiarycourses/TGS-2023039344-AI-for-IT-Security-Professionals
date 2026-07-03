# Lab 2 - Secure App Access with Conditional Access and Managed Identities

In this lab you will review Conditional Access, app registrations, service principals, OAuth consent, and managed identities. These controls are central to secure identity and application access in Azure.

---

## Step 1 - Review Conditional Access policies

1. Open **Microsoft Entra admin center**.
2. Go to **Protection** > **Conditional Access**.
3. Open **Policies**.
4. Review any existing policies.
5. Create a report-only policy named `AZ500 Require MFA for Azure Portal <initials>`.
6. Set **Users** to your test group or your own account.
7. Set **Target resources** to **Microsoft Azure Management**.
8. Set **Grant** to **Require multifactor authentication**.
9. Set policy mode to **Report-only**.
10. Save the policy.

Checkpoint: the policy exists but does not enforce access yet.

---

## Step 2 - Review sign-in impact

1. Open **Sign-in logs**.
2. Filter to your account.
3. Open a recent Azure portal sign-in.
4. Review the Conditional Access tab.
5. Confirm whether the report-only policy would have applied.

Checkpoint: you can assess policy impact before enforcement.

---

## Step 3 - Create an app registration

1. Go to **Microsoft Entra ID** > **App registrations**.
2. Select **New registration**.
3. Name it `app-az500-<initials>`.
4. Use single tenant access.
5. Register the app.
6. Record the Application client ID and Directory tenant ID.

Checkpoint: the app registration exists.

---

## Step 4 - Review API permissions and consent

1. Open the app registration.
2. Select **API permissions**.
3. Add a delegated Microsoft Graph permission such as `User.Read`.
4. Review whether admin consent is required.
5. Do not grant admin consent unless instructed.

Checkpoint: you can explain delegated permissions, application permissions, and admin consent.

---

## Step 5 - Enable a managed identity

1. Create or open a training virtual machine, automation account, or app service.
2. Open **Identity**.
3. Turn **System assigned** identity **On**.
4. Save.
5. Return to the resource group IAM page.
6. Assign the managed identity the **Reader** role on the resource group.

Checkpoint: an Azure resource has an identity that can be assigned RBAC permissions without storing credentials.

---

## What you learned

- How report-only Conditional Access protects against accidental lockout.
- How app registrations expose API permissions and consent decisions.
- How managed identities replace application secrets.
- How service principals connect applications to Azure RBAC.

