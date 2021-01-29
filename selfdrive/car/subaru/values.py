# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  STEER_MAX = 2047              # max_steer 4095
  STEER_STEP = 2                # how often we update the steer cmd
  STEER_DELTA_UP = 50           # torque increase per refresh, 0.8s to max
  STEER_DELTA_DOWN = 70         # torque decrease per refresh
  STEER_DRIVER_ALLOWANCE = 60   # allowed driver torque before start limiting
  STEER_DRIVER_MULTIPLIER = 10  # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1       # from dbc
  
  #SUBARU STOP AND GO - Global
  SNG_DISTANCE_LIMIT = 120      # distance trigger value limit for stop and go (0-255)
  SNG_DISTANCE_DEADBAND = 10     # deadband for SNG lead car refence distance to cater for Close_Distance sensor noises
  THROTTLE_TAP_LIMIT = 5        # send a maximum of 5 throttle tap messages (trial and error)
  THROTTLE_TAP_LEVEL = 5        # send a throttle message with value of 5 (trial and error)
  SNG_DISTANCE_THRESHOLD = 150 

  #SUBARU STOP AND GO - Pre-Global
  SNG_DISTANCE_THRESHOLD_PREGLOBAL = 3 #SnG trigger when lead car distance > 3m
  SNG_DISTANCE_LIMIT_PREGLOBAL = 4  #SnG only trigger if close distance is less than 4
  
  #SUBARU NON-EPB
  NON_EPB_STANDSTILL_THRESHOLD = 1000000000  #1 second
  NON_EPB_FAKE_SPEED = 3 #km/h

class CAR:
  ASCENT = "SUBARU ASCENT LIMITED 2019"
  IMPREZA = "SUBARU IMPREZA LIMITED 2019"
  FORESTER = "SUBARU FORESTER 2019"
  FORESTER_PREGLOBAL = "SUBARU FORESTER 2017 - 2018"
  LEGACY_PREGLOBAL = "SUBARU LEGACY 2015 - 2018"
  OUTBACK_PREGLOBAL = "SUBARU OUTBACK 2015 - 2017"
  OUTBACK_PREGLOBAL_2018 = "SUBARU OUTBACK 2018 - 2019"

FINGERPRINTS = {
  CAR.OUTBACK_PREGLOBAL_2018: [{
  # OUTBACK 2.0D 2018 ADM
    2: 8, 208: 8, 209: 4, 210: 8, 211: 7, 212: 8, 316: 8, 320: 8, 321: 8, 324: 8, 328: 8, 329: 8, 336: 2, 338: 8, 342: 8, 352: 8, 353: 8, 354: 8, 356: 8, 358: 8, 359: 8, 392: 8, 554: 8, 640: 8, 642: 8, 805: 8, 864: 8, 865: 8, 872: 8, 880: 8, 881: 8, 882: 8, 884: 8, 885: 8, 977: 8, 1614: 8, 1632: 8, 1657: 8, 1658: 8, 1672: 8, 1722: 8, 1745: 8, 1786: 5, 1787: 5, 1968: 8, 1976: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
}

STEER_THRESHOLD = {
  CAR.ASCENT: 80,
  CAR.IMPREZA: 80,
  CAR.FORESTER: 80,
  CAR.FORESTER_PREGLOBAL: 75,
  CAR.LEGACY_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL: 75,
  CAR.OUTBACK_PREGLOBAL_2018: 75,
}

DBC = {
  CAR.ASCENT: dbc_dict('subaru_global_2017_generated', None),
  CAR.IMPREZA: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER: dbc_dict('subaru_global_2017_generated', None),
  CAR.FORESTER_PREGLOBAL: dbc_dict('subaru_forester_2017_generated', None),
  CAR.LEGACY_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL: dbc_dict('subaru_outback_2015_generated', None),
  CAR.OUTBACK_PREGLOBAL_2018: dbc_dict('subaru_outback_2019_generated', None),
}

PREGLOBAL_CARS = [CAR.FORESTER_PREGLOBAL, CAR.LEGACY_PREGLOBAL, CAR.OUTBACK_PREGLOBAL, CAR.OUTBACK_PREGLOBAL_2018]
