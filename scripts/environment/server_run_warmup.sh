# Get current work dir
WORK_DIR=$(pwd)/PipeSwitch-main

# Import global variables
source $WORK_DIR/scripts/config/env.sh

PYTHONPATH=$PYTHONPATH:$WORK_DIR python3 $WORK_DIR/scripts/environment/server_run_warmup.py