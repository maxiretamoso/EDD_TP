from sorted_table_map import SortedTableMap

def main():
    stm = SortedTableMap()

    # metodo __setitem__
    stm['clave1'] = 'San Lorenzo'
    stm['clave3'] = 'Boca'
    stm['clave2'] = 'River'
    stm['clave5'] = 'Independiente'
    stm['clave4'] = 'Racing'
    
    # metodo __getitem__
    print(f"\n{stm['clave1']}\n")   

    # metodo __len__
    print(f"{len(stm)}\n") 

    # metodo __del__
    del stm['clave5']
    print(f"{len(stm)}\n")

    #metodo __iter__ e __iterItems__ 
    print(f"{list(stm)}\n")   

    for item in stm.iter_items():
        print(f"{item}\n")   

if __name__ == "__main__":
    main()