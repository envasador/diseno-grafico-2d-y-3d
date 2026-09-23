# Anexo A.1 Introducción al diseño UI/UX para videojuegos

## 1.1 Conceptos iniciales

Cuando diseñas una interfaz para videojuegos, necesitas trabajar con varios elementos que van más allá de simplemente hacer que las cosas se vean bonitas. Cada elemento tiene su función específica y todos trabajan juntos para crear algo que el jugador pueda usar sin pensar demasiado en ello.

**Los componentes visuales** son básicamente todas las piezas gráficas que ves en pantalla: botones, barras de vida, menús, el HUD completo. Lo importante aquí es que cada elemento comunique claramente qué hace. No queremos que el jugador esté adivinando para qué sirve cada cosa mientras está en medio de una batalla.

**El color** hace mucho trabajo pesado en las interfaces. No solo guía tu mirada hacia donde necesitas mirar, sino que también comunica estados del juego de forma instantánea. Piensa en cómo el rojo universalmente significa peligro o daño, mientras que el verde suele indicar salud o cosas positivas. Una paleta de colores bien pensada también tiene que funcionar para jugadores con daltonismo o problemas visuales.

**La tipografía** puede parecer un detalle menor, pero prueba a leer texto pequeño mientras estás esquivando enemigos. Las fuentes tienen que ser legibles en cualquier situación, y además deben encajar con el mundo del juego. No vas a poner Comic Sans en un juego de terror, ¿verdad?

**La consistencia** significa que si un botón azul hace algo en una pantalla, debería hacer algo similar en todas las demás. Los jugadores no deberían tener que reaprender cómo funciona tu interfaz cada vez que cambian de menú.

**La coherencia** es cuando toda la interfaz parece que pertenece al mismo juego. Si estás haciendo un juego cyberpunk, todos los elementos deberían sentirse futuristas y tecnológicos. Es como cuando ves una película y todo el diseño de producción trabaja junto para crear un mundo creíble.

**La usabilidad** es simple: ¿puede el jugador hacer lo que necesita hacer sin frustrarse? Si tienen que buscar en tres menús diferentes para cambiar su arma, algo está mal.

**La experiencia de usuario (UX)** es el panorama completo. No es solo que funcione, sino cómo se siente usarlo. Una buena UX hace que interactuar con el juego sea placentero, no una tarea.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sc3h5JXtIzw?si=8ThGMJLgiGZIsYqE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## 1.2 Características principales del diseño de interfaz

Las interfaces de videojuegos tienen necesidades bastante específicas comparadas con, digamos, una app de banco. Veamos qué las hace especiales:

### Diseño centrado en el usuario

La accesibilidad no es opcional. Necesitas pensar en jugadores con diferentes capacidades desde el principio. Esto significa opciones para ajustar colores, tamaños de texto, subtítulos, y configuraciones de audio.

La consistencia visual es clave. Tu interfaz debería sentirse como parte del juego, no como algo pegado encima. Y sobre la curva de aprendizaje: nadie quiere leer un manual de 50 páginas antes de poder jugar. La interfaz debe enseñarse sola mientras juegas.

### HUD y minimalismo

El HUD es un equilibrio complicado. Necesitas mostrar información importante (salud, munición, minimapa) sin convertir la pantalla en un panel de control de avión. La clave está en mostrar solo lo necesario cuando es necesario.

El diseño modular ayuda mucho aquí. Agrupa información relacionada y colócala donde tenga sentido. La salud y el escudo van juntos, el minimapa en una esquina, las notificaciones en otro lugar predecible.

### Interactividad e inmersión

El feedback es fundamental. Cuando el jugador hace algo, la interfaz debe responder inmediatamente. Un botón que cambia de color, un sonido sutil, una pequeña animación: todo esto confirma que la acción se registró.

Las animaciones no son solo decoración. Una transición suave entre menús hace que la experiencia se sienta pulida y profesional. Pero cuidado con excederte: nadie quiere esperar 3 segundos viendo una animación cada vez que abre el inventario.

### Navegación clara

Los menús deben ser obvios. Si el jugador tiene que adivinar qué hace cada opción, ya perdiste. Usa iconos reconocibles, texto claro, y organiza todo de forma lógica.

