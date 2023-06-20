# your code goes here!

import re

class EmailAddressParser:
    
    email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    
    def __init__(self, emails):
        self.emails = emails

# Class EmailAddressParser in email_address_parser.py instantiates with a single argument, a string.   

    def parse(self):
        strings = re.split(r',|\s', self.emails)

# Class EmailAddressParser in email_address_parser.py contains a method called "parse". 
        
        parsed_emails = set()
        for string in strings:
            if self.email_regex.fullmatch(string):
                parsed_emails.add(string)

        return sorted(list(parsed_emails))
    
# Class EmailAddressParser in email_address_parser.py finds emails with spaces in between.                                                               
# Class EmailAddressParser in email_address_parser.py finds emails with commas in between.                                                             
# Class EmailAddressParser in email_address_parser.py finds emails with commas and spaces in between.                                               
# Class EmailAddressParser in email_address_parser.py finds emails with commas and spaces in between and removes non-email strings.  
                