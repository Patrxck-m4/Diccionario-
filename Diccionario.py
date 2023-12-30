meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "FELIZ": "Que causa felicidad.",
            "RELIEVE" : "Labor o figura que resalta sobre el plano.", 
            "VIENTO" : "Corriente de aire producida en la atmósfera por causas naturales, como diferencias de presión o temperatura.",
            "TEMPERATURA" : "Estado de calor del cuerpo humano o de los seres vivos.",
            "DICTADURA" : "Régimen político que, por la fuerza o violencia, concentra todo el poder en una persona o en un grupo u organización y reprime los derechos humanos y las libertades individuales.",
            "MASA" : "Magnitud física que expresa la cantidad de materia de un cuerpo, medida por la inercia de este, y cuya unidad en el sistema internacional es el kilogramo ",
            "ENERGIA": "Eficacia, poder, virtud para obrar.",
            "MATERIA" : "Realidad espacial y perceptible por los sentidos de la que están hechas las cosas que nos rodean y que, con la energía, constituye el mundo físico.",
            "LEY" : "Cada una de las relaciones existentes entre los diversos elementos que intervienen en un fenómeno.",
            "GOBIERNO" : "Órgano superior del poder ejecutivo de un Estado o de una comunidad política, constituido por el presidente y los ministros o consejeros.",
            "DEMOCRACIA": "Sistema político en el cual la soberanía reside en el pueblo, que la ejerce directamente o por medio de representantes.",
            "ESTADO": "Situación en que se encuentra alguien o algo, y en especial cada uno de sus sucesivos modos de ser o estar." ,
            "HOLA": "presión de saludo utilizada entre dos o más personas de trato familiar, sin importar el momento del día ni las circunstancias",
            }
            

palabra = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if palabra in meme_dict.keys():
    print(meme_dict[palabra])
else:
    print("Palabra no encontrada")
