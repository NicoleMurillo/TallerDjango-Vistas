from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.name = new_measurement["name"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    measurement = Measurement(name=measurement["name"])
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()
    return measurement