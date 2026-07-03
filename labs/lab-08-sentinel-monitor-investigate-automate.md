# Lab 8 - Monitor, Investigate, and Automate with Microsoft Sentinel

In this lab you will configure a Microsoft Sentinel workspace, connect data, run KQL queries, create an analytics rule, and review automation options.

---

## Step 1 - Create a Log Analytics workspace

1. Search for **Log Analytics workspaces**.
2. Create `law-az500-<initials>`.
3. Place it in `rg-az500-<initials>`.
4. Choose the instructor-approved region.

Checkpoint: the Log Analytics workspace exists.

---

## Step 2 - Enable Microsoft Sentinel

1. Search for **Microsoft Sentinel**.
2. Select **Create**.
3. Choose `law-az500-<initials>`.
4. Add Sentinel to the workspace.

Checkpoint: the workspace is now a Sentinel workspace.

---

## Step 3 - Connect Azure activity data

1. Open **Content hub** or **Data connectors**.
2. Find **Azure Activity**.
3. Open the connector page.
4. Connect subscription activity logs if permitted.
5. If connection is blocked, record the required permission.

Checkpoint: Sentinel has at least one planned or active data source.

---

## Step 4 - Run basic KQL queries

1. Open **Logs**.
2. Run:

```kusto
AzureActivity
| take 10
```

3. Run:

```kusto
AzureActivity
| summarize Events=count() by OperationNameValue
| order by Events desc
```

If no data exists yet, run the queries later or use the sample query view.

Checkpoint: you can use KQL to explore security telemetry.

---

## Step 5 - Create an analytics rule

1. Open **Analytics**.
2. Select **Create** > **Scheduled query rule**.
3. Name it `AZ500 Suspicious Resource Changes <initials>`.
4. Use a query based on AzureActivity.
5. Set severity to Medium.
6. Configure entity mapping if available.
7. Set the rule to create incidents.
8. Save the rule.

Checkpoint: Sentinel can convert suspicious activity into incidents.

---

## Step 6 - Review automation

1. Open **Automation**.
2. Review automation rules.
3. Review playbook creation options.
4. If allowed, create a simple automation rule that tags incidents from your lab rule.
5. Do not create external notification or remediation playbooks unless instructed.

Checkpoint: you can explain how Sentinel automation supports incident response.

---

## What you learned

- How Sentinel uses Log Analytics workspaces.
- How data connectors bring telemetry into the SIEM.
- How KQL supports investigation.
- How analytics rules and automation support alerting and response.

