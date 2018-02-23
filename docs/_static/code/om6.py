import t_infinity_python_bindings as infinity
import json
import sys

runtime = infinity.RunTime(sys.argv[1])
comm = runtime.getDomainCommunicator()
mesh = runtime.getDomainMesh()
solver = runtime.getFluidSolver(mesh, comm)

solver.solve()

density = solver.field("density")
x_velocity = solver.field("u")
y_velocity = solver.field("v")
z_velocity = solver.field("w")
pressure = solver.field("pressure")


name = "om6viscous-surface-by-tags"

viz_creator = runtime.getVizPlugin()
selection_type = "surface-by-tags"
options = {"tags":[2]}

viz = viz_creator.createViz(selection_type,json.dumps(options),name,mesh,comm)
viz.addField(density)
viz.addField(x_velocity)
viz.addField(y_velocity)
viz.addField(z_velocity)
viz.addField(pressure)
viz.visualize()
