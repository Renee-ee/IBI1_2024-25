import xml.dom.minidom
from datetime import datetime

start = datetime.now()

doc = xml.dom.minidom.parse("go_obo.xml")
terms = doc.getElementsByTagName("term")

# Dictionary storing term_id, term_name, is_a_count per namespace
max_count = {
    "molecular_function": {"id": "", "name": "", "count": 0},
    "biological_process": {"id": "", "name": "", "count": 0},
    "cellular_component": {"id": "", "name": "", "count": 0}
}

for term in terms:
    term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue
    term_name = term.getElementsByTagName("name")[0].firstChild.nodeValue
    namespace = term.getElementsByTagName("namespace")[0].firstChild.nodeValue.strip()
    is_a= term.getElementsByTagName("is_a")
    is_a_count= len(is_a)
    if namespace in max_count:
        if is_a_count > max_count[namespace]["count"]:
            max_count[namespace]["count"] = is_a_count
            max_count[namespace]["id"] = term_id
            max_count[namespace]["name"] = term_name

for ns in max_count:
    print(ns + ":")
    print("  ID: " + max_count[ns]["id"])
    print("  Name: " + max_count[ns]["name"])
    print("  is_a count: " + str(max_count[ns]["count"]))
    print("")

end = datetime.now()
print("DOM runtime:", end - start)