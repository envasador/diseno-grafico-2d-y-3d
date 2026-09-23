"""Genera todos los diagramas originales del curso en SVG."""
import math, os
from sprites import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'docs', 'assets')
FONT = "IBM Plex Sans, Helvetica, Arial, sans-serif"


class SVG:
    def __init__(self, w, h, fondo=BLANCO):
        self.w, self.h = w, h
        self.p = [f'<rect width="{w}" height="{h}" fill="{fondo}"/>']

    def add(self, s): self.p.append(s)

    def panel(self, x, y, w, h, num=None, borde=TINTA, relleno=BLANCO, sombra=True, badge=AMA):
        if sombra:
            self.add(f'<rect x="{x+5}" y="{y+5}" width="{w}" height="{h}" fill="{TINTA}"/>')
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{relleno}" stroke="{borde}" stroke-width="3"/>')
        if num is not None:
            self.add(f'<rect x="{x}" y="{y}" width="30" height="26" fill="{badge}" stroke="{TINTA}" stroke-width="3"/>')
            self.text(x + 15, y + 19, str(num), 15, anchor='middle', peso=700)

    def text(self, x, y, t, size=15, anchor='start', peso=600, color=TINTA, italic=False):
        st = ' font-style="italic"' if italic else ''
        self.add(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" font-weight="{peso}" fill="{color}"{st}>{t}</text>')

    def linea(self, x1, y1, x2, y2, color=TINTA, w=3, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d}/>')

    def flecha(self, x1, y1, x2, y2, color=TINTA, w=3):
        self.linea(x1, y1, x2, y2, color, w)
        a = math.atan2(y2 - y1, x2 - x1); L = 12
        p1 = (x2 - L * math.cos(a - 0.45), y2 - L * math.sin(a - 0.45))
        p2 = (x2 - L * math.cos(a + 0.45), y2 - L * math.sin(a + 0.45))
        self.add(f'<polygon points="{x2},{y2} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{color}"/>')

    def sprite(self, L, x, y, S):
        self.add(L.svg(x, y, S))

    def guardar(self, ruta):
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
             f'font-family="{FONT}" shape-rendering="crispEdges">\n' + '\n'.join(self.p) + '\n</svg>\n')
        s = s.replace('<text ', '<text shape-rendering="auto" ')
        open(ruta, 'w').write(s)


def tira(frames, S=6, gap=14, num=True, bordes=None, pie=None, guias=None, margen=16, extra_alto=0):
    """Tira de frames en paneles. Devuelve (svg, lista de (x,y) de cada sprite)."""
    fw, fh = frames[0].w * S, frames[0].h * S
    pw, ph = fw + 12, fh + 34
    W = margen * 2 + len(frames) * pw + (len(frames) - 1) * gap + 5
    H = margen * 2 + ph + 5 + (30 if pie else 0) + extra_alto
    g = SVG(W, H)
    pos = []
    for i, L in enumerate(frames):
        x = margen + i * (pw + gap); y = margen
        borde = bordes[i] if bordes else TINTA
        g.panel(x, y, pw, ph, num=(i + 1) if num else None, borde=borde)
        if bordes:
            g.add(f'<rect x="{x+3}" y="{y+3}" width="{pw-6}" height="{ph-6}" fill="none" stroke="{borde}" stroke-width="5"/>')
        sx, sy = x + 6, y + 28
        g.sprite(L, sx, sy, S)
        pos.append((sx, sy))
        if pie:
            g.text(x + pw / 2, y + ph + 27, pie[i], 15, anchor='middle')
    return g, pos, (pw, ph)


def frames_walk(**kw): return [mascota(**p, **kw) for p in WALK]


