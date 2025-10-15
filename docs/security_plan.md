# Security Plan

This document summarizes the security configuration applied to the Two-Campus Three-Tier Design.  

---

## Layer 2 Security

### DHCP Snooping
- Active on all user VLANs.
- Uplinks marked as **trusted**.
- Prevents rogue DHCP servers.  
**Check:** `show ip dhcp snooping`

### Dynamic ARP Inspection (DAI)
- Enabled on VLANs protected by DHCP Snooping.
- Validates ARP using DHCP bindings; drops spoofed ARP.  
**Check:** `show arp inspection`

### Port Security
- Enabled on all **access ports**.  
- **Default rule:** 1 MAC address, **sticky** enabled, violation mode **shutdown**.  
  - Ensures that each port learns and locks the first connected host.  
- **Exception:** On **AS6**, the port used for remote access allows **up to 5 MACs**,  
  uses **restrict** mode and **no sticky learning** (for multiple management devices).  
**Check:** `show port-security`  

### Unused Ports → Black Hole
- **All unused interfaces** are administratively shut down and assigned to **VLAN 999 (BlackHole)**  
  to isolate accidental or unauthorized access attempts.  
**Check:**  
`show interface status`  
`show vlan brief | include 999`

---

## Administrative Access

### SSH + VTY ACL
- **SSH only** (Telnet disabled).
- VTY **ACL `ADMIN_ACCESS`** allows connections **only** from Management VLANs:  
  - Campus A: **10.0.0.192/28**  
  - Campus B: **10.0.1.192/28**  
**Check:** `show access-lists`

### Local Authentication 
- Local admin user with encrypted password.
- `service password-encryption` enabled globally.
- Idle sessions close after **10 minutes** (`exec-timeout 10`).  
**Check:** `show running-config | include username`

---
