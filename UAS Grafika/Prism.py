from OpenGL.GL import *

class Prism:
    def __init__(self):
        # Koordinat puncak prisma
        self.vertices = (
            (-1, -1, -1),  # 0
            (1, -1, -1),   # 1
            (0, 1, -1),    # 2
            (-1, -1, 1),   # 3
            (1, -1, 1),    # 4
            (0, 1, 1)      # 5
        )

        # Indeks sisi prisma (menggunakan quad untuk warna)
        self.faces = (
            (0, 1, 2),  # Segitiga bawah (depan)
            (3, 4, 5),  # Segitiga atas (belakang)
            (0, 1, 4, 3),  # Persegi kiri
            (1, 2, 5, 4),  # Persegi depan
            (2, 0, 3, 5),  # Persegi kanan
        )

        # Warna untuk masing-masing sisi
        self.colors = (
            (1, 0, 0),  # Merah (depan)
            (0, 1, 0),  # Hijau (belakang)
            (0, 0, 1),  # Biru (kiri)
            (1, 1, 0),  # Kuning (depan)
            (1, 0, 1)   # Magenta (kanan)
        )

    def draw(self):
        glBegin(GL_TRIANGLES)  # Untuk segitiga
        for i, face in enumerate(self.faces[:2]):  # Dua sisi segitiga
            glColor3fv(self.colors[i])  # Set warna untuk sisi ini
            for vertex in face:
                glVertex3fv(self.vertices[vertex])  # Gambar puncak
        glEnd()

        glBegin(GL_QUADS)  # Untuk persegi panjang
        for i, face in enumerate(self.faces[2:]):  # Tiga sisi persegi panjang
            glColor3fv(self.colors[i + 2])  # Set warna untuk sisi ini
            for vertex in face:
                glVertex3fv(self.vertices[vertex])  # Gambar puncak
        glEnd()
