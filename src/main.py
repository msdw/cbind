# Check that all modules needed are put in your requirements.txt file
 
import pandas as pd
import argparse
from pathlib import Path



if __name__ == '__main__':
    # Test your component
    # By executing your script with a python main [ARGS]

    # Put meaningful description and args for your user
    parser = argparse.ArgumentParser(description='Add Python Script')
    
    # do not use positionnal argument, always use the --arg syntax
    # note all the args name are they must be reported in the yaml component file
    parser.add_argument('--src1', required=True, type=str, help='Path of the local file containing the Input data 1.')
    parser.add_argument('--src2', required=True, type=str, help='Path of the local file containing the Input data 2.')    
    parser.add_argument('--dst', required=True, type=str, help='Path of the local file for output data.')

        

    args = parser.parse_args()
    src1 = args.src1
    src2 = args.src2
    dst=args.dst

    df1 = pd.read_csv(src1)
    df2 = pd.read_csv(src2)
    try:
        df=pd.concat([df1,df2],axis=1,ignore_index=True)
        # if you save some data , your component must create the output path
        # Even if a file as pipeline may required to create a temp path
        Path(dst).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(dst, index=False)     
        print("cbind successful")   
    except:
        print("cbind is not possible because the 2 dataframes don't contains exactly the same number of rows.")
    


