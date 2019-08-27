# Web Trolling Framework

The Web Trolling Framework (WTF) is an idea of creating web sites with known/easy to find vulnerabilities for the purpose of deceiving attackers into giving away their precense.

The current release of WTF contains a deceptive SSL VPN page with a fake credential harvesting flaw where the page provides different response codes for an invalid username and an invalid password.  Fully successful logins are redirected to a fake MfA challenge.  All connection attempts are stored in a database for reporting or automated blocking of the attacker.

This is a very early release, with much more planned.

See SetupNotex.txt for configuration instructions.