# ---------------------------------------------------------------- WALK CYCLE
def walk():
    fr = frames_walk()
    g, pos, _ = tira(fr, S=6)
    g.guardar(f'{OUT}/ut2/walk-6-frames.svg')

    # alturas: línea de altura máxima y etiqueta
    etiquetas = ['−1 px', '−2 px', 'máx.', '−1 px', '−2 px', 'máx.']
    g, pos, (pw, ph) = tira(fr, S=6, pie=etiquetas)
    S = 6; suelo = 24; top0 = suelo - 21 - 1  # fila del contorno superior con off=0
    for (sx, sy) in pos:
        yl = sy + top0 * S
        g.linea(sx - 2, yl, sx + fr[0].w * S + 2, yl, CORAL, 3, '8 5')
    g.guardar(f'{OUT}/ut2/walk-alturas.svg')

    # colores por parejas equivalentes
    cols = [VERDE, AMAOSC, CORAL] * 2
    g, pos, _ = tira(fr, S=6, bordes=cols, pie=['A', 'B', 'C', 'A′', 'B′', 'C′'])
    g.guardar(f'{OUT}/ut2/walk-copiar.svg')

    # brazos y piernas: frames 1 y 4 con anotaciones
    sel = [fr[0], fr[3]]
    S = 8
    g, pos, (pw, ph) = tira(sel, S=S, num=False, gap=60, extra_alto=70)
    notas = [('pierna cercana delante', 'brazo cercano detrás'), ('pierna cercana detrás', 'brazo cercano delante')]
    for i, (sx, sy) in enumerate(pos):
        p = WALK[0 if i == 0 else 3]
        top = 24 - 21 + p['off']
        pie = (6 + 6 + p['pieA'][0] + 1, 24)
        mano = (6 + 7 + p['brazo'][0], top + 10 + p['brazo'][1])
        px_, py_ = sx + pie[0] * S + S / 2, sy + pie[1] * S + S / 2
        mx_, my_ = sx + mano[0] * S + S / 2, sy + mano[1] * S + S / 2
        g.add(f'<circle cx="{px_}" cy="{py_}" r="11" fill="none" stroke="{CORAL}" stroke-width="4"/>')
        g.add(f'<circle cx="{mx_}" cy="{my_}" r="11" fill="none" stroke="{AMAOSC}" stroke-width="4"/>')
        cx = sx - 6 + pw / 2
        g.text(cx, sy + ph + 10, notas[i][1], 16, anchor='middle', color=AMAOSC, peso=700)
        g.text(cx, sy + ph + 36, notas[i][0], 16, anchor='middle', color=CORAL, peso=700)
    g.guardar(f'{OUT}/ut2/walk-brazos-piernas.svg')


# ---------------------------------------------------------------- IDLE / WAITING
def idle():
    a = [mascota(**IDLE[0]), mascota(**IDLE[1])]
    sentado = mascota(off=7, sentado=True, pieA=(6, 0), pieB=(5, 0), brazo=(3, 2))
    S = 6
    fw, fh = a[0].w * S, a[0].h * S
    pw, ph = fw + 12, fh + 34
    W = 16 * 2 + pw * 3 + 14 * 2 + 70 + 5
    g = SVG(W, 16 * 2 + ph + 70)
    xs = [16, 16 + pw + 14, 16 + 2 * pw + 28 + 70]
    for i, L in enumerate(a + [sentado]):
        g.panel(xs[i], 16, pw, ph, num=i + 1 if i < 2 else None, badge=AMA if i < 2 else VCLARO)
        g.sprite(L, xs[i] + 6, 16 + 28, S)
    g.text(xs[2] + pw - 40, 16 + 70, 'z', 22, peso=700, color=VOSC)
    g.text(xs[2] + pw - 26, 16 + 52, 'z', 28, peso=700, color=VOSC)
    g.flecha(xs[1] + pw + 12, 16 + ph / 2, xs[2] - 14, 16 + ph / 2)
    g.text((xs[0] + xs[1] + pw) / 2, 16 + ph + 38, 'Idle (en bucle)', 16, anchor='middle', peso=700)
    g.text(xs[2] + pw / 2, 16 + ph + 38, 'Waiting', 16, anchor='middle', peso=700)
    g.text(xs[1] + pw + 45, 16 + ph / 2 - 14, 'tras unos', 12, anchor='middle', peso=500)
    g.text(xs[1] + pw + 45, 16 + ph / 2 + 30, 'segundos', 12, anchor='middle', peso=500)
    g.guardar(f'{OUT}/ut2/idle-waiting.svg')


# ---------------------------------------------------------------- ATAQUE
def estela(g, sx, sy, S, cx, cy, r, a0, a1, grosor):
    """Motion blur dibujado como arco de píxeles."""
    pts = set()
    for k in range(200):
        a = math.radians(a0 + (a1 - a0) * k / 199)
        for t in range(grosor):
            rr = r - t * 0.9
            pts.add((round(cx + rr * math.cos(a)), round(cy + rr * math.sin(a))))
    for (x, y) in pts:
        g.add(f'<rect x="{sx + x*S}" y="{sy + y*S}" width="{S}" height="{S}" fill="{AMA}" opacity="0.85"/>')


