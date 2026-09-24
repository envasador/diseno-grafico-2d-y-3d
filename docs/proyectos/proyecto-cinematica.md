# Proyecto 3 · Cinemática

Tu escena 3D ya existe; ahora toca decidir cómo la ve el jugador. En este proyecto vas a dirigir una cinemática corta con varios planos, iluminarla para contar algo y llevarla al motor, donde además configurarás la cámara y la luz que tendría la escena durante el juego. Es el proyecto en el que la cámara y la luz dejan de ser un requisito técnico para convertirse en herramientas de narración.

## Objetivo

Producir una cinemática de entre 20 y 45 segundos a partir de la escena del proyecto 2, con una planificación de planos, una iluminación que responda a una intención y una configuración de cámara y luz adaptada al tipo de juego dentro del motor.

## Resultados de aprendizaje y criterios de evaluación

**RA1** Desarrolla los principios del proceso creativo del arte conceptual del proyecto del videojuego. *(Fase 0: criterios b, c y e)*

| Criterio |
|---|
| b) Se han definido las etapas del proceso creativo. |
| c) Se han aplicado las técnicas para el desarrollo del arte. |
| e) Se han diseñado fondos y escenarios. |

**RA5** Define y configura movimientos de cámara e iluminación 3D aplicando los parámetros técnicos establecidos.

| Criterio |
|---|
| a) Se han identificado los conceptos fundamentales de iluminación. |
| b) Se han manejado los diferentes elementos de iluminación y sombra. |
| c) Se han resuelto problemas de rendimiento de luces. |
| d) Se ha realizado el posicionamiento y el movimiento de objetos en el espacio tridimensional. |
| e) Se han visionado objetos del juego mediante cámaras. |
| f) Se han utilizado múltiples cámaras. |
| g) Se han identificado las diferencias entre iluminación dinámica y estática. |
| h) Se han utilizado diferentes configuraciones según el tipo de juego. |

## Descripción del proyecto

La cinemática puede ser la introducción de un nivel, la presentación de un personaje, el descubrimiento de un objeto o cualquier momento de tu juego que merezca contarse con cámara. Parte de la escena del proyecto 2; puedes ampliarla, añadir elementos o cambiar la hora del día si la historia lo pide.

**Requisitos mínimos:**

| Elemento | Mínimo exigido |
|---|---|
| Duración | Entre 20 y 45 segundos |
| Planos | Al menos 3 planos con cámaras distintas y cortes entre ellas |
| Movimiento de cámara | Al menos 1 plano con la cámara en movimiento, con interpolación cuidada |
| Acción | El personaje o un objeto se mueve por el espacio durante la cinemática |
| Iluminación | Esquema de luz basado en tu color key: luz principal, relleno y al menos una luz de acento |
| Luz estática y dinámica | Iluminación del entorno horneada (baked) en el motor y al menos una luz dinámica justificada |
| Cámara de juego | Una cámara de juego configurada en el motor según el género |
| Salida | Vídeo MP4 a 1080p |

**Nivel avanzado (opcional, mejora la nota del RA5):**

- Una segunda configuración de iluminación para la misma escena (otra hora del día, otro estado del juego) y la comparación de ambas.
- Uso de las herramientas de cinemática del motor (Timeline y Cinemachine en Unity, AnimationPlayer con varias Camera3D en Godot) en lugar de renderizar solo desde Blender.
- Medición del rendimiento antes y después de optimizar las luces, con capturas de las estadísticas del motor.

## Fase 0 · Concept de la cinemática *(obligatoria, evalúa RA1)*

Antes de colocar una sola cámara, prepara en tu biblia de arte el capítulo de la UT4:

