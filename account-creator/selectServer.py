servers = {1:{"EUNE"},2:{"EUW"},3:{"NA"},4:{"RU"},5:{"BR"},6:{"JP"},7:{"TR"},8:{"LAN"},9:{"LAS"},10:{"OCE"}}

def selectServer():
    print("select server please:")
    for x in servers:
        print(servers[x])
    selected = input()
    return selected
selectServer()

#TO DO IT BETTER