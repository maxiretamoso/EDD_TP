from linked_list_ext import LinkedListExt

def main():
    linkedList = LinkedListExt()
    elementos = [1,2,3,4,5,6,7]
    
    for i in elementos:
        linkedList.append(i)
        
    #lista:
    print(f'\nLista: {linkedList}\n')
    
    #lista con metodo reverse:
    linkedList.__reversed__()
    print(f'Lista con reverse: {linkedList}\n')
    
    #lista con metodo pop:
    linkedList.pop()
    print(f'Lista con pop: {linkedList}\n')
    
    #lista con metodo addfirst:
    linkedList.add_first(2)
    print(f'Lista con addfirst: {linkedList}\n')
    
    #lista con metodo iadd:
    linkedList.__iadd__([1,2,'ocho'])
    print(f'Lista con iadd: {linkedList}\n')
    
if __name__ == '__main__':
    main()    