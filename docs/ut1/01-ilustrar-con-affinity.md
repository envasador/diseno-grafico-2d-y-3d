# UT1.1 Ilustrar con Affinity

Piensa en todo lo que pasa por un programa de ilustración antes de que un juego salga a la venta: el primer concept del protagonista, la imagen que se enseña al equipo para convencerlo, el logotipo del título, los iconos del inventario. **Casi todo el arte de un juego vive ahí** en algún momento, así que merece la pena llevarse bien con la herramienta.

En este módulo usamos **Affinity**. Es un programa profesional, desde finales de 2025 **es gratuito** (solo te pide una cuenta de Canva) y junta en una misma aplicación el dibujo vectorial, la pintura en píxeles y la maquetación. Aquí vas a ver lo justo para moverte con soltura. El resto lo irás descubriendo cuando lo necesites, que es como mejor se aprende un programa.

## Un programa, varios estudios

Affinity reparte sus herramientas en **estudios**. En esta unidad vas a vivir en dos: el estudio **Vector**, donde dibujas con formas y curvas, y el estudio **Pixel**, donde pintas con pinceles como lo harías en papel. Cambias de uno a otro con los botones de arriba de la ventana.

Lo bueno es que los dos trabajan sobre el **mismo documento**. Puedes construir un personaje con formas vectoriales, saltar al estudio Pixel y pintarle las sombras con un pincel sin cambiar de archivo ni exportar nada.

