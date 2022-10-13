# Muhammad Falensi Azmi - 2106630334 - Kelas D
# Tugas 4 & 5 PBP
## Link aplikasi: https://tugas2pbp-falensiazmi.herokuapp.com/todolist/

1. 
Pada synchronous programming, client harus menunggu server untuk mengirim response sebelum dapat mengerjakan hal lain. Pada asynchronous programming, client dapat melakukan hal lain tanpa perlu menunggu response dari server. Selain itu, pada asynchronous programming, jika server sudah memberikan response dan perlu mengubah tampilan (html) dari client, maka client tidak harus selalu me-reload halaman web nya (karena proses perubahan halaman dapat dilakukan secara asinkronus dan hanya bagian tertentu saja yang berubah). Ini berbeda dengan synchronous dimana user harus selalu me-reload satu halaman penuh setiap kali ada perubahan pada tampilan.

#

2.
Event-driven programming adalah paradigma dimana fungsionalitas tertentu pada program dapat dijalankan saat terjadi suatu event. Event dapat berupa mouse click, key press, mouse hover, dan lain-lain. Salah satu penerapannya adalah memunculkan modal untuk pengisian task baru saat tombol "add task" di-klik.

#

3.
Asynchronous programming dapat diterapkan untuk mengubah halaman web secara asinkronus, yaitu halaman web yang tidak perlu di-reload seluruhnya ketika beberapa bagian data dari halaman web tersebut berubah. Dalam hal ini, asynchronous programming dapat diterapkan dengan menggunakan AJAX (Asynchronous Javascript and XML). Pada tugas 6 ini, AJAX berperan untuk mengambil data dari server (dalam bentuk JSON) untuk ditampilkan di halaman web dalam bentuk HTML. Selain itu, AJAX juga berperan pada fitur penambahan task, dimana POST request akan dikirim ke server saat user masih berada di halaman todolist dan tidak perlu mereload halamannya. 

Dari sini, juga bisa disimpulkan bahwa AJAX tidak hanya bisa diterapkan untuk data-delivery dalam bentuk XML saja, melainkan juga JSON.

#

4.
- Membuat fungsi get_todolist_json pada views.py untuk mengembalikan seluruh data task dalam bentuk JSON

- Membuat path ke /todolist/json di urls.py yang mengarah ke view get_todolist_json

- Menambahkan fungsi asinkronus "getTodolist" dan "refreshTodolist" ke bagian "script" pada todolist.html.

getTodolist berguna untuk mengambil semua data task melalui endpoint /todolist/json. refreshTodolist berguna untuk me-refresh halaman yang berisi card tasks secara asinkronus.

- Memodifikasi tombol add task agar dapat menampilkan modal dengan form untuk menambahkan task. Pada bagian ini, saya menggunakan modal bawaan dari Bootstrap. Form yang saya gunakan di modal berasal dari form yang ada di create_task.html yang sedikit dimodifikasi.

- Membuat fungsi add_todolist pada views.py untuk menambahkan todolist. Fungsi ini dimaksudkan untuk dijalankan melalui asynchronous javascript.

- Menambahkan path /todolist/add di urls.py yang mengarah ke fungsi add_todolist

- Menambahkan fungsi asinkronus addTodolist pada script di todolist.html. Fungsi ini akan mengirimkan request yang berisi data-data yang diisikan di form. Request tersebut akan dikirimkan ke endpoint /todolist/add untuk menambahkan data ke model Task. Untuk menjalankan fungsi ini, tombol submit pada form sudah dihubungkan dengan "onClick event" yang akan menjalankan fungsi addTodolist ketika user meng-klik tombol submit yang ada di form.

- Untuk menutup modal, tambahkan data-bs-dismiss="modal" ke submit button. Modal akan tertutup otomatis saat submit button ditekan

- Memanggil fungsi refreshTodolist setelah addTodolist berhasil dijalankan agar halaman direfresh secara asinkronus tanpa reload seluruh page

- Menambahkan README-TWO.md