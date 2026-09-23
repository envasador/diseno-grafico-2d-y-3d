# 3. Materiales y texturas

Mientras que el modelado define la forma de un objeto, los materiales y las texturas definen su apariencia. Pueden hacer que un objeto parezca de madera, metal, plástico, tela, y más. En esta sección, aprenderás cómo crear y aplicar materiales en Blender.

## 3.1 Qué son los materiales y cómo funcionan en Blender

En Blender, un material es un conjunto de propiedades que determinan cómo aparece la superficie de un objeto. Estas propiedades incluyen color, brillantez, rugosidad, transparencia, y más.

Puedes pensar en un material como una "receta" para la apariencia de una superficie. Y como una receta, un material está hecho de ingredientes - en este caso, nodos.

## 3.2 Editor de nodos y tipos de nodos básicos

Blender utiliza un sistema basado en nodos para crear materiales. Cada nodo representa una operación o propiedad, y los nodos están conectados entre sí en una red para crear el material final.

Para acceder al editor de nodos:

1. Cambia al modo de diseño "Shading" en la esquina superior izquierda de la vista 3D.
2. En el editor que aparece (probablemente en el centro de tu pantalla), cambia al modo "Nodos" en el menú desplegable en la esquina superior izquierda.

![Editor de nodos en Blender](https://i.imgur.com/lIi9wRD.png)

Algunos de los tipos de nodos más comunes que utilizarás:

- Nodo de salida del material (Material Output): Cada material necesita uno de estos. Es donde todas las otras propiedades del material se unen.
- Nodo BSDF (shader): Define cómo reacciona la superficie a la luz. Hay varios tipos, como Diffuse, Principled, Glossy, etc.
- Nodo de textura: Añade una imagen o patrón a la superficie. El tipo Image Texture es el más común.
- Nodos de color: Te permiten ajustar el color de otras propiedades. Incluyen RGB, MixRGB, y más.
- Nodos de vector: Utilizados para manipular datos de dirección como normales y coordenadas de texturas.

Práctica: Crea un nuevo material y añade algunos nodos. Intenta conectar un nodo de color a un nodo Diffuse BSDF, y luego conecta ese BSDF a la entrada Surface del nodo de salida del material. ¿Qué pasa cuando cambias el color?

## 3.3 Propiedades de materiales (color, especular, rugosidad)

Algunas de las propiedades más comunes de los materiales que ajustarás incluyen:

- Color base (Base Color): El color general de la superficie.
- Especular (Specular): ¿Cuánto "brillo" tiene el material?
- Rugosidad (Roughness): ¿Cómo de áspera o lisa es la superficie? Esto afecta tanto al brillo como a cómo se difumina la reflexión.
- Metalicidad (Metallic): ¿Es el material metálico o no metálico? Esto afecta cómo reacciona a la luz.

Muchas de estas propiedades están disponibles en el nodo Principled BSDF, que es un gran punto de partida para muchos materiales.

![Nodo Principled BSDF en Blender](https://i.imgur.com/zzDxz81.png)

Práctica: Añade un nodo Principled BSDF a tu material anterior. Juega con las propiedades para ver cómo afectan a la apariencia de tu objeto. ¿Puedes hacer que se parezca a plástico? ¿A metal?

## 3.4 UV mapping y aplicación de texturas

Las texturas son imágenes 2D que se envuelven alrededor de un modelo 3D para darle detalle visual, como patrones, logotipos, suciedad, arañazos, etc. El proceso de definir cómo se envuelve una imagen 2D alrededor de un modelo 3D se llama UV mapping.

Aquí está el flujo de trabajo básico para aplicar una textura en Blender:

1. En el Modo Edición, selecciona todo (A) y presiona U para desplegar el menú UV Mapping. Elige "Smart UV Project" para una proyección automática.
2. Cambia al modo de diseño "UV Editing" para ver tu mapeado UV.
3. En el editor de nodos de tu material, añade un nodo Image Texture. Carga tu imagen de textura en este nodo.
4. Conecta el nodo Image Texture a la entrada Base Color del nodo Principled BSDF.

![Texturizado en Blender](https://i.imgur.com/8XIYso8.png)

Consejo: Si tu textura aparece distorsionada o estirada en tu modelo, es posible que necesites ajustar tu mapeado UV. Puedes hacerlo seleccionando partes de tu malla en el editor UV y moviéndolas, escalándolas o rotándolas como lo harías en la vista 3D.

Práctica: Encuentra o crea una simple imagen de textura (un patrón de madera o ladrillo es un buen punto de partida) y aplícala a tu modelo del ejercicio anterior siguiendo los pasos descritos arriba. Si tienes problemas, intenta ajustar tu mapeado UV.

## Práctica: Texturizar un modelo del proyecto

Ahora que has aprendido los fundamentos de los materiales y las texturas en Blender, es hora de aplicar estos conocimientos a tu proyecto del curso.

Tarea: Añade materiales y texturas a uno o más de los props que modelaste para tu proyecto en la sección anterior.

Pasos:

1. Crea un nuevo material para tu prop.
2. Utiliza nodos de color y un nodo Principled BSDF para definir las propiedades básicas del material, como el color y la brillantez.
3. Si es aplicable, crea un mapeado UV para tu objeto y aplica una textura usando un nodo Image Texture.
4. Ajusta las propiedades del material y el posicionamiento de la textura hasta que estés satisfecho con la apariencia.
5. Repite para cualquier prop adicional, si lo deseas.

Recuerda, el objetivo en esta etapa es lograr una apariencia general adecuada para tu prop. No te preocupes por lograr una apariencia perfectamente realista - eso viene con mucha más práctica. Por ahora, ¡diviértete experimentando con diferentes configuraciones de materiales y texturas!

En la siguiente sección, cubriremos cómo añadir y configurar luces en tus escenas para realzar realmente la apariencia de tus modelos. ¡Sigue practicando con materiales y texturas mientras tanto!
