from dagster import Definitions

from OpenStudioLandscapes.n8n.definitions import assets_base
from OpenStudioLandscapes.engine.base.assets import group_out_base_spec


assets_external = []
assets_external.append(group_out_base_spec)


defs = Definitions(
    assets=[
        *assets_base,
        *assets_external,
    ],
)
