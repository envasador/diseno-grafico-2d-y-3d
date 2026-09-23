# Concept · Hojas de producción

Tu personaje está aprobado y te encanta la ilustración que has hecho de él. Ahora se la pasas a alguien que tiene que modelarlo en 3D, y lo primero que te pregunta es cómo es por detrás. Luego, qué pasa con la capa cuando levanta el brazo. Luego, de qué material son las hombreras. Si tu concept no responde a esas preguntas, está incompleto. Las hojas de producción son los documentos que las responden antes de que alguien tenga que hacerlas.

## Turnaround

El turnaround muestra al personaje (o al objeto) desde varios ángulos, normalmente de frente, perfil y espalda, a veces también en tres cuartos. Todas las vistas se dibujan a la misma escala y alineadas con líneas horizontales que marcan puntos clave: la parte superior de la cabeza, los hombros, la cintura, las rodillas, los pies. Así se comprueba que las proporciones son coherentes en todas las vistas.

Se dibuja en pose neutra. Para personajes que se van a modelar y riggear en 3D se usa la **T-pose** (brazos en cruz) o la **A-pose** (brazos a unos 45 grados), porque facilitan el rigging posterior.

En la **UT3** el turnaround se convierte en tus vistas ortográficas: las importarás en Blender como imágenes de fondo en las vistas frontal y lateral para modelar encima.

## Model sheet

El model sheet agrupa todo lo que hace falta para dibujar o reproducir un personaje de forma consistente. Suele incluir el turnaround, las proporciones medidas en cabezas, la paleta con los valores exactos de color y notas sobre los rasgos que no pueden cambiar (la forma de los ojos, el número de puntas del pelo). Es la hoja que usa cualquier persona del equipo que tenga que dibujar al personaje sin haberlo diseñado.

## Hojas de expresiones y de poses

Una **hoja de expresiones** muestra la cara del personaje con sus emociones principales: neutral, alegre, enfadado, asustado, triste. Sirve para mantener la coherencia del rostro y para comprobar que el diseño admite expresividad.

Una **hoja de poses** muestra al personaje en acción: corriendo, atacando, saltando, en reposo. Es especialmente importante antes de animar, porque las poses clave de la hoja se convierten en los fotogramas clave de la animación. En la **UT2** harás una hoja de poses de tu personaje antes de empezar el idle, el ciclo de andar y el ataque.

## Callouts

Los callouts son notas y ampliaciones que explican lo que el dibujo general no deja claro: un detalle de la hebilla a mayor tamaño, una flecha que indica que la capa es de tela gruesa, una muestra del material metálico con su nivel de brillo. En props y en personajes con equipo complejo son imprescindibles.

En la **UT3** los callouts de materiales te servirán para configurar los materiales en Blender: qué parte es metal, cuál es rugosa, cuál refleja.

## Hojas de props y de entornos

Los objetos siguen la misma lógica: vistas desde varios ángulos, escala respecto al personaje (colocar al personaje al lado del objeto evita sorpresas) y callouts de materiales. Para entornos, en lugar de turnarounds se hacen vistas generales, planos de planta y hojas de elementos modulares (piezas que se repiten para construir el nivel), que en 2D serán tus tiles.

| Documento | Qué resuelve | Dónde lo usarás |
|---|---|---|
| Turnaround | Cómo es desde todos los ángulos | UT3 (vistas ortográficas para modelar) |
| Model sheet | Cómo se dibuja de forma consistente | UT2 y UT3 |
| Hoja de expresiones | Cómo expresa emociones | UT2 (retratos, animación facial) |
| Hoja de poses | Cómo se mueve y actúa | UT2 (fotogramas clave) y UT3 (animación) |
| Callouts | Detalles y materiales | UT3 (materiales y texturas) |
| Hoja de props o entornos | Escala, piezas y materiales del mundo | UT2 (tilesets) y UT3 (escena) |
