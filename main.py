"""
Main module for back-end service.
"""

import os
from controller.host_service import Host
from project_secrets import Hidden

if __name__ == '__main__':
    Hidden.set_project_folder(os.getcwd())
    server = Host()
    server.run()
