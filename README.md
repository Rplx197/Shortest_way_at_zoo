Aplikasi ini memungkinkan pengguna untuk mencari informasi tentang hewan-hewan yang ada di sebuah kebun binatang serta menemukan rute tercepat untuk sampai ke kandang hewan yang diinginkan.

Fitur Utama:

Graf Jaringan Kebun Binatang: Program menciptakan representasi visual dari kebun binatang sebagai graf jaringan, di mana tempat-tempat di kebun binatang diwakili sebagai simpul (nodes) dan jalur antara tempat-tempat tersebut diwakili sebagai tepian (edges).
Pencarian Informasi Hewan: Pengguna dapat memasukkan nama hewan untuk mengetahui informasi dasar tentang hewan tersebut, seperti deskripsi dan habitatnya.
Pencarian Rute Tercepat: Program menggunakan algoritma Dijkstra untuk mencari rute tercepat dari gerbang utama ke kandang hewan yang diinginkan.
Cara Penggunaan:

Program akan menampilkan graf jaringan kebun binatang.
Pengguna diminta untuk memasukkan nama hewan yang ingin dicari informasinya.
Setelah mendapatkan informasi tentang hewan tersebut, pengguna akan diberikan rute tercepat dari gerbang utama ke kandang hewan tersebut.
Dokumentasi Kode:

create_zoo_graph(): Fungsi untuk membuat graf jaringan kebun binatang dengan menambahkan simpul dan tepian berdasarkan informasi tempat-tempat di kebun binatang.
find_shortest_path(graph, start, end): Fungsi untuk mencari rute tercepat menggunakan algoritma Dijkstra dari simpul awal (gerbang utama) ke simpul tujuan (kandang hewan).
display_animal_info(animal): Fungsi untuk menampilkan informasi tentang hewan berdasarkan nama hewan yang dimasukkan.
main(): Fungsi utama yang menjalankan seluruh aplikasi, termasuk pembuatan graf jaringan, pencarian informasi hewan, dan pencarian rute tercepat.