- **Guion breve:** qué ocurre en la cinemática, en tres o cuatro frases.
- **Storyboard:** un [thumbnail](../concept/thumbnails.md) por plano, con el encuadre y la dirección del movimiento.
- **Lista de planos:** una tabla con el número de plano, el tipo (general, medio, detalle, subjetivo…), la duración aproximada y el movimiento de cámara.
- **[Color keys](../concept/color.md#color-keys-y-color-script):** al menos dos propuestas de luz para la escena y la elegida, justificando qué emoción busca.
- **Moodboard de luz y cámara:** fotogramas de cine o de juegos con la atmósfera y los encuadres que quieres conseguir.

Sin la Fase 0 entregada, el proyecto no se corregirá.

## Fase 1 · Layout y cámaras

*(RA5d, RA5e, RA5f)*

Con la escena en gris (sin preocuparte todavía por la luz), coloca las cámaras de tu storyboard y anima la acción: el personaje o el objeto que se mueve por el espacio. Monta los cortes entre cámaras y comprueba el ritmo en una previsualización rápida (un animatic). Es el momento de cambiar un plano que no funciona, porque todavía no has invertido tiempo en iluminarlo.

## Fase 2 · Iluminación

*(RA5a, RA5b)*

Ilumina la escena usando tu color key como objetivo. Define la luz principal, el relleno y los acentos, y decide qué tipo de luz necesita cada fuente (direccional, puntual, foco, área). Cuida las sombras: su dureza, su color y lo que ocultan o revelan. Compara tu render con el color key y ajusta hasta acercarte a la atmósfera que buscabas.

## Fase 3 · En el motor: luz estática, dinámica y rendimiento

*(RA5c, RA5g, RA5h)*

Importa la escena en Unity o Godot y prepárala como se jugaría:

- **Luz estática:** hornea la iluminación del entorno (lightmaps) y explica qué ganas y qué pierdes.
- **Luz dinámica:** mantén en tiempo real solo las luces que lo justifiquen (una antorcha que parpadea, una pantalla, un hechizo).
- **Rendimiento:** identifica qué luces o sombras pesan más y aplica al menos una optimización (reducir luces en tiempo real, ajustar la resolución o la distancia de las sombras, limitar el alcance de las luces).
- **Cámara de juego:** configura la cámara que tendría esta escena durante el juego según su género (tercera persona, cenital, isométrica, primera persona…) y explica en qué se diferencia de las cámaras de la cinemática.

## Fase 4 · Render y montaje

Renderiza la cinemática desde Blender o grábala desde el motor, con la resolución, las muestras y el postproceso ajustados a tu estilo. Exporta un MP4 a 1080p.

## Entrega

Sube a Moodle antes de la fecha y hora indicadas:

- Vídeo de la cinemática en MP4 (1080p).
- Archivo `.blend` con las cámaras y la iluminación, organizado en colecciones.
- Proyecto del motor (o un paquete exportable con la escena) con la iluminación horneada y la cámara de juego.
- Presentación en Figma con estas secciones, en este orden:

| Sección | Contenido |
|---|---|
| Concepto | Fase 0 completa: guion, storyboard, lista de planos, color keys y moodboard |
| Proceso | Animatic, capturas de la iluminación por fases y comparación con el color key |
| Motor | Luz estática y dinámica, optimización aplicada (con capturas de estadísticas) y cámara de juego |
| Resultado | Enlace al vídeo y fotogramas destacados |
| Reflexión | Qué ha funcionado, qué cambiarías y qué has aprendido (5-10 líneas) |

## Rúbrica RA1 *(Fase 0)*

| Criterio | Excelente | Notable | Adecuado | Insuficiente | No presenta |
|---|---|---|---|---|---|
| **b)** Etapas del proceso creativo | Guion, storyboard, lista de planos y color keys encadenados con claridad; cada decisión se apoya en la anterior. | Todas las etapas presentes y bien definidas, con alguna conexión poco explicada. | Etapas presentes, pero con poca relación entre ellas. | Etapas incompletas o definidas de forma vaga. | No define el proceso. |
| **c)** Técnicas para el desarrollo del arte | Storyboard y color keys claros y expresivos, útiles para producir la cinemática sin dudas. | Documentos correctos, con algún plano o key poco definido. | Documentos presentes, pero poco precisos. | Documentos muy básicos que no sirven como referencia. | No aplica técnicas de concept. |
| **e)** Fondos y escenarios | Composición de los planos y atmósfera del escenario muy trabajadas y coherentes con la biblia de arte. | Planos y atmósfera coherentes, con algún encuadre mejorable. | Escenario correcto, pero con poca intención en la composición. | Composición y atmósfera sin criterio claro. | No trabaja el escenario en el concept. |

## Rúbrica RA5

| Criterio | Excelente | Notable | Adecuado | Insuficiente | No presenta |
|---|---|---|---|---|---|
| **a)** Conceptos fundamentales de iluminación | Luz principal, relleno y acentos bien definidos; el resultado se acerca al color key y la intención está explicada. | Esquema correcto y coherente con el color key, con alguna explicación breve. | Luces funcionales, pero con problemas de contraste o distribución. | La iluminación no aporta nada a la lectura de la escena. | No se ha configurado la iluminación. |
| **b)** Elementos de iluminación y sombra | Tipos de luz bien elegidos para cada fuente y sombras cuidadas en dureza y color. | Tipos de luz adecuados, con algún ajuste de sombras mejorable. | Varios tipos de luz con resultado aceptable, sin trabajar las sombras. | Uso muy básico de luces y sombras. | No se trabajan luces ni sombras. |
| **c)** Rendimiento de luces | Identifica los problemas de rendimiento, aplica optimizaciones y demuestra la mejora con datos del motor. | Aplica optimizaciones correctas, con una medición incompleta. | Aplica alguna optimización sin comprobar su efecto. | Menciona el rendimiento, pero no aplica ninguna optimización. | No trata el rendimiento. |
| **d)** Posicionamiento y movimiento en el espacio | Movimientos del personaje, los objetos y la cámara fluidos, bien interpolados y coherentes con la acción. | Movimientos correctos, con alguna transición demasiado lineal. | Movimientos funcionales pero mecánicos. | Movimientos con saltos o errores evidentes. | No hay movimiento en la escena. |
| **e)** Visionado mediante cámaras | Encuadres bien compuestos que dirigen la mirada y cuentan la acción. | Encuadres correctos, con algún plano mejorable. | Encuadres funcionales, sin una intención clara. | Encuadres que dificultan la lectura de la escena. | No se han configurado cámaras. |
| **f)** Múltiples cámaras | Tres o más planos diferenciados, con cortes bien situados y ritmo cuidado. | Tres planos bien configurados; el ritmo podría estar más trabajado. | Varios planos, pero muy similares entre sí o con cortes bruscos. | Una sola cámara o cámaras sin encuadres relevantes. | No hay cámaras. |
| **g)** Iluminación dinámica y estática | Entorno horneado y luces dinámicas bien justificadas, con las diferencias explicadas y visibles. | Distinción implementada, con una explicación breve. | Distinción implementada, sin explicar sus diferencias. | Intento de horneado o de luces dinámicas sin resultado funcional. | No se distingue entre luz estática y dinámica. |
| **h)** Configuraciones según el tipo de juego | Cámara de juego y luz adaptadas al género y justificadas frente a la configuración de la cinemática. | Configuración coherente con el género, con una justificación breve. | Se menciona el género, pero la configuración no lo refleja. | La configuración no guarda relación con el tipo de juego. | No se ha considerado el tipo de juego. |
