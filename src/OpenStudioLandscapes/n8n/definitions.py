from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.n8n.assets

assets_base = load_assets_from_modules(
    modules=[OpenStudioLandscapes.n8n.assets],
)


defs = Definitions(
    assets=[
        *assets_base,
    ],
)
