"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import split_data,lag_values


def create_pipeline(**kwargs) -> Pipeline:
     return pipeline([
          node(
                func=split_data,
                inputs="raw_bus_data",
                outputs=["route1_dataset","route2_dataset"],
                name="split_by_route_node"
            ),
            node(
                func=lag_values,
                inputs=["route1_dataset"],
                outputs="L1_route1_dataset",
                name="R1_Lag_value_node"
            ),
            node(
                func=lag_values,
                inputs=["route2_dataset"],
                outputs="L1_route2_dataset",
                name="R2_Lag_value_node"
            )
    ])
