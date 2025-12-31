from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.n8n.assets

assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.n8n.assets],
)


defs = Definitions(
    assets=[
        *assets,
    ],
)
