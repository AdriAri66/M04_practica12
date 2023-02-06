import xml.etree.ElementTree as ET

def alumnos():

    #Root de XML
    root = ET.Element("students")

    #Child1 de root
    child1 = ET.SubElement(root, "student1")

    #SubChild1 de Child1

    subchild1 = ET.SubElement(child1, "name")

    subchild8 = ET.SubElement(child1, "surname")

    subchild9 = ET.SubElement(child1, "email")

    subchild10 = ET.SubElement(child1, "dni")

    # Child2 de root

    child2 = ET.SubElement(root, "student2")

    # SubChild2 de Child2

    subchild2 = ET.SubElement(child2, "name")

    subchild2 = ET.SubElement(child2, "surname")

    subchild2 = ET.SubElement(child2, "email")

    subchild2 = ET.SubElement(child2, "dni")

    # Child3 de root

    child3 = ET.SubElement(root, "student3")

    # SubChild3 de Child3

    subchild3 = ET.SubElement(child3, "name")

    subchild3 = ET.SubElement(child3, "surname")

    subchild3 = ET.SubElement(child3, "email")

    subchild3 = ET.SubElement(child3, "dni")

    # Child4 de root

    child4 = ET.SubElement(root, "student4")

    # SubChild4 de Child4

    subchild4 = ET.SubElement(child4, "name")

    subchild4 = ET.SubElement(child4, "surname")

    subchild4 = ET.SubElement(child4, "email")

    subchild4 = ET.SubElement(child4, "dni")

    # Child5 de root

    child5 = ET.SubElement(root, "student5")

    # SubChild5 de Child5

    subchild5 = ET.SubElement(child5, "name")

    subchild5 = ET.SubElement(child5, "surname")

    subchild5 = ET.SubElement(child5, "email")

    subchild5 = ET.SubElement(child5, "dni")

    # Guardar en XML ElementTree

    tree = ET.ElementTree(root)

    # Añadir atributos con nombre y valor en elemento child "student"

    element = root[0]
    element.set("Genero", "Binario")
    element = root[1]
    element.set("Genero", "Hombre")
    element = root[2]
    element.set("Genero", "Mujer")
    element = root[3]
    element.set("Genero", "Mujer")
    element = root[4]
    element.set("Genero", "Hombre")
    tree.write("students.xml")

    #Imprimir por consola el root

    ET.dump(root)