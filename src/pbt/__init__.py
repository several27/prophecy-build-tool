"""
DATABRICKS_HOST, DATABRICKS_TOKEN
"""
import click
import pkg_resources
from rich import print

from .prophecy_build_tool import ProphecyBuildTool


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--path",
    help="Path to the directory containing the pbt_project.yml file",
    required=True,
)
def build(path):
    pbt = ProphecyBuildTool(path)
    pbt.build(dict())


@cli.command()
@click.option(
    "--path",
    help="Path to the directory containing the pbt_project.yml file",
    required=True,
)
def validate(path):
    pbt = ProphecyBuildTool(path)
    pbt.validate()


@cli.command()
@click.option(
    "--path",
    help="Path to the directory containing the pbt_project.yml file",
    required=True,
)
@click.option("--dependent-projects-path", help="Dependent projects path", default="")
@click.option(
    "--release-version",
    help="Release version to be used during deployments",
    default="",
)
@click.option(
    "--project-id",
    help="Project Id placeholder to be used during deployments",
    default="",
)
@click.option(
    "--prophecy-url",
    help="Prophecy URL placeholder to be used during deployments",
    default="",
)
@click.option(
    "--fabric-ids",
    help="Fabric IDs(comma separated) which can be used to filter jobs for deployments",
    default="",
)
@click.option(
    "--skip-builds", is_flag=True, default=False, help="Flag to skip building Pipelines"
)
def deploy(
    path,
    dependent_projects_path,
    release_version,
    project_id,
    prophecy_url,
    fabric_ids,
    skip_builds,
):
    pbt = ProphecyBuildTool(
        path, dependent_projects_path, release_version, project_id, prophecy_url
    )
    pbt.deploy(fabric_ids, skip_builds)


@cli.command()
@click.option(
    "--path",
    help="Path to the directory containing the pbt_project.yml file",
    required=True,
)
def test(path):
    pbt = ProphecyBuildTool(path)
    pbt.test()


if __name__ == "pbt":
    print(
        f"[bold purple]Prophecy-build-tool[/bold purple] [bold black]"
        f"v{pkg_resources.require('prophecy-build-tool')[0].version}[/bold black]\n"
    )
    cli()
