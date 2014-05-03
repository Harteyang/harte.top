from fabric.api import env
import fabric.contrib.project as project

env.hosts = ["192.81.133.96"]
env.user = "root"
env.colorize_errors = True
env.local_output = "_site/"
env.remote_output = "/opt/blog.tankywoo.com/"

def deploy():
    project.rsync_project(
        local_dir = env.local_output,
        remote_dir = env.remote_output.rstrip("/") + "/",
        delete =True
    )
