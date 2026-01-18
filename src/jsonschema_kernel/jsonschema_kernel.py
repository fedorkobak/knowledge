from command_kernel import command
from tempdir_kernel import TempDirKernel


class JsonSchemaKernel(TempDirKernel):
    """
    Kernel that streamlines check-jsonschema usage.
    Use the magic commands:
      - %schema : store JSON schema from the cell body
      - %check  : run validation with current schema/object
    """

    schema_filename = "schema.json"
    object_filename = "object.json"

    @command('#schema')
    def _set_schema(self, code: str = '') -> str:
        super()._init_dir()
        return self._heredoc_to_file(self.schema_filename, code)

    @command('#check')
    def _check(self, code: str = '') -> str:
        commands = ''
        if code.strip():
            commands = self._heredoc_to_file(self.object_filename, code)
        commands += self._check_command()
        return commands

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _check_command(self) -> str:
        return (
            f"\ncheck-jsonschema --schemafile {self.schema_filename} "
            f"{self.object_filename}\n"
        )

    def _heredoc_to_file(self, filename: str, content: str) -> str:
        marker = "__JSONSCHEMA_EOF__"
        return (
            f"cat << '{marker}' > {filename}\n"
            f"{content}\n"
            f"{marker}\n"
        )
