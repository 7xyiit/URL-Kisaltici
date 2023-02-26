import pyshorteners

while True:
    print(
        "1. Bit.ly \n"
        "2. Clck.ru \n"
        "3. Cutt.ly \n"
        "4. Da.gd \n"
        "5. Is.gd \n"
        "6. TinyURL.com \n"
    )
    print("URL'nin başında HTTP veya HTTPS eki olmalıdır. (Örnek: https://www.google.com)")
    val = int(input("Kullanmak istediğiniz link kısaltıcıyı seçin: "))
    val_2 = input("Site adresini yapıştırın: ")
    print("-"*40)

    def bitly():
        bitly_url = pyshorteners.Shortener(api_key='ac92dffe0773e78fa40e1416f2da8ca4693d3b33')
        print("URL Oluşturuldu. \n", bitly_url.bitly.short(val_2), sep='')

    def clckru():
        clckru_url = pyshorteners.Shortener()
        print("URL Oluşturuldu. \n", clckru_url.clckru.short(val_2), sep='')

    def cuttly():
        cuttly_url = pyshorteners.Shortener(api_key='78d8f202dbbd84794e11db4340fe6d73a83fb')
        print("URL Oluşturuldu. \n", cuttly_url.cuttly.short(val_2), sep='')

    def dagd():
        dagd_url = pyshorteners.Shortener()
        print("URL Oluşturuldu. \n", dagd_url.dagd.short(val_2), sep='')

    def isgd():
        isgd_url = pyshorteners.Shortener()
        print("URL Oluşturuldu. \n", isgd_url.isgd.short(val_2), sep='')

    def tiny():
        tiny_url = pyshorteners.Shortener()
        print("URL Oluşturuldu. \n", tiny_url.tinyurl.short(val_2), sep='')

    if val == 1:
        bitly()
    elif val == 2:
        clckru()
    elif val == 3:
        cuttly()
    elif val == 4:
        dagd()
    elif val == 5:
        isgd()
    elif val == 6:
        tiny()
    
    print("Program başa dönüyor.", "\n", "-"*40, sep='')