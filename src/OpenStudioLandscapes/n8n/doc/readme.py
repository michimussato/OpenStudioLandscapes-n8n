import textwrap

import snakemd


def readme_feature(
    doc: snakemd.Document,
    main_header: str,
) -> snakemd.Document:

    # Some Specific information

    doc.add_heading(
        text=main_header,
        level=1,
    )

    # Logo

    doc.add_paragraph(
        snakemd.Inline(
            text=textwrap.dedent(
                """
                Logo n8n
                """
            ),
            image={
                "n8n": "https://n8n.io/guidelines/logo-dark.svg",
            }["n8n"],
            link="https://n8n.io/",
        ).__str__()
    )

    doc.add_heading(
        text="Official Documentation",
        level=2,
    )

    doc.add_unordered_list(
        [
            "[GitHub](https://github.com/n8n-io/n8n)",
            "[n8n Documentation](https://docs.n8n.io/)",
            "[n8n Docker Installation (self hosted)](https://docs.n8n.io/hosting/installation/docker/)",
            "[n8n Docker Image Readme](https://github.com/n8n-io/n8n/tree/master/docker/images/n8n)",
        ]
    )

    ##################################################
    # TO EDIT THIS FILE FOR YOUR OWN FEATURE,
    # AND USE THIS FILE TO HAVE YOUR OWN README.md
    # PROGRAMMATICALLY GENERATED.
    #
    # Help on snakemd:
    # https://www.snakemd.io/en/latest/
    ##################################################

    doc.add_horizontal_rule()

    return doc


if __name__ == "__main__":
    pass
