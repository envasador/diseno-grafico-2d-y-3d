"""Mascota original y utilidades de pixel art para los diagramas del curso.
Todo se genera por código: no hay imágenes de terceros."""

VERDE = '#43AA8C'; VOSC = '#1E6B55'; VCLARO = '#7FD1B5'
AMA = '#FFD167'; AMAOSC = '#E0A93B'
TINTA = '#10261F'; PAPEL = '#FFFDF7'; BLANCO = '#FFFFFF'
PIEL = '#F4C9A3'; PIELOSC = '#D99E78'
PIERNA_CERCA = '#2F7F68'; PIERNA_LEJOS = '#174D3F'
ACERO = '#E6EEEB'; ACEROSC = '#9FB3AC'
CORAL = '#E4572E'

PAL = {'G': VERDE, 'D': VOSC, 'L': VCLARO, 'Y': AMA, 'y': AMAOSC, 'S': PIEL, 's': PIELOSC,
       'K': TINTA, 'W': BLANCO}

# Capucha y cara, mirando a la derecha (12 de ancho)
CABEZA = [
    "......GGGG..",
    "....GGGGGGG.",
    "..GGGLLGGGGG",
    ".GGGLGGSSSSG",
    "GGGGGGSSSKSG",
    ".GGGGGSSSKSG",
    "..GGGGGssSSG",
    "...GGGGGGGG.",
]
BUFANDA = "...YYYYYYYY."
TORSO = [
    "....DDDDDD..",
    "....DDGDDD..",
    "....DDDDDD..",
    "....KKyKKK..",
    "....DDDDDD..",
]


def linea(x0, y0, x1, y1):
    pts = []; dx = abs(x1 - x0); dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1; sy = 1 if y0 < y1 else -1; err = dx + dy
    while True:
        pts.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy; x0 += sx
        if e2 <= dx:
            err += dx; y0 += sy
    return pts


class Lienzo:
    def __init__(self, w, h):
        self.w, self.h = w, h; self.px = {}

    def put(self, x, y, c, sobre=True):
        if 0 <= x < self.w and 0 <= y < self.h:
            if sobre or (x, y) not in self.px:
                self.px[(x, y)] = c

    def ascii(self, filas, ox, oy):
        for j, fila in enumerate(filas):
            for i, ch in enumerate(fila):
                if ch != '.':
                    self.put(ox + i, oy + j, PAL[ch])

    def trazo(self, x0, y0, x1, y1, c, grosor=2):
        for (x, y) in linea(x0, y0, x1, y1):
            for k in range(grosor):
                self.put(x + k, y, c)

    def contorno(self, c=TINTA):
        nuevos = []
        for (x, y) in list(self.px):
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in self.px and 0 <= q[0] < self.w and 0 <= q[1] < self.h:
                    nuevos.append(q)
        for q in nuevos:
            self.px[q] = c

    def silueta(self, c=TINTA):
        for k in self.px:
            self.px[k] = c

    def bbox(self):
        xs = [x for x, _ in self.px]; ys = [y for _, y in self.px]
        return min(xs), min(ys), max(xs), max(ys)

    def svg(self, x0, y0, S):
        return '\n'.join(f'<rect x="{x0 + x * S}" y="{y0 + y * S}" width="{S}" height="{S}" fill="{c}"/>'
                         for (x, y), c in self.px.items())


def mascota(off=0, pieA=(2, 0), pieB=(-2, 0), brazo=(1, 4), espada=None, ancho=24, alto=26,
            ox=6, sentado=False, contorno=True, bufanda=(0, 0)):
    """Dibuja la mascota.
    off: cuánto baja el cuerpo (px). pieA / pieB: (desplazamiento x del pie respecto a la cadera,
    elevación sobre el suelo). A es la pierna cercana. brazo: vector del brazo cercano desde el hombro.
    espada: vector de la hoja desde la mano, o None."""
    L = Lienzo(ancho, alto)
    suelo = alto - 2
    top = suelo - 21 + off          # altura total del personaje en reposo: 22 px
    cadera = (ox + 6, top + 13)
    # piernas: lejana primero
    for (fx, lift), col in ((pieB, PIERNA_LEJOS), (pieA, PIERNA_CERCA)):
        if sentado:
            fy = cadera[1]
        else:
            fy = suelo - lift
        L.trazo(cadera[0], cadera[1], cadera[0] + fx, fy, col)
        for k in range(3):
            L.put(cadera[0] + fx + k, fy, TINTA)          # bota
    # cuerpo
    L.ascii(TORSO, ox, top + 9)
    L.ascii([BUFANDA], ox, top + 8)
    # cola de la bufanda (ondea hacia atrás)
    bx, by = bufanda
    L.put(ox + 2, top + 9 + by, AMA); L.put(ox + 1, top + 9 + by, AMA); L.put(ox + 0 + bx, top + 10 + by, AMAOSC)
    L.ascii(CABEZA, ox, top)
    # brazo cercano
    hombro = (ox + 7, top + 10)
    mano = (hombro[0] + brazo[0], hombro[1] + brazo[1])
    for (x, y) in linea(hombro[0], hombro[1], mano[0], mano[1]):
        L.put(x, y, VERDE); L.put(x + 1, y, VCLARO)
    L.put(mano[0], mano[1], PIEL); L.put(mano[0] + 1, mano[1], PIEL)
    if espada:
        ex, ey = espada
        L.put(mano[0] + 1, mano[1], AMAOSC)                # empuñadura
        for (x, y) in linea(mano[0] + 1, mano[1], mano[0] + 1 + ex, mano[1] + ey)[1:]:
            L.put(x, y, ACERO); L.put(x, y + 1, ACEROSC)
    if contorno:
        L.contorno()
    return L


# Poses del walking cycle (receta de 6 frames). off, pie cercano, pie lejano, brazo
WALK = [
    dict(off=1, pieA=(4, 0), pieB=(-4, 0), brazo=(-4, 3)),
    dict(off=2, pieA=(1, 0), pieB=(-4, 2), brazo=(-2, 4)),
    dict(off=0, pieA=(-1, 0), pieB=(2, 3), brazo=(1, 4)),
    dict(off=1, pieA=(-4, 0), pieB=(4, 0), brazo=(4, 3)),
    dict(off=2, pieA=(-4, 2), pieB=(1, 0), brazo=(2, 4)),
    dict(off=0, pieA=(2, 3), pieB=(-1, 0), brazo=(-1, 4)),
]
IDLE = [dict(off=0, pieA=(1, 0), pieB=(-2, 0), brazo=(0, 4)),
        dict(off=1, pieA=(1, 0), pieB=(-2, 0), brazo=(0, 4), bufanda=(0, 1))]
ATAQUE = [  # anticipación, golpe, final, retroceso
    dict(off=1, pieA=(2, 0), pieB=(-3, 0), brazo=(-3, -2), espada=(-5, -5)),
    dict(off=1, pieA=(4, 0), pieB=(-4, 0), brazo=(4, 0), espada=(9, 0)),
    dict(off=1, pieA=(4, 0), pieB=(-4, 0), brazo=(4, 2), espada=(7, 5)),
    dict(off=0, pieA=(2, 0), pieB=(-2, 0), brazo=(2, 3), espada=(5, 6)),
]
