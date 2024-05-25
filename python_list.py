if __name__ == '__main__':
    N = int(input())
    output = []
    commands = []
    for _ in range(N):
        command, *args = input().split(" ") 
        commands.append({"command": command, "args": list(map(int,args))})
    for command in commands:
        if (command.get("command") == 'append'):
            output.append(command.get("args")[0])
        if (command.get("command") == 'insert'):
            output.insert(command.get("args")[0], command.get("args")[1])
        if (command.get("command") == 'remove'):
            output.remove(command.get("args")[0])
        if (command.get("command") == 'sort'):
            output.sort()
        if (command.get("command") == 'pop'):
            output.pop()
        if (command.get("command") == 'reverse'):
            output.reverse()  
        if (command.get("command") == 'print'):
            print(output) 