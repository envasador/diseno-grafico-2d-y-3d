# UT1.1 Ilustrar con Affinity

Casi todo el arte de un juego pasa en algún momento por un programa de ilustración: el concept del personaje, la composición que presentas al equipo, el logotipo del título o las piezas de la interfaz. En este módulo usamos Affinity, un programa profesional que desde finales de 2025 es gratuito (solo necesitas una cuenta de Canva) y que reúne en la misma aplicación el dibujo vectorial, la pintura en píxeles y la maquetación. Aquí vas a ver lo imprescindible para trabajar con soltura; el resto lo irás descubriendo a medida que lo necesites.

## Un programa, varios estudios

Affinity organiza sus herramientas en **estudios**. Los dos que vas a usar en esta unidad son el estudio **Vector**, para dibujar con formas y curvas, y el estudio **Pixel**, para pintar con pinceles como lo harías en papel. Cambias de uno a otro con los botones de la parte superior de la ventana, y los dos trabajan sobre el mismo documento: puedes construir un personaje con formas vectoriales y pintarle las sombras con un pincel sin salir del archivo.

Si has usado versiones anteriores (Affinity Designer o Affinity Photo), los estudios son lo que allí se llamaban "personas". Los archivos nuevos se guardan con extensión `.af`. El programa abre los antiguos `.afdesign`, pero las versiones antiguas no abren los nuevos, así que tenlo en cuenta si compartes archivos con alguien que no ha actualizado.

## Vectorial o píxel

Una forma vectorial es una descripción matemática ("un círculo de este radio con este relleno"). Por eso puedes escalarla todo lo que quieras sin que pierda nitidez, y cambiar su color o su curva en cualquier momento. Una capa de píxeles guarda el color de cada punto de la imagen: es ideal para texturas, trazos de pincel y sombras suaves, pero se degrada si la agrandas.

En concept para videojuegos lo habitual es combinarlos. Las formas principales (la silueta, las piezas del personaje, los elementos del escenario) se construyen en vectorial porque vas a cambiarlas muchas veces, y la textura y el acabado pictórico se añaden en píxel al final.

| | Vectorial | Píxel |
|---|---|---|
| Se escala sin perder calidad | Sí | No |
| Se edita después (forma, color) | Siempre | Solo repintando |
| Mejor para | Siluetas, piezas, logotipos, UI | Texturas, pinceladas, sombras suaves |

## Capas: trabajar sin destruir

Las capas son lo que te permite cambiar de opinión. Si el cuerpo, la cabeza y el arma de tu personaje están en capas separadas, puedes probar otra cabeza sin tocar lo demás. Acostúmbrate desde el primer día a tres hábitos: nombrar cada capa por lo que contiene, agrupar las que van juntas (Ctrl+G, o Cmd+G en Mac) y ocultar en lugar de borrar.

Hay dos formas de meter una capa dentro de otra, y conviene distinguirlas. Si arrastras una capa sobre el nombre de otra, queda **recortada** por ella y solo se ve dentro de su forma: así pintas las sombras de una pieza sin salirte, aunque el pincel se pase del borde. Si la arrastras sobre la miniatura, funciona como **máscara**, y sus zonas oscuras ocultan partes de la capa madre sin borrarlas.

Por último, las **capas de ajuste** (brillo y contraste, tono y saturación, curvas) modifican el color de todo lo que tienen debajo sin alterarlo. Son la manera rápida de probar si tu ilustración funciona mejor más fría, más oscura o más saturada.

## Formas, pluma y nodos

Casi todo en vectorial empieza con formas básicas: rectángulos, elipses, polígonos. A partir de ahí tienes tres maneras de llegar a la forma que buscas.

La primera es combinar formas con las **operaciones booleanas** (sumar, restar, intersecar), que aparecen en la barra superior cuando seleccionas dos o más formas. Una cabeza es un círculo; si le restas otro círculo desplazado, tienes una luna, y si le sumas dos triángulos, un gato. Es la forma más rápida de trabajar el lenguaje de formas del que hablamos en [Thumbnails y formas](../concept/thumbnails.md).

La segunda es editar los **nodos**. Con la herramienta Nodo (A) seleccionas los puntos de una curva y sus manejadores, y los mueves para ajustar el contorno. Si la forma todavía es una forma básica (un círculo recién dibujado), primero hay que convertirla en curvas (Ctrl+Intro, o Cmd+Return en Mac).

La tercera es dibujar el trazo directamente. Con la **Pluma** (P) colocas los nodos uno a uno y controlas cada curva; con el **Lápiz** (N) dibujas a mano alzada y el programa lo convierte en curva. La pluma cuesta al principio, pero es la herramienta que te da los contornos más limpios.

## Seleccionar lo que quieres cambiar

Con la herramienta Mover (V) seleccionas objetos completos, y con Nodo (A), partes de su contorno. Cuando el documento crece, lo más fiable es seleccionar desde el panel de Capas, porque ahí aciertas con el objeto aunque haya varios superpuestos. Para cambios en bloque, el menú Seleccionar permite elegir todos los objetos con el mismo relleno, algo muy útil cuando decides cambiar un tono de la paleta en todo el personaje.

En el estudio Pixel las selecciones funcionan como en cualquier programa de pintura (rectangulares, a mano alzada o por color) y limitan la zona donde actúa el pincel.

## Exportar para cada destino

Lo que exportas depende de adónde va. El matiz importante es la resolución: para pantalla cuentan los píxeles de ancho y alto, y los ppp (dpi) solo tienen sentido si vas a imprimir. Una ilustración de 1920 × 1080 px se ve igual en el motor la guardes a 72 o a 300 ppp.

| Formato | Úsalo para |
|---|---|
| PNG | Personajes, props y elementos con transparencia que van al motor o a Figma |
| JPEG | Ilustraciones completas sin transparencia para presentar o compartir |
| SVG | Logotipos, iconos y piezas de interfaz que tienen que escalar |
| PSD | Pasar el archivo con capas a alguien que trabaja con Photoshop |
| PDF | Documentos para imprimir o entregas maquetadas |

Guarda siempre también el archivo `.af`: lo exportado es el resultado, y el `.af` es tu trabajo editable. Cuando necesites exportar muchas piezas por separado (las partes de un personaje, los iconos de una interfaz), usa las **porciones** (slices): marcas cada elemento una vez y los exportas todos de golpe con el mismo formato y tamaño.

## Texto y logotipos

Affinity distingue entre **texto artístico**, pensado para títulos y palabras sueltas que vas a transformar, y **texto de marco**, para párrafos dentro de una caja. Para el logotipo de un juego partes de una tipografía, ajustas el espaciado entre letras y, cuando la composición está decidida, la conviertes en curvas (Ctrl+Intro) para deformar cada letra como una forma más. A partir de ese momento deja de ser texto editable, así que guarda antes una copia. Y comprueba la licencia de la tipografía: para un juego que se publica necesitas una que permita uso comercial.

## Lo que te llevas de este apartado

Affinity une vectorial y píxel en un mismo documento: construyes con formas que puedes cambiar siempre y rematas con pincel al final. Las capas bien nombradas, los recortes y las máscaras te permiten cambiar de opinión sin rehacer nada, y al exportar lo que importa son los píxeles y el formato que pide el destino.