def ataque():
    fr = [mascota(ancho=34, **p) for p in ATAQUE]
    nombres = ['Anticipación', 'Golpe', 'Final del golpe', 'Retroceso']
    S = 5
    g, pos, (pw, ph) = tira(fr, S=S, pie=nombres, num=True)
    # estela en el golpe (frame 2): arco desde arriba-atrás hasta delante
    sx, sy = pos[1]
    top = 24 - 21 + 1; hombro = (6 + 7, top + 10)
    estela(g, sx, sy, S, hombro[0] + 1, hombro[1] + 1, 13, -120, -8, 4)
    g.sprite(fr[1], sx, sy, S)      # personaje por encima de la estela
    # resaltar el golpe
    x = 16 + 1 * (pw + 14)
    g.add(f'<rect x="{x+3}" y="{16+3}" width="{pw-6}" height="{ph-6}" fill="none" stroke="{CORAL}" stroke-width="5"/>')
    g.guardar(f'{OUT}/ut2/ataque-estados.svg')

    # easy out: dos filas
    S = 4
    golpe = ATAQUE[1]
    con = [dict(golpe), dict(golpe, brazo=(4, 1), espada=(8, 3)), dict(golpe, brazo=(4, 2), espada=(7, 5)), dict(golpe, brazo=(4, 2), espada=(7, 5))]
    sin = [dict(golpe), dict(golpe, brazo=(4, 2), espada=(7, 5)), dict(golpe, brazo=(4, 2), espada=(7, 5)), dict(golpe, brazo=(4, 2), espada=(7, 5))]
    filas = [('Con ease out: la espada frena poco a poco', con), ('Sin ease out: la espada se para en seco', sin)]
    fw, fh = 34 * S, 26 * S
    pw, ph = fw + 12, fh + 12
    W = 16 * 2 + 4 * pw + 3 * 12 + 5
    g = SVG(W, 16 + 2 * (ph + 60) + 10)
    for r, (titulo, poses) in enumerate(filas):
        y0 = 16 + r * (ph + 60)
        g.text(16, y0 + 18, titulo, 16, peso=700, color=VOSC if r == 0 else CORAL)
        for i, p in enumerate(poses):
            x = 16 + i * (pw + 12)
            g.panel(x, y0 + 30, pw, ph)
            g.sprite(mascota(ancho=34, **p), x + 6, y0 + 36, S)
    g.guardar(f'{OUT}/ut2/easy-out.svg')


def easing():
    W, H = 900, 300
    g = SVG(W, H)
    curvas = [('Lineal', lambda t: t), ('Ease in', lambda t: t * t), ('Ease out', lambda t: 1 - (1 - t) ** 2)]
    for i, (nom, f) in enumerate(curvas):
        x0 = 20 + i * 290; y0 = 20; w = 260; h = 250
        g.panel(x0, y0, w, h)
        g.text(x0 + 16, y0 + 30, nom, 18, peso=700)
        # ejes
        ax, ay, aw, ah = x0 + 30, y0 + 50, w - 60, 110
        # recorrido: 7 frames como puntos sobre una barra
        yb = y0 + 200
        g.linea(ax, yb, ax + aw, yb, TINTA, 2)
        for k in range(7):
            t = k / 6; px = ax + f(t) * aw
            g.add(f'<rect x="{px-9}" y="{yb-9}" width="18" height="18" fill="{AMA if k in (0,6) else VERDE}" stroke="{TINTA}" stroke-width="3"/>')
        # curva posición-tiempo
        pts = ' '.join(f'{ax + t/40*aw:.1f},{ay + ah - f(t/40)*ah:.1f}' for t in range(41))
        g.add(f'<polyline points="{pts}" fill="none" stroke="{VOSC}" stroke-width="4" shape-rendering="auto"/>')
        g.linea(ax, ay, ax, ay + ah, TINTA, 2); g.linea(ax, ay + ah, ax + aw, ay + ah, TINTA, 2)
        g.text(ax + aw, ay + ah + 16, 'tiempo', 11, anchor='end', peso=500)
        g.text(ax + 4, ay + 10, 'posición', 11, peso=500)
        g.text(ax + aw / 2, yb + 34, 'espaciado de los frames', 12, anchor='middle', peso=500)
    g.guardar(f'{OUT}/ut2/easing.svg')


# ---------------------------------------------------------------- PELOTA
def bola(g, x, y, rx, ry, color, sombra=True):
    if sombra:
        g.add(f'<ellipse cx="{x+4}" cy="{y+4}" rx="{rx}" ry="{ry}" fill="{TINTA}" shape-rendering="auto"/>')
    g.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{color}" stroke="{TINTA}" stroke-width="3" shape-rendering="auto"/>')


