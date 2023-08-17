#!/usr/bin/env python3


# Copyright (C) 2023 Mr. Kelsey

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from argparse import ArgumentParser


copyright_notice = """Copyright (C) 2023 Mr. Kelsey
This program comes with ABSOLUTELY NO WARRANTY; please see license 
for details. This is free software, and you are welcome to redistribute
it under certain conditions; again, please see license for details."""


tooltip = """
Attack Types
-s Sniper - This attack places each payload into each payload position in turn. It uses a single payload set. (refined fuzzing)
-b Battering Ram - This attack places the same payload into all of the defined payload positions simultaneously. It uses a single payload set. (bulk fuzzing)
-p Pitchfork - This attack iterates through a different payload set for each defined position. Payloads are placed into each position simultaneously. (cred stuffing)
-c Cluster Bomb - This attack iterates through a different payload set for each defined position. Payloads are placed from each set in turn, so that all payload combinations are tested. (brute force)

Payload types
--list Simple List - include -p1 [-p2]
-p1 Primary Payload List - needed for all attack types
-p2 Secondondary Payload List - needed with -p and -c
--file Runtime File - include -f
-f File
--custom Custom Iterator
--sub Character substitution
--case Letter Case Modification
--grep Recursive Grep
--uni Illegal Unicode
--blocks Character Blocks
--num Numbers
--date Dates
--brute Brute Forcer
--null Null Payloads
--frob Character Frobber
--bit Bit Flipper
--user Username Generator

Settings
## TODO ##
--settings View default settings
--create-config Tkinter user interface to create new intruder.conf file
--config Override deault settings with settings from intruder.conf
"""

if __name__ == "__main__":
    print(copyright_notice)
    print(tooltip)
