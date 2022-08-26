listBarang  = [
    {
        'Kode Item': 'DS001AD',
        'Nama Item': 'ROG G14',
        'Merk': 'Asus',
        'Jenis': 'Laptop',
        'Harga' : 26000000,
        'Stok' : 100
    },
    {
        'Kode Item': 'DS002BE',
        'Nama Item': 'Blade 15',
        'Merk': 'Razer',
        'Jenis': 'Laptop',
        'Harga' : 40000000,
        'Stok' : 50
    },
    {
        'Kode Item': 'DS003CF',
        'Nama Item': 'AlienwareX17',
        'Merk': 'Dell',
        'Jenis': 'Laptop',
        'Harga' : 62000000,
        'Stok' : 50
    }
]

def halo():
    print(f'''
        Selamat Datang di Aplikasi List Item Aria Storage 
        
        List menu:

        1. Melihat Daftar Stok Item
        2. Menambahkan Daftar Stok Item
        3. Update Daftar Stok Item
        4. Menghapus Daftar Stok Item
        5. Keluar
    ''')

def showItem1(): #fungsi untuk melihat semua item
    print('\n-----  List Stock Barang  -----\n')
    print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
    for i in range(len(listBarang)):
        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))

def showKodeItem(): #fungsi untuk melihat berdasarkan pencarian kode item
        kodeItem = input('\n   Masukkan kode Item : ')
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listBarang)):
            if kodeItem == listBarang[i]['Kode Item']:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                break
        else:
            print('\n     "Data tidak ditemukan"')

def showKeyWord(): #fungsi untuk melihat berdasarkan pencarian nama/jenis/merk
        Search = input('\n     Masukkan keyword : ')
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listBarang)):
            if  Search == listBarang[i]['Nama Item'] or Search == listBarang[i]['Merk'] or Search == listBarang[i]['Jenis']:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))

def showHarga(): #fungsi untuk melihat berdasarkan range harga
        Harga1 = int(input('\n     Masukkan harga minimum : '))
        Harga2 = int(input('     Masukkan harga maksimum : '))
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listBarang)):
            if Harga1 <= listBarang[i]['Harga'] <= Harga2:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))

def showStok(): #fungsi untuk melihat berdasarkan jumlah stok
        Stok = int(input('\n     Masukkan stok maksimum yang dicari : '))
        print('\n----- List Stock Barang -----\n')
        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
        for i in range(len(listBarang)):
            if listBarang[i]['Stok'] <= Stok:
                print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))

def showItem2(): #fungsi untuk pencarian dengan kata kunci
    while True:
        menu_showItem2 = input ('''
        1. Pencarian menggunakan kode item 
        2. Pencarian menggunakan keyword
        3. Pencarian menggunakan range harga
        4. Pencarian menggunakan jumlah stok tersedia
        5. Kembali ke menu sebelumnya
        Ketik nomor menu yang ingin dijalankan : ''')

        if menu_showItem2 == '1' :
            showKodeItem()
        elif menu_showItem2 == '2' :
            showKeyWord()
        elif menu_showItem2 == '3':
            showHarga()
        elif menu_showItem2 == '4':
            showStok()
        elif menu_showItem2 == '5':
            break

