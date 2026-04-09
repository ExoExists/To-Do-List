def lineBreak():
    print('-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~')

def toDoList(userAction,taskList):

    if userAction=="1":
        lineBreak()
        if taskList==[]:
            print("You have no tasks")
        else:
            print("~-~-~-To Do List-~-~-~")
            for index in taskList:       
                print(str(taskList.index(index)+1) + ". " + index)

    elif userAction=="2":
        lineBreak()
        task=input("What task would you like to add: ")
        if task in taskList:
            print("That item is already in the list")
        else:
            if taskList == []:
                taskPriority=1
            else:
                taskPriority=int(input("What is the priority of the task: "))
            taskList.insert(taskPriority-1,task)

        lineBreak()
        print("~-~-~-To Do List-~-~-~")
        for index in taskList:       
            print(str(taskList.index(index)+1) + ". " + index)
    elif userAction=="3":
        lineBreak()
        if taskList==[]:
            print("You have no tasks")
        else:
            removeTask=int(input("What task would you like to remove(Write the task #): "))
            if taskList[removeTask-1] in taskList:
                taskList.remove(taskList[removeTask-1])
                print("Task Removed!")
            else:
                print("That task is not in the list")
taskList=[]

while True:
    lineBreak()
    userAction=input("Options: \n1. View Tasks\n2. Add Tasks\n3. Remove Tasks\n4. Exit program\nWhat would you like to do: ")
    if userAction=='4':
        lineBreak()
        print("Thanks for using the To Do List program!")
        break
    toDoList(userAction,taskList)  
    