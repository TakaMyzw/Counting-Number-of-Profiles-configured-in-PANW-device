Counting Number of Profiles configured in PANW device
==================

Counting number of security profiles.

This script counts number of security profiles is configured in PANW device with parsing exported XML configuration file from PANW firewall. Security Profiles are virus, spyware, vulnerability, URL filtering, file blocking, dos protection and data filtering.

Requirements:

* PAN-OS version: 5.0 (only tested version, but may work with previous/next PAN-OS versions)
* PANW Firewall appliance: all, including VM series

How to use this script:

1. Export an XML configuration file from PANW firewall
2. Place the XML file to your computer
3. Run this script. The first parameter is the filename

$ count_num_of_profiles.py filename

Output format:
```
[5, 2, 3, 3, 3, 2, 0]
18
```
The first line is subtotal of each profile and the second line is the total number of profiles.

Note:
* Default profile isn't included in the count.
* In VSYS environment, this script counts VSYS specific profiles as well as shared profiles
