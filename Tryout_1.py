
k=int(input('Berapa kali proses penginputan: '))
nim_list=[]
nama_list =[]
alamat_list =[]
asal_sekolah_list =[]
kode_prod_list =[]
nilai_ipk1_list = []
uts_list =[]
uas_list =[]
tm_list =[]
nilai_ips_list =[]
nilai_ipk2_list =[]
beasiswa_list =[]
nestedlist=[nim_list,nama_list,alamat_list,asal_sekolah_list,kode_prod_list,nilai_ipk1_list,uts_list,uas_list,tm_list,nilai_ipk2_list,nilai_ips_list,beasiswa_list]
beasiswa = ''
for i in range(k):
    print('=========================''Data Siswa',i+1,'=========================')
    a=(input('Nim : '))
    b=(input('Nama : '))
    c=(input('Alamat : '))
    d=(input('Asal Sekolah : '))
    e=(input('Kode Prodi : '))
    nilai_ipk1=int(input('Nilai IPK awal : '))

    uts=int(input('Nilai UTS : '))
    uas=int(input('Nilai  UAS: '))
    tm=int(input('Nilai TM : '))



    nim_list.append(a)
    nama_list.append(b)
    alamat_list.append(c)
    asal_sekolah_list.append(d)
    kode_prod_list.append(e)
    nilai_ipk1_list.append(nilai_ipk1)
    uts_list.append(uts)
    uas_list.append(uas)
    tm_list.append(tm)
    nilai_ipk2 = ((0.3*uts)+(0.3*tm)+(0.4*uas))
    nilai_ipk2_list.append(nilai_ipk2)
    nilai_ips = (nilai_ipk1 + nilai_ipk2) / 2
    nilai_ips_list.append(nilai_ips)

    if e == 'TI' or 'SI':
        if nilai_ipk2 >75 and nilai_ipk2 <85:
            beasiswa = '20%'
            beasiswa_list.append(beasiswa)
        elif nilai_ipk2 >85 and nilai_ipk2 <100:
            beasiswa = '30%'
            beasiswa_list.append(beasiswa)
        else:
            beasiswa = '0%'
            beasiswa_list.append(beasiswa)
    if e == 'DKV' and 'Teknik Industri':
        if nilai_ipk2 >75 and nilai_ipk2 <85:
            beasiswa = '25%'
            beasiswa_list.append(beasiswa)
        elif nilai_ipk2 >85 and nilai_ipk2 <100:
            beasiswa = '35%'
            beasiswa_list.append(beasiswa)
        else:
            beasiswa = '0%'
            beasiswa_list.append(beasiswa)

    



    
print('================================================= DATABASE MAHASISWA ===============================================================================')
print('Nim       | Nama      | Alamat    | Asal      | Prod      | ipk awal  | UTS       | UAS       | TM        | ipk akhir | Nilai IPS | Beasiswa        ')
print('====================================================================================================================================================')
for i in range(len(nama_list)):
    for j in range(len(nestedlist)):
        print(nestedlist[j][i], end=' '*(10-len(str(nestedlist[j][i]))) +'| ')
    print()


