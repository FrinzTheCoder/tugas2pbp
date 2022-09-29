# Muhammad Falensi Azmi - 2106630334 - Kelas D
# Tugas 4 PBP
## Link aplikasi: https://tugas2pbp-falensiazmi.herokuapp.com/todolist/

1. 

CSRF token adalah token yang di-generate oleh server untuk mencegah serangan CSRF. Biasanya, serangan CSRF terjadi ketika situs-situs berbahaya mengandung link atau button yang bermaksud untuk membuat user melakukan sesuatu yang tidak diinginkan. CSRF token bekerja dengan men-generate token yang disimpan di user session. Ketika request (dari form) diberikan dari user ke server, server akan memeriksa apakah request yang diberikan user disertai token yang sesuai dengan yang ada di user session. Jika token tersebut tidak sesuai, ada kemungkinan bahwa request tersebut tidak berasal dari client yang bersangkutan, melainkan dari pihak ketiga. CSRF token ini akan digenerate terus menerus setiap kali kita mengakses sebuah form sehingga akan sangat sulit untuk ditebak/diprediksi.

Jika tidak ada potongan kode tersebut, ada dua kemungkinan jawaban:
- Django akan menganggap browser tidak memberikan csrf token karena secara default, csrf token itu wajib diikutsertakan pada form django. Dalam kasus ini, csrf token yang diberikan akan tidak valid dan request dari user akan ditolak (tidak diproses).

- Jika ingin tetap tidak menggunakan csrf token (membuat settingan django sendiri), maka situs buatan kita akan rentan terkena csrf attack. Bisa saja ada situs lain yang bermaksud untuk menyuruh kita melakukan sesuatu yang tidak diinginkan (melalui request atas nama kita) di situs kita sendiri.

#

2. 

Bisa.
Pertama kita harus membuat tag form dan menyertakan jenis request yang diinginkan saat form tersebut disubmit (POST, UPDATE, DELETE, dll). Selanjutnya, kita perlu menambahkan {% csrf_token %} agar form kita memiliki csrf token. Lalu, kita dapat menambahkan berbagai macam input (text, password, dll) untuk dikirim bersamaan saat kita mengirim request melalui form tersebut. Terakhir, kita perlu menambahkan button agar form kita dapat tersubmit.

#

3. 
Pertama, browser akan mengirim GET request untuk mendapatkan halaman form dalam bentuk HTML. Lalu, user akan mengirimkan data yang diisi di form dengan POST method. CSRF token yang terkirim melalui form akan divalidasi terlebih dahulu untuk memastikan apakah request berasal dari tempat yang valid (jika menggunakan CSRF token). Selanjutnya, bagian views yang bersangkutan akan mengambil data-data yang diisi di form dan memvalidasi data tersebut (opsional). Jika data tersebut terbukti valid, data akan disimpan ke database.

Selanjutnya, user akan mengakses halaman dimana halaman tersebut berisi data yang akan ditampilkan. User akan mengirimkan request dalam bentuk GET method. Selanjutnya, view yang memproses request tersebut akan mengambil data yang bersangkutan dari model. Data yang sudah diambil akan di-template dengan django template agar bisa tampil di halaman browser. Selanjutnya, server akan memberikan response berupa halaman html yang berisi data yang sudah di-template tersebut untuk dilihat oleh user(client).

#

4. 
- Pertama, saya membuat aplikasi todolist dengan perintah

python manage.py startapp todolist

dan menambahkan app nya di settings.py yang ada di project_django

- Saya menambahkan path ke todolist di urls.py yang ada di folder project_django

- Saya membuat model yang diminta di models.py yang ada di folder todolist

- Saya membuat file login.html dan register.html dan diisikan dengan template yang ada di lab/tutorial. Saya juga membuat views yang berisi function untuk menghandle perintah register, login, dan logout (mengikuti yang ada di lab/tutorial). Di sini, saya juga sudah menerapkan cookie.

- Saya membuat file todolist.html dengan template-template yang ada pada lab/tutorial/tugas sebelumnya. Di sini, saya menambahkan beberapa modifikasi: 

menampilkan user yang sedang login, menambahkan tombol tambah task dan logout, memodifikasi tabel agar menampilkan data yang sesuai, menambahkan tombol ubah dan hapus (untuk poin bonus), Menambahkan tulisan sesi terakhir login di bagian paling bawah.

- Saya membuat sebuah file forms.py untuk template form pengisian Task (untuk fitur tambah task). Selanjutnya, saya membuat create_task.html yang mengimplementasikan form yang saya buat di forms.py agar user bisa menambahkan task.

- Saya membuat fungsi create_task untuk menghandle fitur tambah task. Di sini, user akan menerima halaman html yang berisi form untuk diisi (tambah task). Jika user menekan tombol submit, maka akan ada POST request yang akan dihandle oleh fungsi create_task. Fungsi ini akan memvalidasi data yang ada di form dan menambahkan object User sebagai foreign key dari field user di table Task (menerapkan relational database). Selanjutnya, Task yang sudah komplit akan disimpan ke database dan proses penyimpanan data pun berhasil.

- Saya membuat routing (di urls.py yang ada di todolist) yang akan menjalankan fungsi-fungsi yang saya definisikan di views.py sehingga user dapat mengakses url yang berbeda-beda sesuai dengan fungsionalitasnya (login, logout, create-task, dll).

- Saya menambahkan README.md yang berisi penjelasan mengenai project atau app yang saya buat.

- Terakhir, saya melakukan deployment ke heroku agar aplikasi saya dapat diakses melalui web.
