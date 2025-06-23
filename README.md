# HA Dashbutton Add-On

Mit diesem Add-On kannst du einen Amazon Dashbutton verwenden, um eine Automation in Home Assistant auszulösen.

![IMG_7051](https://github.com/user-attachments/assets/20e73f56-74ae-40e4-b64a-c8baa8ef5b86)


## Konfiguration

Im Reiter **Konfiguration** müssen folgende Werte definiert werden:

- **MAC**: MAC-Adresse des Dash Buttons
- **HA_URL**: IP-Adresse inkl. Port des Home Assistant (z. B. `http://192.168.1.10:8123`)
- **TOKEN**: Dein Long-Lived Access Token aus HA
- **ENTITY**: Die Entität der Automation, z. B. `automation.test_test`

#
**Das Add-On kann über die GitHub URL direkt im Add-on Store von Home Assistant als Repositorie eingefügt werden.** 
