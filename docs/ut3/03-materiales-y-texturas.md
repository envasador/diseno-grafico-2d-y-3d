# UT3.3 Materiales y texturas

Modela una esfera perfecta y enséñasela a alguien. ¿Es una pelota de goma, una canica o una bola de billar? Imposible saberlo. La forma es la misma; lo que cambia es cómo refleja la luz. Eso es exactamente lo que hacen los materiales y las texturas: el modelado dice qué forma tiene un objeto, y el material dice de qué está hecho.

## Qué es un material

Un material es la receta que le dice al motor cómo se comporta la luz al llegar a una superficie: de qué color es, cuánto brilla, si refleja como un espejo o se come la luz como la tela.

Hoy casi todos los juegos usan el mismo sistema de receta, llamado **PBR** (Physically Based Rendering, renderizado basado en física). Su gracia es que describe los materiales con propiedades físicas reales en lugar de con trucos, así que un material bien hecho se ve bien con cualquier luz: al sol, en una cueva o bajo una farola.

## El nodo que lo hace casi todo

En Blender los materiales se construyen con **nodos**, cajitas conectadas con cables en las que cada una aporta algo. Suena complicado, pero cuando creas un material nuevo ya vienen dos nodos puestos, y con ellos puedes hacer la mayoría de materiales de un juego:

- **Principled BSDF**: el nodo PBR. Tiene todas las propiedades del material.
- **Material Output**: la salida. Lo que le llega aquí es lo que ves.

Para trabajar cómodo, ve a la pestaña **Shading** de arriba: te pone el editor de nodos debajo de la vista 3D y la escena ya iluminada.

## Las cuatro propiedades que importan

El Principled BSDF tiene un montón de parámetros, pero con cuatro describes casi cualquier cosa:

| Propiedad | Qué controla | Un truco para entenderla |
|---|---|---|
| Base Color | El color propio del material | El color que tendría con una luz blanca y neutra |
| Metallic | Si es metal (1) o no (0) | Casi nunca va a medias: o es metal o no lo es |
| Roughness | Lo rugosa que es la superficie | 0 es un espejo; 1, una pared de yeso |
| Normal | Relieve falso de la superficie | Arañazos, poros o ladrillos sin añadir ni una cara |

Juega con Metallic y Roughness sobre una esfera y en cinco minutos habrás hecho plástico, oro, goma y cromo. De verdad, pruébalo: es la mejor forma de entenderlo.

## Texturas: detalle sin polígonos

Un material con un solo color queda muy limpio, y a veces eso es justo lo que buscas (en un estilo low poly, por ejemplo). Pero si quieres madera con vetas, piedra con grietas o una armadura con arañazos, necesitas **texturas**: imágenes que se "pegan" sobre el modelo.

En el editor de nodos añades un nodo **Image Texture**, cargas la imagen y conectas su salida a Base Color. Y lo mismo con el resto de propiedades: en PBR es habitual tener una imagen para el color, otra para la rugosidad, otra para el relieve (normal map), etc. Es como si cada propiedad tuviera su propio mapa pintado.

La gran ventaja de las texturas en juegos es que el detalle sale casi gratis. Pintar cien ladrillos en una textura cuesta muchísimo menos que modelarlos.

## UV mapping: desplegar el modelo

Aquí viene la pregunta clave: ¿cómo sabe el programa qué trozo de la imagen va en cada cara del modelo? Con el **mapa UV**.

Imagina que coges una caja de cartón, la cortas por algunas aristas y la despliegas plana sobre la mesa. Eso es un mapa UV: tu modelo 3D desplegado en 2D, para que puedas colocar encima la imagen. Las letras U y V son simplemente los nombres de los dos ejes de esa imagen plana (X, Y y Z ya estaban cogidas).

Para desplegar un modelo:

1. En modo Edición, marca por dónde quieres "cortar": selecciona aristas y usa Ctrl + E > Mark Seam. Igual que con la caja, conviene cortar por sitios poco visibles.
2. Selecciónalo todo (A), pulsa U y elige **Unwrap**.
3. Mira el resultado en la pestaña **UV Editing**: a la izquierda tienes el despliegue, a la derecha el modelo.

Si tienes prisa o el objeto es sencillo, en el menú U también tienes **Smart UV Project**, que corta y despliega él solo. Funciona sorprendentemente bien para props simples, aunque los cortes quedan donde a él le parece.

¿Cómo sabes si tu mapa UV está bien? Aplica una textura de cuadros (el nodo Image Texture te deja generar una de prueba). Si los cuadros se ven del mismo tamaño en todo el modelo y sin estirarse, vas bien. Si ves rombos o cuadros gigantes en una zona y diminutos en otra, toca revisar.

## Pensando en el motor

Unas pocas costumbres hacen que tus materiales lleguen al motor tal y como los ves en Blender:

- **Usa el Principled BSDF** y texturas de imagen. Los formatos de exportación (glTF, FBX) entienden bien ese nodo; las combinaciones raras de nodos se pierden por el camino.
- **Tamaños en potencias de dos** para las texturas (512, 1024, 2048), por el mismo motivo que viste con los sprites en la UT2.
- **Pocos materiales por objeto.** Cada material distinto es trabajo extra para el motor. Un prop sencillo debería apañarse con uno o dos.

## Para practicar

- Crea cuatro esferas y conviértelas en plástico rojo, oro, goma negra y cristal esmerilado usando solo Base Color, Metallic y Roughness.
- Despliega un cubo marcando tú las costuras, de forma que quede con forma de cruz (como una caja de cartón abierta), y compruébalo con la textura de cuadros.
- Busca una textura libre de madera o piedra (en sitios como ambientCG o Poly Haven las tienes gratis) y aplícala a un modelo sencillo hasta que no se vean estiramientos.
