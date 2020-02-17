# AgroJetson
Sustainable sensing and automated irrigation platform with predictive analysis via the Nvidia Jetson Nano.

# Creacion del modelo de deteccion de fruta o verdura.

Para poder realizar la detección en una imagen de una fruta o verdura, en este caso tomate, requería realizar un modelo de detección de objetos personalizado, ya que las redes entrenadas como yoloV3 ya vienen entrenadas con bastantes objetos, sin embargo en mi caso, no tiene tomates maduros e inmaduros, por eso me di a la tarea de realizar el entrenamiento de una red neuronal propia, sin embargo ni la jetson ni mi laptop (laptop gaming) son capaces de realizar este proceso, por eso tuve que realizar el entrenamiento en una jupuyter notebook en google colab.

## Preparacion del dataset.

