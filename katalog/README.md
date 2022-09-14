# Muhammad Falensi Azmi - 2106630334 - Kelas D
# Tugas 2 PBP
## Link aplikasi: https://tugas2pbp-falensiazmi.herokuapp.com/katalog/

1. Bagan

#

2. Virtual environtment diperlukan untuk membuat sebuah environtment terisolasi dimana kita dapat menginstall package atau library (dengan versi tertentu) pada satu project tertentu. Dengan virtual environtment, kita dapat memisahkan package yang digunakan untuk suatu project dengan package yang digunakan di project lainnya. Hal ini memungkinkan kita untuk menginstall package-package yang memang ingin kita pasang untuk project kita tanpa mengganggu project lainnya yang kita kembangkan dari device yang sama.

Tanpa menggunakan virtual environtment, kita tetap dapat membuat aplikasi web berbasis Django. Namun, ada kemungkinan package yang kita pasang untuk aplikasi tersebut konflik dengan package untuk aplikasi lain yang kita kembangkan (terutama versinya). Virtual environtment mencegah hal tersebut sehingga package yang kita pasang untuk sebuah project aplikasi bisa dipisahkan dari package aplikasi lainnya.

#

3.
poin (1):
Pertama-tama, saya mengimport class render untuk me-render file HTML (nantinya) dan class CatalogItem(untuk mengambil data dari model CatalogItem).

Saya mendefinisikan fungsi show_katalog untuk mengambil data yang ada di model CatalogItem, menambahkan data-data pribadi saya dan katalog ke sebuah dictionary, dan me-render file katalog.html beserta data-data yang saya kirim.

poin (2):
Saya memulainya dari file urls.py yang ada di folder project_django. Di sana, pada list urlpatterns, saya menambahkan routing ke 'katalog/' dan meneruskan routing tersebut ke file urls.py yang ada di folder katalog

Pada urls.py yang ada di folder katalog, saya mengimport fungsi show_katalog yang ada di views app katalog dan class path dari django.urls (built-in). Selanjutnya, saya menambahkan sebuah path ke string kosong '' (yang artinya routing yang saya buat tidak perlu kemana-mana lagi). Route ini akan memanggil fungsi show_katalog yang sudah saya import tadi sehingga prosesnya bisa diteruskan ke views.py di katalog.

poin(3):
Pada file katalog.html yang ada di folder templates aplikasi katalog, saya menambahkan nama, npm, dan data-data katalog. Untuk data-data yang ada di katalog, saya menambahkannya dengan melakukan iterasi pada setiap item yang ada di katalog dan mengambil atributnya satu per satu (nama, harga, stock, dll). Iterasi ini akan diterjemahkan oleh templating engine dari django sehingga data-data yang saya masukkan dengan for loop bisa muncul saat dilihat di web browser.

poin(4):
Saya membuat app baru di heroku, menambahkan beberapa line di settings.py yang ada di project_django, menambahkan secrets di github, dan melakukan push ke github. Selanjutnya, github akan memproses deployment sehingga aplikasi saya dapat muncul di heroku.