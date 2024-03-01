import json

f = open('data.json', 'r').read()
x = json.loads(f)
print ("Interface Status")
print ("================================================================================")
print ("DN                                                 Description           Speed    MTU") 
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, sort_keys=True))
a = x["imdata"]
for i in a:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    descr = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
print("{0:50} {1:20} {2:7} {3:6}".format(dn, descr, speed, mtu))