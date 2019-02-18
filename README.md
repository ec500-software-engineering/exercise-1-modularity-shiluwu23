# EC500

## exercise-1-modularity-Shilu Wu

## Health Monitor System
This system consists of Input module, storage module, AI module, Alert module and User Interface module.
Input module receives data from three txt documents. Storage module receives data from Input module.

## Architecture Diagram
![](https://github.com/ec500-software-engineering/exercise-1-modularity-shiluwu23/blob/master/Health_Monitor_system_diagram.png)
## To start
Run the threading_main.py to start the multithreading task.
## User Interface
User Interface module is my individual task. This module receives alert flags from Alert module and shows information to users.
## Pros and Cons
By simply running the threading_main.py file we could integrate the several modules and implement the function of the whole system. It's easy to handle.

Data is analyzed to be normal or abnormal but our system don't give a health condition prediction to users regarding the data received.
## Favorable Improvements
The input data could be come from database instead of being input manually in txt files.
