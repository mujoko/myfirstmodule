# fungsi register to Interactive English
def daftar(name, tgl , gender , school, parent, religion, address):
    if gender=="Laki-Laki":
        print("Selamat Datang di IE Tuan "+name+ " Biodata kamu adalah sebagai berikut")
    else:
        print("Selamat Datang di IE Nona "+name +" Biodata kamu adalah sebagai berikut")
    print("Nama             : "+name)
    print("Tanggal lahir    : "+tgl)
    print("Jenis Kelamin    : "+gender)
    print("Asal Sekolah     : "+school)
    print("Orang Tua        : "+parent)
    print("Agama            : "+religion)
    print("Alamat           : "+address)
    

daftar("Mujoko","26 June 1980", "Laki-Laki","IPB" , "Wiyono", "Islam", "Kl Benda Cicurug")
    
  