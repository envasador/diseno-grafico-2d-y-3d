"""Mascota original del curso, dibujada píxel a píxel en rejillas de texto.
Todo se genera por código: no hay imágenes de terceros.

Cada frame se compone de tres capas: piernas, cuerpo (capucha, bufanda y túnica)
y brazo cercano. Los frames 4-6 del walking cycle reutilizan las piernas de los
frames 1-3 intercambiando pierna cercana y lejana, igual que se hace a mano."""

VERDE = '#43AA8C'; VOSC = '#1E6B55'; VCLARO = '#7FD1B5'
AMA = '#FFD167'; AMAOSC = '#E0A93B'
TINTA = '#10261F'; PAPEL = '#FFFDF7'; BLANCO = '#FFFFFF'
PIEL = '#F4C9A3'; PIELOSC = '#D99E78'
PIERNA_CERCA = '#2F7F68'; PIERNA_LEJOS = '#174D3F'; BOTA = '#33403B'
ACERO = '#E6EEEB'; ACEROSC = '#9FB3AC'
CORAL = '#E4572E'

PAL = {'G': VERDE, 'D': VOSC, 'L': VCLARO, 'Y': AMA, 'y': AMAOSC, 'S': PIEL, 's': PIELOSC,
       'K': TINTA, 'W': BLANCO, 'N': PIERNA_CERCA, 'F': PIERNA_LEJOS, 'B': BOTA,
       'A': VOSC, 'a': '#15473A', 'H': PIEL, 'X': ACERO, 'x': ACEROSC}

CUERPO = [            # 14 filas: capucha (8), bufanda (1), túnica (5)
    "......GGGG..",
    "....GGGLLGG.",
    "..DGGGLLGGGG",
    ".DDGGGGSSSSG",
    "DDDGGGGSSKSG",
    ".DDGGGGSSKSG",
    "..DDGGGsSSSG",
    "...DDGGGGGG.",
    "...YYYYYYYy.",
    "....DGGGGD..",
    "....DGGLGD..",
    "....DGGGGD..",
    "....KKyKKK..",
    "....DDDDDD..",
]
COLA_BUFANDA = [(2, 9, 'Y'), (1, 9, 'Y'), (0, 10, 'y')]   # (x, y relativa al cuerpo, color)

# Piernas: 14 columnas, la cadera ocupa las columnas 5-10. Se apoyan en el suelo.
PIERNAS = {
    'contacto': [          # frame 1: pierna cercana delante tocando el suelo (7 filas, cuerpo -1)
        ".....FFFNNN...",
        "....FFF..NNN..",
        "...FFF....NNN.",
        "...FF......NN.",
        "..FF.......NN.",
        "..FF........NN",
        ".BBB.......BBB",
    ],
    'recepcion': [         # frame 2: carga el peso, la lejana se levanta (6 filas, cuerpo -2)
        ".....FFNNN....",
        "....FF..NNN...",
        "...FF....NN...",
        "..FFB....NN...",
        ".BB......NN...",
        "........BBBB..",
    ],
    'paso': [              # frame 3: la lejana pasa junto a la de apoyo (8 filas, cuerpo arriba)
        ".....FNNNF....",
        ".....NNNFFF...",
        ".....NNN.FFF..",
        ".....NNN..FF..",
        ".....NNN.FF...",
        ".....NNNFBB...",
        ".....NNN......",
        ".....BBBB.....",
    ],
    'firme': [             # idle (8 filas)
        ".....FFNNN....",
        ".....FF.NN....",
        ".....FF.NN....",
        ".....FF.NN....",
        ".....FF.NN....",
        ".....FF.NN....",
        ".....FF.NN....",
        "....BBBBBBB...",
    ],
    'firme_baja': [        # idle respirando (7 filas)
        ".....FFNNN....",
        ".....FF.NN....",
        "....FF..NN....",
        "....FF..NN....",
        ".....FF.NN....",
        ".....FF.NN....",
        "....BBBBBBB...",
    ],
    'guardia': [           # ataque: piernas abiertas (7 filas)
        ".....FFFNNN...",
        "....FFF..NNN..",
        "...FFF....NN..",
        "...FF.....NN..",
        "..FF.......NN.",
        "..FF.......NN.",
        ".BBB.......BBB",
    ],
    'sentado': [           # waiting: sentado con las piernas estiradas (2 filas)
        ".....FFFFFFFFB",
        ".....NNNNNNNNB",
    ],
}


def invertir(filas):
    """Intercambia pierna cercana y lejana: así salen los frames 4-6 de los 1-3."""
    return [f.replace('N', '#').replace('F', 'N').replace('#', 'F') for f in filas]


