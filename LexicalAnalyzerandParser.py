GoLangForSyntax = "for i := 1 ; i < 5 ; i ++ { a = b + c }"  # Meminta input dari pengguna
GoLangForSyntax = GoLangForSyntax.split()  # Memecah input menjadi daftar kata

vars = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}  # Set variabel yang valid
nums = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}  # Set angka yang valid
increments = {"++", "--"}  # Set operator penambahan/pengurangan yang valid
condition = {">=", "<=", "<", ">"}  # Set operator perbandingan yang valid
operation = {"+", "-", "*", "/"}  # Set operasi aritmatika yang valid

statement = [
    "for",  vars, ":=", nums, ";",  # Token yang diharapkan untuk bagian inisialisasi loop for
    vars, condition, nums, ";",  # Token yang diharapkan untuk bagian kondisi loop for
    vars, increments, "{",  # Token yang diharapkan untuk bagian penambahan loop for
    vars, "=", vars, operation, vars, "}"  # Token yang diharapkan untuk isi loop
]

state = 1  # Menginisialisasi hitungan state
finaleState = True  # Menginisialisasi flag keluaran

for sentence in GoLangForSyntax:  # Mengulangi setiap kata dalam input
    print(f"State saat ini: {state}, Kata: {sentence}")  # Mencetak state dan kata saat ini
    if isinstance(statement[state - 1], set):  # Memeriksa apakah token yang diharapkan merupakan set (untuk opsi valid yang lebih dari satu)
        if sentence not in statement[state - 1]:  # Memeriksa apakah kata tersebut tidak ada dalam set opsi valid
            print(f"Error: Token tidak valid '{sentence}', terjebak di state {state}")
            finaleState = False  # Mengubah flag keluaran menjadi False
            break  # Keluar dari loop
    else:
        if sentence != statement[state - 1]:  # Memeriksa apakah kata tersebut cocok dengan token yang diharapkan
            print(f"Error: Token tidak valid '{sentence}', terjebak di state {state}")
            finaleState = False  # Mengubah flag keluaran menjadi False
            break  # Keluar dari loop
    state += 1  # Menambahkan hitungan state

if finaleState and state == len(statement) + 1:  # Memeriksa apakah loop selesai dengan sukses dan mencapai state terakhir
    print("Parsed Well!")  # Menunjukkan bahwa parsing berhasil
elif finaleState and state != len(statement) + 1:  # Memeriksa apakah loop selesai tetapi tidak mencapai state terakhir
    print(f"Error: Akhir input yang tidak diharapkan, terjebak di state {state}")
else:
    print("Parsing Error!")  # Menunjukkan kesalahan parsing