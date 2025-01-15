# CSC_5RO11 - Apprentissage pour la robotique

Author: Mateus GALVÃO

E-mail: mateus.galvao@ensta-paris.fr

## Homework 1

For this first task, we were asked to create the `Telephone Game`. To achieve this, each node was defined as a `publisher` to send the message to the next node (or back to the first in the case of node D) and as a `subscriber` to receive the message from the previous node (or from the last one in the case of node A). This way, each node can connect to two `topics`, the one for the next node and the one for the previous node.

Node A initiates the communication with the message `"Message accessed by: A"`, showing that only it had access to the message, which is then sent to node B. Node B will print the received message and add that it also accessed the message by appending `"+B"`. The same process is followed by the subsequent nodes, with each node appending its identifier (e.g., "A+B+C") to show it has accessed the message, until the message returns to node A, which will print the received message as `"Message accessed by: A+B+C+D"`.

To pass the message from the `callback` function to the one that will publish it to the next topic, a global variable is needed so that all functions have access to the received message.

Regarding the topics, both the node sending the message and the one receiving it need to communicate using the same topic, meaning they need to have the same name. For example, when communicating from A to B, A is defined as a publisher and B as a subscriber, both using the `topic_A_to_B`, and this is repeated for the other pairs of nodes.

The folder structure is as follows:

```
homework_mateus/
├── CMakeLists.txt
├── build/
├── devel/
└──src/
    └── homework_1/
        ├── CMakeLists.txt
        ├── package.xml
        └── src/
            ├── node_A.py
            ├── node_B.py
            ├── node_C.py
            └── node_D.py     
```