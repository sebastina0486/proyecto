import sys
class Camper:
    def __init__(self, id, names, last_names, address, guardian, contact_numbers, status, risk, assigned_route=None):
        self.id = id
        self.names = names
        self.last_names = last_names
        self.address = address
        self.guardian = guardian
        self.contact_numbers = contact_numbers
        self.status = status
        self.risk = risk
        self.assigned_route = assigned_route
class Trainer:
    def __init__(self, name, specialty, schedule, assigned_routes=None):
        self.name = name
        self.specialty = specialty
        self.schedule = schedule
        self.assigned_routes = assigned_routes
class TrainingRoute:
    def __init__(self, name, modules, main_db, alternate_db, trainers=None):
        self.name = name
        self.modules = modules
        self.main_db = main_db
        self.alternate_db = alternate_db
        self.trainers = trainers
class Module:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
class TrainingArea:
    def __init__(self, name, capacity, assigned_campers=None):
        self.name = name
        self.capacity = capacity
        self.assigned_campers = assigned_campers
def show_menu():
    print("Bienvenido al Sistema de Seguimiento Académico de CampusLands")
    print("1. Registrar nuevo Camper")
    print("2. Asignar Ruta de Entrenamiento a Camper")
    print("3. Registrar Notas de Camper")
    print("4. Generar Reportes")
    print("5. Salir")

def main():
    salir = False  # Inicialmente establecemos salir como False para que el bucle se ejecute al menos una vez
    while not salir:  # Usamos not salir para que el bucle se ejecute hasta que salir sea True
        show_menu()
        option = input("Ingrese el número de la opción deseada: ")
        print(repr(option))
        print("a")
        if option == "1":
            id = input("Ingrese el número de identificación del Camper: ")
            names = input("Ingrese los nombres del Camper: ")
            last_names = input("Ingrese los apellidos del Camper: ")
            address = input("Ingrese la dirección del Camper: ")
            guardian = input("Ingrese el nombre del tutor o tutora del Camper: ")
            contact_numbers = input("Ingrese los números de contacto del Camper (separados por coma): ").split(",")
            status = input("Ingrese el estado del Camper (por ejemplo, 'Activo', 'Inactivo', etc.): ")
            risk = input("Ingrese el nivel de riesgo del Camper: ")
    
            new_camper = Camper(id, names, last_names, address, guardian, contact_numbers, status, risk)
    
            register_camper(new_camper)
            # Lógica para registrar un nuevo Camper
        elif option == "2":
            
            # L # Lógica para asignar una Ruta de Entrenamiento a un Camper
            # Aquí puedes solicitar al usuario que ingrese el ID del Camper y el nombre de la ruta de entrenamiento
            camper_id = input("Ingrese el ID del Camper: ")
            route_name = input("Ingrese el nombre de la Ruta de Entrenamiento: ")
    
            # Realizar la lógica para buscar el Camper y la Ruta de Entrenamiento correspondientes
            # y luego llamar a la función assign_training_route(camper, route) con los objetos apropiadosógica para asignar una Ruta de Entrenamiento a un Camper
        elif option == "3":
            # Lógica para registrar las notas de un Camper
            # Aquí puedes solicitar al usuario que ingrese el ID del Camper y las notas teóricas y prácticas
            camper_id = input("Ingrese el ID del Camper: ")
            theoretical_grade = float(input("Ingrese la nota teórica del Camper: "))
            practical_grade = float(input("Ingrese la nota práctica del Camper: "))
    
            # Realizar la lógica para buscar el Camper correspondiente
            # y luego llamar a la función enter_grades(camper, theoretical_grade, practical_grade) con el objeto Camper y las notas ingresadas

        elif option == "4":
        
            generate_reports(existing_data)

        elif option == "5":
            print("¡Hasta luego! 5")
            salir = True  # Cambiamos salir a True para salir del bucle
            sys.exit()
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

    if __name__ == "__main__":
        main()
