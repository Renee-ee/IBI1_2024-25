import xml.sax
from datetime import datetime

# Define a custom ContentHandler called GOHandler
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        # Variables to hold data for each term
        self.term_id = ""
        self.term_name = ""
        self.namespace = ""
        self.is_a_count = 0
        # Check whether inside a <term> element
        self.in_term = False
        # Dictionary storing term_id, term_name, is_a_count per namespace
        self.max_count = {
            "molecular_function": {"id": "", "name": "", "count": 0},
            "biological_process": {"id": "", "name": "", "count": 0},
            "cellular_component": {"id": "", "name": "", "count": 0}
        }
    # Start by entering an element
    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "term":
            self.in_term = True
            self.term_id = ""
            self.term_name = ""
            self.namespace = ""
            self.is_a_count = 0
    # take information out of the elements, using the characters function
    def characters(self, content):
        if self.in_term:
            if self.current_data == "id":
                self.term_id += content
            elif self.current_data == "name":
                self.term_name += content
            elif self.current_data == "namespace":
                self.namespace += content
            elif self.current_data == "is_a":
                self.is_a_count += 1
    # Eding elements
    def endElement(self, tag):
        if tag == "term":
            ns = self.namespace.strip()
            # Update max_count if this term has more is_a entries
            if ns in self.max_count:
                if self.is_a_count > self.max_count[ns]["count"]:
                    self.max_count[ns]["count"] = self.is_a_count
                    self.max_count[ns]["id"] = self.term_id.strip()
                    self.max_count[ns]["name"] = self.term_name.strip()
            # Reset for next term
            self.in_term = False
        # Clear the current_data after each element ends
        self.current_data = ""


start = datetime.now()

# To open the file
parser = xml.sax.make_parser() # create an XMLReader
parser.setFeature(xml.sax.handler.feature_namespaces, 0) # turn off namespaces
# Set the ContentHandler called 'Handler'
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

# Output
for ns in Handler.max_count:
    print(ns + ":")
    print("  ID: " + Handler.max_count[ns]["id"])
    print("  Name: " + Handler.max_count[ns]["name"])
    print("  is_a count: " + str(Handler.max_count[ns]["count"]))
    print("")

# record the time taken
end = datetime.now()
print("SAX runtime:", end - start)

# DOM runtime: 0:00:14.909061
# SAX runtime: 0:00:02.367319
# For this xml, SAX run much faster than DOM