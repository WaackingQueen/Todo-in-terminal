#!/usr/bin/python3
import sys, getopt
import caldav


def main():
    if len(sys.argv) == 1 :
        print ("Usage: XXX")
        return
 
    
    # for faster loading
    from todo_utils import get_todos, delete_todo, add_todo

    # Parse arguments    
    command = sys.argv[1]
    arg = ' '.join(sys.argv[2:])

    if command == "a":       
        add_todo(arg)
    
    elif command == "r":
        i = int(sys.argv[2])
        l = get_todos()

        todo, link = l[i]  # (text, link)
        
        delete_todo(link)

        
    elif command == "l":
        i = 0
        for todo in get_todos() :
            print (f"{i}. {todo[0]}")
            i = i+1    


main()
