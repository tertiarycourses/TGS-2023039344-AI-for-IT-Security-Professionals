# Lab 5 - Secure Virtual Machines, Bastion, JIT Access, and Disk Encryption

In this lab you will secure administrative access to virtual machines and review compute hardening options such as Bastion, Just-in-Time access, and disk encryption.

---

## Step 1 - Create a test virtual machine

1. Create a Windows or Linux VM named `vm-az500-<initials>`.
2. Place it in `rg-az500-<initials>`.
3. Use `snet-app` from Lab 3.
4. Do not expose RDP or SSH directly to the Internet unless your instructor explicitly permits it.
5. Use a small VM size approved by the instructor.

Checkpoint: the VM exists in the app subnet.

---

## Step 2 - Deploy or review Azure Bastion

1. Add subnet `AzureBastionSubnet` with address range `10.50.20.0/26`.
2. Search for **Bastions**.
3. Create Bastion `bas-az500-<initials>` if class budget allows.
4. If Bastion is not deployed, review the required subnet, public IP, and connection flow.

Checkpoint: you can explain how Bastion avoids public management ports on VMs.

---

## Step 3 - Remove public management exposure

1. Open the VM networking blade.
2. Review inbound port rules.
3. Remove any direct inbound RDP or SSH rule from Internet.
4. Confirm NSG rules do not allow broad management access.

Checkpoint: management access is not exposed directly to the Internet.

---

## Step 4 - Configure Just-in-Time VM access

1. Open **Microsoft Defender for Cloud**.
2. Select **Workload protections**.
3. Open **Just-in-time VM access**.
4. Add the VM if Defender plan permissions allow it.
5. Configure allowed ports and approved source IP ranges.

If JIT is unavailable, record: `JIT requires Defender for Servers and sufficient Defender for Cloud permissions.`

---

## Step 5 - Review disk encryption options

1. Open the VM **Disks** blade.
2. Review encryption settings.
3. Identify platform-managed keys and customer-managed key options.
4. Review encryption at host if available.
5. Record which controls would be required for a high-security workload.

---

## What you learned

- How Bastion reduces VM management exposure.
- How JIT limits management ports to approved time windows.
- How NSGs, Defender for Cloud, and encryption combine for VM security.
- How to choose between platform-managed and customer-managed encryption.

