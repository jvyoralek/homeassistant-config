# HomeAssistant + ESPHome konfigurace

V tomto repozitáři můžete najít konfigurační soubory pro [Home Assistant](https://home-assistant.io/) (Hass.io), které jsem použil v seriálu na mém [blogu](https://blog.vyoralek.cz).

Jako integrační platformy používám:

- [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota) - napojení na HomeAssistant pomocí prostředníka MQTT. Velká množina podporovaných produktů zejména od firmy Sonoff.
- [ESPHome](https://esphomelib.com/esphomeyaml/index.html) - přímé napojení na HomeAssistant. Zatím chudší dokumentace a příklady.

Home-Assistant mám nainstalovaný na [Orange Pi Zero Plus2](http://www.orangepi.org/OrangePiZeroPlus2) v dockeru na operačním systému Ubuntu 18.04 LTS. Kompletní návod je v [první části](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-1-cast/) seriálu.

## Konfigurační soubory

### HomeAsisstant

- [configuration.yaml](home-assistant/configuration.yaml) - hlavní konfigurační soubor
- [customize.yaml](home-assistant/customize.yaml) - přejmenovávání a ikonky pro uživatelské rozhraní
- security.yaml - není obsažen v tomto repozitáři. Zde ukládejte své hesla a vaše soukromé nastavení
- [group.yaml](home-assistant/security.yaml) - seskupování prvků do skupin použité v uživatelském rozhraní

### EspHome

- TBD

## Seriál článků na blogu popisující konfiguraci

### 1. [Instalace](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-1-cast/) HomeAssistant

### 2. [Integrace s produkty Sonoff](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-2-cast-integrace-sonoff/)

```yaml
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

### 3. [Integrace s Homekit](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-3-cast-integrace-homekit/) hlasovým asistentem od Applu

```yaml
homekit:
  # nepovinné - pouze pokud provozuje více HomeAssistentů
  name: Homekit Bridge
```

### 4. [Integrace s produkty Sonoff - 2. část](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-4-cast-integrace-sonoff-2//)

#### Definice sensorů

```yaml
- platform: mqtt
  name: "room1_table_lamp_energy_today"
  state_topic: "tele/sonoff/SENSOR"
  value_template: ' {{ value_json["ENERGY"]["Today"] }}'
  unit_of_measurement: "kWh"
...
```

#### Seskupování

```yaml
sonoff:
  name: "Lampička"
  control: hidden
  entities:
    - light.room1_table_lamp
    - sensor.room1_table_lamp_energy_voltage
    - sensor.room1_table_lamp_energy_power
    - sensor.room1_table_lamp_energy_current
    - sensor.room1_table_lamp_energy_today
    - sensor.room1_table_lamp_energy_yesterday
    - sensor.room1_table_lamp_energy_total
```

#### Úprava vzhledu - názvy a ikonky

```yaml
light.room1_table_lamp:
  friendly_name: "Stolní lampička"
  icon: mdi:lamp
...
```

### 5. [Integrace s Wemos D1 Mini a sensory BME280 a SHT31](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-5-cast-wemos-d1-bme280-a-sht31/)

Stejný způsob definice, seskupování a úpravy vzhledu senzorů jako v přechozí 4. části.