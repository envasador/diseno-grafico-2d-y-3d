# Proyecto 2 · Arte 3D

En este proyecto llevas tu mundo a tres dimensiones. Vas a producir una escena 3D en Blender siguiendo un pipeline profesional: planificación en concept, modelado, texturizado, rigging y animación, y exportación al motor. El resultado tiene que poder integrarse directamente en un proyecto de Unity o Godot, y será el escenario de tu cinemática en el proyecto 3.

La escena tiene que contar algo, aunque sea sencillo. Es una escena de juego: un espacio, un personaje que lo habita y objetos que lo definen.

## Objetivo

Producir una escena 3D completa en Blender, desde la planificación hasta la exportación al motor de videojuegos, coherente con la biblia de arte de tu proyecto.

## Resultados de aprendizaje y criterios de evaluación

**RA1** Desarrolla los principios del proceso creativo del arte conceptual del proyecto del videojuego. *(Fase 0: criterios c, d y g)*

| Criterio |
|---|
| c) Se han aplicado las técnicas para el desarrollo del arte. |
| d) Se han diseñado personajes y objetos. |
| g) Se han identificado las técnicas de creación de personajes. |

**RA4** Diseña elementos gráficos y animaciones en 3D siguiendo el guion establecido.

| Criterio |
|---|
| a) Se han representado vectorialmente objetos en el espacio tridimensional. |
| b) Se han manejado y aplicado texturas y materiales. |
| c) Se han elaborado personajes y objetos mediante representación tridimensional utilizando las técnicas de modelado. |
| d) Se han distribuido los diferentes elementos (objetos, luces, cámaras) en una escena. |
| e) Se ha determinado el funcionamiento del sistema de animaciones 3D. |
| f) Se han transformado modelos mediante las tuberías de renderizado. |
| g) Se ha configurado la herramienta de importación y exportación de modelos 3D. |
| h) Se ha añadido textura a objetos 3D. |
| i) Se ha aplicado la interpolación en una escena 3D. |
| j) Se ha generado un conjunto de animaciones para un objeto del juego. |
| k) Se ha configurado la herramienta de importación de modelos 3D. |

## Descripción del proyecto

Crea una escena 3D ambientada en el mundo de tu proyecto. Si puedes, lleva a 3D el personaje que diseñaste en el proyecto 1: es exactamente lo que hace un estudio cuando adapta un diseño 2D. Si tu proyecto todavía no tiene un entorno definido, puedes elegir una temática libre (medieval, futurista, terror, fantasía…).

**Requisitos mínimos:**

| Elemento | Mínimo exigido |
|---|---|
| Personaje | 1, con rig y al menos una animación |
| Objetos secundarios | 2, con materiales y texturas aplicadas |
| Escenario | 1 entorno sencillo que contextualice la escena |
| UV mapping | Aplicado a todos los modelos |
| Animaciones | 1 ciclo del personaje + 1 animación de objeto |
| Luz y cámara | 1 luz principal, 1 de relleno y 1 cámara para el render |
| Exportación | FBX o glTF importado y funcional en el motor |

La luz y la cámara de este proyecto son solo las necesarias para renderizar la escena. La iluminación y las cámaras se trabajan a fondo en el proyecto 3.

**Ejemplo de referencia: mini escena medieval**

| Elemento | Descripción | Técnica |
|---|---|---|
| Personaje | Caballero medieval sencillo | Modelado + rigging básico |
| Objetos secundarios | Espada y cofre | Modelado 3D |
| Escenario | Plaza con suelo empedrado y muro | Modelado 3D |
| Texturas | Piedra, madera y metal | UV mapping |
| Animaciones | Ciclo de caminar + abrir el cofre | Rigging + interpolaciones |

## Fase 0 · Concept para 3D *(obligatoria, evalúa RA1)*

Antes de abrir Blender, prepara en tu biblia de arte de Figma el capítulo de la UT3:

