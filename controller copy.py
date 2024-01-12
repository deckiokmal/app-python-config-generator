import json
import paramiko
import threading
import yaml
from jinja2 import Environment, FileSystemLoader
from paramiko import SSHClient


class Router:
    def __init__(self, ip, username, password, port):
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port


def connect_to_router(router, command):
    try:
        ssh_client: SSHClient = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            router.ip,
            username=router.username,
            password=router.password,
            port=router.port,
        )

        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        print(f"Informasi dari {router.ip}:\n{output}")

    except Exception as e:
        print(f"Terjadi kesalahan saat terhubung ke {router.ip}: {str(e)}")
    finally:
        ssh_client.close()


class ConfigController:
    def __init__(self, yaml_config_file, template_file, json_device_file):
        self.yaml_config_file = yaml_config_file
        self.template_file = template_file
        self.json_device_file = json_device_file

    def load_yaml_config(self):
        with open(self.yaml_config_file, "r") as config_file:
            return yaml.safe_load(config_file)

    def render_template(self, config_data):
        env = Environment(loader=FileSystemLoader(""))
        template = env.get_template(self.template_file)
        return template.render(config_data)

    def load_json_device_data(self):
        with open(self.json_device_file, "r") as json_file:
            return json.load(json_file)

    def configure_routers(self):
        config_data = self.load_yaml_config()
        command = self.render_template(config_data)
        router_data = self.load_json_device_data()

        threads = []
        for router_info in router_data["routers"]:
            router = Router(
                router_info["ip"],
                router_info["username"],
                router_info["password"],
                router_info["port"],
            )
            thread = threading.Thread(
                target=connect_to_router, args=(router, command)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()


if __name__ == "__main__":
    controller = ConfigController("config_mk.yml", "devices.json", "template_mk.j2")
    controller.configure_routers()
