# HomeAssistant konfigurace
V tomto repozitáři můžete najít konfigurační soubory pro HomeAssistent (Hass.io), které jsem použil v seriálu na mém blogu.

## Hlavní soubory
- configuration.yaml
- security.yaml

## Články popisující konfiguraci
1. [Instalace](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-1-cast/) HomeAssistant
2. [Integrace s produkty Sonoff](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-2-cast-integrace-sonoff/)

```
switch:
    - platform: mqtt
      name: Stolni lampicka
      state_topic: "stat/sonoff/RESULT"
      value_template: '{{ value_json["POWER1"] }}'
      command_topic: "cmnd/sonoff/POWER"
      availability_topic: "tele/sonoff/LWT"
      payload_on: "ON"
      payload_off: "OFF"
      payload_available: "Aktivní"
      payload_not_available: "Neaktivní"
```

2. [Integrace s Homekit](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-3-cast-integrace-homekit/) hlasovým asistentem od Applu

```
homekit:
  # nepovinné - pouze pokud provozuje více HomeAssistentů
  name: Homekit Bridge
```