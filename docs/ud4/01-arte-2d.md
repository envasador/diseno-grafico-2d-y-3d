# 1. Introducción al Arte 2D en Videojuegos
El arte 2D en videojuegos es una disciplina que se centra en la creación de gráficos en dos dimensiones. Incluye todo lo visual, desde personajes y escenarios hasta objetos y efectos especiales, y tiene un papel fundamental en la ambientación y la experiencia del jugador. A diferencia del arte 3D, los elementos están diseñados en un plano bidimensional, lo que permite estilos visuales únicos y característicos.

## 2. Tipos de Arte 2D

### 2.1. Pixel Art
El **Pixel Art** es uno de los estilos más clásicos en los videojuegos 2D. Se caracteriza por gráficos compuestos de píxeles visibles, evocando un estilo retro o nostálgico. Cada píxel se coloca manualmente, lo que requiere un control cuidadoso de la paleta de colores.

- **Animación en Pixel Art**:
    - **Personajes**: Animaciones de caminar, correr, saltar, atacar o interactuar. Cada movimiento se divide en "frames" o fotogramas dibujados a mano.
    - **Objetos**: Animaciones simples, como parpadeo, rotación o movimientos básicos.
    - **Escenarios**: Animaciones de fondo, como luces parpadeantes o efectos climáticos pixelados (lluvia, nieve).

