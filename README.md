![Open MQTT Bridges logo](assets/logo.svg)

# Open MQTT Bridges

Open-source bridges that connect devices and services through MQTT. Find a bridge, explore its documentation, and build your own automations.

**[Explore the bridge directory](https://open-mqtt-bridges.github.io/)** · [GitHub organization](https://github.com/open-mqtt-bridges)

## Bridges

<!-- bridges:start -->
| Bridge | What it connects | Documentation | Status |
| --- | --- | --- | --- |
| [AdGuard Home](https://github.com/open-mqtt-bridges/adguardhome) | Publish DNS statistics and control network protection over MQTT. | [README](https://github.com/open-mqtt-bridges/adguardhome#readme) | Active |
| [Display](https://github.com/open-mqtt-bridges/display) | Connect monitor brightness and DDC/CI controls to your MQTT broker. | [Docs](https://open-mqtt-bridges.github.io/display/) | Active |
| [Home Connect](https://github.com/open-mqtt-bridges/homeconnect) | Bring connected home appliances into your MQTT automations. | [Docs](https://open-mqtt-bridges.github.io/homeconnect/) | Active |
| [IDM Energy](https://github.com/open-mqtt-bridges/idm-energy) | A historical MQTT integration for IDM heat-pump systems. | [README](https://github.com/open-mqtt-bridges/idm-energy#readme) | Archived |
| [Landroid](https://github.com/open-mqtt-bridges/landroid) | Connect your robotic lawn mower to MQTT-based automations. | [Docs](https://open-mqtt-bridges.github.io/landroid/) | Active |
| [Modbus](https://github.com/open-mqtt-bridges/modbus) | Bridge Modbus devices and registers to your MQTT network. | [Docs](https://open-mqtt-bridges.github.io/modbus/) | Active |
| [Philips Hue](https://github.com/open-mqtt-bridges/philips-hue) | Connect Hue lights and your MQTT lighting automations. | [Docs](https://open-mqtt-bridges.github.io/philips-hue/) | Active |
| [PocketBase](https://github.com/open-mqtt-bridges/pocketbase) | Publish collection updates as MQTT events or retained state. | [Docs](https://open-mqtt-bridges.github.io/pocketbase/) | Active |
| [Roborock](https://github.com/open-mqtt-bridges/roborock) | Connect vacuum accounts, device state and commands to MQTT. | [Docs](https://open-mqtt-bridges.github.io/roborock/) | Active |
| [WLED](https://github.com/open-mqtt-bridges/wled) | Connect multiple WLED controllers to MQTT lighting scenes. | [Docs](https://open-mqtt-bridges.github.io/wled/) | Active |
<!-- bridges:end -->

“README” links to documentation in the repository. Archived bridges are historical references and are not maintained.

## Contribute

Read the [contribution guide](https://github.com/open-mqtt-bridges/.github/blob/main/CONTRIBUTING.md), [security policy](https://github.com/open-mqtt-bridges/.github/blob/main/SECURITY.md), and [code of conduct](https://github.com/open-mqtt-bridges/.github/blob/main/CODE_OF_CONDUCT.md). Each repository retains its own license, toolchain and MQTT contract.

## Organization maintenance

This repository owns shared community defaults, the organization profile and branding. Website source and the authoritative bridge catalog live in [open-mqtt-bridges.github.io](https://github.com/open-mqtt-bridges/open-mqtt-bridges.github.io).

See the [readiness audit](docs/readiness-audit.md), [development and Spec Kit guide](docs/development.md), and [brand assets](assets/README.md). Run `python3 scripts/check-community.py` to validate this repository. Catalog synchronization commands are documented in the website repository.