def pelota():
    W, H, ground, r = 900, 340, 300, 22
    def tray(n):
        out = []
        for k in range(n):
            t = k / (n - 1); x = 70 + t * 760; u = abs(2 * t - 1)
            out.append((x, ground - r - (u ** 2) * 220, u, k))
        return out
    # 1. solo fotogramas clave
    g = SVG(W, H)
    g.linea(30, ground, W - 30, ground, TINTA, 4)
    pts = tray(13)
    for (x, y, u, k) in pts:
        if k in (0, 6, 12):
            if k == 6: bola(g, x, ground - r * 0.62, r * 1.45, r * 0.62, AMA)
            else: bola(g, x, y, r, r, AMA)
    for i, k in enumerate((0, 6, 12)):
        x = pts[k][0]; g.text(x, pts[k][1] - 34 if k != 6 else ground - 40, str(i + 1), 18, anchor='middle', peso=700)
    g.guardar(f'{OUT}/ut2/keyframes.svg')
    # 2. con interpolaciones
    g = SVG(W, H)
    path = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y, _, _ in pts)
    g.add(f'<path d="{path}" fill="none" stroke="{TINTA}" stroke-width="2" stroke-dasharray="4 6" opacity="0.45" shape-rendering="auto"/>')
    g.linea(30, ground, W - 30, ground, TINTA, 4)
    for (x, y, u, k) in pts:
        key = k in (0, 6, 12)
        if k == 6: bola(g, x, ground - r * 0.62, r * 1.45, r * 0.62, AMA)
        elif u < 0.5: bola(g, x, y, r * 0.82, r * 1.25, VERDE)
        else: bola(g, x, y, r, r, AMA if key else VERDE)
    g.add(f'<rect x="30" y="16" width="16" height="16" fill="{AMA}" stroke="{TINTA}" stroke-width="3"/>')
    g.text(54, 30, 'Fotograma clave', 15)
    g.add(f'<rect x="210" y="16" width="16" height="16" fill="{VERDE}" stroke="{TINTA}" stroke-width="3"/>')
    g.text(234, 30, 'Interpolación', 15)
    g.guardar(f'{OUT}/ut2/interpolaciones.svg')

    # 3. timing: caída con espaciado uniforme vs gravedad
    W2, H2 = 700, 420
    g = SVG(W2, H2)
    cols = [('Espaciado uniforme', lambda t: t, 'parece un ascensor'), ('Espaciado con gravedad', lambda t: t * t, 'parece que cae')]
    for i, (nom, f, nota) in enumerate(cols):
        x0 = 30 + i * 340
        g.panel(x0, 20, 300, 380)
        g.text(x0 + 150, 50, nom, 17, anchor='middle', peso=700)
        g.linea(x0 + 60, 360, x0 + 240, 360, TINTA, 4)
        for k in range(7):
            y = 90 + f(k / 6) * 245
            bola(g, x0 + 150, y, 15, 15, AMA if k in (0, 6) else VERDE, sombra=False)
            g.text(x0 + (185 if k % 2 == 0 else 108), y + 5, str(k + 1), 13, peso=600)
        g.text(x0 + 150, 388, nota, 14, anchor='middle', peso=500, italic=True)
    g.guardar(f'{OUT}/ut2/timing.svg')

    # 4. squash y stretch
    g = SVG(760, 300)
    g.linea(30, 250, 730, 250, TINTA, 4)
    estados = [('Reposo', 130, 250 - 40, 40, 40), ('Stretch (cae deprisa)', 380, 120, 31, 55), ('Squash (impacto)', 620, 250 - 25, 64, 25)]
    for nom, x, y, rx, ry in estados:
        bola(g, x, y, rx, ry, AMA if nom != 'Reposo' else VERDE)
        g.text(x, 285, nom, 15, anchor='middle', peso=700)
    g.flecha(380, 190, 380, 225, VOSC)
    g.text(380, 40, 'El volumen se conserva: si se aplasta, se ensancha', 15, anchor='middle', peso=500, italic=True)
    g.guardar(f'{OUT}/ut2/squash-stretch.svg')


# ---------------------------------------------------------------- TAMAÑO
def raster_pocion(n):
    """Rasteriza una poción original a n x n píxeles con luz desde arriba a la izquierda."""
    L = Lienzo(n, n)
    for j in range(n):
        for i in range(n):
            x, y = (i + 0.5) / n, (j + 0.5) / n
            cx, cy, rr = 0.5, 0.64, 0.30
            d = math.hypot(x - cx, y - cy)
            cuello = abs(x - 0.5) < 0.09 and 0.20 < y < 0.38
            tapon = abs(x - 0.5) < 0.12 and 0.10 < y <= 0.20
            if tapon:
                L.put(i, j, AMAOSC if x > 0.5 else AMA)
            elif cuello:
                L.put(i, j, VCLARO)
            elif d < rr:
                if y < cy - 0.05:
                    col = VCLARO if d > rr * 0.75 else '#CFEDE2'   # vidrio vacío
                else:
                    col = VERDE
                    if (x - cx) + (y - cy) > 0.12: col = VOSC
                if math.hypot(x - 0.40, y - 0.52) < 0.05 and n >= 12: col = BLANCO
                L.put(i, j, col)
    L.contorno()
    return L


