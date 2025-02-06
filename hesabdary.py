import sqlite3

print("\t\t\t\tبه نرم افزار حسابداري بهنام خوش آمديد")

def database():
    

    name_table=input("نام مجصول گروه : ")
        
    conn = sqlite3.connect('database.db')
    cur=conn.cursor()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS {name_table}(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            product TEXT,
                            price REAL);""")
                                
    conn.commit()

    
    while True:
        
        try:
            product = input("محصول : ")
        except:
            print("نام محصول !")
        try:
            price=float(input("قيمت : "))
        except:
            print("مقدار عددي وارد بفرماييد.")
                  
        cur.execute(f"""INSERT INTO  {name_table}(product, price) 
                           VALUES({product}, {price});""")
        conn.commit()
        try:       
            out=int(input("اگر ميخواهي خارج شويد 1 را ارسال بفرماييد در غير اين صورت هر عدد به غير 1 فشار دهيد"))
        except:
            print("مقدار عددي وارد بفرماييد" )  
        if out==1:
                  break

"""

def mohasebe_sodorfactor(name_price_dic , number):
    
    list_sum=[]
    for obj in name_price_dic:
         list_sum.append(name_price_dic.get[obj])     
    jame_factor=sum(list_sum)
    
    with open("D:/software hesabdary/factorchap.doc","w",encoding="utf-8") as f:
        f.write("\t\t: تاريخ \t\t\t\t\t\t\t : نام فروشگاه \n")
        f.write("\t\t\t\t\t\t\t\t\t\t : خريدار \n")
        f.write("-------------------------------------------------------------------------\n")
        for objj in name_price_dic:
            price_product_tedad=name_price_dic.get[objj] * number
            f.write(f"\t {objj} \t\t {price_product_tedad} \n")
        f.write(f"\t\t\t\t\t\t\t\t\t {jame_factor}= جمع کل \n")
        f.write("-------------------------------------------------------------------------\n")
        f.write("\t\t امضاي خريدار \t\t\t\t\t امضاي فروشگاه \n")
"""        
        

def search_name_table():
    
    while True: 
        
        
        table_search=input("نام محصول سر گروه وارد بفرماييد در  خروج   عدد 00 را وارد بفرماييد:  ")
        try:
             table_search=int( table_search)
             if  table_search==00:
                 break
        except:
            pass
        
        conn = sqlite3.connect('database.db')
        cur=conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table=cur.fetchall()
        name_price_dic={}
        list_num=[]
        for i in table:
            equal=i[0]
            if  table_search==equal:
                cur.execute(f"SELECT * FROM {table_search};")
                all_results = cur.fetchall()
                print(all_results)            
                while True:
                    try:
                        select_radif=int(input("عدد رديف مورد نظررا وارد بفرماييد و در صورت خروج عدد 00 را وارد بفرماييد :"))
                        if select_radif==00:
                             break
                    except:
                        print("رديف را به صورت صحيح وارد بفرماييد")
                    try:
                        number=int(input(" تعداد محصول مورد نظر : "))
                        list_num.append(number)
                        #print(number)
                        
                    except:
                        print("به صورت عدد وارد بفرماييد ")
                        
                    
                    try:
                        cur.execute(f"SELECT product,price FROM {table_search} WHERE ID={select_radif};")
                        result_for_add_dic=cur.fetchone()
                        if result_for_add_dic:
                            pru,pri=result_for_add_dic
                            name_price_dic[pru]=pri
                        else:
                            print("رديف مورد نظر يافت نشد")
                     
                        
                    except:
                        continue
        #print(name_price_dic)
        #print(type(name_price_dic))
        #print(list_num)
        counter=0
        list_sum=[]
        for objjj in name_price_dic:
            list_sum.append(name_price_dic[objjj]*list_num[counter])
            counter+=1
        jame_factor=sum(list_sum)
        #print(jame_factor)
        counter2=0
        with open("D:/software hesabdary/factorchap.doc","a",encoding="utf-8") as f:
            f.write("\t\t: تاريخ \t\t\t\t\t\t\t : نام فروشگاه \n")
            f.write("\t\t\t\t\t\t\t\t\t\t : خريدار \n")
            f.write("-------------------------------------------------------------------------\n\n\n")
            for objjjj in name_price_dic:
                f.write(f"\t{table_search} \t {objjjj} \t\t {name_price_dic[objjjj]} \t {list_num[counter2]} \n\n")
                counter2+=1
            f.write(f"\t\t\t\t\t\t\t\t\t {jame_factor}= جمع کل \n")
            f.write("-------------------------------------------------------------------------\n\n")
            f.write("\t\t امضاي خريدار \t\t\t\t\t امضاي فروشگاه \n")
        conn.close()
            
        
#--------------------------------------------------------------------------------------------
      
while True:
    print("عدد گزينه مورد نظر را وارد بفرماييد \n")
    selector=int(input("1-اضافه کردن محصولات \t"+"2-صدور فاکتور \t"+"3-خروج :"))
    try:
        if selector==1:
            database()
        elif selector==2:
            search_name_table()
        elif selector==3:
            exit()
    except:
        print("گزينه انتخاب شده صحيح نمي باشد ")
    

    


























    
