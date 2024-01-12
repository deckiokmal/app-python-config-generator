from controller import ConfigController

test = ConfigController(
    "./templates/ipsecsite2site.yml",
    "./templates/ipsecsite2site.j2",
    "devices.json",
)

config_data = test.load_yaml_config()

command = test.render_template(config_data)

print(command)
