
while True:
    try:
        benimInt = int(input("Numaranizi giriniz : "))
    except:
        print("Lutfen gercek bir numara giriniz : ")
        continue
    else:
        print("Tesekkürler")
        break
    finally:
        print("Finally cagrildi.")
