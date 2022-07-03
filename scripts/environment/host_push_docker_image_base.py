import os
import sys

from scripts.common.util import RunRemoteRepo, import_server_list

def main():
    print('here ok')
    server_list_path = sys.argv[1]
    image_path = sys.argv[2]
    print (server_list_path)
    print (image_path)

    server_list = import_server_list(server_list_path)
    print(server_list)
    for server in server_list:
        src = image_path
        dst = server['id'] + ':~/'
        
        
        print ('%s> Copy docker image for base' % server['id'])
        os.system('chmod a+rwx %s'%src)
        
        os.system('scp %s %s' % (src, dst))
        print ('%s> Complete copying docker image for base' % server['id'])

        print ('%s> Load docker image for base' % server['id'])
        print('here push ok1')
        with RunRemoteRepo(server, 'dev') as rrr:
            rrr.run("bash /home/yangx/PipeSwitch-main/scripts/environment/server_load_docker_image_base.sh")
            print('here push ok2')
        print('here push ok3')
        print ('%s> Complete loading docker image for base' % server['id'])

        

if __name__ == '__main__':
    main()