from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts, http_check


@task
def check_master():
    env.platform_family = detect.detect()

    assert file.exists("/etc/redis/master.conf"), \
        "master.conf does not exist"
    assert file.exists("/etc/redis/sentinel_cluster.conf"), \
        "sentinel_cluster.conf does not exist"
    assert port.is_listening(6379), "port 6379 is not listening"
    assert port.is_listening(26379), "port 26379 is not listening"
    assert user.exists("redis"), "user redis does not exist"
    assert group.is_exists("redis"), "group redis does not exist"
    assert process.is_up("redis-server"), "redis-server process is not up"
    assert service.is_enabled("redismaster"), "redismaster is not enabled"
    assert service.is_enabled("redis_sentinel_cluster"), \
        "redis_sentinel_cluster is not enabled"


@task
def check_slave():
    env.platform_family = detect.detect()

    assert file.exists("/etc/redis/slave.conf"), \
        "slave.conf does not exist"
    assert file.exists("/etc/redis/sentinel_cluster.conf"), \
        "sentinel_cluster.conf does not exist"
    assert port.is_listening(6379), "port 6379 is not listening"
    assert port.is_listening(26379), "port 26379 is not listening"
    assert user.exists("redis"), "user redis does not exist"
    assert group.is_exists("redis"), "group redis does not exist"
    assert process.is_up("redis-server"), "redis-server process is not up"
    assert service.is_enabled("redisslave"), "redisslave is not enabled"
    assert service.is_enabled("redis_sentinel_cluster"), \
        "redis_sentinel_cluster is not enabled"


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
