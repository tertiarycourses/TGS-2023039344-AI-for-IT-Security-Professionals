# Lab 3 - Secure Virtual Networks with NSGs, ASGs, Peering, and Network Watcher

In this lab you will create a segmented virtual network, apply Network Security Groups, use Application Security Groups, and validate traffic using Network Watcher.

---

## Step 1 - Create a virtual network

1. Create a virtual network named `vnet-az500-<initials>`.
2. Use address space `10.50.0.0/16`.
3. Create subnets:
   - `snet-web` - `10.50.1.0/24`
   - `snet-app` - `10.50.2.0/24`
   - `snet-data` - `10.50.3.0/24`
4. Place it in `rg-az500-<initials>`.

Checkpoint: the VNet has three subnets.

---

## Step 2 - Create application security groups

1. Create ASG `asg-web-<initials>`.
2. Create ASG `asg-app-<initials>`.
3. Create ASG `asg-data-<initials>`.

Checkpoint: ASGs exist in the same region as the VNet.

---

## Step 3 - Create network security groups

1. Create NSG `nsg-web-<initials>`.
2. Allow inbound HTTPS from Internet to web tier:
   - Source: `Internet`
   - Destination: `asg-web-<initials>`
   - Destination port: `443`
   - Protocol: TCP
   - Action: Allow
3. Create NSG `nsg-app-<initials>`.
4. Allow inbound app traffic only from `asg-web-<initials>` to `asg-app-<initials>`.
5. Create NSG `nsg-data-<initials>`.
6. Allow database traffic only from `asg-app-<initials>` to `asg-data-<initials>`.

Checkpoint: rules describe tier-to-tier intent instead of broad IP access.

---

## Step 4 - Associate NSGs to subnets

1. Associate `nsg-web-<initials>` to `snet-web`.
2. Associate `nsg-app-<initials>` to `snet-app`.
3. Associate `nsg-data-<initials>` to `snet-data`.

Checkpoint: each subnet has a specific NSG.

---

## Step 5 - Use Network Watcher IP flow verify

1. Open **Network Watcher**.
2. Select **IP flow verify**.
3. Choose a VM NIC if your instructor provided one, or review the input fields if no VM exists.
4. Test allowed and denied flows.
5. Record which NSG rule allows or denies each flow.

Checkpoint: you can use Network Watcher to explain why traffic is allowed or blocked.

---

## What you learned

- How NSGs enforce subnet and NIC-level traffic rules.
- How ASGs make rules easier to manage.
- How Network Watcher validates network security behavior.
- Why least privilege network design uses explicit tier flows.

