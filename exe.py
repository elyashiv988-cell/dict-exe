# part 1
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
