# part 1
agent={'name': 'Alpha', 'level': 3, 'active': True}
print(agent)
print(agent["name"])
if agent["level"]:
    print(agent.get("level"))
else:
    print(0)
agent["score"]=95
print(agent)