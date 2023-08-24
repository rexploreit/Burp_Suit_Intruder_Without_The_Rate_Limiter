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


from argparse import ArgumentParser, RawDescriptionHelpFormatter
from inspect import cleandoc
from pathlib import Path


class Intruder:
    @property
    def copyright_notice(self):
        return """Copyright (C) 2023 Mr. Kelsey
        This program comes with ABSOLUTELY NO WARRANTY; please see license 
        for details. This is free software, and you are welcome to redistribute
        it under certain conditions; again, please see license for details."""

    @property
    def tooltip(self):
        return f"""
        Attack Types
        sniper - This attack places each payload into each payload position in turn. It uses a single payload set. (refined fuzzing)
        battering-ram - This attack places the same payload into all of the defined payload positions simultaneously. It uses a single payload set. (bulk fuzzing)
        pitchfork - This attack iterates through a different payload set for each defined position. Payloads are placed into each position simultaneously. (cred stuffing)
        cluster-bomb - This attack iterates through a different payload set for each defined position. Payloads are placed from each set in turn, so that all payload combinations are tested. (brute force)

        Payload types
        list - Simple List: requires additional parameters -p1 [-p2]
        file - Runtime File: requires additional parameters -f
        custom - Custom Iterator
        sub - Character substitution
        case - Letter Case Modification
        grep - Recursive Grep
        uni - Illegal Unicode
        blocks - Character Blocks
        num - Numbers
        date - Dates
        brute - Brute Forcer
        null - Null Payloads
        frob - Character Frobber
        bit - Bit Flipper
        user - Username Generator

        Extra parameters
        p1 - Primary Payload List: needed for all attack types when using --list payload type
        p2 - Secondondary Payload List: needed with -p and -c when using --list payload type
        f - File: A runtime file read line by line to provide 

        Settings
        --view-tooltip - Show this very tooltip so you can see all your options
        --view-settings - View default settings
        --create-config - Create new intruder.conf file
        --use-config - Override deault settings with settings from intruder.conf
        
        Examples:
        {Path(__file__).name} attack sniper num ./burp.request
        {Path(__file__).name} attack b list ./burp.request p1 ./payload.list
        {Path(__file__).name} attack pitchfork list ./burp.request p1 ./p1.list p2 ./p2.list
        {Path(__file__).name} config --view-settings
        """
    
    def __init__(self):
        self.config_path = None
        self.attack_type = None
        self.payload_type = None
        self.request_file_path = None
        self.first_simple_list_payload_path = None
        self.second_simple_list_payload_path = None
        self.runtime_file_path = None
        self.view_settings = False
        self.create_config = False

    def set_attributes_based_on_args(self, args):
        try:
            with open(Path(args.use_config)) as config:
                self.parse_config_file(config)
        except TypeError:
            pass
        except OSError:
            raise

        if hasattr(args, "attack_type"):
            self.attack_type = args.attack_type
        if hasattr(args, "payload_type"):
            self.payload_type =  args.payload_type
        if hasattr(args, "request_file"):
            self.request_file_path = args.request_file
        if hasattr(args, "p1"):
            self.first_simple_list_payload_path = args.p1
        if hasattr(args, "p2"):
            self.second_simple_list_payload_path = args.p2
        if hasattr(args, "f"):
            self.runtime_file_path = args.f
        if hasattr(args, "view_settings"):
            if args.view_settings:
                self.show_settings()
        if hasattr(args, "create_config"):
            if args.create_config:
                self.create_new_config_file()
    
    def wip(self, feature):
        return f"""The **{feature}** feature has not yet been implemented into the tool.  Please feel free to implement this feature and make a pull request on the project"""

    def parse_config_file(self, config):
        print(self.wip("parse_config_file"))

    def show_settings(self):
        print(self.wip("show_settings"))

    def create_new_config_file(self):
        print(self.wip("create_new_config_file"))

    def parse_request_file(self, file_path):
        pass
    

if __name__ == "__main__":
    intruder = Intruder()
    parser = ArgumentParser(
        description="Burp Suite Intruder Without The Rate Limiter",
        formatter_class=RawDescriptionHelpFormatter,
        epilog=cleandoc(intruder.copyright_notice),
    )
    parser.add_argument("--use-config", type=Path, help="use a custom config file to override default settings")
    parser.add_argument("--view-tooltip", action='version', version=cleandoc(intruder.tooltip), help="Show program tooltip to see all tool options")
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    
    subparsers = parser.add_subparsers()
    
    attack_parser = subparsers.add_parser("attack")
    attack_parser.add_argument("attack_type", choices=["s", "sniper", "b", "battering-ram", "p", "pitchfork", "c", "cluster-bomb"],
                               help="Select your attack type")
    attack_parser.add_argument("payload_type", choices=["list", "file", "custom", "sub", "case", "grep", "uni",
                                            "blocks", "num", "date", "brute", "null", "frob", "bit", "user"], help="specify your payload type")
    attack_parser.add_argument("request_file", type=Path, help="The text file to which you saved your Burp Suite request\
                               [example: ./burp.request]")
    
    attack_subparser = attack_parser.add_subparsers()
    simple_list_parser_1 = attack_subparser.add_parser("p1", help="the list of payloads you would like to try: required for list payload type")
    simple_list_parser_1.add_argument("p1", help="The path to your first list")

    simple_list_subparser = simple_list_parser_1.add_subparsers()
    simple_list_parser_2 = simple_list_subparser.add_parser("p2", help="your second list: required for pitchfork and cluster bomb attack types")
    simple_list_parser_2.add_argument("p2", help="The path to your second list")

    file_parser = attack_subparser.add_parser("f", help="")
    file_parser.add_argument("f", help="")
    
    config_parser = subparsers.add_parser("config")
    config_parser.add_argument("--view-settings", action='store_true', help="View default settings")
    config_parser.add_argument("--create-config", action='store_true', help="Create a new config file to change any settings")

    args = parser.parse_args()
    intruder.set_attributes_based_on_args(args)
