# Muhammad Falensi Azmi - 2106630334 - Kelas D
# Tugas 4 & 5 PBP
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

#

# Tugas 5

#

1. 
- Inline CSS adalah penggunaan CSS yang ditempatkan menyatu dengan element yang ingin diberi style. Cara penggunaannya adalah dengan menuliskan style="(sintaks styling)" langsung di dalam tag html yang ingin diberi style.

- Internal CSS adalah penggunaan CSS yang ditempatkan di satu dokumen HTML yang sama. Cara penggunaannya adalah dengan mendefinisikan styling di bagian header. Selanjutnya, elemen di bagian body yang dikenakan styling tersebut akan terkena efeknya.

- External CSS adalah penggunaan CSS dengan mendefinisikan styling di file yang terpisah. Nantinya, styling yang terpisah ini akan dihubungkan dengan tag "link" pada dokumen html yang ingin menggunakan styling di file CSS tersebut.

Kelebihan inline CSS adalah kita bisa memberikan styling kepada satu tag spesifik yang ingin kita berikan styling. Kekurangannya dari cara ini adalah tidak praktis jika kita ingin memberikan styling kepada beberapa tag karena kita harus copy-paste terus menerus ke tag yang ingin kita beri styling.

Kelebihan internal CSS adalah kita dapat memberikan styling terhadap satu dokumen HTML yang spesifik. Dengan cara ini, kita bisa melakukan modifikasi pada styling suatu halaman tanpa perlu khawatir styling di halaman lain ikut berubah juga. Kekurangan dari styling ini adalah tidak praktis jika kita ingin memberikan styling kepada beberapa dokumen HTML karena kita harus copy-paste CSS nya ke setiap dokumen yang ingin kita beri styling.

Kelebihan external CSS adalah kita dapat menerapkannya ke seluruh dokumen yang ingin kita beri styling karena tinggal di import saja. Jika kita melakukan perubahan pada CSS, halaman-halaman HTML yang menggunakan CSS tersebut juga akan ikut berubah sehingga kita tidak perlu melakukan modifikasi satu per satu. Kekurangan dari styling ini adalah page HTML harus melakukan fetch setiap kali membutuhkan styling CSS (karena berbeda file). Selain itu, belum tentu semua styling di suatu file CSS diperlukan pada suatu dokumen HTML sehingga dokumen HTML juga akan me-load styling yang sebenarnya tidak digunakan dalam file HTML tersebut.

2. 
"nav"
Tag nav digunakan untuk merepresentasikan link navigasi (link yang akan merujuk ke halaman lain atau halaman itu sendiri). Contoh dari pengunaan tag nav adalah untuk membuat menu, table of content, dan index.

"article"
Merupakan representasi dari konten yang "independen" dari sebuah dokumen (misalnya entri blog).

"audio"
Untuk menambahkan konten dalam bentuk audio/suara ke dokumen html

"header"
Merepresentasikan header dari suatu halaman. Biasanya berisi "introductory content" atau link-link navigasi.

"footer"
Merepresentasikan footer dari suatu halaman. Biasanya berisi informasi penulis halaman, kontak penulis,copyright, dan lainnya.


3. 
Element selector: menerapkan styling dengan menggunakan tag HTML sebagai selector untuk mengubah properti yang ada di dalam tag tersebut. Biasa ditulis dalam format (nama_tag){styling}

ID selector: menggunakan ID sebagai selector. ID dapat ditambahkan pada tag html yang ingin diberi style. ID harus bersifat unik. Selector ini menggunakan format #(nama_id){styling}

Class selector: menggunakan class sebagai sebagai selector. Class dapat ditambahkan pada tag html yang ingin diberi style. Berbeda dengan ID, class tidak bersifat unik sehingga dapat diterapkan di beberapa tag berbeda. Selector ini menggunakan format .(nama_class){styling}

4. 

- Menambahkan tag "link" pada header di base.html yang berisi link menuju bootstrap. Link ini diperlukan untuk mengambil CSS dari Bootstrap agar CSS tersebut dapat diterapkan pada dokumen html kita. Dalam kasus ini, tag "link" ditambahkan pada base.html karena semua dokumen html yang lain (login, register, dll) menggunakan base.html sebagai basis template (semacam parent). Hal ini bisa mempermudah kita karena kita tidak perlu menuliskan tag link di setiap dokumen yang ingin kita beri style.

- Mempercantik halaman login, register, dan create_task dengan berbagai styling yang disediakan oleh Bootstrap. Pada proyek saya, styling yang diterapkan ke dokumen yang berisi halaman login, register, dan create task tidak begitu berbeda satu sama lainnya.

- Menerapkan styling pada todolist.html dan mengubah tabel todolist menjadi dalam bentuk card. Di sini, saya menggunakan class row untuk mengatur card dalam bentuk baris dan class card untuk membuat card itu sendiri. Kedua class ini merupakan bawaan dari Bootstrap sehingga saya hanya perlu menerapkannya saja. Selain itu, saya juga menambahkan gambar dummy dari https://www.computerhope.com/jargon/t/task.png untuk dipasang di card saya (untuk memperindah).

- Menambahkan penjelasan di README.md terkait Tugas 5

- Melakukan deployment ke Heroku agar aplikasi saya dapat diakses melalui web.

#