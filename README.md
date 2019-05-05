# HomeAssistant + ESPHome konfigurace

V tomto repozitáři můžete najít konfigurační soubory pro [Home Assistant](https://home-assistant.io/) (Hass.io), které jsem použil v seriálu na mém [blogu](https://blog.vyoralek.cz).

Jako integrační platformy používám:

- [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota) - napojení na HomeAssistant pomocí prostředníka MQTT. Velká množina podporovaných produktů zejména od firmy Sonoff.
- [ESPHome](https://esphome.io/) - přímé napojení na HomeAssistant. Zatím chudší dokumentace a příklady.

Home-Assistant (Hass.io) mám nainstalovaný na [NanoPi M4](http://s.click.aliexpress.com/e/cnx5OdvQ) (dříve [Orange Pi Zero Plus2](http://www.orangepi.org/OrangePiZeroPlus2)) v dockeru na operačním systému Ubuntu 18.04 LTS. Kompletní návod je v [první části](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-1-cast/) seriálu.

## Konfigurační soubory

### HomeAsisstant (Hass.Io)

- [configuration.yaml](home-assistant/configuration.yaml) - hlavní konfigurační soubor
- [customize.yaml](home-assistant/customize.yaml) - přejmenovávání a ikonky pro uživatelské rozhraní
- security.yaml - není obsažen v tomto repozitáři. Zde ukládejte své hesla a vaše soukromé nastavení
- [group.yaml](home-assistant/group.yaml) - seskupování prvků do skupin použité v uživatelském rozhraní

### EspHome (ESP2866/ESP32)

- [Sonoff Basic](esphome/sonoff-basic.yaml) (k dostání na [AliExpressu](https://blog.vyoralek.cz/go/aliexpress-sonoff-basic/), [Banggood](https://blog.vyoralek.cz/go/bangood-sonoff-basic/))
- [Sonoff S20](esphome/sonoff-s20.yaml) (k dostání na [AliExpressu](https://blog.vyoralek.cz/go/aliexpress-sonoff-s20/) nebo novější model S26 na [AliExpressu](https://blog.vyoralek.cz/go/aliexpress-sonoff-s26/), [Banggood](https://blog.vyoralek.cz/go/bangood-sonoff-s26/))
- [Sonoff TH10](esphome/sonoff-th10.yaml) (se sensorem DS18B20, k dostání na [AliExpressu](http://s.click.aliexpress.com/e/SR7soQU)
- [Sonoff POW R2](esphome/sonoff-pow-r2.yaml) (k dostání na [AliExpressu](http://s.click.aliexpress.com/e/eqTCSpS), [Banggood](https://blog.vyoralek.cz/go/banggood-sonoff-pow-r2/))
- [Sonoff Touch](esphome/sonoff-touch.yaml) (k dostání na [AliExpressu](http://s.click.aliexpress.com/e/cMT8oOFI))
- [Sonoff 4ch](esphome/sonoff-4ch.yaml) (k dostání na [AliExpressu](http://s.click.aliexpress.com/e/zh7pyOy))
- [Wemos D1 mini](esphome/wemos-d1-mini.yaml) (k dostání na [AliExpressu](http://s.click.aliexpress.com/e/bQC4hpk4)) se sensory BME280 ([AliExpress](http//s.click.aliexpress.com/e/cdOOdbeu)) a SHT31 ([AliExpress](http://s.click.aliexpress.com/e/cmg8TZtO)) a displejem SSD1306 I2C ([AliExpress](http://s.click.aliexpress.com/e/yxcX9Fi))
- [ZINUO Magic Home RGBW](esphome/magichome-led-rgbw.yaml) (k dostání na [AliExpressu](http://s.click.aliexpress.com/e/c7R7uLXE))
- [Bliztwolf BW-SHP2](esphome/blitzwolf-shp2.yaml) (k dostaní na [AliExpressu](https://blog.vyoralek.cz/go/aliexpress-blitzwolf-bw-shp2/), [Banggood](https://blog.vyoralek.cz/go/banggood-blitzwolf-bw-shp2/))]

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

### 6. [Integrace se Sonoff produkty pomocí ESPHome](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-5-cast-sonoff-esphome/)

#### ESPHome konfigurační soubory

- Sonoff Basic - [konfigurace](esphome/sonoff-basic.yaml)
- Sonoff S20 - [konfigurace](esphome/sonoff-s20.yaml)
- Sonoff TH10 - [konfigurace](esphome/sonoff-th10.yaml)
- Sonoff Touch - [konfigurace](esphome/sonoff-touch.yaml)
- Sonoff 4CH - [konfigurace](esphome/sonoff-4ch.yaml)

Seskupování v HomeAssistentovi jako v části 4 a 5.

### 7. [Integrace se Sonoff produkty pomocí ESPHome 2](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-7-cast-sonoff-pow-esphome/)

- Sonoff POW R2 - [konfigurace](esphome/sonoff-pow-r2.yaml)

Seskupování v HomeAssistentovi jako v části 4 a 5.

### 8. [Integrace s LED ovladačem MagicHome pomocí ESPHome](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-8-cast-led-esphome/)

- Magic Home LED controller - [konfigurace](esphome/magichome-led-rgbw.yaml)

### 9. [Integrace Zigbee s Xiaomi Gateway](https://blog.vyoralek.cz/iot/centrum-chytre-domacnosti-homeassistant-hass-io-9-cast-integrace-zigbee-xiaomi-mijia-a-aqara/)

### 10. [Integrace a stavba vlastní Zigbee Gateway](https://blog.vyoralek.cz/iot/vlastni-zigbee-gateway/)