Si prefieres verlo antes de tocarlo, en los [vídeos de apoyo de la unidad](index.md#videos-de-apoyo) tienes uno sobre la interfaz y otro sobre los estudios y las herramientas.

Si vienes de las versiones anteriores (Affinity Designer o Affinity Photo), los **estudios** son lo que allí se llamaban "personas". Los archivos nuevos se guardan como `.af`. El programa abre sin problema los antiguos `.afdesign`, pero al revés no funciona: si le pasas un `.af` a alguien con la versión vieja, **no podrá abrirlo**. Y suele descubrirse la noche antes de la entrega.

## Vectorial o píxel

Aquí está la decisión que vas a tomar cada vez que crees una capa, así que vale la pena entenderla bien.

Una forma vectorial es una **receta matemática**: "un círculo de este radio, con este relleno". Como el programa la vuelve a calcular cada vez, puedes hacerla gigante **sin que pierda nitidez** y cambiarle la curva o el color cuando quieras. Una capa de píxeles **guarda el color de cada puntito** de la imagen. Es perfecta para texturas, trazos de pincel y sombras suaves, pero si la agrandas, se nota.

¿Con cuál te quedas? **Con los dos.** Lo habitual en concept para juegos es **construir en vectorial todo lo que vas a cambiar muchas veces** (la silueta, las piezas del personaje, los elementos del escenario) y dejar para el final, en píxel, la textura y ese acabado pintado que le da vida.

| | Vectorial | Píxel |
|---|---|---|
| Se escala sin perder calidad | Sí | No |
| Se edita después (forma, color) | Siempre | Solo repintando |
| Mejor para | Siluetas, piezas, logotipos, UI | Texturas, pinceladas, sombras suaves |

## Capas: el botón de cambiar de opinión

Vas a cambiar de opinión. Muchas veces. Y cuando no seas tú, será quien revise tu trabajo. Y las capas son lo que hace que **cambiar de opinión cueste un clic** y no una tarde entera. Si el cuerpo, la cabeza y el arma de tu personaje están cada uno en su capa, puedes probar otra cabeza sin tocar lo demás.

Coge desde el primer día tres costumbres que te van a ahorrar muchos disgustos: **ponle nombre a cada capa**, agrupa las que van juntas (Ctrl+G, o Cmd+G en Mac) y **oculta en lugar de borrar**. "Capa 47" no te dice nada dentro de dos semanas.

Hay dos formas de meter una capa dentro de otra, y se parecen tanto que al principio se confunden:

- Si arrastras una capa sobre el **nombre** de otra, queda **recortada**: solo se ve dentro de la forma de la capa madre. Es la manera de pintar las sombras de una pieza sin salirte, aunque el pincel se pase del borde.
- Si la arrastras sobre la **miniatura**, funciona como **máscara**: sus zonas oscuras ocultan partes de la capa madre, pero sin borrarlas.

Y un último truco: las **capas de ajuste** (brillo y contraste, tono y saturación, curvas) cambian el color de todo lo que tienen debajo sin tocarlo de verdad. ¿Tu ilustración quedaría mejor más fría? ¿Más oscura? Pruébalo en diez segundos y, si no te convence, apagas la capa.

## Formas, pluma y nodos

Casi todo en vectorial empieza igual: **rectángulos, elipses y polígonos**. Desde ahí tienes tres caminos para llegar a la forma que tienes en la cabeza.

El primero es jugar con **operaciones booleanas** (sumar, restar, intersecar), que aparecen en la barra superior cuando seleccionas dos o más formas. Un círculo es una cabeza. Réstale otro círculo un poco desplazado y tienes una luna. Súmale dos triángulos y tienes un gato. Es lo más rápido que hay para poner en práctica el lenguaje de formas que viste en [Thumbnails y formas](../concept/thumbnails.md).

El segundo es tocar los **nodos**. Con la herramienta Nodo (A) seleccionas los puntos de una curva y sus manejadores y los mueves hasta que el contorno te convence. Si la forma todavía es una forma básica (un círculo recién dibujado), antes tendrás que **convertirla en curvas** (Ctrl+Intro, o Cmd+Return en Mac).

El tercero es dibujar el trazo tú mismo. Con la **Pluma** (P) colocas los nodos uno a uno y controlas cada curva; con el **Lápiz** (N) dibujas a mano alzada y el programa lo convierte en curva. Aviso: la pluma se hace cuesta arriba los primeros días. Aguanta, porque **es la que te da los contornos más limpios**.

Para ver todo esto aplicado a una ilustración de principio a fin, tienes el tutorial [Cómo ilustrar con vectores paso a paso](https://www.youtube.com/watch?v=oTfHSFRKjWw) en los vídeos de apoyo de la unidad.

## Seleccionar lo que quieres cambiar

Con la herramienta Mover (V) coges objetos completos, y con Nodo (A), trocitos de su contorno. Cuando el archivo empieza a llenarse de capas, lo más fiable es **seleccionar desde el panel de Capas**: ahí aciertas siempre, aunque haya tres objetos uno encima de otro.

¿Has decidido que el rojo de tu personaje era demasiado chillón? Desde el menú Seleccionar puedes elegir de golpe **todos los objetos que tienen el mismo relleno** y cambiarlos a la vez. En ese momento agradecerás haber trabajado en vectorial; en píxel te tocaría repintarlo todo a mano.

En el estudio Pixel las selecciones funcionan como en cualquier programa de pintura (rectangulares, a mano alzada o por color) y sirven para decirle al pincel dónde puede pintar y dónde no.

## Exportar para cada destino

**Lo que exportas depende de adónde va la imagen.** Y aquí hay un mito que conviene desmontar cuanto antes: los famosos ppp (dpi). Para pantalla **lo único que cuenta son los píxeles de ancho y de alto**; **los ppp solo importan si vas a imprimir**. Una ilustración de 1920 × 1080 px se ve exactamente igual en el motor tanto si la guardas a 72 como a 300 ppp. Así que si alguien te pide "la imagen a 300 ppp para el juego", lo que de verdad necesita saber es cuántos píxeles mide.

| Formato | Úsalo para |
|---|---|
| PNG | Personajes, props y elementos con transparencia que van al motor o a Figma |
| JPEG | Ilustraciones completas sin transparencia para presentar o compartir |
| SVG | Logotipos, iconos y piezas de interfaz que tienen que escalar |
| PSD | Pasar el archivo con capas a alguien que trabaja con Photoshop |
| PDF | Documentos para imprimir o entregas maquetadas |

Y **guarda siempre el `.af`**. Lo exportado es el resultado; el `.af` es tu trabajo, el que podrás volver a abrir y cambiar. Cuando tengas que exportar muchas piezas por separado (las partes de un personaje, todos los iconos de una interfaz), usa las **porciones** (slices): marcas cada elemento una vez y los sacas todos de golpe con el mismo formato y tamaño.

## Texto y logotipos

Affinity tiene dos tipos de texto. El **texto artístico** es para títulos y palabras sueltas que vas a retorcer; el **texto de marco** es para párrafos dentro de una caja.

El logotipo de un juego suele nacer así: eliges una tipografía, ajustas el espacio entre letras hasta que respira bien y, cuando la composición está decidida, lo conviertes en curvas (Ctrl+Intro). A partir de ahí cada letra es una forma más y puedes deformarla, cortarla o añadirle lo que quieras. Eso sí, deja de ser texto editable, así que **guarda antes una copia**. Y mira la licencia de la tipografía: si el juego se va a publicar, necesitas una que permita **uso comercial**. Descubrir que no la permite después de publicar el tráiler es una conversación que nadie quiere tener.
