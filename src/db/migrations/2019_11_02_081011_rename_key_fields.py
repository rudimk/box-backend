from orator.migrations import Migration


class RenameKeyFields(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('credentials') as table:
            table.rename_column('private_key_contents', 'private_key')
            table.rename_column('public_key_contents', 'public_key')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('credentials') as table:
            table.rename_column('private_key', 'private_key_contents')
            table.rename_column('public_key', 'public_key_contents')
