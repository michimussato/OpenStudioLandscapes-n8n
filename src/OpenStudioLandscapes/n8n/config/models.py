import enum
import pathlib
from typing import List, Dict

from OpenStudioLandscapes.engine.config.models import FeatureBaseModel
from pydantic import (
    Field,
    PositiveInt,
)

from OpenStudioLandscapes.n8n import (
    ASSET_HEADER,
    LOGGER,
    dist,
)


class Branches(enum.StrEnum):
    main = "main"


class Config(FeatureBaseModel):

    feature_name: str = dist.name

    group_name: str = ASSET_HEADER["group_name"]

    key_prefixes: List[str] = ASSET_HEADER["key_prefix"]

    n8n_docker_image: str = Field(
        default="docker.n8n.io/n8nio/n8n",
    )

    # GENERIC_TIMEZONE: str = Field(
    #     default="Europe/UTC",
    # )

    # TZ: str = Field(
    #     default="Europe/UTC",
    # )

    N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS: bool = Field(
        default=True,
    )

    N8N_RUNNERS_ENABLED: bool = Field(
        default=True,
    )

    n8n_port_host: PositiveInt = Field(
        default=5666,
        description="The host port.",
        frozen=True,
    )
    n8n_port_container: PositiveInt = Field(
        default=5678,
        description="The n8n container port.",
        frozen=False,
    )

    n8n_volume: pathlib.Path = Field(
        description="The host side mounted volume.",
        default=pathlib.Path("{DOT_LANDSCAPES}/{LANDSCAPE}/{FEATURE}/n8n_data"),
    )

    N8N_USE_POSTGRES: bool = Field(
        default=False,
    )

    # DB_TYPE: str = Field(
    #     default="postgresdb",
    # )
    #
    # DB_POSTGRESDB_DATABASE: str = Field(
    #     default=None,
    # )
    #
    # DB_POSTGRESDB_HOST: str = Field(
    #     default=None,
    # )
    #
    # DB_POSTGRESDB_PORT: str = Field(
    #     default=None,
    # )
    #
    # DB_POSTGRESDB_USER: str = Field(
    #     default=None,
    # )
    #
    # DB_POSTGRESDB_SCHEMA: str = Field(
    #     default=None,
    # )
    #
    # DB_POSTGRESDB_PASSWORD: str = Field(
    #     default=None,
    # )

    # EXPANDABLE PATHS
    @property
    def n8n_volume_expanded(self) -> pathlib.Path:
        LOGGER.debug(f"{self.env = }")
        if self.env is None:
            raise KeyError("`env` is `None`.")
        LOGGER.debug(f"Expanding {self.n8n_volume}...")
        ret = pathlib.Path(
            self.n8n_volume.expanduser()  # pylint: disable=E1101
            .as_posix()
            .format(
                **{
                    "FEATURE": self.feature_name,
                    **self.env,
                }
            )
        )
        return ret


if __name__ == "__main__":
    CONFIG_STR: str = Config.get_docs()
else:
    import yaml

    schema: Dict = Config.model_json_schema(mode="serialization")
    properties: Dict = schema.get("properties", {})

    CONFIG_STR: str = yaml.dump(properties)
