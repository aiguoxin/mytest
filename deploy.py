import urllib2
import argparse
from fabric.api import run, put, env
from fabric.decorators import parallel, task
from fabric.utils import abort
import time
import StringIO
from FabJetty import *
from fabric.colors import *
import sys
from fabric.tasks import execute
from ServerList import *


class PropertiesFileChecker:
    @staticmethod
    def __load_file(file):
        key_set = set()
        with open(file) as fp:
            for line in fp:
                line = line.strip()
                line = line.replace(' ', '')
                if len(line) == 0:
                    continue
                if line[0] == '#':
                    continue
                items = line.split('=')
                if len(items) != 2:
                    continue
                key_set.add(items[0])
        return key_set

    @staticmethod
    def __do_check(file1, file2):
        key_set1 = PropertiesFileChecker.__load_file(file1)
        key_set2 = PropertiesFileChecker.__load_file(file2)
        if key_set2 != key_set1:
            print key_set1 - key_set2
            print key_set2 - key_set1
        return key_set1 == key_set2

    @staticmethod
    def check():
        if not PropertiesFileChecker.__do_check('../src/main/resources/jiyang_config.properties',
                                                '../src/main/resources/config.properties'):
            abort("jiyang_config.properties and config.properties miss match")
        if not PropertiesFileChecker.__do_check('../src/main/resources/shanghai_config.properties',
                                                '../src/main/resources/config.properties'):
            abort("shanghai_config.properties and config.properties miss match")
        if not PropertiesFileChecker.__do_check('../src/main/resources/beijing_dianxin_config.properties',
                                                '../src/main/resources/config.properties'):
            abort("beijing_dianxin_config.properties and config.properties miss match")
        if not PropertiesFileChecker.__do_check('../src/main/resources/beijing_liantong_config.properties',
                                                '../src/main/resources/config.properties'):
            abort("beijing_liantong_config.properties and config.properties miss match")
        if not PropertiesFileChecker.__do_check('../src/main/resources/test_dev_config.properties',
                                                '../src/main/resources/config.properties'):
            abort("test_dev_config.properties and config.properties miss match")


def check_version(host, version, ifsleep):
    if ifsleep:
        for k in range(10):
            time.sleep(30)
            result = urllib2.urlopen('http://' + host + ':8080/video/2.0/version', None, 7200).read()
            server_version = result.strip()
            if version == server_version:
                return True
    else:
        result = urllib2.urlopen('http://' + host + ':8080/video/2.0/version', None, 7200).read()
        server_version = result.strip()
        if version == server_version:
            return True
    print "server version = " + server_version
    print "svn checkout   = " + version
    return False


def hosts_prod_one(area, host_ip):
    # PropertiesFileChecker.check()
    env.user = 'root'
    env.hosts = [
        host_ip
    ]
    if area in RESOURCE_DATA:
        env.resources = RESOURCE_DATA[area]
    else:
        ip_items = host_ip.split(".")
        ip_area_key = '.'.join(ip_items[:2])
        env.resources = RESOURCE_DATA[ip_area_key]


class Parameter:
    def __init__(self, ):
        parser = argparse.ArgumentParser()
        parser.add_argument('--area', metavar='/'.join(machine_list.keys()), type=str, nargs=1,
                            help='the location of server room')
        parser.add_argument('--host', metavar='/'.join(machine_list.keys()), type=str, nargs=1, help='server ip')
        parser.add_argument('--operation', metavar='deploy/put_script/roll_back', type=str, nargs=1,
                            help='the operation name deploy/put_script/roll_back')
        parser.add_argument('--version', metavar='svn version', type=str, nargs=1,
                            help='the svn version (must provide this parameter if operation=deploy)')
        parser.add_argument('--deploy', metavar='deploy way,S represents serial, P represents parallel', type=str,
                            nargs=1,
                            help='the parallel deploy (not must provide , default serial)')

        self.host = None
        self.tag = None

        if len(sys.argv) == 1:
            parser.parse_args(" ")
        args = parser.parse_args()
        if args.area is not None:
            if args.area[0] not in machine_list.keys():
                parser.parse_args(" ")
            self.area = args.area[0]

        if args.host is not None:
            self.host = args.host[0]

        if args.operation[0] not in ['deploy', 'put_script']:
            parser.parse_args(" ")
        self.operation = args.operation[0]

        if self.operation == 'deploy' and args.version is None:
            parser.parse_args(" ")
        if args.version is not None:
            self.version = args.version[0]

        if args.deploy is not None:
            self.deploy = args.deploy[0]
        else:
            self.deploy = 'N'


def deploy_package(area, host, version, deploy):
    print(green('start to mvn package...'))
    execute(package)
    sys.stdout.flush()
    sys.stderr.flush()
    if area is not None:
        host_list = machine_list[area]
    else:
        host_list = host.split(',')
    if cmp("P", deploy.strip().upper()) == 0:
        # deploy_package_parallel
        print(green('start to deploy by parallel...'))
        deploy_package_parallel(area, host_list, version)
    else:
        # deploy_package_serial
        print(green('start to deploy by serial...'))
        deploy_package_serial(area, host_list)


def deploy_package_serial(area, host_list):
    for host in host_list:
        hosts_prod_one(area, host)
        execute(copy_dependencies)
        execute(deploy)
        execute(jetty_restart)
        sys.stdout.flush()
        sys.stderr.flush()


def deploy_package_parallel(area, host_list, version):
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
        out_dict = execute(deploy_task, version)
        for host, (out, status) in out_dict.items():
            print "=" * 10, host, "=" * 10
            print out.getvalue()


@task
@parallel(pool_size=5)
def deploy_task(version):
    output = StringIO.StringIO()
    execute(copy_dependencies)
    output.write(green("copy_dependencies success\n"))
    deploy_link(version)
    output.write(green("deploy success\n"))
    execute(jetty_restart)
    output.write(green("jetty restart success"))
    return (output, "ok")


def deploy_link(version):
    artifactId = Utils.getArtifactId('../pom.xml')
    run('mkdir -p /data/logs/jetty')
    run('mkdir -p /data/' + artifactId)
    run('mkdir -p /data/backup')
    if hasattr(env, 'resources'):
        for (src, dst) in env.resources:
            put(src, dst)
    version_file = '/data/backup/' + artifactId + '_' + version + '.war'
    link_file = '/data/backup/' + artifactId + '.war'
    put('../target/' + artifactId + '.war', version_file)
    run('rm -fr /usr/local/jetty/webapps/* '+link_file)
    run('cp '+version_file+' '+link_file)
    if run('cd /usr/local/jetty/webapps/ && ln -s ' + link_file + ' ' + artifactId + '.war').succeeded:
        execute(jetty_restart)
        print green(env.host_string + " deploy succeeded")
    else:
        print red(env.host_string + " deploy failed")


def upload_scripts(area, host):
    if area is not None:
        host_list = machine_list[area]
    else:
        host_list = [host]
    for host in host_list:
        hosts_prod_one(area, host)
        # execute(put_script)
        execute(copy_dependencies)
    pass


if __name__ == '__main__':
    parameter = Parameter()
    if parameter.operation == 'deploy':
        deploy_package(parameter.area, parameter.host, parameter.version, parameter.deploy)
    elif parameter.operation == 'put_script':
        upload_scripts(parameter.area, parameter.host)