def raster_espada(n):
    L = Lienzo(n, n)
    def P(u, v): return (min(n - 1, int(u * n)), min(n - 1, int(v * n)))
    # hoja diagonal
    for (x, y) in linea(*P(0.28, 0.72), *P(0.88, 0.12)):
        L.put(x, y, ACERO)
        if n >= 24: L.put(x + 1, y, ACERO); L.put(x, y + 1, ACEROSC)
        else: L.put(x, y + 1, ACEROSC)
    # guarda
    for (x, y) in linea(*P(0.14, 0.62), *P(0.38, 0.86)):
        L.put(x, y, AMA)
        if n >= 24: L.put(x + 1, y, AMAOSC)
    # empuñadura
    for (x, y) in linea(*P(0.24, 0.76), *P(0.10, 0.90)):
        L.put(x, y, VOSC)
    L.put(*P(0.07, 0.93), AMA)
    L.contorno()
    return L


def tamano():
    # más píxeles, más detalle: poción a 8, 16 y 32
    g = SVG(900, 330)
    for i, n in enumerate((8, 16, 32)):
        x0 = 20 + i * 295
        g.panel(x0, 20, 260, 280)
        S = 224 // n
        L = raster_pocion(n)
        g.sprite(L, x0 + 130 - n * S / 2, 36, S)
        g.text(x0 + 130, 285, f'{n} × {n} px', 17, anchor='middle', peso=700)
    g.guardar(f'{OUT}/ut2/tamano-estilos.svg')

    # espada 16 vs 32 (dos zooms)
    g = SVG(760, 360)
    for i, n in enumerate((16, 32)):
        x0 = 20 + i * 370
        g.panel(x0, 20, 330, 320)
        S = 256 // n
        g.sprite(raster_espada(n), x0 + 165 - n * S / 2, 36, S)
        g.text(x0 + 165, 312, f'{n} × {n} px = {n*n} píxeles', 17, anchor='middle', peso=700)
    g.guardar(f'{OUT}/ut2/tamano-16-32.svg')

    # potencias de dos anidadas
    g = SVG(560, 560)
    base = 520
    tam = [1024, 512, 256, 128, 64, 32]
    for k, t in enumerate(tam):
        s = base * t / 1024
        fill = [BLANCO, '#F3FAF7', '#E3F4EC', VCLARO, VERDE, AMA][k]
        g.add(f'<rect x="20" y="{20 + base - s}" width="{s}" height="{s}" fill="{fill}" stroke="{TINTA}" stroke-width="3"/>')
        if t >= 128:
            g.text(20 + s - 8, 20 + base - s + 22, f'{t}×{t}', 15, anchor='end', peso=700)
    for t, ly in ((64, 470), (32, 505)):
        s_ = base * t / 1024
        yb = 20 + base - s_ / 2
        g.linea(20 + s_, yb, 330, ly, TINTA, 2)
        g.text(338, ly + 5, f'{t}×{t}', 15, peso=700)
    g.guardar(f'{OUT}/ut2/tamano-potencias.svg')


# ---------------------------------------------------------------- TILES
TIERRA = '#9A6B45'; TIERRAOSC = '#744D30'; TIERRACLARA = '#B8865C'; CIELO = '#D9F0E8'
import random


def tile(tipo, n=16, semilla=0):
    rnd = random.Random(semilla)
    L = Lienzo(n, n)
    arriba = tipo in ('tl', 't', 'tr'); izq = tipo in ('tl', 'l', 'bl'); der = tipo in ('tr', 'r', 'br'); abajo = tipo in ('bl', 'b', 'br')
    for j in range(n):
        for i in range(n):
            c = TIERRA
            r = rnd.random()
            if r < 0.10: c = TIERRAOSC
            elif r < 0.16: c = TIERRACLARA
            if arriba and j < 4:
                c = VERDE if j < 3 else VOSC
                if j == 0: c = VCLARO
                if j == 3 and rnd.random() < 0.5: c = TIERRA
            if izq and i < 1 or der and i > n - 2 or abajo and j > n - 2: c = TIERRAOSC
            L.put(i, j, c)
    if tipo == 'flor':
        pass
    return L


