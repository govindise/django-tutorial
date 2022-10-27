myList = [4, 2, 'a', 'x', 7, 'k', 2, 'y', 8]
asciiList = [ ascii(x) if type(x) == int else x for x in myList]
asciiList = sorted(asciiList)

import pandas as pd
policy_file_df = pd.read_table('C:\\Users\\govindaraju.seethara\\Downloads\\113_CRG_POLICY_JUN_2022.dat', sep=',,', low_memory=True, na_filter=False, dtype=str)