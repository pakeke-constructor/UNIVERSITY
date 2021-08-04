

def connection_setup_delay(cableLength_km, speedOfLight_kms, dataRate_bps,
                           messageLength_b, processingTimes_s):
    cab_del = cableLength_km / speedOfLight_kms
    mes_del = messageLength_b / dataRate_bps
    proc = processingTimes_s
    
    return (cab_del * 2 + mes_del * 2 + proc) * 2 + 2 * proc


def message_delay(connSetupTime_s, cableLength_km,
            speedOfLight_kms, messageLength_b, dataRate_bps):
    return connSetupTime_s + (2 * cableLength_km) / speedOfLight_kms + \
            messageLength_b / dataRate_bps



print(message_delay(0.2, 10_000, 200_000, 1000_000_000, 1000_000))


