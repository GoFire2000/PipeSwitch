import os
import sys

from scripts.common.util import RunDocker

def main():
    with RunDocker('pipeswitch:ready_model', 'figure6_kill_restart_10s') as rd:
        # Start the server: ready_model
        rd.run('python PipeSwitch/scripts/run_data.py')
        
        # Get and return the data point

if __name__ == '__main__':
    main()