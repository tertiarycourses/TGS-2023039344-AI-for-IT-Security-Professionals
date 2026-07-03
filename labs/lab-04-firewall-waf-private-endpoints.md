# Lab 4 - Protect Public and Private Access with Azure Firewall, WAF, and Private Endpoints

In this lab you will design public and private access protections using Azure Firewall, Web Application Firewall concepts, and Private Endpoints. Some resources can be reviewed instead of deployed if your training subscription has quota or cost limits.

---

## Step 1 - Plan firewall placement

1. Open the VNet from Lab 3.
2. Add subnet `AzureFirewallSubnet` with address range `10.50.10.0/26`.
3. Review the Azure Firewall creation wizard.
4. Name the firewall `afw-az500-<initials>`.
5. If your instructor allows deployment, create it with a firewall policy.
6. If not deploying, document the required subnet, public IP, and policy components.

Checkpoint: you can describe where Azure Firewall sits in a hub-spoke network.

---

## Step 2 - Review firewall policy rules

1. Open the firewall policy.
2. Create a rule collection group named `rcg-az500-training`.
3. Add an application rule allowing outbound HTTPS to `learn.microsoft.com`.
4. Add a network rule allowing DNS to your approved DNS server.
5. Review threat intelligence mode.

Checkpoint: you can distinguish application rules from network rules.

---

## Step 3 - Review WAF protection

1. Search for **Application Gateway**.
2. Review the creation workflow.
3. Select WAF v2 tier in the review steps if deployment is allowed.
4. Open **Web application firewall policies**.
5. Review managed OWASP rule sets.
6. Create a policy named `waf-az500-<initials>` if permitted.
7. Leave prevention mode disabled unless instructed.

Checkpoint: you can explain how WAF protects HTTP applications differently from Azure Firewall.

---

## Step 4 - Create a storage account private endpoint

1. Create a storage account named `staz500<initials>001`.
2. Disable public blob access.
3. Open **Networking**.
4. Choose **Private endpoint connections**.
5. Create a private endpoint for the Blob service.
6. Place it in `snet-data`.
7. Enable private DNS zone integration if available.

Checkpoint: the storage account can be reached privately from the VNet.

---

## Step 5 - Review public access settings

1. Return to the storage account networking page.
2. Set public network access to disabled or selected networks, depending on class constraints.
3. Review firewall and virtual network rules.
4. Record why private endpoints reduce public exposure.

---

## What you learned

- When to use Azure Firewall, WAF, and Private Endpoints.
- How firewall policies organize network and application rules.
- How private access reduces public attack surface.
- How to document cost-sensitive security resources without deploying every component.

