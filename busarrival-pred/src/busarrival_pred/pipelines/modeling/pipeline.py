"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import split_data, train_model,evaluate_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["L1_route1_dataset","params:model_options"],
                outputs=["x_train_r1","x_test_r1","y_train_r1","y_test_r1"],
                name="R1_train_test_split_node"
            ),
          
            node(
                func=split_data,
                inputs=["L1_route2_dataset","params:model_options"],
                outputs=["x_train_r2","x_test_r2","y_train_r2","y_test_r2"],
                name="R2_train_test_split_node"
            ),
               node(
                func=train_model,
                inputs=["x_train_r1","y_train_r1"],
                outputs="regressor1",
                name="model_r1_node"
            ),
           
            node(
                func=train_model,
                inputs=["x_train_r2","y_train_r2"],
                outputs="regressor2",
                name="model_r2_node"
            ),
               node(
                func=evaluate_model,
                inputs=["regressor1",'x_test_r1','y_test_r1'],
                outputs="model_pred1",
                name="evaluate_model_route1"   
                ),
               node(
                func=evaluate_model,
                inputs=["regressor2","x_test_r2","y_test_r2"],
                outputs="model_pred2",
                name="evaluate_model_route2"
               )

        ])
