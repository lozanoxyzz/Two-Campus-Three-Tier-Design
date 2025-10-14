# VLAN and Subnet Plan

This document defines the VLAN IDs, names, associated subnets, default gateways, and their purpose in the Two-Campus Three-Tier Design.

---

## Campus A

| Campus   | VLAN ID | Name           | Subnet        | Gateway    | Description                     |
|----------|---------|----------------|---------------|------------|---------------------------------|
| Campus A | 10      | IT             | 10.0.0.0/26   | 10.0.0.1   | IT department                   |
| Campus A | 20      | Engineering    | 10.0.0.64/26  | 10.0.0.65  | Engineering department          |
| Campus A | 30      | Administration | 10.0.0.128/26 | 10.0.0.129 | Administration and Finance      |
| Campus A | 99      | Admin-A        | 10.0.0.192/28 | 10.0.0.193 | Network management VLAN         |
| Campus A | 999     | BlackHole      | N/A           | N/A        | Isolated VLAN for unused ports  |
| Campus A | 1000    | Native         | N/A           | N/A        | Native VLAN for trunks          |

---

## Campus B

| Campus   | VLAN ID | Name           | Subnet        | Gateway    | Description                     |
|----------|---------|----------------|---------------|------------|---------------------------------|
| Campus B | 40      | IT             | 10.0.1.0/26   | 10.0.1.1   | IT department                   |
| Campus B | 50      | Engineering    | 10.0.1.64/26  | 10.0.1.65  | Engineering department          |
| Campus B | 60      | Administration | 10.0.1.128/26 | 10.0.1.129 | Administration and Finance      |
| Campus B | 199     | Admin-B        | 10.0.1.192/28 | 10.0.1.193 | Network management VLAN         |
| Campus B | 999     | BlackHole      | N/A           | N/A        | Isolated VLAN for unused ports  |
| Campus B | 1000    | Native         | N/A           | N/A        | Native VLAN for trunks          |

## Point-to-Point Links (IPv4)

| Link | From Device | From Interface | From IP        | To Device | To Interface | To IP          | Network         |
|------|-------------|----------------|----------------|-----------|--------------|----------------|-----------------|
| L1   | DS1         | e2/1           | 10.0.3.1/30    | CS1       | Gi0/1        | 10.0.3.2/30    | 10.0.3.0/30     |
| L2   | DS2         | e2/1           | 10.0.3.5/30    | CS1       | Gi0/2        | 10.0.3.6/30    | 10.0.3.4/30     |
| L3   | DS3         | e2/1           | 10.0.3.9/30    | CS2       | Gi0/1        | 10.0.3.10/30   | 10.0.3.8/30     |
| L4   | DS4         | e2/1           | 10.0.3.13/30   | CS2       | Gi0/2        | 10.0.3.14/30   | 10.0.3.12/30    |
| L5   | CS1         | Po1            | 10.0.3.18/30   | CS2       | Po1          | 10.0.3.17/30   | 10.0.3.16/30    |