def tileset():
    tipos = [['tl', 't', 'tr'], ['l', 'c', 'r'], ['bl', 'b', 'br']]
    S = 5; n = 16; ts = n * S
    W, H = 900, 380
    g = SVG(W, H)
    # tileset en rejilla
    g.panel(20, 40, 3 * ts + 24, 3 * ts + 24)
    g.text(20, 26, 'Tileset (9 piezas de 16×16)', 16, peso=700)
    for j in range(3):
        for i in range(3):
            x, y = 32 + i * (ts + 0), 52 + j * (ts + 0)
            g.sprite(tile(tipos[j][i], semilla=j * 3 + i), x, y, S)
    for k in range(4):
        g.linea(32 + k * ts, 52, 32 + k * ts, 52 + 3 * ts, BLANCO, 2)
        g.linea(32, 52 + k * ts, 32 + 3 * ts, 52 + k * ts, BLANCO, 2)
    g.flecha(3 * ts + 70, 40 + 1.5 * ts + 12, 3 * ts + 140, 40 + 1.5 * ts + 12)
    # escena montada
    ox, oy = 3 * ts + 160, 40
    cols, filas = 17, 9; S2 = 2; t2 = n * S2
    g.text(ox, 26, 'Nivel montado con esas piezas', 16, peso=700)
    g.add(f'<rect x="{ox}" y="{oy}" width="{cols*t2}" height="{filas*t2}" fill="{CIELO}" stroke="{TINTA}" stroke-width="3"/>')
    mapa = [
        '.................',
        '.................',
        '..........[=].....',
        '.................',
        '....[=]..........',
        '.................',
        '[=====]...[======',
        '|#####|...|######',
        '|#####|...|######',
    ]
    cod = {'[': 'tl', '=': 't', ']': 'tr', '|': 'l', '#': 'c'}
    for j, fila in enumerate(mapa):
        for i, ch in enumerate(fila[:cols]):
            if ch in cod:
                tp = cod[ch]
                if ch == '#' and i == cols - 1: tp = 'c'
                if ch == '#' and i + 1 < len(fila) and fila[i + 1] == '|': tp = 'r'
                if ch == '|' and i > 0 and fila[i - 1] == '#': tp = 'r'
                if ch == '=' and i + 1 < len(fila) and fila[i + 1] in '.': tp = 'tr'
                g.sprite(tile(tp, semilla=i * 7 + j), ox + i * t2, oy + j * t2, S2)
    m = mascota(contorno=True)
    g.sprite(m, ox + 1 * t2, oy + 6 * t2 - 24 * S2 + 2, S2)
    g.w = ox + cols * t2 + 20
    g.guardar(f'{OUT}/ut2/tileset.svg')