- **Concepto de la escena:** qué ocurre, dónde y quién es el personaje. Dos o tres frases bastan.
- **Moodboard de materiales:** al menos cuatro referencias (fotografías, juegos, ilustraciones o tu propio concept art) que definan el estilo visual y las superficies que quieres conseguir.
- **Boceto o thumbnails de la escena:** lo importante es tener claro qué vas a modelar y cómo se distribuye en el espacio.
- **[Turnaround](../concept/hojas-de-produccion.md#turnaround) del personaje:** vista frontal y lateral a la misma escala, en T-pose o A-pose. Lo usarás como referencia en Blender.
- **[Callouts](../concept/hojas-de-produccion.md#callouts) de materiales** del personaje y de los objetos secundarios.

Sin la Fase 0 entregada, el proyecto no se corregirá.

## Fase 1 · Modelado y texturizado

*(RA4a, RA4b, RA4c, RA4d, RA4h)*

Crea los modelos a partir de la Fase 0. El orden recomendado es escenario, objetos secundarios y personaje: así tienes el espacio definido antes de modelar al protagonista, lo que te ayuda con las proporciones.

**Modelado:**

- Personaje principal con una topología limpia, pensada para el rigging posterior.
- Al menos dos objetos secundarios que aporten contexto narrativo a la escena.
- Escenario sencillo: basta con el área visible desde la cámara.

**Texturizado:**

- UV mapping en todos los modelos antes de texturizar.
- Materiales configurados en el Shader Editor, cuidando la rugosidad y la metalicidad además del color base. Compáralos con tus callouts.
- Las texturas pueden ser procedurales, pintadas en Texture Paint o importadas de recursos externos (indicando la fuente).

## Fase 2 · Animación

*(RA4e, RA4i, RA4j)*

**Rigging:** un rig básico para el personaje. Basta con una jerarquía de huesos funcional y un weight painting cuidado en las zonas de deformación (caderas, hombros, rodillas).

**Animaciones:**

- **Personaje:** al menos un ciclo completo (caminar, idle o ataque). Aplica lo que viste en los [principios de animación](../ut2/05-principios-de-animacion.md): poses clave primero, después interpolaciones y timing.
- **Objeto secundario:** al menos una animación (una puerta, un cofre, una bandera, una rueda…).

**Interpolaciones:** revisa las curvas en el Graph Editor. La interpolación lineal pura resulta mecánica; busca ease in y ease out en las transiciones importantes.

## Fase 3 · Render y exportación

*(RA4f, RA4g, RA4k)*

**Render:** configura el motor de render (Eevee o Cycles según tus necesidades) y ajusta al menos la resolución de salida, el número de muestras y el postproceso. Renderiza al menos una imagen de la escena final con una luz principal, una de relleno y una cámara bien encuadrada.

**Exportación:**

- Exporta en **FBX o glTF** (glTF si usas Godot, FBX si usas Unity).
- Comprueba que la importación en el motor funciona: geometría, materiales y animaciones deben conservarse.
- Añade a la presentación una captura del modelo importado en el motor.

## Entrega

Sube a Moodle antes de la fecha y hora indicadas:

- Archivo `.blend` con los assets organizados en colecciones.
- Modelo exportado en FBX o glTF.
- Capturas del modelo importado y funcionando en el motor.
- Presentación en Figma con estas secciones, en este orden:

| Sección | Contenido |
|---|---|
| Concepto | Fase 0 completa: concepto, moodboard, turnaround y callouts |
| Proceso | Capturas de cada fase: modelado en gris, UV map, materiales, rig y animación |
| Resultado | Render final y capturas en el motor |
| Reflexión | Qué ha funcionado, qué cambiarías y qué has aprendido (5-10 líneas) |

## Rúbrica RA1 *(Fase 0)*

| Criterio | Excelente | Notable | Adecuado | Insuficiente | No presenta |
|---|---|---|---|---|---|
| **c)** Técnicas para el desarrollo del arte | Turnaround, callouts y moodboard de materiales precisos y útiles para producir sin dudas. | Documentos correctos, con alguna vista o material poco definido. | Documentos presentes, pero con inconsistencias entre vistas o materiales sin definir. | Documentos incompletos que no sirven como referencia de modelado. | No presenta concept para 3D. |
| **d)** Diseño de personajes y objetos | Personaje y objetos coherentes con la biblia de arte y pensados para 3D desde el concept. | Coherentes con el estilo, con algún detalle poco resuelto para 3D. | Correctos, pero con poca relación con el estilo del proyecto. | Básicos o incoherentes entre sí. | No diseña personajes ni objetos. |
| **g)** Técnicas de creación de personajes | Turnaround en pose neutra adecuada para rigging, con proporciones coherentes en todas las vistas. | Turnaround correcto, con pequeñas diferencias de proporción entre vistas. | Turnaround con varias vistas, pero con incoherencias visibles. | Una sola vista o vistas que no se corresponden. | No aplica técnicas de creación de personajes. |

