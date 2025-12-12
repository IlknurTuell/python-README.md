# Kullanıcıya hangi boyutta oyun tahtası çizmek istediğini sor (3x3, 4x4,...) ve python ifadesi kullanarak bunu ekrana çizdir.

def draw_board(size):
    for i in range(size):
        print(" ---"*size)  #üst çizgi
        print("|   "*size + "|")  #dikey çizgiler
    print(" ---" * size)

n = int(input("Tahta boyutunu girin: "))
draw_board(n)

