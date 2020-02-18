# AgroJetson
Sustainable sensing and automated irrigation platform with predictive analysis via the Nvidia Jetson Nano.

# Creacion del modelo de deteccion de fruta o verdura.

## Prerequisitos:

- Tener una cuenta de google drive.

## Proceso:

Para poder realizar la detección en una imagen de una fruta o verdura, en este caso tomate, requería realizar un modelo de detección de objetos personalizado, ya que las redes entrenadas como yoloV3 ya vienen entrenadas con bastantes objetos, sin embargo en mi caso, no tiene tomates maduros e inmaduros, por eso me di a la tarea de realizar el entrenamiento de una red neuronal propia, sin embargo ni la jetson ni mi laptop (laptop gaming) son capaces de realizar este proceso, por eso tuve que realizar el entrenamiento en una jupuyter notebook en google colab.

## Preparacion del dataset.

En este caso he modificado una herramienta para realizar manualemnte las labels, mi herramienta modificada esta en la carpeta "yolo-dataset" y la original.

https://github.com/xiaqunfeng/BBox-Label-Tool

- Primero escribiremos nuestras labels en los siguientes archivos:

Una en cada linea:

<img src="https://i.ibb.co/MPvnbB5/image.png" width="400">

Escribimos el numero de clases:

<img src="https://i.ibb.co/nRJc5QM/image.png" width="400">

Separado por comas:

<img src="https://i.ibb.co/7kJ4Zwg/image.png" width="400">

- Abrimos la herramienta mediante el comando:
    python main.py

<img src="https://i.ibb.co/9V58HKc/image.png" width="1000">

- En la sección de "Image input folder" y "Label output folder" ponemos la carpeta donde van las imágenes y seleccionamos "Load Dir".

<img src="https://i.ibb.co/4dDJyWK/image.png" width="1000">

- Seleccionamos la Label que vamos a poner y preisonamos "ConfirmClass"

<img src="https://i.ibb.co/ZXW9YxB/image.png" width="1000">

- Ahora vamos seleccionamos los objetos que tendran esa categoria con el cursor.

<img src="https://i.ibb.co/tz9mHbc/image.png" width="1000">

Al presionar Next en la parte inferior las labels se guardaran junto al archivo de esta forma.

<img src="https://i.ibb.co/pzGCmz4/image.png" width="1000">

Ya que todas nuestras imágenes tengan su label archivo correspondiente, tenemos que correr el archivo "createtest.py" para crear el archivo de entrenamiento, este es una lista con todos los archivos que tenemos en la carpeta de img.

    python createtest.py

Una vez este todo esto listo, tenemos que comprimir el arhivo como un zip y en nuestro google drive pegarlo dentro de una carpeta llamada "ml" de esta forma.

<img src="https://i.ibb.co/17SDstj/image.png" width="1000">

Una veste este esto listo, podremos pasar realizar el proceso en google colab.

https://colab.research.google.com/

<img src="https://i.ibb.co/j54p14c/image.png" width="1000">

Tenemos que subir el archivo dentro de la carpeta "Jupyter Yolo Colab" a nuestra plataforma Colab y seguir las intrucciones explicadas dentro de el jupyter notebook hasta que termine la seccion de entrenamiento.

<img src="https://i.ibb.co/g74jdWv/image.png" width="1000">

Una vez terminada la seccion de entrenamiento tendremos nuestro modelo terminado y su archivo cfg dentro de la carpeta de drive "ml".

<img src="https://i.ibb.co/yWPHznB/image.png" width="1000">

Una vez terminada la seccion de entrenamiento tendremos nuestro modelo terminado y su archivo cfg dentro de la carpeta de drive "ml".

<img src="https://i.ibb.co/yWPHznB/image.png" width="1000">

Descarga todos los archivos mostrados en la imagen y pegalos en la carpeta donde guardes el archivo Yolo with "OpenCV.ipynb"

<img src="https://i.ibb.co/YWxmF5z/image.png" width="1000">




