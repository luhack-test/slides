# Rusty Nails Ltd Network Spec

## Current State

There are 6 planes in the network, each with a different VLAN and IP range.

| VLAN | Plane       | IP Range    |
|------|-------------|-------------|
| 10   | Edge        | 172.16.10.x |
| 20   | Honeypot    | 172.16.20.x |
| 30   | Data        | 172.16.30.x |
| 40   | Finance     | 172.16.40.x |
| 50   | Engineering | 172.16.50.x |
| 60   | Executive   | 192.168.1.x |

## Known Issues

- Secretary PC appears to have been connected to the Data plane, and cannot
  access anything.
- Honeypot can connect back to the Edge plane
- BYOD system has been set up on the Finance plane.
- Firewalls haven't been configured.

## Task

- Connect the Secretary PC to the Executive Plane
- Ensure the honeypot can receive a connection but not transmit
- Set up a separate BYOD plane
- Configure Firewalls
- Items have been left to create an R&D plane within the packet tracer file,
  build this plane and configure it as you see fit.