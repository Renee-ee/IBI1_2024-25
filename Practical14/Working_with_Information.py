#=============================DOM================================
import xml.dom.minidom
from datetime import datetime

# Start timer
dom_start = datetime.now()

doc = xml.dom.minidom.parse("go_obo.xml")
terms = doc.getElementsByTagName("term")

# Dictionary storing term_id, term_name, is_a_count per namespace
max_count = {
    "molecular_function": {"id": "", "name": "", "count": 0},
    "biological_process": {"id": "", "name": "", "count": 0},
    "cellular_component": {"id": "", "name": "", "count": 0}
}

for term in terms:
    # Extract terms from tags
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue.strip()
    is_a= term.getElementsByTagName("is_a")
    is_a_count= len(is_a)
    # Update max_count if current term has more is_a entries than previous max
    if namespace in max_count:
        if is_a_count > max_count[namespace]["count"]:
            max_count[namespace]["count"] = is_a_count
            max_count[namespace]["id"] = term_id
            max_count[namespace]["name"] = term_name

print('===========DOM==============')
for ns in max_count:
    print(ns + ":")
    print("  ID: " + max_count[ns]["id"])
    print("  Name: " + max_count[ns]["name"])
    print("  is_a count: " + str(max_count[ns]["count"]))
    print("")

# Stop timer and print execution time
dom_end = datetime.now()
dom_time = dom_end - dom_start
print("DOM runtime:", dom_time)
print('\n')

#==============================SAX================================
import xml.sax

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

# Start timer
sax_start = datetime.now()

# To open the file
parser = xml.sax.make_parser() # create an XMLReader
parser.setFeature(xml.sax.handler.feature_namespaces, 0) # turn off namespaces
# Set the ContentHandler called 'Handler'
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.parse('go_obo.xml')

# Output
print('===========SAX==============')
for ns in Handler.max_count:
    print(ns + ":")
    print("  ID: " + Handler.max_count[ns]["id"])
    print("  Name: " + Handler.max_count[ns]["name"])
    print("  is_a count: " + str(Handler.max_count[ns]["count"]))
    print("")

# record the time taken
sax_end = datetime.now()
sax_time = sax_end - sax_start
print("SAX runtime:", sax_time)
print('\n')

#==============Compare time taken of two APIs==========================
print('===========Compare==============')
if dom_time > sax_time:
    print("For this xml, SAX runs faster than DOM")
elif dom_time == sax_time:
    print("For this xml, SAX runs much as same fast as DOM")
else:
    print("For this xml, DOM runs faster than SAX")
# For this xml, SAX run much faster than DOM