- **Ejemplos**:
    - *Shovel Knight* - Un clásico juego de plataformas que utiliza un estilo de Pixel Art moderno, con animaciones cuidadosas y un diseño nostálgico. [Shovel Knight Gameplay](https://hipertextual.com/2014/07/shovel-knight)
    - *Celeste* - Utiliza Pixel Art detallado para crear escenarios complejos y animaciones fluidas. [Celeste Gameplay](https://www.celestegame.com/)


### 2.2. Arte Vectorial
El **Arte Vectorial** se basa en gráficos escalables, definidos mediante ecuaciones matemáticas. Este estilo es limpio y fácilmente adaptable a diferentes resoluciones sin pérdida de calidad, lo que lo hace ideal para dispositivos móviles.

- **Animación en Arte Vectorial**:
    - **Personajes**: Se utilizan esqueletos digitales para animaciones complejas (andar, atacar, saltar), que permiten un movimiento fluido.
    - **Objetos**: Transformaciones sencillas, rotación o escala.
    - **Escenarios**: Creación de fondos animados con transiciones suaves, como árboles oscilantes o luces móviles.

- **Ejemplos**: 
    - *Vector Park* - Conocido por sus juegos minimalistas, muestra ejemplos de arte vectorial limpio y animación fluida. [Vector Park Gameplay](https://www.youtube.com/watch?v=8q-lM3tR6lM)
    - *Badland* - Utiliza gráficos vectoriales y siluetas para un estilo visual único. [Badland Gameplay](https://www.youtube.com/watch?v=wUSo2A9lYdE)



### 2.3. Arte Digital o Dibujo Manual (Hand-drawn)
El **Arte Digital** dibujado a mano simula un estilo tradicional, con ilustraciones hechas digitalmente utilizando herramientas de dibujo. Permite un mayor detalle y un estilo más artístico.

- **Animación en Arte Digital**:
    - **Personajes**: Animaciones detalladas cuadro a cuadro, estilo tradicional, donde cada movimiento se dibuja manualmente.
    - **Objetos**: Animaciones detalladas con efectos de iluminación y sombras.
    - **Escenarios**: Paisajes con efectos de parallax scrolling, donde diferentes capas se mueven a diferentes velocidades para simular profundidad.

- **Ejemplos**: 
    - *Hollow Knight* - Un juego con un estilo artístico dibujado a mano, con animaciones cuadro a cuadro muy detalladas. [Hollow Knight Gameplay](https://www.youtube.com/watch?v=UAO2urG23S4)
    - *Cuphead* - Famoso por sus gráficos dibujados a mano que emulan la animación clásica de los años 30. [Cuphead Gameplay](https://www.youtube.com/watch?v=2ht-7ACKfYQ)

## 3. Tipos de Animación en Arte 2D

### 3.1. Animación Frame-by-Frame (Cuadro a Cuadro)
Cada fotograma se dibuja individualmente, creando una animación fluida pero laboriosa. Es común en Pixel Art y arte dibujado a mano.

### 3.2. Animación Cut-out
Utiliza partes recortadas del personaje u objeto, que se animan mediante rotación y traslación, como si fueran marionetas digitales. Es frecuente en el arte vectorial.

### 3.3. Skeletal Animation (Animación Esquelética)
Consiste en construir un "esqueleto" digital que controla el movimiento de los gráficos. Ideal para animaciones más complejas en arte vectorial o digital, ya que permite reutilizar partes del cuerpo.

## 4. Creación de Personajes, Objetos y Escenarios en Arte 2D

### 4.1. Personajes
La creación de personajes en 2D requiere considerar la silueta, la paleta de colores y la animación, adaptándolos al estilo visual del juego:
- **Pixel Art**: Enfoque minimalista, usando píxeles grandes para enfatizar características.
- **Arte Vectorial**: Detalles limpios y movimientos precisos.
- **Arte Digital**: Uso intensivo de sombras y detalles para profundidad.

### 4.2. Objetos
Los objetos deben ser coherentes con el estilo visual del juego:
- **Pixel Art**: Objetos simples pero reconocibles, con colores limitados.
- **Arte Vectorial**: Objetos escalables con colores planos.
- **Arte Digital**: Elementos detallados que pueden tener efectos de iluminación.

### 4.3. Escenarios
El diseño de escenarios en 2D implica la creación de fondos y elementos interactivos:
- **Pixel Art**: Tiled maps y fondos que utilizan repeticiones de patrones.
- **Arte Vectorial**: Fondos escalables y elementos interactivos.
- **Arte Digital**: Escenarios pintados a mano con múltiples capas para parallax.


## 5. Tiled y Tiled Maps

### 5.1. ¿Qué es Tiling?
El **Tiling** es una técnica para crear escenarios grandes reutilizando pequeños bloques o "tiles" (módulos gráficos). Permite ahorrar recursos y facilita la edición.

- **Tiled Maps**: Son mapas compuestos por múltiples "tiles", lo que permite crear escenarios amplios sin necesidad de dibujar cada detalle individualmente.

### 5.2. Ventajas del Tiling
- **Optimización**: Reduce la carga gráfica y de memoria.
- **Reutilización**: Permite utilizar los mismos tiles en diferentes contextos.
- **Edición Sencilla**: Modificar el diseño del nivel es más fácil al cambiar solo los tiles necesarios.

#### 5.3 Ejemplos de Tiled Maps
- *Stardew Valley* - Usa tiled maps para construir un mundo agrícola con tiles detallados y variados. [Stardew Valley Gameplay](https://www.youtube.com/watch?v=ot7uXNQskhs)
- *Super Mario Maker* - Aunque es en 2D, utiliza una mecánica similar a los tiled maps para que los jugadores creen sus propios niveles. [Super Mario Maker Gameplay](https://www.youtube.com/watch?v=INh7hD_52_A)


## 6. Otras Técnicas y Términos Relevantes

### 6.1. Parallax Scrolling
Una técnica donde varias capas del fondo se mueven a diferentes velocidades para simular profundidad. Es común en plataformas y juegos con desplazamiento lateral.

### 6.2. Sprite Sheets
Un **Sprite Sheet** es un archivo de imagen que contiene todas las poses de un personaje o animación, lo que permite cambiar rápidamente de un fotograma a otro sin cargar múltiples imágenes.

### 6.3. Shaders 2D
Los **Shaders 2D** son pequeños scripts que permiten modificar la apariencia de los gráficos en tiempo real. Pueden añadir efectos visuales como sombras dinámicas, luces, o distorsiones.

---

## 7. Ejemplos de Flujo de Trabajo en Arte 2D

### 7.1. Flujo de Trabajo para Pixel Art
1. **Boceto Inicial**:
    - Crear un boceto simple utilizando una cuadrícula para establecer proporciones básicas.
2. **Definición del Sprite**:
    - Dibujar los contornos del personaje, objeto o tile utilizando una paleta de colores limitada.
3. **Coloreado y Sombras**:
    - Rellenar las áreas principales y añadir sombras o brillos para dar profundidad.
4. **Animación**:
    - Crear un sprite sheet, diseñando cada frame de la animación (por ejemplo, un ciclo de caminar).
5. **Exportación y Testeo**:
    - Exportar los sprites en formato PNG o similar y probarlos en el motor del juego.

**Herramientas sugeridas**: Pixelorama, Pixel Edit, Aseprite, Piskel, Photoshop, Affinity Photo.

---

### 7.2. Flujo de Trabajo para Arte Vectorial
1. **Diseño Base**:
    - Crear el diseño inicial del personaje u objeto utilizando formas geométricas básicas.
2. **Detalles y Colores**:
    - Refinar el diseño añadiendo detalles y definir colores planos (flat).
3. **Creación del Esqueleto**:
    - Establecer un rigging básico con huesos digitales para animaciones.
4. **Animación**:
    - Realizar movimientos como caminar, saltar o interactuar utilizando el esqueleto.
5. **Escenarios**:
    - Diseñar elementos del fondo y objetos interactivos escalables.
6. **Exportación**:
    - Exportar como SVG o PNG según las necesidades del proyecto.

**Herramientas sugeridas**: Adobe Illustrator, Affinity Designer, Inkscape, Spine.

---

##### 7.3. Flujo de Trabajo para Arte Digital Dibujado a Mano
1. **Boceto Digital**:
    - Realizar un boceto detallado a mano alzada en una tablet gráfica.
2. **Línea Limpia y Coloreado**:
    - Trazar líneas definitivas y colorear utilizando técnicas de pintura digital.
3. **Sombras y Texturas**:
    - Añadir detalles como sombras, luces y texturas para dar un aspecto artístico único.
4. **Animación Cuadro a Cuadro**:
    - Dibujar cada frame manualmente para movimientos fluidos.
5. **Fondos con Parallax**:
    - Crear capas separadas para los fondos y configurarlas para movimientos de parallax.
6. **Integración**:
    - Exportar las animaciones y gráficos en formato compatible con el motor.

**Herramientas sugeridas**: Photoshop, Affinity Photo, Procreate, Clip Studio Paint.

---

##### 7.4. Flujo de Trabajo para Arte Flat
1. **Boceto y Formas Básicas**:
    - Diseñar con formas geométricas simples y líneas limpias.
2. **Paleta de Colores Minimalista**:
    - Seleccionar una paleta de colores reducida para mantener el estilo sencillo.
3. **Animación Sencilla**:
    - Aplicar movimientos básicos como deslizamientos, rotaciones y cambios de opacidad.
4. **Diseño de Escenarios**:
    - Crear fondos simples con elementos móviles (como nubes o árboles).
5. **Optimización**:
    - Comprimir gráficos para mejorar el rendimiento en dispositivos móviles.

**Herramientas sugeridas**: Figma, Adobe XD, 

---

##### 7.5. Flujo de Trabajo para Tiled Maps
1. **Diseño de Tiles**:
    - Crear pequeños gráficos reutilizables (16x16 o 32x32 píxeles, por ejemplo) que representen partes del escenario (suelo, paredes, objetos).
2. **Montaje del Mapa**:
    - Utilizar una herramienta como Tiled para organizar los tiles en un mapa grande.
3. **Añadir Elementos Interactivos**:
    - Marcar tiles específicos como interactivos o utilizarlos para eventos (trampas, puertas, enemigos).
4. **Pruebas de Jugabilidad**:
    - Probar el mapa dentro del motor del juego para verificar colisiones, fluidez y diseño visual.
5. **Ajustes Finales**:
    - Editar tiles según sea necesario para mejorar la coherencia visual.

**Herramientas sugeridas**: Tiled, Pyxel Edit, Pixelorama.

---
