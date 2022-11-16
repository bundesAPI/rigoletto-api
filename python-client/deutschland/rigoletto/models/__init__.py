# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from deutschland.rigoletto.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from deutschland.rigoletto.model.http_validation_error import HTTPValidationError
from deutschland.rigoletto.model.location_inner import LocationInner
from deutschland.rigoletto.model.validation_error import ValidationError
