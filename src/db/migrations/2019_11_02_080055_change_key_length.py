from orator.migrations import Migration


class ChangeKeyLength(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('credentials') as table:
            table.drop_column('private_key')
            table.drop_column('public_key')
            table.text('private_key_contents').nullable()
            table.text('public_key_contents').nullable()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('credentials') as table:
            table.drop_column('private_key')
            table.drop_column('public_key')
            table.char('private_key', 100).nullable()
            table.char('public_key', 100).nullable()
