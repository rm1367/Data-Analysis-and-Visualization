import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

class Runner:
    def __init__(self, args):

        #creating arguments to pass to the command-line function
        self.file_name = args[0]
        self.index_col = args[1]
        self.start_date = args[2]
        self.end_date = args[3]
        self.start_col = args[4]
        self.end_col = args[5]
        
    def run(self):
        # data variable set to read and load csv file
        data = pd.read_csv(self.file_name, index_col=self.index_col)
        
        # creating data2 variable to filter the data by start and end date
        data2 = data.loc[self.start_date:self.end_date]
        
        # creating data3 to filter data further and set the column ranges
        data3 = data2.loc[:, self.start_col:self.end_col]

        sd3_1 = data3[[self.start_col]] #filtering date for plotting
        sd3_2 = data3[[self.end_col]] #filtering data for plotting
        sd3_3 = data3[self.start_col] - data3[self.end_col] #created series to calculate difference
        
        fig, (ax1,ax2,ax3) = plt.subplots(3,1,facecolor='0.75',linewidth=3,edgecolor='Red')
        sd3_1.plot(ax=ax1,xticks=range(0,len(data2),25), rot = 25, grid = True, xlabel='Date',ylabel='Price')
        sd3_2.plot(ax=ax2,xticks=range(0,len(data2),25), rot = 25, grid = True, color = 'orange',
                   xlabel='Date',ylabel='Price')       
        sd3_3.plot(ax=ax3,xticks=range(0,len(data2),25), rot = 25, grid = True, label ='Difference', color =
                   'green', xlabel='Date',ylabel='Price')
        ax3.legend()
        
        #passing arguments to the plot suptitle
        fig.suptitle(f"args = ['{self.file_name}','{self.index_col}','{self.start_date}','{self.end_date}','{self.start_col}','{self.end_col}']")
        

        print('I certify that this program is my own work\n'
             'and is not the work of others. I agree\n'
             'not to share my solution with others.\n'
             'Ryan Maldonado')
        
        plt.tight_layout()
        fig.savefig("Proj10.jpg")
        plt.show()
    
