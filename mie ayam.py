import pandas as pd
import datetime
import os
def garis():
    print(50*'=')

def clear_screen():
    os.system('cls')

list_menu=[]
list_jumlah=[]
list_harga=[]
list_total=[]

def menu_makanan():
    garis()
    print('                 MIE AYAM KHINANTI')
    garis()
    print("                 MENU MAKANAN ")
    garis()
    print("KODE         MAKANAN                  HARGA")
    print(" c        MIE AYAM CEKER            Rp.13.000")
    print(" j        MIE AYAM JAMUR            Rp.13.000")
    print(" k        MIE AYAM KEJU             Rp.13.000")
    print(" p        MIE AYAM PANGSIT REBUS    Rp.13.000")
    print(" mbk      MIE AYAM BAKSO KECIL      Rp.13.000")
    print(" mbd      MIE AYAM BAKSO DAGING     Rp.18.000")
    print(" mbu      MIE AYAM BAKSO URAT       Rp.21.000")
    print(" mbt      MIE AYAM BAKSO TELUR      Rp.21.000")
    garis()
    print(" bu       BAKSO URAT                Rp.18.000")
    print(" bt       BAKSO TELUR               Rp.18.000")
    print(" bd       BAKSO daging              Rp.15.000")
    garis()
    kode1=input("Masukan Kode Makanan : ")
    if kode1=='c' or kode1=='C':
        list_menu.append("MIE AYAM CEKER")
        jumlah1=int(input("Masukan jumlah makanan :"))
        list_harga.append(13000)
        total1=13000*jumlah1
        list_jumlah.append(jumlah1)
        list_total.append(total1)
        tanya1()
    elif kode1=='j' or kode1=='J':
        list_menu.append("MIE AYAM JAMUR")
        jumlah2=int(input("Masukan jumlah makanan :"))
        list_harga.append(13000)
        total2=13000*jumlah2
        list_jumlah.append(jumlah2)
        list_total.append(total2)
        tanya1()
    elif kode1=='k' or kode1=='K':
        list_menu.append("MIE AYAM KEJU")
        jumlah3=int(input("Masukan jumlah makanan :"))
        list_harga.append(13000)
        total3=13000*jumlah3
        list_jumlah.append(jumlah3)
        list_total.append(total3)
        tanya1()
    elif kode1=='p' or kode1=='P':
        list_menu.append("MIE AYAM PANGSIT REBUS")
        jumlah4=int(input("Masukan jumlah makanan :"))
        total4=13000*jumlah4
        list_jumlah.append(jumlah4)
        list_total.append(total4)
        tanya1()
    elif kode1=='mbk' or kode1=='MBK':
        list_menu.append("MIE AYAM BAKSO KECIL")
        jumlah5=int(input("Masukan jumlah makanan :"))
        list_harga.append(13000)
        total5=13000*jumlah5
        list_jumlah.append(jumlah5)
        list_total.append(total5)
        tanya1()
    elif kode1=='mbd' or kode1=='MBD':
        list_menu.append("MIE AYAM BAKSO DAGING")
        jumlah6=int(input("Masukan jumlah makanan :"))
        list_harga.append(18000)
        total6=18000*jumlah6
        list_jumlah.append(jumlah6)
        list_total.append(total6)
        tanya1()
    elif kode1=='mbu' or kode1=='MBU':
        list_menu.append("MIE AYAM BAKSO URAT")
        jumlah7=int(input("Masukan jumlah makanan :"))
        list_harga.append(21000)
        total7=21000*jumlah7
        list_jumlah.append(jumlah7)
        list_total.append(total7)
        tanya1()
    elif kode1=='mbt' or kode1=='MBT':
        list_menu.append("MIE AYAM BAKSO TELUR")
        jumlah8=int(input("Masukan jumlah makanan :"))
        list_harga.append(21000)
        total8=21000*jumlah8
        list_jumlah.append(jumlah8)
        list_total.append(total8)
        tanya1()
    elif kode1=='bd' or kode1 == 'BD':
        list_menu.append("BAKSO DAGING")
        jumlah9=int(input("Masukan jumlah makanan :"))
        list_harga.append(15000)
        total9=15000*jumlah9
        list_jumlah.append(jumlah9)
        list_total.append(total9)
        tanya1()
    elif kode1=='bu' or kode1=='BU':
        list_menu.append("BAKSO URAT")
        jumlah10=int(input("Masukan jumlah makanan :"))
        list_harga.append(18000)
        total10=18000*jumlah10
        list_jumlah.append(jumlah10)
        list_total.append(total10)
        tanya1()
    elif kode1=='bt' or kode1=='BT':
        list_menu.append("BAKSO TELUR")
        jumlah11=int(input("Masukan jumlah makanan :"))
        list_harga.append(18000)
        total11=18000*jumlah11
        list_jumlah.append(jumlah11)
        list_total.append(total11)
        tanya1()
    else:
        print("Pilihan yang anda masukan salah!")
    return