def readData(): #fungsi menampilkan read data
    while True:
        menuRead = input('''
        1. Tampilkan seluruh data stok item
        2. Tampilkan data pencarian kata kunci
        3. Kembali ke menu utama
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuRead == '1' :
            showItem1()
        elif menuRead == '2' :
            showItem2()
        elif menuRead == '3' :
            break
            
def addItems(): #fungsi menambahkan data / create data
    while True:
        inKode = input('\n        Masukkan kode item : ')
        inItem = input('        Masukkan nama item : ')
        inMerk = input('        Masukkan nama merk : ')
        inJenis = input('        Masukkan nama Jenis : ')
        inHarga = int(input('        Masukkan harga : '))
        inStok = int(input('        Masukkan jumlah stok : '))
        tambahan = {
        'Kode Item' : '{}'.format(inKode),
        'Nama Item' : '{}'.format(inItem),
        'Merk' : '{}'.format(inMerk),
        'Jenis' : '{}'.format(inJenis),
        'Harga' : '{}'.format(inHarga),
        'Stok' : '{}'.format(inStok)
    }
        print('\n        Item yang ditambahkan adalah : ',tambahan)
        cekCreate = input('\n        Mohon dikonfirmasi kembali apakah data yang ingin ditambahkan sudah benar? (Y/N) : ').lower()
        if cekCreate == 'y':
            listBarang.append(tambahan)
            print('\n        "Item berhasil ditambahkan"')
            break
        elif cekCreate == 'n':
            print('\n        "Item tidak ditambahkan"')
            break
        else:
            break
        
def createData(): #fungsi menampilkan menu add / create data
    while True:
        menuCreate = input('''
        1. Tambahkan data item baru
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')
    
        if menuCreate == '1' :
            addItems()
        elif menuCreate == '2' :
            break

def Update(): #fungsi untuk update data
    codeUpdate = input('\n        Masukkan kode barang yang ingin diupdate : ')
    print('\n----- List Stock Barang -----\n')
    for i in range(len(listBarang)):
        if codeUpdate == listBarang[i]['Kode Item']:
            print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
            print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
            cekUpdate = input('\n        Mohon dikonfirmasi kembali apakah data yang ingin diupdate sudah benar? (Y/N) : ' ).lower()
            if cekUpdate == 'y':
                while True:
                    cmUpdate = input('''
                    1. Update Kode item
                    2. Update Nama item
                    3. Update Merk item
                    4. Update Jenis item
                    5. Update Harga item
                    6. Update Stok item
                    7. Selesai update data
                    
                    Ketik nomor menu yang ingin dijalankan : ''')
                   
                    if cmUpdate == '1':
                        listBarang[i]['Kode Item'] = input('\n        Update kode : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '2':
                        listBarang[i]['Nama Item'] = input('\n        Update nama : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '3':
                        listBarang[i]['Merk'] = input('\n        Update merk : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '4':
                        listBarang[i]['Jenis'] = input('\n        Update Jenis : ')
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '5':
                        listBarang[i]['Harga'] = int(input('\n        Update harga : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '6':
                        listBarang[i]['Stok'] = int(input('\n        Update stok : '))
                        print('\n        "Data berhasil diupdate"\n')
                        print(' '+'Nomor\t| Kode Item\t|  Nama Item\t\t|   Merk\t|  Jenis\t|  Harga\t|  Stok')
                        print('   {}\t| {}\t|  {}\t\t|   {}\t|  {}\t|  {}\t|  {}\t'.format(i+1,listBarang[i]['Kode Item'],listBarang[i]['Nama Item'],listBarang[i]['Merk'],listBarang[i]['Jenis'],listBarang[i]['Harga'],listBarang[i]['Stok']))
                    elif cmUpdate == '7':
                        break
            elif cekUpdate == 'n':
                print('\n        "Data tidak diupdate"')
                break
            else:
                print('\n        "Perintah yang anda masukkan salah"')
                break

def updateData(): #fungsi menampilkan menu update data
    while True:
        menuUpdate = input('''
        1. Update data
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuUpdate == '1' :
            Update()
        elif menuUpdate == '2':
            break

def Delete(): #fungsi delete data
    while True:
        codeDelete = input('\n        Masukkan kode item barang yang ingin dihapus : ')
        for i in range(len(listBarang)):
            if codeDelete == listBarang[i]['Kode Item']:
                print('\n        Item yang ingin dihapus adalah : ', listBarang[i])
                cekDelete = input('\n        Apakah yakin ingin menghapus data ini? (Y/N) : ')
                if cekDelete == 'y':
                    del listBarang[i]
                    print('\n        "Data berhasil dihapus"') 
                    break
                elif cekDelete == 'n':
                    print('\n        "Data tidak terhapus"')
                    break
                else:
                    print('\n        "Perintah yang anda masukkan salah"')
                    break

        else:
            print('\n        "Data tidak ditemukan"')
        break

def deleteData(): #fungsi menampilkan menu delete data
    while True:
        menuDelete = input('''
        1. Delete Data
        2. Kembali ke menu utama
        
        Ketik nomor menu yang ingin dijalankan : ''')

        if menuDelete == '1' :
            Delete()
        elif menuDelete == '2':
            break

def keluar(): #fungsi untuk keluar dari aplikasi
    print(f'''
        \nTerima kasih telah berkunjung ke Aplikasi List Item Aria Storage
        \n              ==========Sampai Jumpa==========''')

while True: #fungsi menu awal
    halo()
    pilihan_menu = (input('Ketik nomor menu yang ingin dijalankan : '))
    if pilihan_menu =='1':
        readData()
    if pilihan_menu == '2':
        createData()
    if pilihan_menu == '3':
        updateData()
    if pilihan_menu =='4':
        deleteData()
    elif pilihan_menu =='5':
        keluar()
        break
    else:
        print('Pilihan yang anda masukan salah')
        continue