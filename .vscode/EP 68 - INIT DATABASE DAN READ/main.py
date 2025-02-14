import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt" : os.system("cls")
        
    print("SELAMATA DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("="*24)
    
    # check database itu ada atau tidak
    CRUD.init_consule()

    while(True):
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt" : os.system("cls")
        
        print("SELAMATA DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("="*24)

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data")

        use_option = input("Pilih Opsi : ")

        match use_option:
            case "1": CRUD.read_console()
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        is_done = input("Apakah Selesai (y/n)? ")
        if is_done == "y" or is_done == "Y":
            break

    print("Program Berakhir, Terima Kasih")






