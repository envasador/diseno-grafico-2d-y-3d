# UT3.2 Modelado básico

¿Recuerdas lo de construir con formas simples de la UT1? Pues en 3D se hace literalmente. Casi cualquier modelo de un juego empieza siendo un cubo, un cilindro o una esfera que vas estirando, cortando y empujando hasta que se parece a lo que tienes en el turnaround. Es más parecido a trabajar con plastilina que a dibujar.

## De qué está hecho un modelo 3D

Un modelo 3D es una **malla**: un montón de puntos en el espacio (**vértices**) unidos por líneas (**aristas**) que forman superficies (**caras**). Todo lo que hagas al modelar es mover, crear o borrar esas tres cosas.

En juegos hay una cuarta idea que no puedes olvidar: cada cara cuesta. El motor tiene que dibujar todas las caras de todos los objetos muchas veces por segundo, así que un modelo con más caras de las necesarias es un modelo que hace ir el juego más lento. Por eso en videojuegos se habla de **presupuesto de polígonos**, y por eso aquí la elegancia está en conseguir la forma con las caras justas.

## Primitivas y transformaciones básicas

Las primitivas son las formas de serie de Blender (cubo, esfera, cilindro, cono, plano...). Se añaden con Mayús + A, en el menú Mesh.

Una vez en la escena, las tres transformaciones básicas son de una letra:

| Tecla | Acción |
|---|---|
| G | Mover |
| R | Rotar |
| S | Escalar |

Pulsa la tecla, mueve el ratón y haz clic para confirmar (o clic derecho para cancelar). Si después de la letra pulsas X, Y o Z, la transformación queda limitada a ese eje. Y si además escribes un número, se aplica exacto: G, Z, 2 sube el objeto dos metros. Parece un lío, pero en cuanto lo pruebes verás que es rapidísimo.

## Modo Objeto y modo Edición

Blender tiene dos modos principales, y confundirlos es el error número uno de las primeras semanas:

- En **modo Objeto** trabajas con objetos completos: los colocas, los giras, los escalas.
- En **modo Edición** trabajas dentro del objeto, con sus vértices, aristas y caras.

Cambias de uno a otro con Tab. Dentro del modo Edición, las teclas 1, 2 y 3 (las de arriba del teclado) eligen si seleccionas vértices, aristas o caras.

¿Te ha pasado que escalas algo y "no se escala"? O que mueves una cara y se mueve todo el objeto? Mira en qué modo estás. Casi siempre es eso.

## Seleccionar con cabeza

En modo Edición, seleccionar bien es la mitad del trabajo. Además del clic normal (y Mayús + clic para añadir a la selección), estas tres te van a salvar la vida:

- **Alt + clic** sobre una arista selecciona el **bucle** completo que da la vuelta al objeto.
- **Ctrl + Alt + clic** selecciona el **anillo** de aristas paralelas.
- **Ctrl + teclado numérico +/−** amplía o reduce la selección a lo que está alrededor.

## Las herramientas que más vas a usar

Con cuatro herramientas se modela una cantidad sorprendente de cosas:

| Herramienta | Atajo | Qué hace |
|---|---|---|
| Extruir | E | Saca geometría nueva a partir de lo seleccionado, como estirar plastilina |
| Inset | I | Crea una cara más pequeña dentro de otra, perfecta antes de extruir |
| Corte en bucle | Ctrl + R | Añade un bucle de aristas alrededor del objeto para tener más detalle donde lo necesitas |
| Bisel | Ctrl + B | Redondea aristas vivas para que atrapen la luz |

Un ejemplo para que veas cómo se combinan: coge un cubo, selecciona la cara de arriba, haz un inset y extruye hacia abajo. Acabas de hacer una caja abierta. Unos cuantos cortes en bucle y un par de extrusiones más, y es un cofre.

## Modificadores: trabajar sin destruir

Los **modificadores** hacen algo sobre tu malla sin cambiarla de verdad, igual que las capas de ajuste en Affinity. Se añaden en la pestaña de la llave inglesa del panel Propiedades, y puedes apagarlos, reordenarlos o quitarlos cuando quieras. Tres que vas a usar mucho:

- **Mirror**: modelas media cara del personaje y el modificador genera la otra mitad reflejada. La mitad de trabajo, simetría perfecta.
- **Subdivision Surface**: subdivide y suaviza la malla para que parezca orgánica. Muy útil, pero multiplica las caras, así que en juegos se usa con mucha cabeza.
- **Bevel**: bisela las aristas sin tener que hacerlo a mano.

## Suavizado

Por defecto, Blender enseña los objetos facetados, con cada cara plana bien visible. Con clic derecho en modo Objeto tienes **Shade Smooth**, que suaviza el sombreado de toda la superficie, y **Shade Auto Smooth**, que suaviza solo donde el ángulo entre caras es pequeño y deja vivas las aristas marcadas. Para la mayoría de props de juego, la segunda es la buena: un barril queda redondo por el costado y con el borde de la tapa nítido.

Ojo, que esto es solo sombreado: el objeto sigue teniendo las mismas caras. Es un truco visual, y de los baratos, que es lo que nos gusta en juegos.

## Antes de dar un modelo por terminado

Hay tres comprobaciones que evitan muchísimos problemas cuando el modelo llega al motor:

- **Aplica la escala** (Ctrl + A > Scale) si has escalado el objeto en modo Objeto. Si no, las texturas, la física y la exportación pueden comportarse de forma rara.
- **Revisa las normales**, que indican hacia dónde "mira" cada cara. Si alguna está al revés, en el motor esa cara se verá transparente.
- **Borra lo que no se ve**. Una cara que siempre queda pegada al suelo o dentro de otro objeto es presupuesto de polígonos tirado a la basura.

## Para practicar

- Modela una taza partiendo de un cilindro, usando solo inset, extrusión y cortes en bucle. El asa, con una extrusión que vas girando.
- Modela una espada con el modificador Mirror activado, de forma que solo construyas la mitad.
- Coge cualquiera de los dos modelos e intenta dejarlo con la mitad de caras sin que cambie su silueta. Es el mejor ejercicio que existe para entender el presupuesto de polígonos.
