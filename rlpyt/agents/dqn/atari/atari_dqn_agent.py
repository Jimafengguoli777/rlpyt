
from rlpyt.agents.dqn.dqn_agent import DqnAgent
from rlpyt.models.dqn.atari_dqn_model import AtariDqnModel


class AtariDqnAgent(DqnAgent):

    def __init__(self, ModelCls=AtariDqnModel, **kwargs):
        super().__init__(ModelCls=ModelCls, **kwargs)

    def make_env_to_model_kwargs(self, env_spec):
        return dict(image_shape=env_spec.observation_space.shape,
                    output_dim=env_spec.action_space.n)