# part 1
'''
agent={'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
print(agent["name"])
print(agent.get("level"))
print(agent.get(0))
agent["score"]=95
print(agent)
agent["level"]=5
print(agent)
del agent["active"]
print(agent)
print(agent.keys())
print(agent.values())
print(agent.items())
print(True) if "score" in agent else print(False)
scores={'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
print(max(scores,key=scores.get))
new_agent=agent.copy()
new_agent["level"]=999
print(agent, new_agent)
# part 2

# 1
conflig={}
con1=conflig.setdefault("tineout",30)
print(conflig)
con2=conflig.setdefault("tineout",50)
print(conflig)
# 2

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(d1|d2)
'''
#3
d1 = {'a': 1, 'b': 2}
print(d1.pop('a'))
missing= d1.pop('y', "no key")
print(missing)
#4
nested={'server': {'host': 'localhost', 'port': 8080}}
print(nested["server"]["port"])