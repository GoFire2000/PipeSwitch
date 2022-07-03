# Get current work dir
WORK_DIR=$(pwd)/PipeSwitch-main

# Import global variables
source $WORK_DIR/scripts/config/env.sh

PYTHONPATH=$PYTHONPATH:$WORK_DIR python $WORK_DIR/scripts/figures/figure6/ready_model_2s/remote_run_data.py