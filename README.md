# Solving farmers Dilemma Puzzle with random walk and monte carlo simulation
TLDR; To see this simulation in action please visit <br>
https://nbviewer.jupyter.org/ <br>
and provide this link to render <br>
https://github.com/ravipawase/farmersDilemmaPuzzle/blob/master/show_simulation.ipynb <br>

### The puzzle <br>
Everyone must have come across this puzzle sometime, where we need to help farmer cross a river with his belonging; which are wolf goat and cabbage. There is boat avaialble though it can only have two things onboard i.e. farmer himself and one more thing from his stuff. To complecate the affairs we can not leave the combinations of things unattend such as Wolf and Goat and Goat and Cabbage. If this kept unattended wolf will eat goat and goat will finish Cabbage.<br>

We can take advise from [XKCD](https://xkcd.com/1134/) and solve the problem for once and all!<br>

### Stratergy <br>
Now, to solve this puzzle we can think successively what actions to take, undoing the action if results into a Goat being eaten by Wolf or Goat eating Cabbage. This is not difficult, with some efforts we can find out the sequence and we have a solution. But let us say we need to solve it by a computer program, what will be our stratergy then?<br>

We can actually ask computer to take these actions successively only we have following problems<br>
1. Computers cannot take decision on their own.<br>
2. Computer will not know the result of each action, whether it resulted into sucess or failure etc.<br>

So, to solve this problem we can take inspirations and use bits and parts from follwing two concepts / field of studies. <br>
1. Random walk:<br>
As described on wikipedia, a random walk is a mathematical object, known as a stochastic or random process, that describes a path that consists of a succession of random steps on some mathematical space such as the integers. <br>
2. Reinforcement Learning :<br>
As describe on wikipedia, Reinforcement learning (RL) is an area of machine learning, inspired by behaviorist psychology, concerned with how software agents ought to take actions in an environment so as to maximize some notion of cumulative reward.<br>
<br>

### Implementation <br>
So to use these concepts we need to set up an environment and define the interaction of agent with it. In our case environment is a computers ability to keep track of all the elemnets in problem like Farmer, Wolf, Goat, Cabbage; where they are, like on bank1, bank2 or boat. Where the boat itself is. It also includes the ability to chnage these states like taking a goat from bank1 and putting it into boat which is parked on the same bank and so on. This can be done by defining a class which has all these attributes and methods to change the values/states of these attributes<br>
To set up interaction of agent with environment, after a certain action is taken cab be accomplished by a method of such a class in which rules are coded to check if the current state of environment results into a failure or sucees.<br>
In this way once we have set upped the environment the question remain about the action taken by the agent on its own. Here we can follow a philosophy of random walk and can decide randomly what action to take, in our case it would be whether to board/deboard someone or not if yes which out of the available options. This will be done by choosing one of the avaailable option randomly.<br>

Once we have an environment and interaction of agent with environment set upped we can define a flow of simulation and during this flow actions will be taken randomly and after every action sucess or failure will be evaluated. The simulation will run untill a failure or sucess is encountered. So any indivisual simulation can be resulted into a success or failure. To solve the problem we can repeat the simulation untill we get a sucess.<br>

### Viewing it in action <br>
To see simulation in action, run the [show_simulation.ipynb](https://github.com/ravipawase/farmersDilemmaPuzzle/blob/master/show_simulation.ipynb) notebook locally or nbviever as described above, since github cannot render dynamic notebooks.

### Results <br>




