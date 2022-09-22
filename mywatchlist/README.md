# Muhammad Falensi Azmi - 2106630334 - Kelas D
# Tugas 3 PBP
## Link aplikasi: https://tugas2pbp-falensiazmi.herokuapp.com/mywatchlist/html

1. 
JSON: 
- Merupakan singkatan dari JavaScript Object Notation
- Dibuat berdasarkan bahasa JavaScript
- Merupakan sebuah format yang berfungsi untuk merepresentasikan objek
- Support namespace
- Tidak support array
- Mudah dibaca (jika dibandingkan dengan HTML atau XML)
- Tidak menggunakan tag
- Lebih tidak aman (dibandingkan XML)
- Tidak bisa memuat komentar
- Hanya support UTF-8 Encoding

XML:
- Merupakan singkatan dari Extensible Markup Language
- Merupakan turunan dari Standard Generalized Markup Language(SGML)
- Merupakan sebuah markup language yang menggunakan struktur tag untuk merepresentasikan data
- Support namespace
- Tidak support array
- Data lebih sulit dibaca jika dibandingkan dengan JSON
- Tag dibuat oleh user dan digunakan untuk mendeskripsikan data (bukan menampilkan)
- Lebih aman dari JSON
- Bisa memuat komentar
- Bisa menggunakan berbagai macam text encoding
- Membutuhkan closing tag
- Ukuran file/dokumen relatif besar

HTML:
- Merupakan singkatan dari Hyper Text Markup Language
- Bersifat statis
- Mempunyai tag yang sudah terdefinisi
- Tidak preserve whitespace
- Tag digunakan untuk menampilkan data
- Tidak selalu membutuhkan closing tag
- Tidak digunakan untuk membawa data, namun untuk menampilkan data
- Ukuran file/dokumen relatif kecil (dibandingkan XML)

Sumber: 
https://www.geeksforgeeks.org/difference-between-json-and-xml/
https://www.geeksforgeeks.org/html-vs-xml/


#

2. 

Data delivery dibutuhkan agar data dapat dikirim dari client ke server atau sebaliknya. Pada umumnya, semua jenis data (HTML, JSON, XML, dll) di-deliver melalui suatu protokol yang disebut HTTP. Melalui HTTP inilah transaksi data yang kita kirim (ke server melalui request) dan yang kita terima (dari server melalui response) dapat terjadi. Oleh karena itu, data delivery dibutuhkan agar client dan server dapat saling berkomunikasi.

#

3. 
- Pertama, saya membuat aplikasi mywatchlist dengan perintah

python manage.py startapp mywatchlist

- Saya menambahkan path ke mywatchlist di urls.py yang ada di folder project_django

- Saya membuat model yang diminta di models.py yang ada di folder mywatchlist

- Saya membuat sebuah file baru di fixture yang isinya data-data yang ingin saya masukkan dan memuat data tersebut (ke database) dengan perintah

python manage.py loaddata initial_mywatchlist_data.json

(tentunya setelah saya buat migrationsnya dan melakukan migrate)

- Saya membuat sebuah file mywatchlist.html untuk menampilkan data saya dalam format html

- Saya menambahkan beberapa fungsi (show_html, show_xml, show_json, dll) dan import beberapa modul di views.py yang ada di folder mywatchlist. Hal ini diperlukan untuk memproses data (mulai dari mengambil data sampai meneruskannya (memberikan response) dalam format html, xml, ataupun json)

- Lalu, saya membuat routing (di urls.py yang ada di mywatchlist) yang akan menjalankan fungsi-fungsi yang saya definisikan di views.py sehingga user dapat mengakses data dalam tiga format berbeda melalui tiga url berbeda (../mywatchlist/html, ../mywatchlist/xml, ../mywatchlist/json)

- Terakhir, saya melakukan deployment ke heroku agar aplikasi saya dapat diakses melalui web

#

SCREENSHOT POSTMAN:

#

HTML
![this is an image](https://raw.githubusercontent.com/FrinzTheCoder/tugas2pbp/main/mywatchlist/resources/sshtml.png)

#

XML
![this is an image](https://raw.githubusercontent.com/FrinzTheCoder/tugas2pbp/main/mywatchlist/resources/ssxml.png)

#

JSON
![this is an image](https://raw.githubusercontent.com/FrinzTheCoder/tugas2pbp/main/mywatchlist/resources/ssjson.png)
