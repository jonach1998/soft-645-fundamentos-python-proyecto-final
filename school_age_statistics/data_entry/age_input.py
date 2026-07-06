_MIN_AGE = 1
_MAX_AGE = 100


def request_age_sample():
    sample_size = _request_sample_size()
    ages = _request_ages(sample_size)

    return {
        "sample_size": sample_size,
        "ages": ages,
    }


def _request_integer(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Este campo no puede estar vacío.")
            continue

        try:
            return int(value)
        except ValueError:
            print(f"'{value}' no es un número entero válido.")


def _request_sample_size():
    while True:
        sample_size = _request_integer("Ingrese el tamaño de la muestra: ")

        if sample_size <= 0:
            print("El tamaño de la muestra debe ser mayor que 0.")
            continue

        return sample_size


def _request_age(position):
    while True:
        age = _request_integer(f"Ingrese la edad #{position}: ")

        if age < _MIN_AGE:
            print(f"La edad #{position} es muy baja. La edad mínima es {_MIN_AGE}.")
            continue

        if age > _MAX_AGE:
            print(f"La edad #{position} es muy alta. La edad máxima es {_MAX_AGE}.")
            continue

        return age


def _request_ages(sample_size):
    ages = []

    for position in range(1, sample_size + 1):
        age = _request_age(position)
        ages.append(age)

    return ages
