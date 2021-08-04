


def connection_setup_delay(cableLength_km, speedOfLight_kms, dataRate_bps,
                           messageLength_b, processingTimes_s):
    cab_del = cableLength_km / speedOfLight_kms
    mes_del = messageLength_b / dataRate_bps
    proc = processingTimes_s
    
    return (cab_del * 2 + mes_del * 2 + proc) * 2 + 2 * proc


def message_delay(connSetupTime_s, cableLength_km,
            speedOfLight_kms, messageLength_b, dataRate_bps):
    return connSetupTime_s + cableLength_km / speedOfLight_kms + \
            messageLength_b / dataRate_bps

print ("{:.3f}".format(message_delay(0.305, 15000, 200000, 5000, 1000000)))



