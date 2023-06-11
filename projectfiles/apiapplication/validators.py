from sqlalchemy.orm import validates


@validates('number')
def validate_number(value):
    if value < 0:
        raise ValueError('"number" must be positive')
    else:
        print("Userid is positive number")
    return value
