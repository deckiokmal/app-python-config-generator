from controller import ConfigController

data = ConfigController(
    "./templates/bsg_type_e.yml",
    "./templates/bsg_type_e.j2",
    "devices.json",
)

config_data = data.load_yaml_config()

command = data.render_template(config_data)

print(command)
