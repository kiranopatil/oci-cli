# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from services.mysql.src.oci_cli_mysqlaas.generated import mysqlaas_cli
from services.mysql.src.oci_cli_mysql.generated import mysql_service_cli

# oci mysql mysqlaas instance -> oci mysql instance
mysql_service_cli.mysql_service_group.commands.pop(mysqlaas_cli.mysqlaas_root_group.name)
mysql_service_cli.mysql_service_group.add_command(mysqlaas_cli.shape_group)
mysql_service_cli.mysql_service_group.add_command(mysqlaas_cli.configuration_group)
mysql_service_cli.mysql_service_group.add_command(mysqlaas_cli.version_group)
