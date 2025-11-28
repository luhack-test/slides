# Cisco IOS command sheet

You don't need to write the full command, just enough to be unique

`<TAB>` to complete the command

`?` to show all possible completions

## Command Modes

| EXEC Mode            | Prompt               | Enter                                                                  | Exit   | 
|----------------------|----------------------|------------------------------------------------------------------------|--------|
| User                 | `>`                  | the default                                                            |        |
| Privileged           | `#`                  | `enable`                                                               | `exit` |
| Global configuration | '(config)#`          | `configure terminal`                                                   | `end`  |
| Interface            | `(config-if)#`       | `interface <interface>`                                                | `exit` |
| VLAN                 | `(config-vlan)#`     | `vlan <number>`                                                        | `exit` |
| Access list          | `(config-ext-nacl)#` | `access-list <number> <permit/deny> <protocol> <source> <destination>` | `exit` |

## Device Management

Run these commands from the global configuration mode.

`hostname <NAME>` to assign the device a memorable name

`enable password <password>` create a password

## Interface Management

Run these commands from the global configuration mode.

`show ip interface brief` to show all interfaces

`interface <interface>` to enter interface configuration mode

`ip address <IP> <subnet>` to assign an IP address to an interface

`no shutdown` to enable an interface

`switchport mode access` to set the interface to access mode

`switchport access vlan <VLAN_ID>` to assign the interface to a specific VLAN

`interface range <interface_range>` to configure multiple interfaces at once

## VLANs

Run these commands from the global configuration mode.

`show vlan brief` to show all VLANs

`vlan <number>` to enter VLAN configuration mode

`name <name>` to assign a name to a VLAN

## Firewalls

Run these commands from the global configuration mode.

`show access-lists` to show all access lists

`access-list <number> permit <protocol> <source> <destination>` to create an access list

`access-group <number> in/out` to apply an access list to an interface

`ip access-list extended <name>` to create a named access list

`permit <protocol> <source> <destination>` to permit traffic in the access list

`deny <protocol> <source> <destination>` to deny traffic in the access list

`interface <interface>` to apply the access list to an interface

`ip access-group <name> in/out` to apply the access list to an interface

# Abbreviations

- `Fa0/0` = `FastEthernet0/0`
- `Gi0/0` = `GigabitEthernet0/0`
- BYOD = Bring Your Own Device
- MLS = Multi-Layer Switch