La jerarquía visual es tu mejor amiga aquí. Los elementos más importantes deben destacar naturalmente, ya sea por tamaño, color o posición.

### Compatibilidad con múltiples dispositivos

Un juego moderno puede jugarse en PC con teclado y ratón, en consola con mando, o en móvil con pantalla táctil. Tu interfaz necesita funcionar bien en todos estos contextos.

En móviles especialmente, los elementos táctiles necesitan ser lo suficientemente grandes para dedos humanos reales, no para stylus de precisión quirúrgica.

### Personalización y configuración

Dale poder al jugador. Algunos querrán el HUD mínimo, otros querrán toda la información posible. Las opciones de personalización no son lujo, son necesidad.

Las opciones de configuración extensas permiten que cada jugador ajuste el juego a sus necesidades: dificultad, controles, audio, video. Más opciones significa más jugadores que pueden disfrutar tu juego.

### Integración narrativa

La interfaz puede contar historia también. En un juego medieval, los menús pueden parecer pergaminos antiguos. En uno de ciencia ficción, interfaces holográficas. Estos detalles suman inmersión.

El género del juego también dicta el estilo de interfaz. Un shooter frenético necesita información rápida y clara. Un juego de gestión puede permitirse interfaces más densas y detalladas.

## 1.3 Tipos de retícula

Las retículas son la estructura invisible que mantiene todo organizado. En videojuegos usamos varios tipos según lo que necesitemos:

### Retícula de 8 puntos

Esta es probablemente la más práctica para videojuegos. Todo se basa en múltiplos de 8 píxeles: botones de 40px de alto (5×8), márgenes de 16px (2×8), espaciados de 24px (3×8).

¿Por qué 8? Porque funciona perfectamente con las resoluciones de pantalla más comunes y hace que todo se vea consistente sin esfuerzo. También facilita muchísimo el trabajo cuando necesitas adaptar tu interfaz a diferentes tamaños de pantalla.

### Retícula modular

Piensa en esto como dividir tu pantalla en cajas o contenedores. Cada caja tiene su propósito: una para el inventario, otra para las estadísticas, otra para el mapa.

Es especialmente útil en juegos de estrategia o RPGs donde tienes mucha información que mostrar. Cada módulo puede actualizarse independientemente sin afectar a los demás.

### Retícula jerárquica

Esta es más orgánica y se adapta al contenido en lugar de forzar el contenido a adaptarse a ella. Es perfecta cuando tienes elementos de diferentes importancias y tamaños.

Un árbol de habilidades en un RPG es un ejemplo perfecto. No todas las habilidades son igual de importantes, y la retícula jerárquica te permite reflejar eso visualmente.

### Retícula de columnas

Divide la pantalla verticalmente. Es simple pero efectiva, especialmente para menús de opciones donde tienes categorías claras: gráficos a la izquierda, audio en el centro, controles a la derecha.

### Retícula fluida

Esta se adapta dinámicamente al tamaño de pantalla. Los elementos se escalan proporcionalmente, manteniendo las relaciones entre ellos.

Es esencial para juegos multiplataforma. El mismo juego puede verse bien en un móvil de 5 pulgadas o en un monitor ultrawide de 34 pulgadas.

La realidad es que probablemente uses una combinación de varias retículas en tu juego. El HUD podría usar una retícula de 8 puntos, los menús una de columnas, y el árbol de habilidades una jerárquica. Lo importante es que cada una sirva su propósito y que juntas creen una experiencia coherente.

Citas:
- [1] https://www.uifrommars.com/mejora-tu-diseno-ui-utilizando-reticulas/
- [2] https://www.youtube.com/watch?v=lFQ9Hcjuu6o
- [3] https://www.youtube.com/watch?v=nq6cA-np5SE
- [4] https://myk.graphics/grillas-el-secreto-para-interfaces-intuitivas/
- [5] https://www.uifrommars.com/reticula-8pt-que-es-para-que-sirve/
- [6] https://cei.es/que-es-una-reticula-en-diseno-grafico/
- [7] https://platzi.com/clases/1493-diseno-interfaz/17098-disenando-con-grid-y-espaciado/
