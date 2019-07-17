#!/usr/bin/python3
import sys, getopt
import caldav


def main():
    if len(sys.argv) == 1 :
        print ("Usage: ./todo.py 'a' to add, 'l' list, 'r' remove")
        return
    
    # for faster loading
    from todo_utils import get_todos, delete_todo, add_todo, show_all

    # Parse arguments    
    command = sys.argv[1]
    arg = ' '.join(sys.argv[2:])

    if command == "a":       
        add_todo(arg)
        show_all() 
    
    elif command == "r":
        i = int(sys.argv[2])
        l = get_todos()

        todo, link = l[i]  # (text, link)
        
        delete_todo(link)

    elif command == "ra":
        i = 0
        l = get_todos()
        for todo in get_todos():
            todo, link = l[i]
            delete_todo(link)
            i = i+1
             
        print("Deletion completed")    

    elif command == "l":
        if not get_todos():
            print ('No TODOs')
        else :
            show_all()  


main()