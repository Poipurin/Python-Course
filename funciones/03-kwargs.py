# keywords arguments
def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"])


get_product(id="33",
            name="ratón",
            descripción="squeek")  # nombrar el parámetro
