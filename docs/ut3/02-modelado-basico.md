# UT3.2 Modelado básico

En esta sección, aprenderás los fundamentos del modelado 3D en Blender. Empezaremos con formas simples y progresaremos hacia técnicas más avanzadas.

## 2.1 Primitivas y cómo transformarlas

Las primitivas son las formas básicas que Blender proporciona de serie, como cubos, esferas, cilindros, planos, etc. Son el punto de partida para la mayoría de los modelos.

Para añadir una primitiva a tu escena:

1. En la vista 3D, haz clic derecho para abrir el menú Add.
2. Elige Mesh y luego selecciona la primitiva que quieras.

Una vez que tienes un objeto en tu escena, puedes transformarlo de varias maneras:

- Mover (Grab): Presiona G, luego mueve el mouse.
- Escalar: Presiona S, luego mueve el mouse.
- Rotar: Presiona R, luego mueve el mouse.

Consejo: Puedes restringir estas transformaciones a un eje específico presionando X, Y o Z después del atajo de teclado. Por ejemplo, G, then Z moverá el objeto solo a lo largo del eje Z.

## 2.2 Modos de edición (objeto, vértices, aristas, caras)

Blender tiene dos modos principales en los que trabajarás: Modo Objeto y Modo Edición.

- Modo Objeto: Aquí es donde transformas objetos enteros.
- Modo Edición: Aquí es donde modificas la geometría de un objeto a nivel de vértices, aristas y caras.

Puedes cambiar entre estos modos presionando la tecla Tab o utilizando el menú desplegable en la esquina superior izquierda de la vista 3D.

En el Modo Edición, puedes seleccionar entre tres modos de selección:

1. Modo Vértice: Selecciona vértices individuales.
2. Modo Arista: Selecciona aristas enteras.
3. Modo Cara: Selecciona caras enteras.

Puedes cambiar entre estos modos haciendo clic en los botones correspondientes en la barra de herramientas o utilizando los atajos de teclado Ctrl + Tab.

Práctica: Añade un cubo a tu escena, entra en el Modo Edición y practica cambiar entre los diferentes modos de selección y seleccionando diferentes partes de la geometría.

## 2.3 Herramientas de selección y transformación

En el Modo Edición, tienes acceso a varias herramientas de selección y transformación más allá de las básicas que ya hemos visto.

Algunas herramientas de selección útiles:

- Seleccionar anillo (Alt + clic izquierdo): Selecciona un bucle continuo de aristas alrededor del objeto.
- Seleccionar bucle (Alt + clic izquierdo): Selecciona un bucle continuo de caras o aristas a lo largo del objeto.
- Seleccionar más/menos (Ctrl + NumPad+/-): Expande o contrae tu selección a elementos adyacentes.

Y algunas herramientas de transformación útiles:

- Rotar alrededor del cursor 3D (R, R): Rota la selección alrededor de la ubicación del cursor 3D.
- Escalar a lo largo de la normal (Alt + S): Escala la selección a lo largo de sus normales locales.
- Doblar (Shift + W): Dobla la selección de varias maneras.

Consejo: Muchas de estas herramientas también están disponibles en el menú Mesh en la barra de menú en la parte superior de la ventana de Blender.

Práctica: Utiliza las herramientas de selección para seleccionar diferentes partes de un cubo y experimentar con las diferentes herramientas de transformación en ellas.

Esto concluye la segunda sección sobre modelado básico. En la siguiente, cubriremos técnicas más avanzadas como la extrusión y la subdivisión.

## 2.4 Extrusión, escalado, rotación

La extrusión es una técnica fundamental en el modelado 3D que te permite crear geometría nueva a partir de una selección existente. Funciona "extendiendo" la selección en una nueva dirección.

Para extruir:

1. En el Modo Edición, selecciona la cara, arista o vértice que quieres extruir.
2. Presiona E para extruir.
3. Mueve el mouse para colocar la nueva geometría.
4. Haz clic izquierdo para confirmar la posición.

Después de extruir, a menudo querrás escalar o rotar la nueva geometría:

- Para escalar, presiona S y mueve el mouse. Puedes restringir el escalado a un eje presionando X, Y o Z.
- Para rotar, presiona R y mueve el mouse. Puedes restringir la rotación a un eje presionando X, Y o Z.

Consejo: Si quieres extruir múltiples veces en una fila, puedes presionar E múltiples veces después de la extrusión inicial. Cada presión extruirá la geometría aún más.

Práctica: Toma el cubo del ejercicio anterior y utiliza la extrusión, el escalado y la rotación para modelar una forma más compleja, como una casa simple o una letra del alfabeto.

## 2.5 Suavizado y subdivisión de superficies

Por defecto, los objetos en Blender tienen superficies nítidas y facetadas. Para crear formas más suaves y orgánicas, puedes usar el suavizado y la subdivisión de superficies.

Suavizado:

1. En el Modo Objeto, selecciona el objeto que quieres suavizar.
2. En el panel Propiedades (normalmente a la derecha), ve a la pestaña Objeto Data (icono de triángulo).
3. Bajo Normals, haz clic en Auto Smooth.

Subdivisión de superficies:

1. Con el objeto aún seleccionado, ve al panel Modifier en el editor de Propiedades.
2. Haz clic en Add Modifier y selecciona Subdivision Surface.
3. Ajusta los valores de View y Render para controlar la cantidad de subdivisión.

Consejo: La subdivisión de superficies puede aumentar rápidamente la complejidad de tu malla y ralentizar el rendimiento. Utilízala con moderación y trata de mantener tu geometría lo más simple posible para tu uso previsto.

Práctica: Aplica el suavizado y la subdivisión de superficies a tu modelo de la casa o letra del ejercicio anterior. Experimenta con diferentes niveles de subdivisión para ver cómo afecta a la superficie de tu objeto.

## Práctica: Modelar un prop sencillo para el proyecto

Ahora que has aprendido los fundamentos del modelado en Blender, es hora de aplicar estos conocimientos a tu proyecto del curso.

Tarea: Modela un prop sencillo que podrías necesitar en tu proyecto, como una caja, una roca, un árbol, un arma, o una pieza de mobiliario.

Pasos:

1. Empieza con una primitiva que se acerque a la forma general que necesitas.
2. Utiliza las herramientas de selección y transformación para darle a tu objeto su forma básica.
3. Utiliza la extrusión para añadir detalles como protuberancias, hendiduras o adornos.
4. Aplica el suavizado y la subdivisión de superficies si es necesario para tu estilo deseado.
5. Itera y refina tu modelo hasta que estés satisfecho con la forma general.

Recuerda, el objetivo en esta etapa es capturar la forma general de tu prop, no preocuparse por los pequeños detalles. ¡Mantén las cosas simples y diviértete practicando estas nuevas habilidades!

En la siguiente sección, cubriremos cómo añadir materiales y texturas a tus modelos para darles color y detalle visual. ¡Sigue practicando tu modelado mientras tanto!
