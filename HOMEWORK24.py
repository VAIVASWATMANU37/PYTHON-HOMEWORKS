class JDM:
    def E(self):
        pass
class SUPRA_MK4(JDM):
    def E(self):
        return "SUPRA_MK4: 3.0 L TWIN-TURBO INLINE-6"
class SKYLINE_GTR_BNCR34_NISMO_ZTUNE(JDM):
    def E(self):
        return "SKYLINE_GTR_BNCR34_NISMO_ZTUNE: 2.6L TWIN-TURBO INLINE-6"
class RX7_FD(JDM):
    def E(self):
        return "Pagani: 1.3L TWIN-TURBO 2-ROTOR"
class TRUENO_AE86(JDM):
    def E(self):
        return "2.0L TWIN-TURBO INLINE-4"
class CIVIC_TYPE_R_G1(JDM):
    def E(self):
        return "2.0L TWIN-TURBO INLINE-4"
def P(cars):
    for car in cars:
        print(car.engine_sound())
J = [SUPRA_MK4(), SKYLINE_GTR_BNCR34_NISMO_ZTUNE(), RX7_FD(), TRUENO_AE86(), CIVIC_TYPE_R_G1()]
P(J)