from controller import ConfigController


controller = ConfigController(
    "./templates/ngfw_default.yml", "./templates/ngfw_default.j2", "devices.json"
)
controller.configure_routers()
