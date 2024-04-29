import networkx as nx
import matplotlib.pyplot as plt

# Fungsi untuk membuat graf jaringan (network graph) dari tempat-tempat di kebun binatang
def create_zoo_graph():
    G = nx.Graph()

    # Tambahkan simpul (nodes) untuk tempat-tempat di kebun binatang
    places = {
        "Gerbang Utama": {"pos": (1, 2)},
        "Kandang Singa": {"pos": (2, 4)},
        "Kandang Gajah": {"pos": (4, 3)},
        "Kandang Kera": {"pos": (3, 1)},
        "Kandang Harimau": {"pos": (6, 2)},
        "Kandang Jerapah": {"pos": (7, 4)},
        "Kandang Zebra": {"pos": (9, 3)},
        "Kandang Burung": {"pos": (8, 1)},
        "Kandang Beruang": {"pos": (5, 5)},
        "Kandang Panda": {"pos": (6, 6)},
        "Kandang Kancil": {"pos": (8, 5)}
    }

    for place, place_info in places.items():
        G.add_node(place, pos=place_info['pos'])

    # Tambahkan tepian (edges) yang menghubungkan tempat-tempat di kebun binatang
    edges = [
        ("Gerbang Utama", "Kandang Singa"),
        ("Gerbang Utama", "Kandang Kera"),
        ("Kandang Singa", "Kandang Gajah"),
        ("Kandang Gajah", "Kandang Kera"),
        ("Kandang Gajah", "Kandang Harimau"),
        ("Kandang Gajah", "Kandang Jerapah"),
        ("Kandang Kera", "Kandang Harimau"),
        ("Kandang Harimau", "Kandang Jerapah"),
        ("Kandang Jerapah", "Kandang Zebra"),
        ("Kandang Jerapah", "Kandang Burung"),
        ("Kandang Zebra", "Kandang Burung"),
        ("Kandang Beruang", "Kandang Panda"),
        ("Kandang Panda", "Kandang Kancil"),
        ("Kandang Jerapah", "Kandang Kancil"),
        ("Kandang Jerapah", "Kandang Beruang"),
        ("Kandang Jerapah", "Kandang Panda")
    ]

    G.add_edges_from(edges)

    return G

# Fungsi untuk mencari jalur tercepat menggunakan algoritma Dijkstra
def find_shortest_path(graph, start, end):
    try:
        shortest_path = nx.shortest_path(graph, source=start, target=end)
        return shortest_path
    except nx.NetworkXNoPath:
        return None

# Fungsi untuk menampilkan informasi tentang hewan
def display_animal_info(animal):
    animal_info = {
        "Singa": "Singa adalah hewan karnivora besar yang ditemukan di Afrika.",
        "Gajah": "Gajah adalah hewan herbivora besar yang ditemukan di Asia dan Afrika.",
        "Kera": "Kera adalah hewan primata cerdas yang ditemukan di seluruh dunia.",
        "Harimau": "Harimau adalah karnivora besar yang ditemukan di Asia.",
        "Jerapah": "Jerapah adalah hewan herbivora tinggi yang ditemukan di Afrika.",
        "Zebra": "Zebra adalah hewan herbivora dengan garis-garis hitam dan putih yang ditemukan di Afrika.",
        "Burung": "Burung adalah hewan yang memiliki sayap dan biasanya bisa terbang.",
        "Beruang": "Beruang adalah hewan besar dengan bulu yang tebal dan sering dijumpai di berbagai belahan dunia.",
        "Panda": "Panda adalah hewan yang berasal dari China dan dikenal dengan warna putih dan hitamnya.",
        "Kancil": "Kancil adalah hewan kecil yang biasa ditemukan di hutan tropis."
    }

    if animal in animal_info:
        print(animal_info[animal])
    else:
        print("Informasi tentang hewan tidak ditemukan.")

# Main program
def main():
    # Buat graf jaringan (network graph) kebun binatang
    zoo_graph = create_zoo_graph()

    # Tampilkan graf jaringan kebun binatang
    pos = nx.get_node_attributes(zoo_graph, 'pos')
    nx.draw(zoo_graph, pos, with_labels=True, node_size=700, node_color='lightblue')
    plt.title("Peta Kebun Binatang")
    plt.show()

    # Input nama hewan dari pengguna
    animal_name = input("Masukkan nama hewan yang ingin Anda cari di kebun binatang: ")

    # Tampilkan informasi tentang hewan
    print("Informasi tentang", animal_name)
    display_animal_info(animal_name)

    # Cari rute tercepat untuk sampai ke tempat hewan tersebut
    start_location = "Gerbang Utama"
    end_location = "Kandang " + animal_name
    shortest_path = find_shortest_path(zoo_graph, start_location, end_location)

    # Tampilkan rute tercepat
    if shortest_path:
        print("Rute tercepat untuk sampai ke", end_location, "adalah:", shortest_path)
    else:
        print("Tidak ada rute yang tersedia untuk sampai ke", end_location)

if __name__ == "__main__":
    main()
