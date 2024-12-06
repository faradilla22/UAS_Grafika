from OpenGL.GL import *

class Cube:
    def __init__(self):
        # Koordinat puncak kubus
        self.vertices = (
            (1, -1, -1),  # 0
            (1, 1, -1),   # 1
            (-1, 1, -1),  # 2
            (-1, -1, -1), # 3
            (1, -1, 1),   # 4
            (1, 1, 1),    # 5
            (-1, -1, 1),  # 6
            (-1, 1, 1)    # 7
        )

        # Indeks sisi kubus (menggunakan quad untuk warna)
        self.faces = (
            (0, 1, 2, 3),  # Belakang
            (4, 5, 6, 7),  # Depan
            (0, 1, 5, 4),  # Kanan
            (2, 3, 6, 7),  # Kiri
            (1, 2, 7, 5),  # Atas
            (0, 3, 6, 4)   # Bawah
        )

        # Warna untuk masing-masing sisi
        self.colors = (
            (1, 0, 0),  # Merah
            (0, 1, 0),  # Hijau
            (0, 0, 1),  # Biru
            (1, 1, 0),  # Kuning
            (1, 0, 1),  # Magenta
            (0, 1, 1)   # Cyan
        )

    def draw(self):
        glBegin(GL_QUADS)
        for i, face in enumerate(self.faces):
            glColor3fv(self.colors[i])  # Set warna untuk sisi ini
            for vertex in face:
                glVertex3fv(self.vertices[vertex])  # Gambar puncak
        glEnd()
