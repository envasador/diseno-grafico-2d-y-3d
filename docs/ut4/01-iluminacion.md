# UT4.1 Iluminación

La iluminación es un elemento crucial en cualquier escena 3D. Puede crear atmósfera, resaltar áreas importantes, y añadir profundidad y realismo a tus modelos. En esta sección, aprenderás cómo trabajar con luces en Blender.

## 4.1 Tipos de luces en Blender

Blender tiene varios tipos de luces, cada una con sus propias características y usos:

1. Point (Punto): Emite luz uniformemente en todas las direcciones desde un solo punto. Útil para simular bombillas o velas.
2. Spot (Foco): Emite luz en forma de cono desde un punto. Útil para simular linternas, focos de escenario, o luz solar a través de una ventana.
3. Area (Área): Emite luz desde un rectángulo o un cuadrado. Útil para simular luz suave de ventanas o tiras de luz.
4. Sun (Sol): Emite luz direccional constante desde infinitamente lejos. Útil para simular luz solar.

Para añadir una luz a tu escena:

1. En la vista 3D, haz clic derecho para abrir el menú Add.
2. Elige Light y luego selecciona el tipo de luz que quieras.

![Menú Add de Blender con opciones de luz](https://i.imgur.com/nDm0DjB.png)

Práctica: Añade diferentes tipos de luces a tu escena. Observa cómo cada una afecta a la apariencia de tus objetos.

## 4.2 Propiedades y ajustes de luces

Cada luz en Blender tiene varias propiedades que puedes ajustar para personalizar su apariencia y comportamiento. Algunas de las más comunes incluyen:

- Power (Potencia): La intensidad de la luz.
- Color: El color de la luz.
- Specular: Si la luz causa reflejos especulares brillantes.
- Radius (Radio): El tamaño de la luz (para luces Point y Spot).
- Angle (Ángulo): El ángulo del cono de luz (para luces Spot).
- Shape (Forma): La forma de la luz (para luces Area).

Puedes acceder a estas propiedades en el panel Light en el editor Properties cuando tienes una luz seleccionada.

![Panel de propiedades de luz en Blender](https://i.imgur.com/1cKBgIi.png)

Práctica: Juega con las propiedades de las luces que añadiste en el ejercicio anterior. Observa cómo cada propiedad afecta a la apariencia de la luz y cómo interactúa con tus objetos.

## 4.3 Iluminación básica de una escena

Una configuración de iluminación básica pero efectiva que puedes usar en muchas situaciones es la iluminación de tres puntos. Consiste en tres luces:

1. Key Light (Luz clave): La fuente de luz principal, generalmente colocada a un lado de la cámara y un poco elevada.
2. Fill Light (Luz de relleno): Una luz más suave y menos intensa colocada al lado opuesto de la luz clave para rellenar las sombras.
3. Back Light (Luz de fondo): Una luz colocada detrás del sujeto para separarlo del fondo.

Aquí hay un ejemplo de cómo configurar una iluminación de tres puntos en Blender:

1. Añade una luz Sun a tu escena. Esta será tu luz clave. Colócala a un lado de tu objeto y un poco elevada.
2. Añade una luz Area al lado opuesto de tu luz clave. Haz esta luz más grande y menos intensa que la luz clave. Esta será tu luz de relleno.
3. Añade otra luz Area detrás de tu objeto, apuntando hacia él. Esta será tu luz de fondo.

![Iluminación de tres puntos en Blender](https://i.imgur.com/dOcZHAP.png)

Consejo: No te sientas limitado a usar solo tres luces. Puedes añadir más luces para resaltar características específicas o crear efectos especiales. La iluminación de tres puntos es solo un punto de partida.

Práctica: Configura una iluminación de tres puntos en tu escena. Experimenta con las posiciones e intensidades de las luces hasta que estés satisfecho con la apariencia.

## 4.4 Sombras y oclusión ambiental

Las sombras y la oclusión ambiental son dos efectos que pueden añadir mucho realismo a tu escena.

Para habilitar las sombras para una luz:

1. Selecciona la luz en la vista 3D.
2. En el panel Light en el editor Properties, ve a la sección Shadow.
3. Haz clic en el botón junto a la opción Shadow para habilitarla.

![Configuración de sombras en Blender](https://i.imgur.com/lP8RURC.png)

La oclusión ambiental (AO) es un efecto que simula cómo las áreas cercanas de un objeto bloquean la luz ambiental, creando sombras suaves en grietas y esquinas. Para añadir AO:

1. En el panel World en el editor Properties, ve a la sección Ambient Occlusion.
2. Haz clic en el botón junto a la opción Ambient Occlusion para habilitarla.
3. Ajusta los controles Factor y Distance para controlar la fuerza y el alcance del efecto.

![Configuración de oclusión ambiental en Blender](https://i.imgur.com/QMhwl6O.png)

Consejo: Tanto las sombras como la oclusión ambiental pueden aumentar significativamente los tiempos de renderizado. Utilízalas con moderación y considera desactivarlas para borradores o renders de previsualización.

Práctica: Habilita las sombras para tus luces y añade oclusión ambiental a tu escena. Observa cómo estos efectos mejoran el realismo y la percepción de profundidad.

## Práctica: Iluminar una escena del proyecto

Ahora que has aprendido los fundamentos de la iluminación en Blender, es hora de aplicar estos conocimientos a tu proyecto del curso.

Tarea: Crea una configuración de iluminación básica para una escena que incluya uno o más de los props que has creado.

Pasos:

1. Coloca tus props en una nueva escena de Blender.
2. Configura una iluminación de tres puntos usando una combinación de luces Sun y Area.
3. Ajusta las propiedades de las luces (intensidad, tamaño, ángulo, etc.) hasta que estés satisfecho con la apariencia.
4. Habilita las sombras para tus luces y añade oclusión ambiental a la escena.
5. Haz algunos renders de prueba y ajusta la iluminación según sea necesario.

Recuerda, el objetivo en esta etapa es lograr una iluminación básica que resalte tus modelos de manera efectiva. La iluminación avanzada es todo un arte en sí mismo, así que no te preocupes por lograr perfección. ¡Lo importante es experimentar y observar cómo la iluminación afecta a la apariencia de tus modelos!

En la siguiente sección, cubriremos cómo configurar cámaras y hacer renders finales de tus escenas. ¡Sigue practicando con la iluminación mientras tanto!
