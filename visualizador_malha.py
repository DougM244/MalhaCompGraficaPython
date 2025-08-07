import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Vertice:
    def __init__(self, x, y, z):
        self.coord = (x, y, z)
        self.faces = []

class Face:
    def __init__(self, indices):
        self.indices = indices

class Malha:
    def __init__(self):
        self.vertices = []
        self.faces = []

    def carregar_off(self, caminho):
        with open(caminho, 'r') as f:
            if f.readline().strip() != 'OFF':
                raise Exception('Formato inválido')

            npontos, nfaces, _ = map(int, f.readline().split())

            for _ in range(npontos):
                x, y, z = map(float, f.readline().split())
                self.vertices.append(Vertice(x, y, z))

            for _ in range(nfaces):
                valores = list(map(int, f.readline().split()))
                indices = valores[1:]
                face = Face(indices)
                self.faces.append(face)
                for i in indices:
                    self.vertices[i].faces.append(face)

def visualizar_malha(malha, titulo='Malha'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    coords = [v.coord for v in malha.vertices]

    for face in malha.faces:
        pontos = [coords[i] for i in face.indices]
        poly = Poly3DCollection([pontos], edgecolor='k', facecolor='lightblue', alpha=0.8)
        ax.add_collection3d(poly)

    ax.set_title(titulo)
    ax.auto_scale_xyz(
        [v.coord[0] for v in malha.vertices],
        [v.coord[1] for v in malha.vertices],
        [v.coord[2] for v in malha.vertices]
    )
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    caminho_arquivo = input("Digite o caminho do arquivo OFF: ").strip()
    malha = Malha()
    malha.carregar_off(caminho_arquivo)
    visualizar_malha(malha, titulo=f'Malha: {caminho_arquivo}')