## Rúbrica RA4

| Criterio | Excelente | Notable | Adecuado | Insuficiente | No presenta |
|---|---|---|---|---|---|
| **a)** Modelado | Topología limpia, sin errores de malla, con proporciones coherentes con la Fase 0. | Topología mayoritariamente correcta, con algún error menor que no afecta al resultado. | Objetos reconocibles y funcionales, con problemas de topología visibles. | Modelado muy básico o incompleto, con errores que afectan al resultado. | No se han creado modelos 3D. |
| **b)** Materiales | Rugosidad, metalicidad y color bien ajustados y coherentes con los callouts y el estilo. | Materiales correctos y coherentes, con algún parámetro mal ajustado. | Materiales básicos en todos los objetos, sin criterio técnico ni artístico claro. | Materiales incompletos o inconsistentes; algún objeto no tiene material. | No se han aplicado materiales. |
| **c)** Personaje y objetos | Bien definidos, reconocibles y coherentes dentro del mismo universo visual. | Reconocibles y coherentes, con alguna imprecisión en proporciones o detalle. | Personaje identificable, pero con falta de detalle o coherencia con la escena. | Personaje muy simplificado o apenas distinguible de los objetos. | No se han modelado personajes ni objetos. |
| **d)** Distribución en escena | Objetos, luces y cámara con una disposición coherente que facilita la lectura visual y narrativa. | Distribución correcta, con algún elemento mal posicionado. | Los elementos están en escena, pero sin un criterio claro de composición. | Escena desorganizada o con elementos esenciales ausentes. | No se ha trabajado la distribución. |
| **e)** Rigging y animaciones | Rig con jerarquía correcta; animaciones fluidas y creíbles, sin deformaciones. | Rig funcional con algún error menor que no rompe la animación. | Rig básico funcional, con deformaciones visibles en algunos movimientos. | Rig incompleto o con deformaciones que impiden valorar la animación. | No hay sistema de animación. |
| **f)** Render | Resolución, muestras y postproceso configurados de forma coherente con el estilo. | Configuración correcta, con algún parámetro mejorable. | Render con la configuración por defecto. | Render con artefactos evidentes o configuración incorrecta. | No se ha realizado ningún render. |
| **g)** y **k)** Exportación e importación | Formato correcto; geometría, materiales y animaciones se conservan y la importación funciona sin errores. | Exportación correcta, con algún material o animación que no se transfiere bien. | Se exporta, pero se pierden texturas o animaciones en el motor. | El archivo no se importa correctamente en el motor. | No se ha exportado. |
| **h)** UV mapping | Sin solapamientos, con buen aprovechamiento del espacio y sin distorsiones. | Correcto en casi todos los modelos, con alguna distorsión en zonas poco visibles. | Básico, con distorsiones o solapamientos en algunas partes. | Problemas graves que deforman las texturas. | No se ha hecho UV mapping. |
| **i)** Interpolación | Transiciones fluidas, con curvas bien ajustadas (ease in y ease out). | Interpolaciones correctas, con alguna transición demasiado lineal. | Movimientos funcionales pero mecánicos. | Movimientos poco naturales o con saltos evidentes. | No se han aplicado interpolaciones. |
| **j)** Conjunto de animaciones | Ciclo del personaje y animación de objeto diferenciados, fluidos y bien definidos. | Las dos animaciones son correctas; una podría mejorar. | Al menos una animación funcional, aunque básica. | Animación incompleta o con errores evidentes. | No se han generado animaciones. |