# Brazos: (rejilla, columna y fila del hombro dentro de la rejilla). La mano va marcada con H.
BRAZOS = {
    'atras':         (["...AA", "..Aa.", ".Aa..", "HH..."], 3, 0),
    'medio_atras':   (["..AA", "..Aa", ".Aa.", ".HH."], 2, 0),
    'medio_delante': (["AA..", "aA..", ".aA.", "..HH"], 0, 0),
    'delante':       (["AA...", ".aA..", "..aA.", "...HH"], 0, 0),
    'colgando':      (["AA", "aA", "aA", "HH"], 0, 0),
    'rodilla':       (["AA...", ".aAA.", "...HH"], 0, 0),
    # con espada
    'anticipacion': (["X.......",
                      "xX......",
                      ".xX.....",
                      "..xX....",
                      "...YHH..",
                      "....HHa.",
                      ".....aAA",
                      "......AA"], 6, 7),
    'golpe':      (["AAaHHYXXXXXXXXX",
                    ".AaHHYxxxxxxxxx"], 0, 0),
    'golpe_baja': (["AA.........",
                    ".aAHHYXX...",
                    "..aHHYxxXX.",
                    "......xxxXX",
                    ".........xx"], 0, 0),
    'final':      (["AA......",
                    ".aA.....",
                    "..aAHH..",
                    "...YHHX.",
                    ".....xX.",
                    "......xX",
                    ".......xX",
                    "........x"], 0, 0),
    'retroceso':  (["AA....",
                    ".aA...",
                    ".aA...",
                    "..aHH.",
                    "..YHH.",
                    "...xX.",
                    "...xX.",
                    "....xX",
                    "....x."], 0, 0),
}


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
        self.mano = None; self.pie = None; self.hombro = None

    def put(self, x, y, c):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.px[(x, y)] = c

    def ascii(self, filas, ox, oy):
        for j, fila in enumerate(filas):
            for i, ch in enumerate(fila):
                if ch not in '.#':
                    self.put(ox + i, oy + j, PAL[ch])

    def contorno(self, c=TINTA):
        nuevos = set()
        for (x, y) in self.px:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in self.px and 0 <= q[0] < self.w and 0 <= q[1] < self.h:
                    nuevos.add(q)
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


def mascota(piernas='firme', brazo='colgando', invertidas=False, bufanda=0, ancho=24, alto=26,
            ox=6, contorno=True):
    """Compone un frame. El suelo está en la fila alto-2; el cuerpo baja según la altura
    de la rejilla de piernas (8 filas = altura máxima)."""
    L = Lienzo(ancho, alto)
    suelo = alto - 2
    pier = PIERNAS[piernas]
    if invertidas:
        pier = invertir(pier)
    hp = len(pier)
    top = suelo - hp - 13
    y_p = suelo - hp + 1
    L.ascii(pier, ox - 1, y_p)
    L.ascii(CUERPO, ox, top)
    for (x, y, ch) in COLA_BUFANDA:
        L.put(ox + x, top + y + bufanda, PAL[ch])
    rej, hx, hy = BRAZOS[brazo]
    hombro = (ox + 7, top + 10)
    bx, by = hombro[0] - hx, hombro[1] - hy
    L.ascii(rej, bx, by)
    manos = [(bx + i, by + j) for j, f in enumerate(rej) for i, ch in enumerate(f) if ch == 'H']
    L.mano = manos[0] if manos else hombro
    L.hombro = hombro
    botas = [(ox - 1 + i, y_p + j) for j, f in enumerate(pier) for i, ch in enumerate(f) if ch == 'B']
    ns = [(ox - 1 + i, y_p + j) for j, f in enumerate(pier) for i, ch in enumerate(f) if ch == 'N']
    if ns and botas:
        n_bajo = max(ns, key=lambda p: (p[1], p[0]))
        L.pie = min(botas, key=lambda b: abs(b[0] - n_bajo[0]) + abs(b[1] - n_bajo[1]))
    if contorno:
        L.contorno()
    return L


# Poses. Los frames 4-6 son los 1-3 con las piernas intercambiadas.
WALK = [
    dict(piernas='contacto', brazo='atras'),
    dict(piernas='recepcion', brazo='medio_atras'),
    dict(piernas='paso', brazo='medio_delante'),
    dict(piernas='contacto', brazo='delante', invertidas=True),
    dict(piernas='recepcion', brazo='medio_delante', invertidas=True),
    dict(piernas='paso', brazo='medio_atras', invertidas=True),
]
IDLE = [dict(piernas='firme', brazo='colgando'),
        dict(piernas='firme_baja', brazo='colgando', bufanda=1)]
SENTADO = dict(piernas='sentado', brazo='rodilla')
ATAQUE = [  # anticipación, golpe, final, retroceso
    dict(piernas='guardia', brazo='anticipacion'),
    dict(piernas='guardia', brazo='golpe'),
    dict(piernas='guardia', brazo='final'),
    dict(piernas='firme_baja', brazo='retroceso'),
]
GOLPE_BAJA = dict(piernas='guardia', brazo='golpe_baja')