import json

# Archivo donde se guardarán los datos
FILE_NAME = "data.json"


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None


    # Cargar datos existentes (si hay)
    existing_data = load_data()
    if existing_data:
        print("Datos cargados:", existing_data)
    else:
        print("No se encontraron datos existentes.")

    # Datos de ejemplo para guardar
    data_to_save = {
        "campers": [],
        "trainers": [],
        "training_routes": [],
        "training_areas": []
    }

    # Guardar datos de ejemplo
    save_data(data_to_save)
    print("Datos guardados:", data_to_save)


if __name__ == "__main__":
    main()
class InvalidInputError(Exception):
    pass


def validate_camper(camper):
    if not isinstance(camper, Camper):
        raise InvalidInputError("El objeto no es un Camper.")
    if not camper.id:
        raise InvalidInputError("El Camper debe tener un número de identificación.")
    # Agregar más validaciones según sea necesario


def register_camper(camper):
    try:
        validate_camper(camper)
        # Lógica para registrar al Camper en el sistema
        print("Camper registrado exitosamente.")
    except InvalidInputError as e:
        print("Error al registrar al Camper:", e)


# Ejemplo de uso
    # Intentamos registrar un Camper con datos inválidos
    invalid_camper = Camper("", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Inscrito", "Bajo")
    register_camper(invalid_camper)

    # Intentamos registrar un Camper con datos válidos
    valid_camper = Camper("123456789", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Inscrito", "Bajo")
    register_camper(valid_camper)

if __name__ == "__main__":
    main()

def assign_training_route(camper, route):
    try:
        validate_camper(camper)
        # Verificar capacidad del área de entrenamiento para la ruta asignada
        # Lógica para asignar la ruta de entrenamiento al Camper
        print(f"Ruta de entrenamiento '{route.name}' asignada al Camper '{camper.names} {camper.last_names}'.")
    except InvalidInputError as e:
        print("Error al asignar ruta de entrenamiento:", e)


def enter_grades(camper, theoretical_grade, practical_grade):
    try:
        validate_camper(camper)
        if not (isinstance(theoretical_grade, (int, float)) and isinstance(practical_grade, (int, float))):
            raise InvalidInputError("Las notas deben ser números.")
        if theoretical_grade < 0 or theoretical_grade > 100 or practical_grade < 0 or practical_grade > 100:
            raise InvalidInputError("Las notas deben estar entre 0 y 100.")
        # Lógica para ingresar las notas del Camper
        print(f"Notas registradas para el Camper '{camper.names} {camper.last_names}'.")
    except InvalidInputError as e:
        print("Error al ingresar notas:", e)


def generate_reports(data):
    try:
        # Generar diferentes tipos de reportes según los datos proporcionados
        # Lógica para generar reportes
        print("Reportes generados exitosamente.")
    except Exception as e:
        print("Error al generar reportes:", e)


# Ejemplo de uso
    # Datos de ejemplo
    camper_to_assign = Camper("123456789", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Inscrito", "Bajo")
    route_to_assign = TrainingRoute("Ruta NodeJS", [Module("Fundamentos de programación", 30)], "MySQL", "MongoDB")
    theoretical_grade = 85
    practical_grade = 70
    data = {}  # Datos de ejemplo para generar reportes

    # Asignar ruta de entrenamiento
    assign_training_route(camper_to_assign, route_to_assign)

    # Ingresar notas
    enter_grades(camper_to_assign, theoretical_grade, practical_grade)

    # Generar reportes
    generate_reports(data)


if __name__ == "__main__":
    main()



def conduct_evaluation(camper):
    try:
        validate_camper(camper)
        # Lógica para realizar la evaluación del Camper
        print(f"Evaluación realizada para el Camper '{camper.names} {camper.last_names}'.")
    except InvalidInputError as e:
        print("Error al realizar la evaluación:", e)
# Ejemplo de uso
    # Datos de ejemplo
    camper_to_evaluate = Camper("123456789", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Cursando", "Bajo")
    theoretical_grade = 85
    practical_grade = 70

    # Ingresar notas
    enter_grades(camper_to_evaluate, theoretical_grade, practical_grade)

    # Realizar evaluación
    conduct_evaluation(camper_to_evaluate)


if __name__ == "__main__":
    main()
def list_registered_campers(data):
    try:
        campers = data.get("campers", [])
        print("Campers registrados:")
        for camper in campers:
            print(f"- {camper['names']} {camper['last_names']} ({camper['status']})")
    except Exception as e:
        print("Error al listar campers registrados:", e)


def list_approved_campers(data):
    try:
        approved_campers = [camper for camper in data.get("campers", []) if camper["status"] == "Aprobado"]
        print("Campers aprobados:")
        for camper in approved_campers:
            print(f"- {camper['names']} {camper['last_names']}")
    except Exception as e:
        print("Error al listar campers aprobados:", e)


def list_active_trainers(data):
    try:
        trainers = data.get("trainers", [])
        print("Entrenadores activos:")
        for trainer in trainers:
            print(f"- {trainer['name']} ({trainer['specialty']})")
    except Exception as e:
        print("Error al listar entrenadores activos:", e)


# Otras funciones de reportes


# Ejemplo de uso
    # Datos de ejemplo
    example_data = {
        "campers": [
            {"names": "John", "last_names": "Doe", "status": "Inscrito"},
            {"names": "Jane", "last_names": "Smith", "status": "Aprobado"}
        ],
        "trainers": [
            {"name": "Trainer 1", "specialty": "Ruta NodeJS"},
            {"name": "Trainer 2", "specialty": "Ruta Java"}
        ]
    }

    # Generar reportes
    list_registered_campers(example_data)
    list_approved_campers(example_data)
    list_active_trainers(example_data)


if __name__ == "__main__":
    main()
#apartir de aqui animal
def registrar_notas_y_cambiar_estado(camper, nota_teoria, nota_practica):
    try:
        # Validar que las notas sean números válidos
        if not (isinstance(nota_teoria, (int, float)) and isinstance(nota_practica, (int, float))):
            raise ValueError("Las notas deben ser números.")
        
        # Calcular el promedio de las notas
        promedio = (nota_teoria + nota_practica) / 2
        
        # Cambiar estado a "Aprobado" si el promedio es mayor o igual a 60
        if promedio >= 60:
            camper.status = "Aprobado"
            print(f"Notas registradas y estado cambiado a 'Aprobado' para el Camper {camper.names} {camper.last_names}.")
        else:
            print("Las notas no alcanzan el promedio mínimo para aprobar.")
    except Exception as e:
        print("Error al registrar notas y cambiar estado:", e)
def assign_training_route(camper, route):
    try:
        validate_camper(camper)
        if camper.status != "Aprobado":
            raise ValueError("El Camper debe estar en estado 'Aprobado' para asignarle una Ruta de Entrenamiento.")
        
        # Verificar si la Ruta de Entrenamiento existe
        if route not in existing_data["training_routes"]:
            raise ValueError("La Ruta de Entrenamiento especificada no existe.")
        
        # Verificar capacidad del área de entrenamiento para la ruta asignada
        # Aquí debes agregar la lógica para verificar si hay capacidad en el área de entrenamiento
        # para asignar al Camper a la Ruta de Entrenamiento
        
        # Asignar la ruta de entrenamiento al Camper
        camper.assigned_route = route.name
        print(f"Ruta de entrenamiento '{route.name}' asignada al Camper '{camper.names} {camper.last_names}'.")
    except Exception as e:
        print("Error al asignar ruta de entrenamiento:", e)
def enter_grades(camper_id, theoretical_grade, practical_grade):
    try:
        # Buscar el Camper correspondiente en los datos existentes
        camper = next((c for c in existing_data["campers"] if c["id"] == camper_id), None)
        if not camper:
            raise ValueError("No se encontró ningún Camper con el ID especificado.")
        
        # Verificar si las notas son números válidos
        if not (isinstance(theoretical_grade, (int, float)) and isinstance(practical_grade, (int, float))):
            raise ValueError("Las notas deben ser números.")
        
        # Verificar si las notas están dentro del rango válido (0-100)
        if theoretical_grade < 0 or theoretical_grade > 100 or practical_grade < 0 or practical_grade > 100:
            raise ValueError("Las notas deben estar entre 0 y 100.")
        
        # Llamar a la función para registrar las notas y cambiar el estado del Camper si es necesario
        registrar_notas_y_cambiar_estado(camper, theoretical_grade, practical_grade)
    except Exception as e:
        print("Error al ingresar notas:", e)
class TrainingArea:
    def __init__(self, name, capacity, assigned_campers=None):
        self.name = name
        self.capacity = capacity
        self.assigned_campers = assigned_campers if assigned_campers is not None else []

    def assign_camper(self, camper):
        if len(self.assigned_campers) < self.capacity:
            self.assigned_campers.append(camper)
            print(f"Camper {camper.names} {camper.last_names} asignado al área de entrenamiento {self.name}.")
        else:
            print(f"No hay capacidad disponible en el área de entrenamiento {self.name}.")

    def __str__(self):
        return f"TrainingArea(Name: {self.name}, Capacity: {self.capacity}, Assigned Campers: {len(self.assigned_campers)})"

# Función para buscar un área de entrenamiento por nombre
def find_training_area_by_name(name, training_areas):
    for area in training_areas:
        if area.name == name:
            return area
    return None
class TrainingArea:
    def __init__(self, name, capacity, assigned_campers=None):
        self.name = name
        self.capacity = capacity
        self.assigned_campers = assigned_campers if assigned_campers is not None else []

    def assign_camper(self, camper):
        if len(self.assigned_campers) < self.capacity:
            self.assigned_campers.append(camper)
            print(f"Camper {camper.names} {camper.last_names} asignado al área de entrenamiento {self.name}.")
        else:
            print(f"No hay capacidad disponible en el área de entrenamiento {self.name}.")

    def __str__(self):
        return f"TrainingArea(Name: {self.name}, Capacity: {self.capacity}, Assigned Campers: {len(self.assigned_campers)})"

# Función para buscar un área de entrenamiento por nombre
def find_training_area_by_name(name, training_areas):
    for area in training_areas:
        if area.name == name:
            return area
    return None
# Crear instancias de TrainingArea
area1 = TrainingArea("Área 1", 30)
area2 = TrainingArea("Área 2", 25)

# Ejemplo de asignación de Camper a un área de entrenamiento
camper = Camper("001", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Inscrito", "Bajo")
area1.assign_camper(camper)

# Ejemplo de búsqueda de un área de entrenamiento por nombre
training_areas = [area1, area2]
found_area = find_training_area_by_name("Área 1", training_areas)
if found_area:
    print("Área de entrenamiento encontrada:", found_area)
else:
    print("No se encontró ningún área de entrenamiento con ese nombre.")
class Module:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class TrainingRoute:
    def __init__(self, name, modules, main_db, alternate_db, trainers=None):
        self.name = name
        self.modules = modules
        self.main_db = main_db
        self.alternate_db = alternate_db
        self.trainers = trainers if trainers is not None else []

    def add_trainer(self, trainer):
        self.trainers.append(trainer)
        print(f"Trainer {trainer.name} asignado a la ruta de entrenamiento {self.name}.")

    def __str__(self):
        return f"TrainingRoute(Name: {self.name}, Modules: {', '.join(module.name for module in self.modules)})"

# Función para crear una nueva ruta de entrenamiento
def create_training_route(name, modules, main_db, alternate_db):
    return TrainingRoute(name, modules, main_db, alternate_db)

# Función para agregar módulos a una ruta de entrenamiento
def add_modules_to_route(route, modules):
    route.modules.extend(modules)
    print(f"Módulos agregados a la ruta de entrenamiento {route.name}.")

# Función para buscar una ruta de entrenamiento por nombre
def find_training_route_by_name(name, training_routes):
    for route in training_routes:
        if route.name == name:
            return route
    return None
modules = [
    Module("Fundamentos de programación", 30),
    Module("Programación Web", 30),
    Module("Programación formal", 30),
    Module("Bases de datos", 30),
    Module("Backend", 30)
]
new_route = create_training_route("Ruta Python", modules, "MySQL", "MongoDB")

# Ejemplo de asignación de entrenador a la ruta de entrenamiento
trainer = Trainer("John Trainer", "Python Specialist", "Monday - Friday")
new_route.add_trainer(trainer)

# Ejemplo de búsqueda de una ruta de entrenamiento por nombre
training_routes = [new_route]
found_route = find_training_route_by_name("Ruta Python", training_routes)
if found_route:
    print("Ruta de entrenamiento encontrada:", found_route)
else:
    print("No se encontró ninguna ruta de entrenamiento con ese nombre.")
# Función para asignar un Camper a una Ruta de Entrenamiento
def assign_training_route(camper, route, training_areas):
    # Verificar la capacidad del área de entrenamiento asociada a la ruta
    area = find_training_area_by_name(route.name, training_areas)
    if area and len(area.assigned_campers) < area.capacity:
        camper.assigned_route = route
        area.assign_camper(camper)
    else:
        print(f"No se pudo asignar el Camper {camper.names} {camper.last_names} a la ruta {route.name} debido a la capacidad insuficiente del área de entrenamiento.")

# Función para buscar un Camper por ID
def find_camper_by_id(camper_id, campers):
    for camper in campers:
        if camper.id == camper_id:
            return camper
    return None
campers = [camper1, camper2, camper3]  # Suponiendo que tienes una lista de campers
training_areas = [area1, area2]  # Suponiendo que tienes una lista de áreas de entrenamiento

# Solicitar al usuario que ingrese el ID del Camper y el nombre de la ruta de entrenamiento
camper_id = input("Ingrese el ID del Camper: ")
route_name = input("Ingrese el nombre de la Ruta de Entrenamiento: ")

# Buscar el Camper por ID
selected_camper = find_camper_by_id(camper_id, campers)
if selected_camper:
    # Buscar la Ruta de Entrenamiento por nombre
    selected_route = find_training_route_by_name(route_name, training_routes)
    if selected_route:
        assign_training_route(selected_camper, selected_route, training_areas)
    else:
        print("No se encontró ninguna ruta de entrenamiento con ese nombre.")
else:
    print("No se encontró ningún Camper con ese ID.")
# Función para asignar un Entrenador a una Ruta de Entrenamiento
def assign_trainer_to_route(trainer, route):
    route.add_trainer(trainer)

# Función para verificar la disponibilidad de un Entrenador en un horario específico
def is_trainer_available(trainer, schedule):
    # Aquí puedes implementar la lógica para verificar la disponibilidad del entrenador en el horario especificado
    return True  # Por ahora siempre devuelve True, se puede personalizar según las necesidades

# Función para buscar un Entrenador por nombre
def find_trainer_by_name(name, trainers):
    for trainer in trainers:
        if trainer.name == name:
            return trainer
    return None
# Ejemplo de asignación de Entrenador a una Ruta de Entrenamiento
trainers = [trainer1]  # Suponiendo que tienes una lista de entrenadores

# Solicitar al usuario que ingrese el nombre del Entrenador y el nombre de la Ruta de Entrenamiento
trainer_name = input("Ingrese el nombre del Entrenador: ")
route_name = input("Ingrese el nombre de la Ruta de Entrenamiento: ")

# Buscar el Entrenador por nombre
selected_trainer = find_trainer_by_name(trainer_name, trainers)
if selected_trainer:
    # Verificar la disponibilidad del Entrenador en el horario de la Ruta de Entrenamiento
    if is_trainer_available(selected_trainer, route_schedule):
        # Asignar el Entrenador a la Ruta de Entrenamiento
        assign_trainer_to_route(selected_trainer, selected_route)
    else:
        print("El Entrenador no está disponible en el horario especificado.")
else:
    print("No se encontró ningún Entrenador con ese nombre.")
class Enrollment:
    def __init__(self, camper, route, start_date, end_date, training_area):
        self.camper = camper
        self.route = route
        self.start_date = start_date
        self.end_date = end_date
        self.training_area = training_area

    def __str__(self):
        return f"Enrollment(Camper: {self.camper.names} {self.camper.last_names}, Route: {self.route.name}, Start Date: {self.start_date}, End Date: {self.end_date}, Training Area: {self.training_area.name})"

# Función para realizar una matrícula
def enroll_camper(camper, route, start_date, end_date, training_area):
    enrollment = Enrollment(camper, route, start_date, end_date, training_area)
    print(f"Matrícula realizada para el Camper {camper.names} {camper.last_names} en la ruta {route.name}.")
    return enrollment
# Ejemplo de matrícula de un Camper en una Ruta de Entrenamiento
camper = Camper("001", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Inscrito", "Bajo")
route = TrainingRoute("Ruta Python", [Module("Fundamentos de programación", 30)], "MySQL", "MongoDB")
start_date = "2024-06-10"
end_date = "2024-08-10"
training_area = TrainingArea("Área Python", 30)

enrollment = enroll_camper(camper, route, start_date, end_date, training_area)
print("Detalles de la matrícula:")
print(enrollment)
# Función para realizar la evaluación de un Camper en un módulo específico
def evaluate_camper_module(camper, module, theoretical_grade, practical_grade):
    # Calcular la nota final del módulo
    module_weight = module.weight / 100
    theoretical_score = theoretical_grade * 0.3
    practical_score = practical_grade * 0.6
    total_score = theoretical_score + practical_score

    # Determinar si el Camper aprueba el módulo
    if total_score >= 60:
        print(f"El Camper {camper.names} {camper.last_names} ha aprobado el módulo {module.name}.")
        return True
    else:
        print(f"El Camper {camper.names} {camper.last_names} ha reprobado el módulo {module.name}.")
        return False
# Ejemplo de evaluación de un Camper en un módulo
camper = Camper("001", "John", "Doe", "123 Main St", "Jane Doe", ["123456789"], "Cursando", "Bajo")
module = Module("Fundamentos de programación", 30)
theoretical_grade = 75
practical_grade = 65

evaluation_result = evaluate_camper_module(camper, module, theoretical_grade, practical_grade)
if evaluation_result:
    # Actualizar el estado del Camper si aprueba el módulo
    camper.status = "Cursando siguiente módulo"
# Función para evaluar el rendimiento de un Camper al finalizar un módulo
def evaluate_camper_performance(camper, module, theoretical_grade, practical_grade):
    # Calcular la nota final del módulo
    module_weight = module.weight / 100
    theoretical_score = theoretical_grade * 0.3
    practical_score = practical_grade * 0.6
    total_score = theoretical_score + practical_score

    # Verificar si la nota es menor a 60 y clasificar el rendimiento del Camper
    if total_score < 60:
        print(f"El Camper {camper.names} {camper.last_names} tiene un bajo rendimiento en el módulo {module.name}.")
        return "Bajo Rendimiento"
    else:
        return "Aceptable"

# Función para identificar campers con bajo rendimiento en un módulo específico
def identify_underperforming_campers(module, campers, theoretical_grades, practical_grades):
    underperforming_campers = []

    # Evaluar el rendimiento de cada Camper en el módulo
    for i, camper in enumerate(campers):
        theoretical_grade = theoretical_grades[i]
        practical_grade = practical_grades[i]
        performance = evaluate_camper_performance(camper, module, theoretical_grade, practical_grade)
        if performance == "Bajo Rendimiento":
            underperforming_campers.append(camper)

    return underperforming_campers
module = Module("Fundamentos de programación", 30)
campers = [camper1, camper2, camper3]  # Lista de campers que han completado el módulo
theoretical_grades = [70, 55, 80]  # Notas teóricas de los campers
practical_grades = [65, 45, 75]  # Notas prácticas de los campers

underperforming_campers = identify_underperforming_campers(module, campers, theoretical_grades, practical_grades)
if underperforming_campers:
    print("Campers con bajo rendimiento en el módulo:")
    for camper in underperforming_campers:
        print(f"- {camper.names} {camper.last_names}")
else:
    print("No se encontraron campers con bajo rendimiento en el módulo.")

# Función para listar los campers en estado de inscrito
    print("Campers en estado de inscrito:")
    for camper in campers:
        if camper.status == "Inscrito":
            print(f"- {camper.names} {camper.last_names}")

# Función para listar los campers que aprobaron el examen inicial
    print("Campers que han aprobado el examen inicial:")
    for camper in campers:
        if camper.status == "Aprobado":
            print(f"- {camper.names} {camper.last_names}")

# Función para listar los entrenadores activos
    print("Entrenadores activos:")
    for trainer in trainers:
        print(f"- {trainer.name} ({trainer.specialty})")

# Función para listar los campers con bajo rendimiento
def list_underperforming_campers(underperforming_campers):
    print("Campers con bajo rendimiento:")
    for camper in underperforming_campers:
        print(f"- {camper.names} {camper.last_names}")

# Función para listar los campers y entrenadores asociados a una ruta de entrenamiento
def list_campers_and_trainers_by_route(route, campers, trainers):
    print(f"Campers y entrenadores asociados a la ruta de entrenamiento '{route.name}':")
    print("Campers:")
    for camper in campers:
        if camper.assigned_route == route:
            print(f"- {camper.names} {camper.last_names}")
    print("Entrenadores:")
    for trainer in trainers:
        if route in trainer.assigned_routes:
            print(f"- {trainer.name}")

# Función para mostrar cuántos campers perdieron y aprobaron cada módulo por ruta de entrenamiento
def show_module_results_by_route(training_routes):
    for route in training_routes:
        print(f"Resultados de módulos para la ruta de entrenamiento '{route.name}':")
        for module in route.modules:
            print(f"- Módulo: {module.name}")
            approved_count = 0
            failed_count = 0
            # Aquí debes tener la lógica para contar cuántos campers aprobaron y cuántos reprobaron el módulo
            print(f"  Aprobados: {approved_count}")
            print(f"  Reprobados: {failed_count}")
list_registered_campers(campers)
list_approved_campers(campers)
list_active_trainers(trainers)
list_underperforming_campers(underperforming_campers)
list_campers_and_trainers_by_route(route, campers, trainers)
show_module_results_by_route(training_routes)
def generate_module_reports(training_routes):
    for route in training_routes:
        print(f"Reporte de módulos para la ruta de entrenamiento '{route.name}':")
        for module in route.modules:
            print(f"- Módulo: {module.name}")
            for trainer in route.trainers:
                approved_count = 0
                failed_count = 0
                for camper in trainer.assigned_campers:
                    # Verificar si el Camper está asignado a esta ruta y si aprobó o reprobó el módulo
                    if camper.assigned_route == route:
                        if camper.module_results.get(module.name) == "Aprobado":
                            approved_count += 1
                        else:
                            failed_count += 1
                print(f"  Entrenador: {trainer.name}")
                print(f"    Aprobados: {approved_count}")
                print(f"    Reprobados: {failed_count}")