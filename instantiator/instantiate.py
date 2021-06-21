# %%
import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig

from segfactory import SegFactory


@hydra.main(config_path="../configs", config_name="config")
def my_app(cfg: DictConfig) -> None:

    model = instantiate(cfg.model.model, _convert_="all")
    optim_getter = instantiate(cfg.optim.optimizer, _convert_="all")
    dataloader_train = instantiate(cfg.data.dataloader_train, _convert_="all")
    dataloader_val = instantiate(cfg.data.dataloader_val, _convert_="all")
    trainer = instantiate(cfg.train.trainer, _convert_="all")

    # ...


if __name__ == "__main__":
    my_app()