def tile_frame():
    fr = frames_walk()
    S = 3; fw = fr[0].w * S; fh = fr[0].h * S
    W, H = 900, 240
    g = SVG(W, H)
    # tira de película
    g.text(20, 30, 'Un tile es un frame', 17, peso=700)
    x0, y0 = 20, 50
    g.add(f'<rect x="{x0}" y="{y0}" width="{4*(fw+10)+10}" height="{fh+44}" fill="{TINTA}"/>')
    for k in range(4 * 3 + 1):
        g.add(f'<rect x="{x0 + 6 + k*((4*(fw+10))/13)}" y="{y0+5}" width="10" height="8" fill="{BLANCO}"/>')
        g.add(f'<rect x="{x0 + 6 + k*((4*(fw+10))/13)}" y="{y0+fh+31}" width="10" height="8" fill="{BLANCO}"/>')
    for i in range(4):
        x = x0 + 10 + i * (fw + 10)
        g.add(f'<rect x="{x}" y="{y0+20}" width="{fw}" height="{fh+4}" fill="{BLANCO}"/>')
        g.sprite(fr[i], x, y0 + 22, S)
    # rejilla con filas de animaciones
    gx, gy = 470, 50
    g.text(gx, 30, 'Cada fila de la rejilla, una animación', 17, peso=700)
    S2 = 2; cw, ch = 24 * S2 + 4, 26 * S2 + 4
    filas = [('idle', [mascota(**p) for p in IDLE]), ('walk', frames_walk()), ('ataque', [mascota(**p) for p in ATAQUE])]
    for r, (nom, lst) in enumerate(filas):
        g.text(gx, gy + r * ch + ch / 2 + 5, nom, 13, peso=700)
        for c in range(6):
            x = gx + 60 + c * cw; y = gy + r * ch
            g.add(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{BLANCO}" stroke="{TINTA}" stroke-width="2"/>')
            if c < len(lst):
                L = lst[c]
                if L.w > 24:  # recortar espada al tile
                    L2 = Lienzo(24, 26); L2.px = {k: v for k, v in L.px.items() if k[0] < 24}; L = L2
                g.sprite(L, x + 2, y + 2, S2)
    g.add(f'<rect x="{gx+60-3}" y="{gy+ch-3}" width="{6*cw+6}" height="{ch+6}" fill="none" stroke="{CORAL}" stroke-width="4"/>')
    g.guardar(f'{OUT}/ut2/tile-frame.svg')


def spritesheet():
    fr = frames_walk()
    S = 3; fw = fr[0].w * S; fh = fr[0].h * S
    W, H = 900, 260
    g = SVG(W, H)
    g.text(20, 30, 'Frames de la animación', 16, peso=700)
    for i, L in enumerate(fr):
        x = 20 + i * (fw + 14)
        g.panel(x, 45, fw, fh, sombra=False)
        g.sprite(L, x, 45, S)
    g.flecha(20 + 6 * (fw + 14) + 4, 45 + fh / 2, 20 + 6 * (fw + 14) + 60, 45 + fh / 2)
    sx = 20 + 6 * (fw + 14) + 80
    g.text(sx, 30, 'walk.png', 16, peso=700)
    g.panel(sx, 45, 3 * fw, 2 * fh)
    for i, L in enumerate(fr):
        g.sprite(L, sx + (i % 3) * fw, 45 + (i // 3) * fh, S)
    for k in range(1, 3): g.linea(sx + k * fw, 45, sx + k * fw, 45 + 2 * fh, VCLARO, 2, '4 4')
    g.linea(sx, 45 + fh, sx + 3 * fw, 45 + fh, VCLARO, 2, '4 4')
    g.w = sx + 3 * fw + 30
    g.guardar(f'{OUT}/ut2/spritesheet.svg')


def mismo_tamano():
    fr = frames_walk()
    S = 4; fw = fr[0].w * S; fh = fr[0].h * S
    W = 20 + 6 * (fw + 10) + 20
    g = SVG(W, fh + 120)
    for i, L in enumerate(fr):
        x = 20 + i * (fw + 10)
        g.add(f'<rect x="{x}" y="20" width="{fw}" height="{fh}" fill="{BLANCO}" stroke="{CORAL}" stroke-width="3" stroke-dasharray="7 5"/>')
        g.sprite(L, x, 20, S)
        g.flecha(x + fw / 2, fh + 40, x + 4, fh + 40, TINTA, 2); g.flecha(x + fw / 2, fh + 40, x + fw - 4, fh + 40, TINTA, 2)
        g.text(x + fw / 2, fh + 65, '24 px', 14, anchor='middle', peso=700)
    g.text(W / 2, fh + 100, 'Todos los frames de la animación miden exactamente lo mismo', 16, anchor='middle', peso=600, italic=True)
    g.guardar(f'{OUT}/ut2/frames-mismo-tamano.svg')


def potencia_dos():
    L = mascota(ancho=34, **ATAQUE[1])
    x0, y0, x1, y1 = L.bbox(); bw, bh = x1 - x0 + 1, y1 - y0 + 1
    S = 7
    g = SVG(900, 420)
    # izquierda: recorte ajustado
    g.text(40, 34, f'Sprite recortado: {bw} × {bh}', 16, peso=700, color=CORAL)
    ox, oy = 40, 60
    g.sprite(L, ox - x0 * S, oy - y0 * S, S)
    g.add(f'<rect x="{ox}" y="{oy}" width="{bw*S}" height="{bh*S}" fill="none" stroke="{CORAL}" stroke-width="3" stroke-dasharray="7 5"/>')
    g.text(ox + bw * S / 2, oy + bh * S + 36, '✗ tamaño irregular', 16, anchor='middle', peso=700, color=CORAL)
    g.flecha(ox + bw * S + 30, 170, ox + bw * S + 100, 170)
    # derecha: frame 64x64
    F = 32; S2 = 9
    fx, fy = ox + bw * S + 130, 30
    g.text(fx, 24, '', 1)
    g.panel(fx, fy, F * S2, F * S2)
    g.sprite(L, fx + ((F - bw) // 2 - x0) * S2, fy + (F - 2 - bh - y0) * S2, S2)
    g.text(fx + F * S2 / 2, fy + F * S2 + 36, '✓ frame de 32 × 32', 16, anchor='middle', peso=700, color=VOSC)
    g.w = fx + F * S2 + 30; g.h = fy + F * S2 + 50
    g.guardar(f'{OUT}/ut2/potencia-de-dos.svg')
    return bw, bh


# ---------------------------------------------------------------- SILUETAS (concept)
def fig_guerrero(g, x, y, c):   # base: pies en (x, y)
    g.add(f'<rect x="{x-34}" y="{y-120}" width="68" height="78" fill="{c}"/>')        # torso cuadrado
    g.add(f'<rect x="{x-30}" y="{y-44}" width="24" height="44" fill="{c}"/><rect x="{x+6}" y="{y-44}" width="24" height="44" fill="{c}"/>')
    g.add(f'<rect x="{x-16}" y="{y-150}" width="32" height="32" fill="{c}"/>')        # cabeza
    g.add(f'<rect x="{x+34}" y="{y-205}" width="14" height="150" fill="{c}"/><rect x="{x+22}" y="{y-80}" width="38" height="10" fill="{c}"/>')  # espadón
    g.add(f'<rect x="{x-50}" y="{y-122}" width="100" height="18" fill="{c}"/>')     # hombreras


def fig_maga(g, x, y, c):
    g.add(f'<polygon points="{x-45},{y} {x+45},{y} {x+12},{y-110} {x-12},{y-110}" fill="{c}"/>')  # túnica
    g.add(f'<circle cx="{x}" cy="{y-122}" r="16" fill="{c}"/>')
    g.add(f'<polygon points="{x-36},{y-132} {x+36},{y-132} {x+14},{y-150} {x-22},{y-210}" fill="{c}"/>')  # sombrero doblado
    g.add(f'<rect x="{x+50}" y="{y-170}" width="8" height="170" fill="{c}"/><circle cx="{x+54}" cy="{y-178}" r="14" fill="{c}"/>')
    g.add(f'<polygon points="{x+8},{y-100} {x+52},{y-120} {x+52},{y-108} {x+10},{y-88}" fill="{c}"/>')


def fig_picaro(g, x, y, c):
    g.add(f'<polygon points="{x-20},{y-60} {x+22},{y-60} {x+30},{y-120} {x-6},{y-128}" fill="{c}"/>')   # torso inclinado
    g.add(f'<polygon points="{x-6},{y-128} {x+34},{y-124} {x+18},{y-160} {x-26},{y-150}" fill="{c}"/>')  # capucha puntiaguda
    g.add(f'<polygon points="{x-20},{y-62} {x-4},{y-62} {x-34},{y} {x-50},{y}" fill="{c}"/>')           # pierna atrás
    g.add(f'<polygon points="{x+6},{y-62} {x+22},{y-62} {x+40},{y} {x+24},{y}" fill="{c}"/>')           # pierna delante
    g.add(f'<polygon points="{x+24},{y-110} {x+70},{y-90} {x+66},{y-82} {x+22},{y-98}" fill="{c}"/>')    # brazo con daga
    g.add(f'<polygon points="{x+66},{y-94} {x+96},{y-104} {x+70},{y-84}" fill="{c}"/>')


def fig_gigante(g, x, y, c):
    g.add(f'<ellipse cx="{x}" cy="{y-80}" rx="70" ry="62" fill="{c}" shape-rendering="auto"/>')
    g.add(f'<rect x="{x-44}" y="{y-40}" width="30" height="40" fill="{c}"/><rect x="{x+14}" y="{y-40}" width="30" height="40" fill="{c}"/>')
    g.add(f'<circle cx="{x+6}" cy="{y-150}" r="14" fill="{c}" shape-rendering="auto"/>')
    g.add(f'<ellipse cx="{x-72}" cy="{y-58}" rx="20" ry="40" fill="{c}" shape-rendering="auto"/><ellipse cx="{x+72}" cy="{y-58}" rx="20" ry="40" fill="{c}" shape-rendering="auto"/>')


def fig_generico(g, x, y, c):
    g.add(f'<rect x="{x-24}" y="{y-120}" width="48" height="70" fill="{c}"/>')
    g.add(f'<rect x="{x-22}" y="{y-52}" width="18" height="52" fill="{c}"/><rect x="{x+4}" y="{y-52}" width="18" height="52" fill="{c}"/>')
    g.add(f'<rect x="{x-36}" y="{y-118}" width="12" height="60" fill="{c}"/><rect x="{x+24}" y="{y-118}" width="12" height="60" fill="{c}"/>')
    g.add(f'<circle cx="{x}" cy="{y-136}" r="17" fill="{c}" shape-rendering="auto"/>')


def siluetas():
    W, H = 1000, 330
    g = SVG(W, H)
    g.panel(20, 20, 640, 290)
    figs = [(fig_guerrero, 'Guerrero'), (fig_maga, 'Maga'), (fig_picaro, 'Pícaro'), (fig_gigante, 'Gigante')]
    for i, (f, nom) in enumerate(figs):
        x = 95 + i * 150
        f(g, x, 270, TINTA)
        g.text(x, 298, nom, 14, anchor='middle', peso=700)
    g.panel(690, 20, 290, 290)
    fig_generico(g, 780, 270, TINTA); fig_generico(g, 890, 270, TINTA)
    g.text(835, 298, '¿Quién es quién?', 14, anchor='middle', peso=700, color=CORAL)
    g.guardar(f'{OUT}/concept/silueta-lectura.svg')

    # prueba del negro con la mascota
    m1 = mascota(**WALK[0]); m2 = mascota(**WALK[0]); m2.silueta()
    m3 = mascota(ancho=34, **ATAQUE[1]); m4 = mascota(ancho=34, **ATAQUE[1]); m4.silueta()
    S = 6
    g = SVG(1000, 250)
    items = [(m1, 'En color'), (m2, 'En negro'), (m3, 'En color'), (m4, 'En negro')]
    x = 20
    for L, nom in items:
        w = L.w * S + 12
        g.panel(x, 20, w, L.h * S + 12)
        g.sprite(L, x + 6, 26, S)
        g.text(x + w / 2, 20 + L.h * S + 42, nom, 15, anchor='middle', peso=700)
        x += w + 26
    g.w = x; g.h = 20 + 26 * S + 60
    g.guardar(f'{OUT}/concept/silueta-personajes.svg')


if __name__ == '__main__':
    walk(); idle(); ataque(); easing(); pelota(); tamano(); tileset(); tile_frame(); spritesheet(); mismo_tamano()
    print('potencia de dos:', potencia_dos())
    siluetas()
    print('ok')
