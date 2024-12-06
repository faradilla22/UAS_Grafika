from OpenGL.GL import *

class Pyramid:
    def __init__(self):
        # Koordinat puncak piramida
        self.vertices = (
            (1, -1, -1),  # 0
            (1, 1, -1),   # 1
            (-1, 1, -1),  # 2
            (-1, -1, -1), # 3
            (0, 0, 1)     # 4 (Puncak piramida)
        )

        # Indeks sisi piramida (menggunakan triangle untuk warna)
        self.faces = (
            (0, 1, 2),  # Sisi bawah
            (0, 1, 3),  # Sisi depan
            (1, 2, 3),  # Sisi kanan
            (2, 0, 3),  # Sisi kiri
            (4, 0, 1),  # Sisi depan atas
            (4, 1, 2),  # Sisi kanan atas
            (4, 2, 3),  # Sisi belakang atas
            (4, 3, 0)   # Sisi kiri atas
        )

        # Warna untuk masing-masing sisi
        self.colors = (
            (1, 0, 0),  # Merah (bawah)
            (0, 1, 0),  # Hijau (depan)
            (0, 0, 1),  # Biru (kanan)
            (1, 1, 0),  # Kuning (kiri)
            (1, 0, 1),  # Magenta (depan atas)
            (0, 1, 1),  # Cyan (kanan atas)
            (1, 1, 1),  # Putih (belakang atas)
            (0.5, 0.5, 0.5)  # Abu-abu (kiri atas)
        )

    def draw(self):
        glBegin(GL_TRIANGLES)  # Untuk sisi segitiga
        for i, face in enumerate(self.faces):
            glColor3fv(self.colors[i])  # Set warna untuk sisi ini
            for vertex in face:
                glVertex3fv(self.vertices[vertex])  # Gambar puncak
        glEnd()
