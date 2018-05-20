import networkx as nx
import numpy as np
import json
from ndlib.models.ModelConfig import Configuration
from ndlib.models.CompositeModel import CompositeModel
from ndlib.models.compartments.NodeStochastic import NodeStochastic

g1 = nx.erdos_renyi_graph(n=300, p=0.1)
SIR = CompositeModel(g1)
SIR.add_status('Susceptible')
SIR.add_status('Infected')
SIR.add_status('Removed')
c1 = NodeStochastic(triggering_status='Infected', rate=0.1, probability=1, name="None")
c2 = NodeStochastic(rate=0.1, probability=1, name="None")
SIR.add_rule('Susceptible', 'Infected', c1)
SIR.add_rule('Infected', 'Removed', c2)
config = Configuration()
config.add_model_parameter('percentage_infected', 0.1)
SIR.set_initial_status(config)
iterations = SIR.iteration_bunch(100, node_status=False)
res = json.dumps(iterations)
print(res)