def tanya1():
    garis()
    tanya1=input("ingin tambah makanan? [y/t]")
    clear_screen()
    garis()
    if tanya1=="y" or tanya1=="Y":
        menu_makanan()
    elif tanya1 =="t" or tanya1=="T":
        menu_minuman()
    else:
        print("Pilihan yang anda masukan salah")

def menu_minuman():
    print("                 MENU MINUMAN ")
    garis()
    print("KODE          MINUMAN                  HARGA")
    print(" tm           ES TEH MANIS            Rp.5000")
    print(" lm           LEE MINERAL             Rp.4000")
    print(" jp           ES JERUK PERAS          Rp.7000")
    garis()
    kode2=input("Masukan kode Minuman : ")
    if kode2=='tm' or kode2=='TM':
        list_menu.append("ES TEH MANIS")
        jumlah12=int(input("Masukan jumlah minuman :"))
        list_harga.append(5000)
        total12=5000*jumlah12
        list_jumlah.append(jumlah12)
        list_total.append(total12)
        tanya2()
    elif kode2=='lm' or kode2=='LM':
        list_menu.append("LEE MINERAL")
        jumlah13=int(input("Masukan jumlah minuman :"))
        list_harga.append(4000)
        total13=4000*jumlah13
        list_jumlah.append(jumlah13)
        list_total.append(total13)
        tanya2()
    elif kode2=='jp' or kode2=='JP':
        list_menu.append("ES JERUK PERAS")
        jumlah14=int(input("Masukan jumlah minuman :"))
        list_harga.append(7000)
        total14=7000*jumlah14
        list_jumlah.append(jumlah14)
        list_total.append(total14)
        tanya2()
    else:
        print("Pilihan yang anda masukan salah")
        tanya2()
    return

def tanya2():
    garis()
    tanya2=input("ingin tambah minuman? [y/t]")
    clear_screen()
    garis()
    if tanya2=="y" or tanya2=="Y":
        menu_minuman()
    elif tanya2 =="t" or tanya2=="T":
        akhir()
    else:
        print("Pilihan yang anda masukan salah")

def akhir():
    for harga in list_total:
        jumhar=sum(list_total)
        if jumhar > 100000:
            diskon=jumhar * 0.1
        elif jumhar > 200000:
            diskon=jumhar * 0.2
        elif jumhar > 300000:
            diskon=jumhar * 0.3
        else:
            diskon=0
        total=jumhar-diskon
        pajak=(jumhar-diskon) * 0.1
        totalakhir= total + pajak
        break
    menu={
        " MENU YANG DIPESAN" :list_menu,
        "JUMLAH" :list_jumlah,
        "HARGA SATUAN"  :list_harga,
        " TOTAL" :list_total
        }
    date=datetime.datetime.now()
    data_menu=pd.DataFrame(menu)
    data_menu.index=range(1,len(data_menu)+1)
    print("{:^50}".format("STRUK PEMBAYARAN"))
    print("{:^50}".format("MIE AYAM KHINANTI"))
    print("{:^50}".format(date.strftime("%A-%x-%X")))
    garis()
    print(data_menu)
    garis()
    print("Total Pembelian           :   Rp.",+int(jumhar))
    print("Diskon Pembelian          :   Rp.",+int(diskon))
    print("PPN Sebesar 10%           :   Rp.",+int(pajak))
    garis()
    print("Total Yang Harus Dibayar  :   Rp.",+int(totalakhir))
    bayar=int(input("Bayar Tagihan             :   Rp. "))
    kembalian=bayar-totalakhir
    print("Kembalian anda            :   Rp. ",+int(kembalian))
    garis()
    print("\n{:^50}".format("TERIMA KASIH !!"))
    print("{:^50}".format("Jl.Sukahati Blok U3a, Kec.Cibinong, Kab.Bogor"))
    print("{:^50}".format("Samping SDN Muara Beres"))
    print("{:^50}".format("Call: 081311274228"))
    garis()

menu_makanan()