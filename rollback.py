__author__ = 'aiguoxin'

import argparse
from fabric.contrib.files import *
from fabric.api import *
from fabric.decorators import parallel, task
from FabJetty import *
from fabric.colors import *
import StringIO
import sys
from fabric.tasks import execute
from ServerList import *


class Parameter:
    def __init__(self, ):
        parser = argparse.ArgumentParser()
        parser.add_argument('--area', metavar='/'.join(machine_list.keys()), type=str, nargs=1,
                            help='the location of server room')
        parser.add_argument('--host', metavar='/'.join(machine_list.keys()), type=str, nargs=1, help='server ip')
        parser.add_argument('--version', metavar='roll back version', type=str, nargs=1,
                            help='roll back to version')
        self.host = None
        self.tag = None
        self.version = None
        if len(sys.argv) == 1:
            parser.parse_args(" ")
        args = parser.parse_args()
        if args.area is not None:
            if args.area[0] not in machine_list.keys():
                parser.parse_args(" ")
            self.area = args.area[0]

        if args.host is not None:
            self.host = args.host[0]

        if args.version is not None:
            self.version = args.version[0]


def roll_back(area, host, version):
    if area is not None:
        host_list = machine_list[area]
    else:
        host_list = host.split(',')
    roll_back_parallel(area, host_list, version)


def roll_back_parallel(area, host_list, version):
    # 1.put host into group by resource
    host_dict = {}
    for host in host_list:
        resource_key = host_resource_group(area, host)
        host_dict.setdefault(resource_key, []).append(host)

    # 2.parallel to handle host by group
    for deploy_host_list in host_dict.values():
        env.user = 'root'
        env.hosts = deploy_host_list
        resource_key = host_resource_group(area, deploy_host_list[0])
        env.resources = RESOURCE_DATA[resource_key]
        env.parallel = True
        env.warn_only = True
        out_dict = execute(roll_back_task, version)
        for host, (out, status) in out_dict.items():
            print "=" * 10, host, " roll back ", status, "=" * 10
            print out.getvalue()


@task
@parallel(pool_size=1)
def roll_back_task(version):
    output = StringIO.StringIO()
    artifactId = Utils.getArtifactId('../pom.xml')
    version_file = '/data/backup/' + artifactId + '_' + version + '.war'
    if exists(version_file):
        run('rm -fr /usr/local/jetty/webapps/*')
        if run('cd /usr/local/jetty/webapps/ && ln -s ' + version_file + ' ' + artifactId + '.war').succeeded:
            execute(jetty_restart)
            output.write(green(env.host_string + " roll back success"))
            status = "succeeded"
    else:
        output.write(red(env.host_string + ":" + version_file + " not exist, roll back failed"))
        status = "failed"
    return (output, status)


if __name__ == '__main__':
    parameter = Parameter()
    if parameter.version is None:
        print("please input version, try again")
        exit()
    else:
        roll_back(parameter.area, parameter.host, parameter.version)