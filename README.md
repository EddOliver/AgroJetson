# AgroJetson
Sustainable sensing and automated irrigation platform with predictive analysis via the Nvidia Jetson Nano.

# Creacion del modelo de deteccion de fruta o verdura.

Para poder realizar la detección en una imagen de una fruta o verdura, en este caso tomate, requería realizar un modelo de detección de objetos personalizado, ya que las redes entrenadas como yoloV3 ya vienen entrenadas con bastantes objetos, sin embargo en mi caso, no tiene tomates maduros e inmaduros, por eso me di a la tarea de realizar el entrenamiento de una red neuronal propia, sin embargo ni la jetson ni mi laptop (laptop gaming) son capaces de realizar este proceso, por eso tuve que realizar el entrenamiento en una jupuyter notebook en google colab.

## Preparacion del dataset.

En este caso he modificado una herramienta para realizar manualemnte las labels, mi herramienta modificada esta en la carpeta "yolo-dataset" y la original.

https://github.com/xiaqunfeng/BBox-Label-Tool

- Primero escribiremos nuestras labels en los siguientes archivos:

Una en cada linea:
<img src="https://i.ibb.co/z48YcmM/image.png" width="400">
Separado por comas:
<img src="https://i.ibb.co/mGy0pgj/image.png" width="400">

- Abrimos la herramienta mediante el comando:
    python main.py

<img src="https://i.ibb.co/G0nntmF/image.png" width="1000">

- En la sección de "Image input folder" y "Label output folder" ponemos la carpeta donde van las imágenes y seleccionamos "Load Dir".

<img src="https://i.ibb.co/9prKKPf/image.png" width="1000">

- Seleccionamos la Label que vamos a poner y preisonamos "ConfirmClass"

<img src="https://i.ibb.co/C0cs9qG/image.png" width="1000">

- Ahora vamos seleccionamos los objetos que tendran esa categoria con el cursor.

<img src="https://i.ibb.co/H7G6Vkh/image.png" width="1000">

Al presionar Next en la parte inferior las labels se guardaran junto al archivo de esta forma.

<img src="https://i.ibb.co/xmJdZhc/image.png" width="1000">

Ya que todas nuestras imágenes tengan su label archivo correspondiente, tenemos que correr el archivo "createtest.py" para crear el archivo de entrenamiento, este es una lista con todos los archivos que tenemos en la carpeta de img.

    python createtest.py



